#!/usr/bin/env python3
"""Deepen the PBR ground's parallax toward a target relief, without moving where layers win at their edges.

  python -X utf8 tools/terrain_depth.py [--target 0.09] [--max-gain 3] [--skip <regex>] [--dry-run]

Relief here is a height map's standard deviation times its texture set's displacementScale, the measure in
research/road_edges_and_debris.md. Community Shaders' terrain height blending weighs each layer by
(height - 0.5) * displacementScale, so raising displacementScale alone also lifts a map's average and lets it
swallow its neighbours' edges. Instead this stretches each height map's contrast around its own average:

  new = mean' + gain * (smoothed - mean),  with (mean' - 0.5) * scale' = (mean - 0.5) * scale

A set below displacementScale 1 first rises toward 1, only as far as the target needs, with its average
re-centred to match; a scale under 1 also cuts the shader's step count. The stretch backs off until no more
than --max-clip of the pixels clip. Sets already at the target, maps that sets share with different
scales, and maps matching --skip (by default the converted dirt road, the reference) are left alone. A
light wrap-around 3x3 blur goes under any gain above 1.5, so BC4 block noise isn't amplified with the detail.

Reads the winning landscape texture sets from the profile's load order, the winning PBRTextureSets JSON and
height map from the mods folder by MO2 priority, and writes the new maps and any changed JSON files into
its own mod, which it ignores when it reads. Needs numpy and Texconv (see terrain_to_pbr.py). Run it with
MO2 and the game closed; nothing needs regenerating after it, since no path changes.

Tried on 2026-11-03 with the defaults below: TomatoRim's ground smeared into streaks in game, because its maps
hold surface detail rather than real height. The output is disabled. Don't enable it again without a much
milder --max-gain and a look in game.
"""
import argparse
import json
import os
import re
import shutil
import struct
import sys
import tempfile
import zlib

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from terrain_to_pbr import check_mips, texconv  # noqa: E402

MO2 = os.environ.get("MO2_DIR", r"C:\Modding\MO2")
PROFILE = os.path.join(MO2, "profiles", os.environ.get("MO2_PROFILE", "Default"))
DATA = r"C:\Modding\STOCK\Data"
OUT = "Terrain Depth - Outputs"


def subrecords(body):
    out, q, big = [], 0, None
    while q < len(body):
        kind, size = body[q:q + 4], struct.unpack_from("<H", body, q + 4)[0]
        if big is not None:
            size, big = big, None
        if kind == b"XXXX":
            big = struct.unpack_from("<I", body, q + 6)[0]
            q += 10
            continue
        out.append((kind, body[q + 6:q + 6 + size]))
        q += 6 + size
    return out


def load_order():
    order = [l.strip() for l in open(os.path.join(PROFILE, "loadorder.txt"), encoding="utf-8") if l.strip() and not l.startswith("#")]
    active = {l.strip().lstrip("*").lower() for l in open(os.path.join(PROFILE, "plugins.txt"), encoding="utf-8") if l.startswith("*")}
    active |= {"skyrim.esm", "update.esm", "dawnguard.esm", "hearthfires.esm", "dragonborn.esm"}
    ccc = os.path.join(os.path.dirname(DATA), "Skyrim.ccc")
    if os.path.exists(ccc):
        active |= {l.strip().lower() for l in open(ccc, encoding="utf-8") if l.strip()}
    return [p for p in order if p.lower() in active]


MODS = [l[1:].strip() for l in open(os.path.join(PROFILE, "modlist.txt"), encoding="utf-8") if l.startswith("+")]


def locate(relative):
    """The winning loose file for a data-relative path, ignoring this tool's own output."""
    for mod in MODS:
        if mod == OUT:
            continue
        path = os.path.join(MO2, "mods", mod, relative)
        if os.path.exists(path):
            return path, mod
    path = os.path.join(DATA, relative)
    return (path, "STOCK") if os.path.exists(path) else (None, None)


