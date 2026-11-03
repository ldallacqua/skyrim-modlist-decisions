# 0002. Run from a separate game folder and test on a cloned profile

- **Status:** accepted (recorded after the fact)
- **Date:** 2026-11-02
- **Summary:** MO2's game path points to a dedicated copy of the game, which Steam can't update.

## Context

A downgraded game ([0001](0001-pin-skyrim-se-1597-with-cc.md)) has to stay out of reach of Steam updates. Plugin cleaning also rewrites official masters in place ([0011](0011-clean-plugins-with-backups.md)), which shouldn't touch the Steam install.

## Options considered

- **Separate folder:** safe from updates, at a cost of about 12 GB. The downgraded state may be impossible to reproduce by downloading, so it needs its own backup.
- **Steam folder:** no extra disk, but exposed to updates and verification.

## Decision

Keep the separate folder and keep a single zip of it as the recovery point. The profile uses local saves and local INIs.

## Consequences

- Tools that find the game through the Windows registry can open the Steam install instead. This happened in practice: SSEEdit, launched without `-D:`, cleaned a plugin in the Steam folder. Pass the data folder explicitly to any such tool.
- New builds are tested on a cloned profile with a new character, never on an old save. Check that `settings.ini` overrides were copied to the clone.

## Confirmation

By hand: `gamePath` in `ModOrganizer.ini` points to the separate folder, and the zip exists.

## Revisit when

Moving to a current game version, or adopting a list manager that handles this differently.

## Evidence

- [Wabbajack, keeping the game folder clean](https://wiki.wabbajack.org/modlist_author_documentation/Keeping%20the%20Game%20Folder%20clean.html): the Stock Game pattern and its size.
- [Step 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3): testing new builds on a new character.
