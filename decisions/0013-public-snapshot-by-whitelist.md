# 0013. Publish the real list, by whitelist, as text only

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** The repository holds the actual list, exported by a script that copies only named files and fields.

## Context

Decisions are more useful next to the real list they govern, so a change can be diffed and checked. The list includes adult mods, and the owner chose to publish it knowing that.

## Options considered

- **Decisions only:** nothing personal is exposed, but nothing can be checked.
- **Decisions plus the list:** can be checked, and it shows every mod.

## Decision

Publish the list. `tools/snapshot.py` copies `modlist.txt`, `plugins.txt` and `loadorder.txt`, takes only the version and mod ID from each `meta.ini`, and takes only plugin names and counts from Clean Load Order's reports. The [site](https://ldallacqua.github.io/skyrim-modlist-decisions/) is built from these same files.

Never published: saves, mod files, `downloads/`, generated output, `ModOrganizer.ini`, INIs, logs and keys. Adult mods appear as factual names only, with no images.

## Consequences

- Naming mods follows the same logic as Nexus Collections, which reference mods without including their files. We found no rule specific to GitHub, and this is practical reasoning, not legal advice.
- This repository is not a Wabbajack list, and becoming one would mean reviewing its licensing.

## Confirmation

`tools/check.py` scans for secrets and personal paths, and rejects mod and save file types.

## Revisit when

A mod author objects, or the list becomes a distributed Wabbajack list.

## Evidence

- [Nexus Mods, guidelines for Collections](https://help.nexusmods.com/article/115-guidelines-for-collections).
- [GitHub, sexually obscene content policy](https://docs.github.com/en/site-policy/acceptable-use-policies/github-sexually-obscene-content).
- [Documenting decisions](../research/documenting_decisions.md): the full notes.