def landscape_sets():
    """EDID and texture paths of every texture set a winning LTEX record uses."""
    ltex, txst = {}, {}
    for plugin in load_order():
        path, _ = locate(plugin)
        if path is None:
            continue
        data = open(path, "rb").read()
        size = struct.unpack_from("<I", data, 4)[0]
        masters = [v[:-1].decode("cp1252") for k, v in subrecords(data[24:24 + size]) if k == b"MAST"]

        def key(fid):
            index = fid >> 24
            return ((masters[index] if index < len(masters) else plugin).lower(), fid & 0xFFFFFF)

        p = 24 + size
        while p < len(data):
            kind, length = data[p:p + 4], struct.unpack_from("<I", data, p + 4)[0]
            if kind == b"GRUP":
                top = struct.unpack_from("<I", data, p + 12)[0] == 0
                p += 24 if not top or data[p + 8:p + 12] in (b"LTEX", b"TXST") else length
                continue
            flags, fid = struct.unpack_from("<II", data, p + 8)
            if kind in (b"LTEX", b"TXST"):
                body = data[p + 24:p + 24 + length]
                if flags & 0x40000:
                    body = zlib.decompress(body[4:])
                subs = subrecords(body)
                if kind == b"LTEX":
                    ltex[key(fid)] = next((key(struct.unpack_from("<I", v)[0]) for k, v in subs if k == b"TNAM"), None)
                else:
                    edid = next((v[:-1].decode("cp1252") for k, v in subs if k == b"EDID"), "")
                    txst[key(fid)] = (edid, [v[:-1].decode("cp1252") for k, v in subs if k[:2] == b"TX"])
            p += 24 + length
    return {txst[t][0]: txst[t][1] for t in set(ltex.values()) if t in txst}


def decode_float(path):
    with tempfile.TemporaryDirectory() as folder:
        texconv(["-f", "R32_FLOAT", "-m", "1", "-o", folder, path])
        data = open(os.path.join(folder, os.listdir(folder)[0]), "rb").read()
    height, width = struct.unpack_from("<II", data, 12)
    offset = 128 + (20 if data[84:88] == b"DX10" else 0)
    return np.frombuffer(data, "<f4", width * height, offset).reshape(height, width).astype(np.float64)


def encode_bc4(values, target):
    height, width = values.shape
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with tempfile.TemporaryDirectory() as folder:
        raw = os.path.join(folder, os.path.basename(target))
        head = struct.pack("<4sIIIIIII44s", b"DDS ", 124, 0x100F, height, width, width * 4, 0, 1, b"\0" * 44)
        pixel_format = struct.pack("<II4sIIIII", 32, 0x4, b"DX10", 0, 0, 0, 0, 0)
        caps = struct.pack("<IIIII", 0x1000, 0, 0, 0, 0)
        dx10 = struct.pack("<IIIII", 41, 3, 0, 1, 0)  # R32_FLOAT, 2D texture
        with open(raw, "wb") as file:
            file.write(head + pixel_format + caps + dx10 + values.astype("<f4").tobytes())
        texconv(["-f", "BC4_UNORM", "-m", "0", "-o", os.path.dirname(target), raw])
    written = next(n for n in os.listdir(os.path.dirname(target)) if n.lower() == os.path.basename(target).lower())
    os.replace(os.path.join(os.path.dirname(target), written), target)
    check_mips(target)


