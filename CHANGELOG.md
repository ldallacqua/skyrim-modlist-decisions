# Changelog

Each version says whether it's safe for an existing save. Mods are marked **Added**, **Moved**, **Updated**, **Incorporated** or **Dropped**, the legend Step uses.

## Unversioned (2026-11-02), save safety not assessed

First snapshot of the list: 80 mods under 17 separators.

- **Adopted:** decisions 0003, 0008, 0009, 0010 and 0012.
- **Moved:** `Recently Added` below `Outputs`.
- **Changed:** Pandora now writes to `Pandora - Outputs` through its own `-o` argument and finds the game with `--tesv`. MO2's redirects for Pandora and BodySlide were removed. Pandora hasn't been rerun since.
- **Moved:** Overwrite's SKSE and shader cache files into `SKSE - Outputs` and `ShaderCache - Outputs`.
- **Cleaned:** 44 plugins with Clean Load Order. The game hasn't been launched since. See [0011](decisions/0011-clean-plugins-with-backups.md).
- **Moved:** BodySlide output to `Bodyslide - Outputs`.
- **Updated:** JContainers SE to 4.3.4 and MCM Helper to 1.4.0.
