#!/usr/bin/env python3
"""Counts which mods the published Skyrim SE Wabbajack lists install, from Wabbajack's own reports.

  python tools/wabbajack.py count <regex> [--top N]          lists installing each mod whose name matches
  python tools/wabbajack.py lists <regex> [--with <regex>]   the lists that match, and what else they install
  python tools/wabbajack.py show <list name part> <regex>    matching mods in the named lists

Mod names are Nexus names as the lists record them. A list counts as Skyrim SE when it installs Address
Library and isn't a VR list, and as a Community Shaders list when it installs Community Shaders. The index
is cached for a day in the system temp folder.
"""
import argparse
import collections
import json
import os
import re
import tempfile
import time
import urllib.request

INDEX_URL = "https://raw.githubusercontent.com/wabbajack-tools/mod-lists/master/reports/searchIndex.json"
CACHE = os.path.join(tempfile.gettempdir(), "wabbajack-searchIndex.json")


def load_lists():
    if not os.path.exists(CACHE) or time.time() - os.path.getmtime(CACHE) > 86400:
        request = urllib.request.Request(INDEX_URL, headers={"User-Agent": "skyrim-modlist-decisions/1.0"})
        with urllib.request.urlopen(request, timeout=120) as response, open(CACHE, "wb") as output:
            output.write(response.read())
    with open(CACHE, encoding="utf-8") as file:
        index = json.load(file)["ModsPerList"]
    lists = {name: set(mods) for name, mods in index.items()
             if any("Address Library for SKSE" in mod for mod in mods)
             and not any("VR" in mod and "Address Library" in mod for mod in mods)}
    shaders = {name for name, mods in lists.items() if any(mod.startswith("Community Shaders") for mod in mods)}
    print(f"{len(lists)} Skyrim SE lists, {len(shaders)} with Community Shaders "
          f"(index from {time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(CACHE)))})")
    return lists, shaders


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("count")
    command.add_argument("pattern")
    command.add_argument("--top", type=int, default=60)
    command = commands.add_parser("lists")
    command.add_argument("pattern")
    command.add_argument("--with", dest="pair", default=None)
    command = commands.add_parser("show")
    command.add_argument("name")
    command.add_argument("pattern")
    args = parser.parse_args()
    pattern = re.compile(args.pattern, re.I)
    lists, shaders = load_lists()

    if args.command == "count":
        counts = collections.Counter(mod for mods in lists.values() for mod in mods if pattern.search(mod))
        for mod, total in counts.most_common(args.top):
            print(f"{total:>3} lists ({sum(mod in lists[name] for name in shaders):>2} CS) | {mod}")
    elif args.command == "lists":
        pair = re.compile(args.pair, re.I) if args.pair else None
        for name in sorted(lists):
            hits = sorted(mod for mod in lists[name] if pattern.search(mod))
            if hits:
                extra = sorted(mod for mod in lists[name] if pair and pair.search(mod))
                print(f"{name}{' [CS]' if name in shaders else ''} ({len(lists[name])} mods): {hits}" + (f"\n    with: {extra}" if pair else ""))
    else:
        for name, mods in sorted(lists.items()):
            if args.name.lower() in name.lower():
                print(f"{name} ({len(mods)} mods): {sorted(mod for mod in mods if pattern.search(mod))}")


if __name__ == "__main__":
    main()
