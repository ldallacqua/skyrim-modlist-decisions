#!/usr/bin/env python3
"""Exports a Mod Organizer 2 profile into list/, so the list can be diffed and checked.

Usage: python tools/snapshot.py <MO2 folder> [profile]

It works from a whitelist on purpose: only the files named below are copied, and mods.csv only takes the
fields named below from each mod's meta.ini. Saves, INIs, ModOrganizer.ini and mod files never come along.
"""
import configparser
import csv
import glob
import os
import re
import shutil
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROFILE_FILES = ("modlist.txt", "plugins.txt", "loadorder.txt")
SEPARATOR = "_separator"


def read_meta(path):
    parser = configparser.RawConfigParser(strict=False, interpolation=None)
    try:
        parser.read(path, encoding="utf-8")
    except (configparser.Error, UnicodeDecodeError):
        return "", ""
    return parser.get("General", "version", fallback=""), parser.get("General", "modid", fallback="")


def read_pane(modlist_path):
    """modlist.txt is stored highest priority first, the reverse of what the left pane shows."""
    with open(modlist_path, encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip() and not line.startswith("#")]
    return [(line[0], line[1:]) for line in reversed(lines)]


def snapshot(mo2, profile):
    source = os.path.join(mo2, "profiles", profile)
    target = os.path.join(ROOT, "list")
    os.makedirs(target, exist_ok=True)
    for name in PROFILE_FILES:
        shutil.copyfile(os.path.join(source, name), os.path.join(target, name))
    rows, section = [], ""
    for position, (state, name) in enumerate(read_pane(os.path.join(source, "modlist.txt")), 1):
        if name.endswith(SEPARATOR):
            section = name[: -len(SEPARATOR)]
            rows.append((position, "separator", section, "", section, "", ""))
        elif state == "*":
            rows.append((position, "unmanaged", name, "yes", section, "", ""))
        else:
            version, modid = read_meta(os.path.join(mo2, "mods", name, "meta.ini"))
            rows.append((position, "mod", name, "yes" if state == "+" else "no", section, version, "" if modid in ("", "0", "-1") else modid))
    with open(os.path.join(target, "mods.csv"), "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(("position", "type", "name", "enabled", "separator", "version", "nexus_id"))
        writer.writerows(rows)
    write_cleaning(mo2, target)
    return rows


def write_cleaning(mo2, target):
    """Sums what Clean Load Order reports across its runs. Only plugin names and counts come along, never the paths."""
    totals = {}
    for report in sorted(glob.glob(os.path.join(glob.escape(mo2), "cleaning-backups", "*", "report.txt"))):
        with open(report, encoding="utf-8") as file:
            for line in file:
                cleaned = re.match(r"CLEANED (.+?): (\d+) ITMs, (\d+) UDRs\.", line)
                navmesh = re.match(r"NAVMESH (.+?): (\d+)", line)
                if cleaned:
                    entry = totals.setdefault(cleaned[1], [0, 0, 0])
                    entry[0] += int(cleaned[2])
                    entry[1] += int(cleaned[3])
                elif navmesh:
                    totals.setdefault(navmesh[1], [0, 0, 0])[2] = int(navmesh[2])
    with open(os.path.join(target, "cleaning.csv"), "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(("plugin", "itm", "udr", "deleted_navmeshes"))
        writer.writerows((name, *counts) for name, counts in sorted(totals.items()))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    rows = snapshot(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "Default")
    kinds = [row[1] for row in rows]
    print(f"{kinds.count('mod')} mods, {kinds.count('separator')} separators, {kinds.count('unmanaged')} unmanaged")
