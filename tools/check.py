#!/usr/bin/env python3
"""Compares list/ with rules/rules.json. Each check cites the decision it enforces.

A check on an accepted decision fails the run. A check on a proposed decision only warns.
Usage: python tools/check.py
"""
import csv
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FORBIDDEN_NAMES = {"modorganizer.ini", "nxmhandler.ini", "skyrim.ini", "skyrimprefs.ini", "skyrimcustom.ini"}
FORBIDDEN_TYPES = {".esp", ".esm", ".esl", ".bsa", ".dds", ".nif", ".ess", ".skse", ".dll", ".exe", ".7z", ".zip", ".rar"}
SECRET_PATTERNS = (
    re.compile(r"[A-Za-z]:[\\/]+Users[\\/]+", re.IGNORECASE),
    re.compile(r"\bapi[_-]?key\s*[=:]\s*\S{12,}", re.IGNORECASE),
    re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+"),
)
TEXT_TYPES = {".md", ".txt", ".csv", ".json", ".py", ".yml", ".yaml"}
SKIP_DIRS = {".git", "__pycache__"}


def load_rows():
    with open(os.path.join(ROOT, "list", "mods.csv"), encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def repository_files():
    for folder, dirs, files in os.walk(ROOT):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        for name in files:
            yield os.path.join(folder, name)


def check_no_secrets(rows, rules):
    problems = []
    for path in repository_files():
        if os.path.splitext(path)[1].lower() not in TEXT_TYPES or os.path.abspath(path) == os.path.abspath(__file__):
            continue
        with open(path, encoding="utf-8", errors="replace") as file:
            for number, line in enumerate(file, 1):
                if any(pattern.search(line) for pattern in SECRET_PATTERNS):
                    problems.append(f"{os.path.relpath(path, ROOT)}:{number} looks like a secret or personal path")
    return problems


def check_no_forbidden_files(rows, rules):
    return [
        f"{os.path.relpath(path, ROOT)} must not be published"
        for path in repository_files()
        if os.path.basename(path).lower() in FORBIDDEN_NAMES or os.path.splitext(path)[1].lower() in FORBIDDEN_TYPES
    ]


def check_separator_order(rows, rules):
    actual = [row["name"] for row in rows if row["type"] == "separator"]
    return [] if actual == rules["separators"] else [f"separators are {actual}, expected {rules['separators']}"]


def check_required_mods(rows, rules):
    enabled = {row["name"] for row in rows if row["type"] == "mod" and row["enabled"] == "yes"}
    return [f"required mod is missing or disabled: {name}" for name in rules["required_mods"] if name not in enabled]


def check_outputs(rows, rules):
    section = {row["name"]: row["separator"] for row in rows if row["type"] == "mod"}
    return [f"{name} should be under {rules['outputs_separator']}" for name in rules["output_mods"] if section.get(name) != rules["outputs_separator"]]


def check_inbox_empty(rows, rules):
    return [f"{row['name']} is still in {rules['inbox_separator']}" for row in rows if row["type"] == "mod" and row["separator"] == rules["inbox_separator"]]


def check_inbox_last(rows, rules):
    last = [row["name"] for row in rows if row["type"] == "separator"][-1]
    return [] if last == rules["inbox_separator"] else [f"the last separator is {last}, not {rules['inbox_separator']}"]


CHECKS = (
    ("No secrets or personal paths", "0013", check_no_secrets),
    ("No mod, save or config files", "0013", check_no_forbidden_files),
    ("Separators in the agreed order", "0003", check_separator_order),
    ("Required mods enabled", "0001", check_required_mods),
    ("Each generator has its output mod", "0007", check_outputs),
    ("Inbox is empty", "0012", check_inbox_empty),
    ("Inbox is the last separator", "0012", check_inbox_last),
)


def decision_status(number):
    folder = os.path.join(ROOT, "decisions")
    for name in os.listdir(folder):
        if name.startswith(number + "-"):
            with open(os.path.join(folder, name), encoding="utf-8") as file:
                return re.search(r"\*\*Status:\*\* (\w+)", file.read())[1]
    return None


def main():
    rows = load_rows()
    with open(os.path.join(ROOT, "rules", "rules.json"), encoding="utf-8") as file:
        rules = json.load(file)
    failures = warnings = 0
    for title, number, check in CHECKS:
        status = decision_status(number)
        if status is None:
            print(f"FAIL  {title}: decision {number} doesn't exist")
            failures += 1
            continue
        problems = check(rows, rules)
        label = "ok  " if not problems else "WARN" if status == "proposed" else "FAIL"
        print(f"{label}  {title} [{number}, {status}]")
        for problem in problems:
            print(f"        {problem}")
        if problems:
            if status == "proposed":
                warnings += 1
            else:
                failures += 1
    print(f"\n{failures} failed, {warnings} warnings")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
