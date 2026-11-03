#!/usr/bin/env python3
"""Looks up Skyrim SE mods on Nexus Mods, and downloads files into MO2's downloads folder.

Lookups use the public GraphQL API and need no key:
  python tools/nexus.py search <name> [--count N]     mods whose name contains <name>, most downloaded first
  python tools/nexus.py info <mod id> [...]           summary, version, dates and requirements
  python tools/nexus.py files <mod id> [...]          current files with their ids and sizes
  python tools/nexus.py description <mod id>          the description page as plain text, to read install notes

Downloads use the v1 API and a premium account's personal API key. The key comes from the NEXUS_API_KEY
environment variable, or else from Windows Credential Manager, where store-key saves it (read from
standard input, so it never appears in a command line). The key is never printed or written to a file:
  python tools/nexus.py store-key < key.txt     or: "<key>" | python tools/nexus.py store-key
  python tools/nexus.py validate
  python tools/nexus.py get <mod id>:<file id> [...] [--segments N]

`get` writes the archive and the .meta file MO2 expects into <MO2>/downloads, where <MO2> comes from the
MO2_DIR environment variable (default C:\\Modding\\MO2). Each file is checked against Nexus by its MD5.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

GRAPHQL = "https://api.nexusmods.com/v2/graphql"
V1 = "https://api.nexusmods.com/v1"
GAME_DOMAIN = "skyrimspecialedition"
KEY_VARIABLE = "NEXUS_API_KEY"
CREDENTIAL_TARGET = "nexusmods-api-key"
AGENT = "skyrim-modlist-decisions/1.0"
MO2 = os.environ.get("MO2_DIR", r"C:\Modding\MO2")


def graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    request = urllib.request.Request(GRAPHQL, body, {"Content-Type": "application/json", "User-Agent": AGENT})
    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.load(response)
    if "errors" in result:
        sys.exit(json.dumps(result["errors"])[:1500])
    return result["data"]


def credential_api():
    """Windows Credential Manager's generic credentials, through advapi32."""
    import ctypes
    from ctypes import wintypes

    class Credential(ctypes.Structure):
        _fields_ = [("Flags", wintypes.DWORD), ("Type", wintypes.DWORD), ("TargetName", wintypes.LPWSTR),
                    ("Comment", wintypes.LPWSTR), ("LastWritten", wintypes.FILETIME), ("CredentialBlobSize", wintypes.DWORD),
                    ("CredentialBlob", ctypes.POINTER(ctypes.c_ubyte)), ("Persist", wintypes.DWORD),
                    ("AttributeCount", wintypes.DWORD), ("Attributes", ctypes.c_void_p), ("TargetAlias", wintypes.LPWSTR),
                    ("UserName", wintypes.LPWSTR)]

    advapi32 = ctypes.WinDLL("advapi32", use_last_error=True)
    advapi32.CredReadW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD, ctypes.POINTER(ctypes.POINTER(Credential))]
    advapi32.CredWriteW.argtypes = [ctypes.POINTER(Credential), wintypes.DWORD]
    advapi32.CredFree.argtypes = [ctypes.c_void_p]
    return ctypes, Credential, advapi32


def stored_key():
    if os.name != "nt":
        return None
    ctypes, Credential, advapi32 = credential_api()
    found = ctypes.POINTER(Credential)()
    if not advapi32.CredReadW(CREDENTIAL_TARGET, 1, 0, ctypes.byref(found)):  # 1: a generic credential
        return None
    try:
        return ctypes.string_at(found.contents.CredentialBlob, found.contents.CredentialBlobSize).decode("utf-16-le")
    finally:
        advapi32.CredFree(found)


def store_key():
    secret = sys.stdin.read().strip()
    if not re.fullmatch(r"[A-Za-z0-9+/=_-]{40,}", secret):
        sys.exit("That doesn't look like a Nexus API key; nothing was saved.")
    ctypes, Credential, advapi32 = credential_api()
    blob = secret.encode("utf-16-le")
    buffer = (ctypes.c_ubyte * len(blob)).from_buffer_copy(blob)
    # Persist 2 keeps it for this Windows user on this machine, encrypted by Windows
    credential = Credential(Type=1, TargetName=CREDENTIAL_TARGET, UserName="nexusmods", Persist=2,
                            CredentialBlobSize=len(blob), CredentialBlob=ctypes.cast(buffer, ctypes.POINTER(ctypes.c_ubyte)))
    if not advapi32.CredWriteW(ctypes.byref(credential), 0):
        raise ctypes.WinError(ctypes.get_last_error())
    print(f"Saved in Windows Credential Manager as '{CREDENTIAL_TARGET}'.")


