#!/usr/bin/env python3
"""Reads a mod's FOMOD installer and installs it with explicit choices, without MO2's dialog.

  python tools/fomod.py extract <archive> <staging dir>        unpack with 7-Zip (skipped if already unpacked)
  python tools/fomod.py show <staging dir>                     steps, groups, options, defaults and their files
  python tools/fomod.py install <staging dir> <mod dir> [choices]

Choices look like "Group=Option;Step/Group=Option,Option". A group name alone is enough when it's unique;
use Step/Group when two steps reuse a name such as "Pick one". Names are compared without surrounding
spaces, since installers often pad them. Without a FOMOD, install copies the archive's data root.

Read `show` and the mod's description before choosing: this script never picks a default for you.
File and game dependencies in conditional installs are assumed present, so check those by hand.
7-Zip comes from the SEVEN_ZIP environment variable, or its default install folder.
"""
import os
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET

SEVEN_ZIP = os.environ.get("SEVEN_ZIP", r"C:\Program Files\7-Zip\7z.exe")
DATA_DIRS = {"meshes", "textures", "skse", "scripts", "interface", "sound", "seq", "grass", "lodsettings", "pbrnifpatcher",
             "pbrtexturesets", "parallaxgen", "shadersfx", "calientetools", "music", "strings", "video", "nemesis_engine",
             "dyndolod", "tools", "fomod", "docs", "distantlod", "lod", "terrain"}
DATA_EXTENSIONS = (".esp", ".esm", ".esl", ".bsa", ".ini", ".json")


def extract(archive, staging):
    if os.path.isdir(staging) and os.listdir(staging):
        print("already extracted:", staging)
        return
    os.makedirs(staging, exist_ok=True)
    result = subprocess.run([SEVEN_ZIP, "x", "-y", "-bso0", "-bsp0", archive, f"-o{staging}"], capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"7-Zip failed: {result.stderr[-2000:]}")
    print("extracted:", staging)


def find_config(staging):
    for folder, _, names in os.walk(staging):
        for name in names:
            if name.lower() == "moduleconfig.xml" and os.path.basename(folder).lower() == "fomod":
                return os.path.join(folder, name)
    return None


def load(path):
    raw = open(path, "rb").read()
    for encoding in ("utf-8-sig", "utf-16"):
        try:
            text = raw.decode(encoding)
            break
        except UnicodeDecodeError:
            continue
    return ET.fromstring(re.sub(r"<\?xml[^>]*\?>", "", text, count=1))


def files_of(node):
    if node is None:
        return []
    return [(item.tag.lower(), item.get("source", ""), item.get("destination"), int(item.get("priority", "0")))
            for item in node if item.tag.lower() in ("file", "folder")]


def options(config):
    for step in config.iter("installStep"):
        for group in step.iter("group"):
            for plugin in group.iter("plugin"):
                yield step, group, plugin


def show(staging):
    path = find_config(staging)
    if not path:
        print("no FOMOD; top level:", os.listdir(staging))
        return
    config = load(path)
    print("FOMOD:", config.findtext("moduleName"), "| base:", os.path.relpath(os.path.dirname(os.path.dirname(path)), staging))
    required = files_of(config.find("requiredInstallFiles"))
    if required:
        print("required:", [source for _, source, _, _ in required])
    for step in config.iter("installStep"):
        visible = step.find("visible")
        condition = f"  (visible if {ET.tostring(visible, encoding='unicode')[:200]})" if visible is not None else ""
        print(f"\n# STEP {step.get('name')}{condition}")
        for group in step.iter("group"):
            print(f"  ## {group.get('name')} [{group.get('type')}]")
            for plugin in group.iter("plugin"):
                descriptor = plugin.find("typeDescriptor")
                kind = descriptor.find(".//type") if descriptor is not None else None
                default = kind.get("name") if kind is not None else "?"
                patterns = descriptor.find("dependencyType") if descriptor is not None else None
                if patterns is not None:
                    default = "depends: " + " | ".join(
                        f"{p.find('type').get('name')} if {ET.tostring(p.find('dependencies'), encoding='unicode')[:160]}"
                        for p in patterns.iter("pattern"))
                text = (plugin.findtext("description") or "").strip().replace("\n", " ")[:160]
                sources = [source for _, source, _, _ in files_of(plugin.find("files"))]
                flags = [f"{flag.get('name')}={flag.text}" for flag in plugin.iter("flag")]
                print(f"    - {plugin.get('name')} <{default}> files={sources} flags={flags}\n        {text}")
    conditional = config.find("conditionalFileInstalls")
    if conditional is not None:
        print("\n# CONDITIONAL")
        for pattern in conditional.iter("pattern"):
            dependencies = re.sub(r"\s+", " ", ET.tostring(pattern.find("dependencies"), encoding="unicode"))[:300]
            print(f"  if {dependencies}\n     -> {[source for _, source, _, _ in files_of(pattern.find('files'))]}")


