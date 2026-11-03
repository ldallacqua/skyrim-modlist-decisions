#!/usr/bin/env python3
"""Works on the MO2 instance directly, for what MO2's interface would otherwise do by hand.

  python tools/mo2.py install <mod folder> --mod <id> --version <v> --part <file id>[:<choices>] [...]
  python tools/mo2.py separator <name> --above <existing separator>
  python tools/mo2.py place <separator> <mod> [...] [--after <mod>]
  python tools/mo2.py enable <mod> [...]  /  disable <mod> [...]
  python tools/mo2.py exe-args <executable title> [--set "<arguments>"]
  python tools/mo2.py loot-update on|off
  python tools/mo2.py enable-plugins <mod folder> [...]
  python tools/mo2.py headers <plugin file or mod folder> [...]
  python tools/mo2.py conflicts <mod> [...] [--all]
  python tools/mo2.py downloads [--fix]
  python tools/mo2.py pgpatcher-check

install unpacks each downloaded file (found by its file id in downloads/*.meta), runs its FOMOD with the
given choices (see tools/fomod.py), writes the mod's meta.ini with the choices in its notes, and marks
the downloads installed. A part given without ":" refuses to guess when the archive has a FOMOD; "id:"
installs only a FOMOD's required files.

place moves mods to the end of a separator's section, in the order given, so the last one wins
conflicts; --after puts them right after a mod in that section instead. enable-plugins appends a mod's
plugins to the load order for LOOT to sort. downloads reports archives whose flags disagree with the mods
folder, and --fix clears a wrong "uninstalled". pgpatcher-check confirms PGPatcher patched the files
that really win, not its own earlier output.

Commands that write profile files refuse to run while MO2 is open, because MO2 rewrites them on exit.
The instance comes from MO2_DIR (default C:\\Modding\\MO2) and the profile from MO2_PROFILE (default Default).
"""
import argparse
import collections
import configparser
import glob
import json
import os
import re
import shutil
import stat
import struct
import subprocess
import sys
import zlib

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fomod  # noqa: E402

MO2 = os.environ.get("MO2_DIR", r"C:\Modding\MO2")
PROFILE = os.path.join(MO2, "profiles", os.environ.get("MO2_PROFILE", "Default"))
MODS = os.path.join(MO2, "mods")
DOWNLOADS = os.path.join(MO2, "downloads")
SEPARATOR = "_separator"


def require_mo2_closed():
    # tasklist answers in the console's code page, which UTF-8 mode can't decode when Windows isn't in English
    tasks = subprocess.run(["tasklist", "/FI", "IMAGENAME eq ModOrganizer.exe"], capture_output=True, text=True,
                           errors="replace").stdout
    if "ModOrganizer.exe" in tasks:
        sys.exit("Close MO2 first: it rewrites the profile files when it exits.")


def read_lines(path):
    with open(path, encoding="utf-8") as file:
        return file.read().splitlines()


def write_lines(path, lines):
    with open(path, "w", encoding="utf-8", newline="\r\n") as file:
        file.write("\n".join(lines) + "\n")


def ini_string(value):
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


# install

def download_for(file_id):
    for meta in glob.glob(os.path.join(glob.escape(DOWNLOADS), "*.meta")):
        if re.search(rf"^fileID={file_id}$", open(meta, encoding="utf-8", errors="replace").read(), re.M):
            return meta[:-5]
    sys.exit(f"no download with file id {file_id}; fetch it with tools/nexus.py get")


def set_download_flags(archive, installed):
    path = archive + ".meta"
    text = open(path, encoding="utf-8", errors="surrogateescape").read()
    # Anchored to the line start, because "installed=" also ends "uninstalled="
    text = re.sub(r"^installed=\w+$", f"installed={str(installed).lower()}", text, flags=re.M)
    text = re.sub(r"^uninstalled=\w+$", f"uninstalled={str(not installed).lower()}", text, flags=re.M)
    open(path, "w", encoding="utf-8", errors="surrogateescape").write(text)


def remove_tree(path):
    """rmtree that clears the read-only flag some archives set on their folders, which Windows won't delete otherwise."""
    def retry(function, target, _):
        os.chmod(target, stat.S_IWRITE)
        function(target)
    shutil.rmtree(path, onerror=retry)


