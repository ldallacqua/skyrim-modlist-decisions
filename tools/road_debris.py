#!/usr/bin/env python3
"""Build a small ESL-flagged plugin that puts sparse pebbles and small rocks on Northern Roads' dirt roads.

  python -X utf8 tools/road_debris.py [--scale <density multiplier>] [--dry-run]

Northern Roads gives its road landscape textures no grass, so nothing grows on them, debris included.
This copies the dirt road LTEX records from Northern Roads.esp, adds GNAM entries for a few new GRAS
records, and writes the plugin into its own mod folder. The models are DrJacopo's, already installed:
the plugin references meshes only, no textures of its own.

Tune the mix in DEBRIS below, or scale every density with --scale, then run it again. The game reads
grass at load, and this list doesn't cache grass, so a new build shows on the next start. Run it with
the game closed. The mod folder and its meta.ini come from MO2_DIR (default C:\\Modding\\MO2).
"""
import argparse
import os
import struct
import sys

MO2 = os.environ.get("MO2_DIR", r"C:\Modding\MO2")
SOURCE = os.path.join(MO2, "mods", "Northern Roads", "Northern Roads.esp")
MOD = "Northern Roads - Road Debris"
PLUGIN = MOD + ".esp"

# (editor id, model under meshes\, density 0-100 of the iMinGrassSize grid). Region-neutral on purpose:
# one road texture runs from the tundra to the Rift, so leaves and pine needles would be wrong somewhere.
DEBRIS = [
    ("NRDebris_Pebbles01", r"Landscape\Grass\PebbleGrass01.nif", 6),
    ("NRDebris_Pebbles03", r"Landscape\Grass\PebbleGrass03.nif", 5),
    ("NRDebris_Pebbles06", r"Landscape\Grass\PebbleGrass06.nif", 4),
    ("NRDebris_SmallRocks02", r"Landscape\Grass\RockGrass02_Small.nif", 2),
]
# Northern Roads' landscape textures that draw the dirt road set (COTN_LandscapeRoadDirt01 and its trails),
# plus the Whiterun outer road, which TomatoRim's plugin points at the same dirt.
ROADS = [
    "COTN_LRoadDirt01", "COTN_LRoadDirt02", "COTN_LRoadDirt01Trail0", "COTN_LRoadDirt01Trail22",
    "COTN_LRoadDirt01Trail45", "COTN_LRoadDirt01Trail77", "COTN_LRoadDirt01Trail90",
    "COTN_LRoadDirt01Trail113", "COTN_LRoadDirt01Trail135", "COTN_LRoadDirt01Trail157", "COTN_LWRStone",
]
MASTERS = ["Skyrim.esm", "Northern Roads.esp"]
# Vanilla RockGrass01's bounds, placement and look: slope 0-40, offset up to 32 units, 25% size spread
OBND = struct.pack("<6h", -30, -23, -6, 31, 23, 7)
SLOPE = (0, 40)
POSITION_RANGE, HEIGHT_RANGE, COLOR_RANGE, WAVE_PERIOD = 32.0, 0.25, 0.1, 0.0
FLAGS = 0x02 | 0x04  # uniform scaling, fit to slope
FORM_VERSION = 44


def subrecord(kind, payload):
    return kind + struct.pack("<H", len(payload)) + payload


def subrecords(body):
    out, q = [], 0
    while q < len(body):
        kind, size = body[q:q + 4], struct.unpack_from("<H", body, q + 4)[0]
        if kind == b"XXXX":
            sys.exit("unexpected XXXX in an LTEX record")
        out.append((kind, body[q + 6:q + 6 + size]))
        q += 6 + size
    return out


def record(kind, form_id, body, flags=0):
    # size, flags, form id, version control, form version, unknown
    return kind + struct.pack("<IIIIHH", len(body), flags, form_id, 0, FORM_VERSION, 0) + body


def group(label, records):
    body = b"".join(records)
    return b"GRUP" + struct.pack("<I", 24 + len(body)) + label + struct.pack("<IHHI", 0, 0, 0, 0) + body