def v1(path):
    key = os.environ.get(KEY_VARIABLE) or stored_key()
    if not key:
        sys.exit(f"No key: run store-key, or set {KEY_VARIABLE}. Keys come from nexusmods.com/settings/api-keys")
    headers = {"apikey": key, "User-Agent": AGENT, "Application-Name": "skyrim-modlist-decisions", "Application-Version": "1.0"}
    with urllib.request.urlopen(urllib.request.Request(V1 + path, headers=headers), timeout=60) as response:
        return json.load(response)


def mods_by_id(ids, fields):
    query = f"query($ids:[CompositeDomainWithIdInput!]!){{legacyModsByDomain(ids:$ids){{nodes{{{fields}}}}}}}"
    return graphql(query, {"ids": [{"gameDomain": GAME_DOMAIN, "modId": int(i)} for i in ids]})["legacyModsByDomain"]["nodes"]


def search(name, count):
    query = """query($f:ModsFilter,$n:Int){mods(filter:$f,count:$n,sort:[{downloads:{direction:DESC}}]){totalCount
      nodes{modId name version downloads endorsements updatedAt author summary}}}"""
    data = graphql(query, {"f": {"gameDomainName": [{"value": GAME_DOMAIN}], "name": [{"value": name, "op": "WILDCARD"}]},
                           "n": count})["mods"]
    print(f"{data['totalCount']} mods match '{name}'")
    for mod in data["nodes"]:
        print(f"{mod['modId']:>7}  {mod['downloads']:>9,} dl  {mod['endorsements']:>7,} end  {mod['updatedAt'][:10]}  v{mod['version']}"
              f"  {mod['name']}  by {mod['author']}\n         {(mod['summary'] or '').strip()[:160]}")


def info(ids):
    fields = """modId name version author downloads endorsements createdAt updatedAt summary
      modRequirements{nexusRequirements{nodes{modId modName notes url}} modsRequiringThisMod{totalCount}}"""
    for mod in mods_by_id(ids, fields):
        requirements = mod.get("modRequirements") or {}
        print(f"== {mod['modId']} {mod['name']} v{mod['version']} by {mod['author']}")
        print(f"   {mod['downloads']:,} downloads, {mod['endorsements']:,} endorsements, created {mod['createdAt'][:10]},"
              f" updated {mod['updatedAt'][:10]}, required by {(requirements.get('modsRequiringThisMod') or {}).get('totalCount')} mods")
        print(f"   {(mod['summary'] or '').strip()}")
        for need in (requirements.get("nexusRequirements") or {}).get("nodes", []):
            note = f" - {need['notes'].strip()[:140]}" if need.get("notes") else ""
            print(f"   requires {need.get('modName') or need.get('url')} [{need.get('modId')}]{note}")


def files(ids):
    query = "query($id:ID!){modFiles(modId:$id,gameId:1704){fileId name version category sizeInBytes date}}"
    for mod in ids:
        print(f"== {mod}")
        for file in graphql(query, {"id": mod})["modFiles"]:
            if file["category"] in ("ARCHIVED", "OLD_VERSION", "DELETED", "REMOVED"):
                continue
            date = datetime.date.fromtimestamp(int(file["date"])) if str(file["date"]).isdigit() else file["date"]
            print(f"   {file['fileId']:>7} {file['category']:9} {int(file['sizeInBytes'] or 0) / 2**30:6.2f} GB  {date}"
                  f"  v{file['version']}  {file['name']}")


def description(mod):
    text = (mods_by_id([mod], "modId name description")[0]["description"] or "").replace("﻿", "")
    text = re.sub(r"<br\s*/?>", "\n", text)
    text = re.sub(r"\[url=([^\]]+)\](.*?)\[/url\]", r"\2 (\1)", text, flags=re.S | re.I)
    text = re.sub(r"\[/?[a-z*]+(=[^\]]*)?\]", "", text, flags=re.I)  # the remaining BBCode tags
    print(re.sub(r"\n{3,}", "\n\n", text).strip())


def validate():
    user = v1("/users/validate.json")
    print(f"user {user.get('name')}, premium: {user.get('is_premium')}")