def resolve(base, relative):
    """Finds a path inside the unpacked archive, ignoring case as Windows installers do."""
    current = base
    for part in filter(None, re.split(r"[\\/]+", relative.strip("\\/"))):
        match = next((entry for entry in os.listdir(current) if entry.lower() == part.lower()), None)
        if match is None:
            raise FileNotFoundError(f"{relative} (no {part} in {current})")
        current = os.path.join(current, match)
    return current


def copy_item(source, target):
    if os.path.isdir(source):
        for folder, _, names in os.walk(source):
            for name in names:
                path = os.path.join(folder, name)
                destination = os.path.join(target, os.path.relpath(path, source))
                os.makedirs(os.path.dirname(destination), exist_ok=True)
                shutil.copy2(path, destination)
    else:
        os.makedirs(os.path.dirname(target), exist_ok=True)
        shutil.copy2(source, target)


def dependencies_met(node, flags):
    if node is None:
        return True
    results = []
    for child in node:
        if child.tag == "flagDependency":
            results.append(flags.get(child.get("flag")) == child.get("value"))
        elif child.tag == "dependencies":
            results.append(dependencies_met(child, flags))
        elif child.tag in ("fileDependency", "gameDependency", "fommDependency", "foseDependency"):
            results.append(child.get("state", "Active") != "Missing")
    return all(results) if node.get("operator", "And") == "And" else any(results)


def install(staging, mod_dir, choices=""):
    os.makedirs(mod_dir, exist_ok=True)
    path = find_config(staging)
    if not path:
        root = staging
        # Step through single wrapper folders until data shows up
        while True:
            entries = os.listdir(root)
            if len(entries) != 1 or any(e.lower() in DATA_DIRS or e.lower().endswith(DATA_EXTENSIONS) for e in entries):
                break
            if not os.path.isdir(os.path.join(root, entries[0])):
                break
            root = os.path.join(root, entries[0])
        if any(entry.lower() == "data" for entry in os.listdir(root)):
            root = resolve(root, "data")
        copy_item(root, mod_dir)
        print("copied data root", os.path.relpath(root, staging), "->", mod_dir)
        return
    config = load(path)
    base = os.path.dirname(os.path.dirname(path))
    wanted = {}
    for part in filter(None, choices.split(";")):
        key, _, picked = part.partition("=")
        wanted[key.strip()] = [option.strip() for option in picked.split(",") if option.strip()]
    plan = list(files_of(config.find("requiredInstallFiles")))
    flags = {}
    for step, group, plugin in options(config):
        keys = [f"{(step.get('name') or '').strip()}/{group.get('name').strip()}", group.get("name").strip()]
        chosen = next((wanted[key] for key in keys if key in wanted), None)
        if chosen is None or plugin.get("name").strip() not in chosen:
            continue
        plan += files_of(plugin.find("files"))
        for flag in plugin.iter("flag"):
            flags[flag.get("name")] = flag.text or ""
        print("chose:", group.get("name"), "->", plugin.get("name"))
    conditional = config.find("conditionalFileInstalls")
    if conditional is not None:
        for pattern in conditional.iter("pattern"):
            if dependencies_met(pattern.find("dependencies"), flags):
                plan += files_of(pattern.find("files"))
    for kind, source, destination, _ in sorted(plan, key=lambda entry: entry[3]):
        found = resolve(base, source)
        destination = source if destination is None else destination
        target = os.path.join(mod_dir, destination) if destination else mod_dir
        if kind == "file" and destination == "":
            target = os.path.join(mod_dir, os.path.basename(found))
        copy_item(found, target)
    print(f"installed {len(plan)} entries -> {mod_dir}; flags={flags}")


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] not in ("extract", "show", "install"):
        sys.exit(__doc__)
    if sys.argv[1] == "extract":
        extract(sys.argv[2], sys.argv[3])
    elif sys.argv[1] == "show":
        show(sys.argv[2])
    else:
        install(sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv) > 4 else "")