def read_ltex(path):
    data = open(path, "rb").read()
    header_size = struct.unpack_from("<I", data, 4)[0]
    masters = [v[:-1].decode("cp1252") for k, v in subrecords(data[24:24 + header_size]) if k == b"MAST"]
    found, p = {}, 24 + header_size
    while p < len(data):
        kind, length = data[p:p + 4], struct.unpack_from("<I", data, p + 4)[0]
        if kind == b"GRUP":
            top = struct.unpack_from("<I", data, p + 12)[0] == 0
            p += 24 if not top or data[p + 8:p + 12] == b"LTEX" else length
            continue
        flags, form_id = struct.unpack_from("<II", data, p + 8)
        if kind == b"LTEX":
            if flags & 0x40000:
                sys.exit("compressed LTEX records aren't handled")
            subs = subrecords(data[p + 24:p + 24 + length])
            edid = next(v[:-1].decode("cp1252") for k, v in subs if k == b"EDID")
            found[edid] = (form_id, flags, subs)
        p += 24 + length
    return masters, found


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--scale", type=float, default=1.0, help="multiply every density")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    source_masters, ltex = read_ltex(SOURCE)
    source_names = source_masters + ["Northern Roads.esp"]

    def remap(form_id):
        owner = source_names[min(form_id >> 24, len(source_masters))]
        if owner not in MASTERS:
            sys.exit(f"{form_id:08X} belongs to {owner}, which isn't a master here")
        return (MASTERS.index(owner) << 24) | (form_id & 0xFFFFFF)

    own = len(MASTERS) << 24
    grass_records, grass_ids = [], []
    for i, (edid, model, density) in enumerate(DEBRIS):
        density = max(0, min(100, round(density * args.scale)))
        data = struct.pack("<BBBBHHIffffB3x", density, SLOPE[0], SLOPE[1], 0, 0, 0, 0,
                           POSITION_RANGE, HEIGHT_RANGE, COLOR_RANGE, WAVE_PERIOD, FLAGS)
        assert len(data) == 32
        form_id = own | (0x800 + i)
        body = (subrecord(b"EDID", edid.encode() + b"\0") + subrecord(b"OBND", OBND)
                + subrecord(b"MODL", model.encode("cp1252") + b"\0") + subrecord(b"DATA", data))
        grass_records.append(record(b"GRAS", form_id, body))
        grass_ids.append(form_id)
        print(f"GRAS {form_id:08X} {edid:24} density {density:3}  {model}")

    ltex_records = []
    for edid in ROADS:
        if edid not in ltex:
            sys.exit(f"{edid} isn't in {SOURCE}")
        form_id, flags, subs = ltex[edid]
        if any(k == b"GNAM" for k, v in subs):
            sys.exit(f"{edid} already has grass in Northern Roads.esp; this script assumes it has none")
        out = b""
        for k, v in subs:
            if k == b"INAM":  # GNAM entries go before the flags
                out += b"".join(subrecord(b"GNAM", struct.pack("<I", g)) for g in grass_ids)
            if k in (b"TNAM", b"MNAM"):
                v = struct.pack("<I", remap(struct.unpack("<I", v)[0]))
            out += subrecord(k, v)
        if not any(k == b"INAM" for k, v in subs):
            out += b"".join(subrecord(b"GNAM", struct.pack("<I", g)) for g in grass_ids)
        ltex_records.append(record(b"LTEX", remap(form_id), out, flags))
        print(f"LTEX {remap(form_id):08X} {edid}")

    count = len(grass_records) + len(ltex_records) + 2  # records and groups, as xEdit counts them
    header = subrecord(b"HEDR", struct.pack("<fII", 1.7, count, 0x800 + len(DEBRIS)))
    header += subrecord(b"CNAM", b"skyrim-modlist-decisions\0")
    header += subrecord(b"SNAM", "Sparse pebbles and small rocks on Northern Roads' dirt roads, built by "
                        "tools/road_debris.py.".encode() + b"\0")
    for master in MASTERS:
        header += subrecord(b"MAST", master.encode() + b"\0") + subrecord(b"DATA", bytes(8))
    plugin = record(b"TES4", 0, header, 0x200) + group(b"GRAS", grass_records) + group(b"LTEX", ltex_records)

    if args.dry_run:
        print(f"{len(plugin)} bytes, not written")
        return
    folder = os.path.join(MO2, "mods", MOD)
    os.makedirs(folder, exist_ok=True)
    with open(os.path.join(folder, PLUGIN), "wb") as f:
        f.write(plugin)
    meta = os.path.join(folder, "meta.ini")
    if not os.path.exists(meta):
        notes = ("Built here by tools/road_debris.py in skyrim-modlist-decisions. Sparse pebbles and small rocks "
                 "from DrJacopo's library on Northern Roads' dirt road textures. No textures or meshes of its own.")
        with open(meta, "w", encoding="utf-8", newline="\r\n") as f:
            f.write(f"[General]\ngameName=SkyrimSE\nmodid=0\nversion=1.0\nnewestVersion=\ncategory=\n"
                    f"installationFile=\nrepository=\nnotes=\"{notes}\"\n")
    print(f"wrote {os.path.join(folder, PLUGIN)} ({len(plugin)} bytes)")


if __name__ == "__main__":
    main()