def install(folder, mod_id, version, parts, merge, keep_staging):
    target = os.path.join(MODS, folder)
    if os.path.exists(target) and not merge:
        sys.exit(f"{folder} already exists; pass --merge to add to it")
    installed, notes = [], []
    for part in parts:
        file_id, has_choices, choices = part.partition(":")
        archive = download_for(file_id)
        staging = os.path.join(MO2, "_staging", file_id)
        fomod.extract(archive, staging)
        if not has_choices and fomod.find_config(staging):
            fomod.show(staging)
            sys.exit(f"\n{os.path.basename(archive)} has a FOMOD: read the options above and pass --part {file_id}:<choices>")
        fomod.install(staging, target, choices)
        installed.append((os.path.basename(archive), file_id))
        if choices:
            notes.append(f"{os.path.basename(archive)}: {choices}")
        if not keep_staging:
            remove_tree(staging)
    lines = ["[General]", "gameName=SkyrimSE", f"modid={mod_id}", f"version={version}", f"newestVersion={version}",
             "category=", "nexusFileStatus=1", f"installationFile={installed[-1][0]}", "repository=Nexus", "ignoredVersion=",
             "comments=", f"notes={ini_string(' | '.join(notes))}", "url=", "hasCustomURL=false", "converted=false",
             "validated=false", "", "[installedFiles]", f"size={len(installed)}"]
    for number, (_, file_id) in enumerate(installed, 1):
        lines += [f"{number}\\modid={mod_id}", f"{number}\\fileid={file_id}"]
    with open(os.path.join(target, "meta.ini"), "w", encoding="utf-8") as file:
        file.write("\n".join(lines) + "\n")
    for archive, _ in installed:
        set_download_flags(os.path.join(DOWNLOADS, archive), True)
    print(f"installed {folder}; now place it with: python tools/mo2.py place <separator> \"{folder}\"")


# modlist.txt is stored highest priority first, and a separator's line comes after its own mods

def new_separator(name, above):
    require_mo2_closed()
    path = os.path.join(PROFILE, "modlist.txt")
    lines = read_lines(path)
    anchor = f"-{above}{SEPARATOR}"
    if anchor not in lines:
        sys.exit(f"no separator named {above}")
    lines.insert(lines.index(anchor) + 1, f"-{name}{SEPARATOR}")
    folder = os.path.join(MODS, name + SEPARATOR)
    os.makedirs(folder, exist_ok=True)
    template = next(iter(glob.glob(os.path.join(glob.escape(MODS), "*" + SEPARATOR, "meta.ini"))), None)
    if template and not os.path.exists(os.path.join(folder, "meta.ini")):
        shutil.copyfile(template, os.path.join(folder, "meta.ini"))  # keeps the separators' shared color
    write_lines(path, lines)
    print(f"added separator {name} above {above}; add it to rules/rules.json too")


def set_enabled(mods, enabled):
    """Turns mods on or off. Turning one off also drops its plugins, so tools don't read a missing plugin."""
    require_mo2_closed()
    path = os.path.join(PROFILE, "modlist.txt")
    lines = read_lines(path)
    for mod in mods:
        if f"+{mod}" not in lines and f"-{mod}" not in lines:
            sys.exit(f"{mod} isn't in modlist.txt")
    lines = [("+" if enabled else "-") + line[1:] if line[1:] in mods else line for line in lines]
    write_lines(path, lines)
    if not enabled:
        plugins = {os.path.basename(p).lower() for mod in mods
                   for p in glob.glob(os.path.join(glob.escape(os.path.join(MODS, mod)), "*.es[pml]"))}
        for name in ("plugins.txt", "loadorder.txt"):
            listed = os.path.join(PROFILE, name)
            write_lines(listed, [line for line in read_lines(listed) if line.lstrip("*").lower() not in plugins])
        print(f"disabled {len(mods)} mods and dropped their plugins: {', '.join(sorted(plugins)) or 'none'}")
    else:
        print(f"enabled {len(mods)} mods; enable their plugins with enable-plugins, then sort with LOOT")


def executable_arguments(title, value):
    """Shows or sets an MO2 executable's arguments, stored as <n>\\arguments= under [customExecutables]."""
    path = os.path.join(MO2, "ModOrganizer.ini")
    text = open(path, encoding="utf-8").read()
    found = re.search(rf"^(\d+)\\title={re.escape(title)}$", text, re.M)
    if not found:
        sys.exit(f"no MO2 executable titled {title}")
    pattern = rf"^{found[1]}\\arguments=.*$"
    if value is not None:
        require_mo2_closed()
        text = re.sub(pattern, lambda _: f"{found[1]}\\arguments={value}", text, count=1, flags=re.M)
        open(path, "w", encoding="utf-8").write(text)
    print(re.search(pattern, text, re.M)[0])


def loot_masterlist_update(enabled):
    """LOOT's own update can time out and leave an empty masterlist, so sorts run with it off."""
    path = os.path.join(os.environ["LOCALAPPDATA"], "LOOT", "settings.toml")
    text = re.sub(r"^updateMasterlist = \w+", f"updateMasterlist = {str(enabled).lower()}",
                  open(path, encoding="utf-8").read(), count=1, flags=re.M)
    open(path, "w", encoding="utf-8").write(text)
    print(re.search(r"^updateMasterlist = \w+", text, re.M)[0])


