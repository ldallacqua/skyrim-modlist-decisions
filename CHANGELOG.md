# Changelog

Each version says whether it's safe for an existing save. Mods are marked **Added**, **Moved**, **Updated**, **Incorporated** or **Dropped**, the legend Step uses.

## Unversioned (2026-11-02), save safety not assessed

Snapshot of the list: 82 mods under 17 separators.

- **Updated:** Community Shaders 1.8.4 to 1.9.1, which Grass Optimizations needs. NGIO now has a `GrassControl.ini` for extended grass. See [0014](decisions/0014-extended-grass-without-cache.md).
- **Added:** Animation Queue Fix 1.0.2 and Paired Animation Improvements 1.0.3, under Animation. Both are SKSE plugins that export the entry point SKSE needs on 1.5.97.
- **Updated:** Pandora 4.4.0-beta to 5.0.0-beta, Open Animation Replacer to 3.2.1, and Dyn FNIS AA functions to 3.1.1. Pandora was rerun, and its behavior files came out identical to 4.4's. See [0005](decisions/0005-pandora-behavior-engine.md).

- **Adopted:** decisions 0003, 0008, 0009, 0010 and 0012.
- **Moved:** `Recently Added` below `Outputs`.
- **Changed:** Pandora now writes to `Pandora - Outputs` through its own `-o` argument and finds the game with `--tesv`. MO2's redirects for Pandora and BodySlide were removed.
- **Moved:** Overwrite's SKSE and shader cache files into `SKSE - Outputs` and `ShaderCache - Outputs`.
- **Cleaned:** 44 plugins with Clean Load Order. The game hasn't been launched since. See [0011](decisions/0011-clean-plugins-with-backups.md).
- **Moved:** BodySlide output to `Bodyslide - Outputs`.
- **Updated:** JContainers SE to 4.3.4 and MCM Helper to 1.4.0.
