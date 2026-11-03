#!/usr/bin/env python3
"""Shows which vanilla assets still look vanilla in the profile, and how much candidate mods would replace.

  python tools/coverage.py "<regex on vanilla paths>" [--candidate <mod id>:<file id> ...] [--list]

The regex runs on lowercase paths inside the game's own BSAs, such as "^textures\\\\plants\\\\". A file
counts as replaced when an enabled mod ships it, loose or in a BSA. A PBR texture at textures\\pbr\\X
counts as replacing textures\\X, because PGPatcher matches PBR textures by path. Generated outputs (mods
named "... - Outputs") don't count, since they only re-patch what's already there.

A candidate is a Nexus file, read from the archive preview Nexus publishes, so nothing is downloaded.
Previews follow the archive's own layout, FOMOD option folders included, so a candidate's count is the
most it could replace if every option were picked. Mods that swap objects through Base Object Swapper
or plugins use new paths and won't show up here.

The game's Data folder comes from GAME_DATA (default C:\\Modding\\STOCK\\Data), and the instance from
MO2_DIR and MO2_PROFILE, as in tools/mo2.py.
"""
import argparse
import collections
import glob
import json
import os
import re
import struct
import urllib.parse
import urllib.request

GAME_DATA = os.environ.get("GAME_DATA", r"C:\Modding\STOCK\Data")
MO2 = os.environ.get("MO2_DIR", r"C:\Modding\MO2")
PROFILE = os.path.join(MO2, "profiles", os.environ.get("MO2_PROFILE", "Default"))
GRAPHQL = "https://api.nexusmods.com/v2/graphql"
PREVIEW = "https://file-metadata.nexusmods.com/file/nexus-files-s3-meta/1704/{mod}/{uri}.json"
AGENT = "skyrim-modlist-decisions/1.0"
# Texture maps that belong to a diffuse texture of the same name
MAP_SUFFIX = re.compile(r"(_n|_rmaos|_p|_s|_g|_cnr|_f|_m|_sk|_em|_b|_d|_msn|_h)$")


def bsa_files(path):
    """Lists the files in a Skyrim SE (v105) or LE (v104) BSA."""
    with open(path, "rb") as file:
        magic, version, offset, flags, folders, _, _, names_length = struct.unpack("<4sIIIIIII", file.read(32))
        if magic != b"BSA\0":
            return []
        record = 24 if version == 105 else 16
        file.seek(offset)
        counts = [struct.unpack_from("<I", file.read(record), 8)[0] for _ in range(folders)]
        names = []
        for count in counts:
            length = file.read(1)[0]
            names.append(file.read(length).rstrip(b"\0").decode("cp1252"))
            file.seek(count * 16, 1)
        file_names = file.read(names_length).split(b"\0")
    result, index = [], 0
    for folder, count in zip(names, counts):
        for _ in range(count):
            result.append(f"{folder}\\{file_names[index].decode('cp1252')}".lower())
            index += 1
    return result


def key(path):
    """Reduces a path to what decides its look: the mesh path, or the diffuse texture it belongs to."""
    path = path.lower().replace("/", "\\")
    match = re.search(r"(?:^|\\)(meshes|textures)\\(.*)$", path)
    if not match:
        return None
    kind, rest = match.groups()
    if kind == "meshes":
        return ("mesh", rest) if rest.endswith(".nif") else None
    if not rest.endswith(".dds"):
        return None
    return ("texture", MAP_SUFFIX.sub("", os.path.splitext(re.sub(r"^pbr\\", "", rest))[0]))


def vanilla_files(pattern):
    found = set()
    for path in glob.glob(os.path.join(glob.escape(GAME_DATA), "*.bsa")):
        name = os.path.basename(path).lower()
        if name.startswith(("skyrim - ", "dawnguard", "hearthfires", "dragonborn", "update")):
            found |= {file for file in bsa_files(path) if pattern.search(file)}
    return found


def installed_keys():
    keys = set()
    with open(os.path.join(PROFILE, "modlist.txt"), encoding="utf-8") as file:
        mods = [line[1:].strip() for line in file if line.startswith("+")]
    for mod in mods:
        if mod.endswith(" - Outputs"):
            continue
        root = os.path.join(MO2, "mods", mod)
        for bsa in glob.glob(os.path.join(glob.escape(root), "*.bsa")):
            keys |= {key(file) for file in bsa_files(bsa)}
        for folder, _, names in os.walk(root):
            for name in names:
                keys.add(key(os.path.relpath(os.path.join(folder, name), root)))
    keys.discard(None)
    return keys


def preview_keys(spec):
    mod, file_id = spec.split(":")
    query = "query($id:ID!){modFiles(modId:$id,gameId:1704){fileId name uri}}"
    body = json.dumps({"query": query, "variables": {"id": mod}}).encode()
    request = urllib.request.Request(GRAPHQL, body, {"Content-Type": "application/json", "User-Agent": AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        files = json.load(response)["data"]["modFiles"]
    file = next(item for item in files if str(item["fileId"]) == file_id)
    url = PREVIEW.format(mod=mod, uri=urllib.parse.quote(file["uri"]))
    with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": AGENT}), timeout=60) as response:
        tree = json.load(response)
    paths, stack = [], [tree]
    while stack:
        node = stack.pop()
        if node.get("type") == "file":
            paths.append(node["path"])
        stack += node.get("children") or []
    return file["name"], {key(path) for path in paths} - {None}


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pattern")
    parser.add_argument("--candidate", action="append", default=[], metavar="mod:file")
    parser.add_argument("--list", action="store_true")
    args = parser.parse_args()
    vanilla = vanilla_files(re.compile(args.pattern, re.I))
    looks = collections.defaultdict(set)
    for path in vanilla:
        item = key(path)
        if item and not (item[0] == "texture" and MAP_SUFFIX.search(os.path.splitext(path)[0])):
            looks[item].add(path)
    still = set(looks) - installed_keys()
    by_folder = collections.Counter(os.path.dirname(item[1]) for item in still)
    total_folder = collections.Counter(os.path.dirname(item[1]) for item in looks)
    print(f"{len(vanilla)} vanilla files match; {len(still)} of {len(looks)} meshes and diffuse textures still vanilla")
    for folder, total in sorted(total_folder.items()):
        print(f"  {by_folder[folder]:>4} of {total:<4} still vanilla in {folder}")
    remaining = set(still)
    for spec in args.candidate:
        name, keys = preview_keys(spec)
        hits = still & keys
        remaining -= keys
        print(f"\n{spec} {name}: would replace {sum(k[0] == 'mesh' for k in hits)} meshes and"
              f" {sum(k[0] == 'texture' for k in hits)} textures still vanilla")
    if args.list:
        print(f"\nstill vanilla{' after the candidates' if args.candidate else ''}: {len(remaining)}")
        for kind, path in sorted(remaining):
            print(f"  {kind:<7} {path}")


if __name__ == "__main__":
    main()
