# 0005. Generate behaviors with Pandora

- **Status:** accepted (recorded after the fact)
- **Date:** 2026-11-02
- **Summary:** Pandora Behaviour Engine+ 5.0.0-beta generates behaviors and writes them to its own output mod.

## Context

The list uses Pandora with Open Animation Replacer and OStim, and loads `fnis_aa.dll` through Dyn FNIS AA functions. The original comparison with Nemesis wasn't written down.

An earlier version of this record said to stay on 4.4.0-beta until version 5 was tested on a cloned profile, because 5 reworks FNIS handling. Pandora was updated to 5.0.0-beta on 2026-11-02 without that test, together with Open Animation Replacer 3.2.1 and Dyn FNIS AA functions 3.1.1.

## Options considered

- **Pandora 4.4.0-beta:** worked.
- **Pandora 5.0.0-beta:** the current release, with reworked FNIS building.
- **Nemesis or FNIS:** not compared in depth.

## Decision

Keep 5.0.0-beta. Its first run, with the same patches as the last 4.4 run, produced behavior files identical to 4.4's: 13 of 15 files match byte for byte, and the other two are its log and run record. It wrote only to `Pandora - Outputs`, and nothing landed in Overwrite.

Version 5 logs new warnings, `Scan FNIS Animations > FAILED`, for the OStim, MSSL and NickNak animation folders. None of those folders contain FNIS list files, so there is nothing for that scan to read. That's our reading of the log, not something Pandora documents.

## Consequences

- Animations haven't been tested in game with version 5.
- Any change to animations, behaviors or the skeleton means rerunning Pandora. Don't update Pandora in the middle of a save without a backup.
- The 4.4 output is kept as a backup outside MO2.

## Confirmation

`tools/check.py` requires Pandora to be enabled and `Pandora - Outputs` to exist. After each run, check that Overwrite is empty and read the log's warnings.

## Revisit when

An animation breaks in game, a new warning appears in the log, or Pandora 5 leaves beta.

## Evidence

- [Pandora](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus): usage and arguments.
- [Pandora's argument parser](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/blob/main/Pandora.Skyrim/CLI/CommandLineParser.cs): `-o`/`--output` and `--tesv` as used here, unchanged since before 5.0.0-beta.
- [MO2 plugins and tools](../research/mo2_plugins_and_tools.md): version status as of 2026-11-02.