def fetch(url, target, size, segments):
    """Downloads with curl in parallel byte ranges, resuming any partial segment."""
    step = -(-size // segments)
    parts, processes = [], []
    for index in range(segments):
        low, high = index * step, min(size, (index + 1) * step) - 1
        part = f"{target}.seg{index}"
        have = os.path.getsize(part) if os.path.exists(part) else 0
        parts.append((part, high - low + 1))
        if have < high - low + 1:
            command = ["curl.exe", "-s", "--retry", "5", "--retry-all-errors", "-r", f"{low + have}-{high}", "-o", "-", url]
            processes.append(subprocess.Popen(command, stdout=open(part, "ab")))
    for process in processes:
        process.wait()
    for part, expected in parts:
        if os.path.getsize(part) != expected:
            sys.exit(f"{part} has {os.path.getsize(part)} of {expected} bytes; run again to resume")
    digest = hashlib.md5()
    with open(target + ".part", "wb") as output:
        for part, _ in parts:
            with open(part, "rb") as source:
                while chunk := source.read(1 << 24):
                    output.write(chunk)
                    digest.update(chunk)
    for part, _ in parts:
        os.remove(part)
    return digest.hexdigest()


def get(specs, segments):
    downloads = os.path.join(MO2, "downloads")
    for spec in specs:
        mod, file_id = spec.split(":")
        mod_info = v1(f"/games/{GAME_DOMAIN}/mods/{mod}.json")
        file = v1(f"/games/{GAME_DOMAIN}/mods/{mod}/files/{file_id}.json")
        target = os.path.join(downloads, file["file_name"])
        size = file["size_in_bytes"] or file["size_kb"] * 1024
        if os.path.exists(target):
            print(f"have  {file['file_name']}")
        else:
            links = v1(f"/games/{GAME_DOMAIN}/mods/{mod}/files/{file_id}/download_link.json")
            # CDN links can carry the raw file name, spaces and quotes included
            url = urllib.parse.quote(links[0]["URI"], safe=":/?&=%~+")
            # Newer files report only a rounded size in KB, so ask the CDN for the exact length
            head = urllib.request.Request(url, method="HEAD", headers={"User-Agent": AGENT})
            with urllib.request.urlopen(head, timeout=60) as response:
                size = int(response.headers["Content-Length"])
            start = time.time()
            md5 = fetch(url, target, size, segments if size > 256 * 2**20 else 1)
            # The md5= in a CDN link signs the link; the file's real MD5 is checked against Nexus instead
            try:
                matches = v1(f"/games/{GAME_DOMAIN}/mods/md5_search/{md5}.json")
            except urllib.error.HTTPError:  # 404 when Nexus knows no file with this MD5
                matches = []
            if not any(str(match["file_details"]["file_id"]) == file_id for match in matches):
                sys.exit(f"{file['file_name']}: MD5 {md5} doesn't match file {file_id} on Nexus; kept as .part")
            os.replace(target + ".part", target)
            print(f"got   {file['file_name']}  {size / 2**30:.2f} GB in {time.time() - start:.0f}s, MD5 verified")
        # The .meta file MO2 writes next to each download, so it knows the source and can check for updates
        summary = re.sub(r"\s+", " ", file.get("description") or "").replace('"', "'")[:200]
        meta = [
            "[General]", "gameName=SkyrimSE", f"modID={mod}", f"fileID={file_id}",
            f'url="https://www.nexusmods.com/skyrimspecialedition/mods/{mod}?tab=files&file_id={file_id}"',
            f"name={file['name']}", f'description="{summary}"', f"modName={mod_info['name']}", f"version={file['version']}",
            "newestVersion=", f"fileCategory={file['category_id']}", f"category={mod_info.get('category_id', 0)}",
            "repository=Nexus", "installed=false", "uninstalled=false", "paused=false", "removed=false",
        ]
        if not os.path.exists(target + ".meta"):
            with open(target + ".meta", "w", encoding="utf-8") as output:
                output.write("\n".join(meta) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("search")
    command.add_argument("name")
    command.add_argument("--count", type=int, default=15)
    for name in ("info", "files"):
        commands.add_parser(name).add_argument("ids", nargs="+")
    commands.add_parser("description").add_argument("id")
    commands.add_parser("validate")
    commands.add_parser("store-key")
    command = commands.add_parser("get")
    command.add_argument("specs", nargs="+", metavar="mod:file")
    command.add_argument("--segments", type=int, default=6)
    args = parser.parse_args()
    if args.command == "search":
        search(args.name, args.count)
    elif args.command == "info":
        info(args.ids)
    elif args.command == "files":
        files(args.ids)
    elif args.command == "description":
        description(args.id)
    elif args.command == "validate":
        validate()
    elif args.command == "store-key":
        store_key()
    else:
        get(args.specs, args.segments)


if __name__ == "__main__":
    main()