def place(separator, mods, after):
    require_mo2_closed()
    path = os.path.join(PROFILE, "modlist.txt")
    lines = [line for line in read_lines(path) if line[1:] not in mods]
    for mod in mods:
        if not os.path.isdir(os.path.join(MODS, mod)):
            sys.exit(f"no mod folder named {mod}")
    anchor = f"-{separator}{SEPARATOR}"
    if anchor not in lines:
        sys.exit(f"no separator named {separator}")
    if after:
        position = lines.index(f"+{after}") if f"+{after}" in lines else lines.index(f"-{after}")
    else:
        position = lines.index(anchor)
        while position > 0 and not lines[position - 1].endswith(SEPARATOR):
            position -= 1
    lines[position:position] = [f"+{mod}" for mod in reversed(mods)]
    write_lines(path, lines)
    print(f"placed {len(mods)} mods in {separator}, enabled")


# Plugins

def header(path):
    data = open(path, "rb").read(1 << 20)
    size, flags = struct.unpack_from("<II", data, 4)
    form_version = struct.unpack_from("<H", data, 20)[0]
    position, version, records, masters = 24, None, None, []
    while position < 24 + size:
        name, length = struct.unpack_from("<4sH", data, position)
        body = data[position + 6:position + 6 + length]
        if name == b"HEDR":
            version, records = struct.unpack_from("<fi", body)
        elif name == b"MAST":
            masters.append(body.rstrip(b"\0").decode("cp1252"))
        position += 6 + length
    return flags, version, form_version, records, masters


def headers(targets):
    paths = []
    for target in targets:
        folder = target if os.path.isdir(target) else os.path.join(MODS, target)
        paths += sorted(glob.glob(os.path.join(glob.escape(folder), "*.es[pml]"))) if os.path.isdir(folder) else [target]
    for path in paths:
        flags, version, form_version, records, masters = header(path)
        kind = "+".join(name for bit, name in ((1, "ESM"), (0x200, "ESL")) if flags & bit) or "ESP"
        print(f"{os.path.basename(path)} | {kind} | HEDR {version:.2f} | form {form_version} | {records} records"
              f" | masters: {', '.join(masters)}")


def enable_plugins(mods):
    require_mo2_closed()
    found = []
    for mod in mods:
        for path in sorted(glob.glob(os.path.join(glob.escape(os.path.join(MODS, mod)), "*.es[pml]"))):
            is_master = header(path)[0] & 1 or path.lower().endswith(".esm")
            found.append((not is_master, os.path.basename(path)))
    # Masters first; a plugin shipped by two mods (one replacing the other) is listed once
    names = list(dict.fromkeys(name for _, name in sorted(found, key=lambda item: item[0])))
    order_path, plugins_path = os.path.join(PROFILE, "loadorder.txt"), os.path.join(PROFILE, "plugins.txt")
    order, plugins = read_lines(order_path), read_lines(plugins_path)
    known_order = {line.lower() for line in order}
    known_plugins = {line.lstrip("*").lower() for line in plugins}
    order += [name for name in names if name.lower() not in known_order]
    plugins += ["*" + name for name in names if name.lower() not in known_plugins]
    write_lines(order_path, order)
    write_lines(plugins_path, plugins)
    print(f"enabled: {', '.join(names)}\nnow sort with LOOT (see AGENTS.md)")


# Checks

def mod_files(mod):
    root = os.path.join(MODS, mod)
    found = set()
    for folder, _, names in os.walk(root):
        for name in names:
            relative = os.path.relpath(os.path.join(folder, name), root).lower()
            if relative != "meta.ini" and not relative.startswith(("fomod", "docs")):
                found.add(relative)
    return found


def enabled_mods():
    """Enabled mods, highest priority first."""
    return [line[1:] for line in read_lines(os.path.join(PROFILE, "modlist.txt")) if line.startswith("+")]


def conflicts(mods, against_all):
    def report(a, b, files_a, files_b):
        both = files_a & files_b
        if both:
            kinds = collections.Counter(path.split(os.sep)[0] for path in both)
            print(f"{len(both):>6}  {a}  <->  {b}   {dict(kinds)}   e.g. {sorted(both)[:3]}")

    if against_all:
        others = [mod for mod in enabled_mods() if os.path.isdir(os.path.join(MODS, mod))]
        cache = {mod: mod_files(mod) for mod in set(others) | set(mods)}
        for mod in mods:
            for other in others:
                if other != mod:
                    report(mod, other, cache[mod], cache[other])
    else:
        cache = {mod: mod_files(mod) for mod in mods}
        for index, a in enumerate(mods):
            for b in mods[index + 1:]:
                report(a, b, cache[a], cache[b])