def smooth(values):
    """3x3 binomial blur that wraps, since landscape textures tile."""
    for axis in (0, 1):
        values = (np.roll(values, 1, axis) + 2 * values + np.roll(values, -1, axis)) / 4
    return values


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--target", type=float, default=0.09, help="relief to raise shallower ground to")
    parser.add_argument("--max-gain", type=float, default=3.0, help="largest contrast stretch for one map")
    parser.add_argument("--max-clip", type=float, default=0.005, help="largest share of pixels a stretch may clip")
    parser.add_argument("--skip", default=r"grounddirt01_p\.dds$", help="regex of height map paths to leave alone")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    out_root = os.path.join(MO2, "mods", OUT)
    maps = {}  # winning height map file -> (data-relative path, [(set, json path, json, scale)])
    for edid, paths in sorted(landscape_sets().items()):
        json_path, _ = locate(os.path.join("PBRTextureSets", edid + ".json"))
        height = next((p for p in paths if p.lower().endswith("_p.dds")), None)
        if not json_path or not height:
            continue
        relative = os.path.join("textures", height).lower()
        found, mod = locate(relative)
        if not found:
            print(f"  no loose file for {relative} ({edid}), skipped")
            continue
        settings = json.load(open(json_path, encoding="utf-8-sig"))
        entry = maps.setdefault(found.lower(), (relative, mod, []))
        entry[2].append((edid, json_path, settings, float(settings.get("displacementScale", 1.0))))

    if not args.dry_run and os.path.isdir(out_root):
        for sub in ("textures", "PBRTextureSets"):
            shutil.rmtree(os.path.join(out_root, sub), ignore_errors=True)
    changed = 0
    print(f"{'relief':>13} {'gain':>5} {'scale':>11} {'clip':>5}  height map  (sets)")
    for found, (relative, mod, sets) in sorted(maps.items(), key=lambda kv: kv[1][0]):
        scales = {s for _, _, _, s in sets}
        names = ", ".join(e for e, _, _, _ in sets)
        if re.search(args.skip, relative, re.I):
            print(f"{'':>13} {'':>5} {'':>11} {'':>5}  {relative}  reference, left alone")
            continue
        if len(scales) > 1:
            print(f"  {relative}: its sets use different scales {sorted(scales)}, left alone ({names})")
            continue
        scale = scales.pop()
        if scale <= 0:
            continue
        values = decode_float(found)
        mean, std = values.mean(), values.std()
        # A scale under 1 rises only as far as the target needs, and never past 1
        new_scale = max(scale, min(1.0, args.target / max(std, 1e-6)))
        gain = min(args.max_gain, max(1.0, args.target / max(std * new_scale, 1e-6)))
        new_mean = 0.5 + (mean - 0.5) * scale / new_scale
        while True:
            detail = smooth(values) if gain > 1.5 else values
            result = new_mean + gain * (detail - mean)
            clipped = ((result < 0) | (result > 1)).mean()
            if clipped <= args.max_clip or gain <= 1.0:
                break
            gain = max(1.0, gain * 0.9)
        if new_scale == scale and gain < 1.05:
            note = "already deep enough" if std * scale >= args.target else "would clip, left alone"
            print(f"{std * scale:6.3f}       {'':>5} {scale:11.3f} {'':>5}  {relative}  {note}")
            continue
        result = np.clip(result, 0, 1)
        relief = result.std() * new_scale
        print(f"{std * scale:6.3f}>{relief:6.3f} {gain:5.2f} {scale:5.3g}>{new_scale:<5.3g} {clipped:5.1%}  {relative}  ({names}; {mod})")
        changed += 1
        if args.dry_run:
            continue
        encode_bc4(result, os.path.join(out_root, relative))
        if new_scale != scale:
            for edid, json_path, settings, _ in sets:
                os.makedirs(os.path.join(out_root, "PBRTextureSets"), exist_ok=True)
                settings = dict(settings, displacementScale=new_scale)
                with open(os.path.join(out_root, "PBRTextureSets", edid + ".json"), "w", encoding="utf-8") as file:
                    json.dump(settings, file, indent=4)
    print(f"{changed} height maps {'would change' if args.dry_run else 'written to ' + out_root}")
    if not args.dry_run and changed:
        meta = os.path.join(out_root, "meta.ini")
        if not os.path.exists(meta):
            notes = (f"Generated by tools/terrain_depth.py in skyrim-modlist-decisions: contrast-stretched copies of the "
                     f"winning PBR landscape height maps, toward relief {args.target}. Rerun the tool after changing "
                     f"landscape mods. For this setup only.")
            with open(meta, "w", encoding="utf-8", newline="\r\n") as file:
                file.write(f"[General]\ngameName=SkyrimSE\nmodid=0\nversion=1.0\nnewestVersion=\ncategory=\n"
                           f"installationFile=\nrepository=\nnotes=\"{notes}\"\n")


if __name__ == "__main__":
    main()