def downloads(fix):
    if fix:
        require_mo2_closed()
    archives, pairs = {}, {}
    for path in glob.glob(os.path.join(glob.escape(MODS), "*", "meta.ini")):
        parser = configparser.RawConfigParser(strict=False, interpolation=None)
        try:
            parser.read(path, encoding="utf-8")
        except (configparser.Error, UnicodeDecodeError):
            continue
        mod = os.path.basename(os.path.dirname(path))
        archive = parser.get("General", "installationFile", fallback="")
        if archive:
            archives[os.path.basename(archive.replace("\\", "/")).lower()] = mod
        if parser.has_section("installedFiles"):
            section = parser["installedFiles"]
            for number in range(1, int(section.get("size", "0")) + 1):
                pairs[(section.get(f"{number}\\modid"), section.get(f"{number}\\fileid"))] = mod
    for meta in sorted(glob.glob(os.path.join(glob.escape(DOWNLOADS), "*.meta"))):
        archive = meta[:-5]
        fields = dict(line.split("=", 1) for line in open(meta, encoding="utf-8", errors="replace").read().splitlines() if "=" in line)
        mod = archives.get(os.path.basename(archive).lower()) or pairs.get((fields.get("modID"), fields.get("fileID")))
        marked_gone = fields.get("uninstalled") == "true"
        if mod and marked_gone:
            print(f"wrongly uninstalled, in {mod}: {os.path.basename(archive)}")
            if fix:
                set_download_flags(archive, True)
        elif not mod and marked_gone:
            print(f"uninstalled, safe to delete if no longer wanted: {os.path.basename(archive)}")


def pgpatcher_check():
    """ParallaxGen_Diff.json keeps each patched file's CRC32 from before patching."""
    output = "PGPatcher - Outputs"
    winners = {}
    for mod in reversed([mod for mod in enabled_mods() if mod != output]):
        root = os.path.join(MODS, mod)
        for folder, _, names in os.walk(root):
            for name in names:
                winners[os.path.relpath(os.path.join(folder, name), root).lower()] = mod
    with open(os.path.join(MODS, output, "ParallaxGen_Diff.json"), encoding="utf-8") as file:
        diff = json.load(file)
    result, different = collections.Counter(), []
    for relative, crcs in diff.items():
        mod = winners.get(relative.lower())
        if mod is None:
            result["from a BSA"] += 1
        elif zlib.crc32(open(os.path.join(MODS, mod, relative), "rb").read()) == crcs["crc32original"]:
            result["match the winning loose file"] += 1
        else:
            result["differ"] += 1
            different.append(f"{relative} <- {mod}")
    print(f"{len(diff)} patched files: {dict(result)}")
    for line in different[:20]:
        print("  differs:", line)


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    commands = parser.add_subparsers(dest="command", required=True)
    command = commands.add_parser("install")
    command.add_argument("folder")
    command.add_argument("--mod", required=True)
    command.add_argument("--version", required=True)
    command.add_argument("--part", action="append", required=True)
    command.add_argument("--merge", action="store_true")
    command.add_argument("--keep-staging", action="store_true")
    command = commands.add_parser("separator")
    command.add_argument("name")
    command.add_argument("--above", required=True)
    command = commands.add_parser("place")
    command.add_argument("separator")
    command.add_argument("mods", nargs="+")
    command.add_argument("--after")
    command = commands.add_parser("exe-args")
    command.add_argument("title")
    command.add_argument("--set", dest="value")
    commands.add_parser("loot-update").add_argument("state", choices=("on", "off"))
    commands.add_parser("enable").add_argument("mods", nargs="+")
    commands.add_parser("disable").add_argument("mods", nargs="+")
    commands.add_parser("enable-plugins").add_argument("mods", nargs="+")
    commands.add_parser("headers").add_argument("targets", nargs="+")
    command = commands.add_parser("conflicts")
    command.add_argument("mods", nargs="+")
    command.add_argument("--all", action="store_true")
    commands.add_parser("downloads").add_argument("--fix", action="store_true")
    commands.add_parser("pgpatcher-check")
    args = parser.parse_args()
    if args.command == "install":
        install(args.folder, args.mod, args.version, args.part, args.merge, args.keep_staging)
    elif args.command == "separator":
        new_separator(args.name, args.above)
    elif args.command == "place":
        place(args.separator, args.mods, args.after)
    elif args.command == "exe-args":
        executable_arguments(args.title, args.value)
    elif args.command == "loot-update":
        loot_masterlist_update(args.state == "on")
    elif args.command in ("enable", "disable"):
        set_enabled(args.mods, args.command == "enable")
    elif args.command == "enable-plugins":
        enable_plugins(args.mods)
    elif args.command == "headers":
        headers(args.targets)
    elif args.command == "conflicts":
        conflicts(args.mods, args.all)
    elif args.command == "downloads":
        downloads(args.fix)
    else:
        pgpatcher_check()


if __name__ == "__main__":
    main()
