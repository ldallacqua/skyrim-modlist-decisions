# Changelog

Each version says whether it's safe for an existing save. Mods are marked **Added**, **Moved**, **Updated**, **Incorporated** or **Dropped**, the legend Step uses.

## Unversioned (2026-11-02), save safety not assessed

Snapshot of the list: 129 mods under 22 separators.

- **Added:** a plant overhaul from [the plant research](research/plants.md), in a new `Plants` separator between Trees & Grass and Architecture. Not yet seen in game.
  - **Meshes:** DrJacopo's 3D plants. That's Deathbell, Dragons Tongue (Dark Orange), Cathedral Mountain Flowers, Nightshade, Pine Shrubs, Snow Berries (Green), Stonecrop, Sword Ferns, Thicket and Dead Shrub, Thistle, Tundra Cotton, Tundra Shrubs, Lavender (Vanilla Size) and Clover (Full 3D PBR). Also Cathedral - Mushrooms, A Nirnroot with its PBR version, and snowy mountain flowers through Base Object Swapper.
  - **Textures:**
    - **Cathedral PBR Plants:** non-seasonal, default colors, Faultier's sword ferns and dry mushrooms, no glow.
    - **PBR Flora Overhaul:** every non-seasonal default except clover (DrJacopo's covers it), cabbage (Faultier's covers it), and the Reach tree and driftwood options, which ship tree meshes that would fight Nature of the Wild Lands.
  - **Shrubs:** Diverse high-quality PBR shrubs for the Reach, yellow and fall forest shrubs and the vine maple. DrJacopo's keeps tundra shrubs, thickets and dead shrubs.
  - **Ivy:** Animated Ivy (farmhouse and stonewall, through Base Object Swapper) and Tomato's PBR Vanilla Ivy.
  - **Conflicts on purpose:**
    - Faultier's keeps the tendril vines and the ruin ivy, since it loads after its gap fillers.
    - The new nirnroot and creep cluster meshes replace the copies Nature of the Wild Lands ships.
    - PBR Flora's glowing mushroom mesh replaces Particle Patch's.
  - **Result:** six new plugins, all ESL-flagged. Vanilla plant textures still in use by path fell from 103 to 44, and most of the rest are grass, which Merethic handles.
- **Regenerated:** PGPatcher with its output disabled first, as rule 14 says. PGPatcher itself refuses to run otherwise. It found 2,497 PBR entries, up from 2,365, with no errors. LOOT sorted before and after.

- **Added:** USSEP 4.2.5b, the last build for 1.5.97, at the top of Fixes.
- **Added:** a PBR visual set from [the research](research/pbr_trees_and_grass.md). The owner tried it in game on 2026-11-03 and reports it working well.
  - Four new separators sit between Armor and Gameplay: Models, Landscape, Trees & Grass, and Architecture. That's nature before structures, as decision 0003 suggests, with the order inside each one set by what the authors ask:
    - Better Dynamic Snow wins over SMIM.
    - Icy Mesh Remaster loads after Better Dynamic Snow.
    - TomatoRim loads after Icy Mesh, ERM and Blended Roads.
    - Vanaheimr's caves load after TomatoRim, whose cave ground they share.
    - Faultier's AIO comes after the mods that fill its gaps.
  - **Models:** SMIM, Assorted Mesh Fixes, and Better Dynamic Snow 3.6 (brighter snow, no glacier snow).
  - **Landscape:** Blended Roads, ERM meshes, Icy Mesh Remaster with its fixes, and TomatoRim PBR Landscapes 2K with its 1.7 update. TomatoRim ships its own road meshes and projected snow texture.
  - **Trees & Grass:** Nature of the Wild Lands with Autumn Rift, its Nordic Cut and Nordic Cut's CC Tundra Homestead patch, NOTWL PBR, DrJacopo's grass library meshes, Merethic Grasslands, and Merethic Grasslands PBR.
  - **Architecture:** Tomato's Imperial Forts Remake, TomatoRim Farmhouses, Tomato's Whiterun Remake, Tomato's Riften and Ratway, Vanaheimr Mines and Caves (PBR 2k with blending meshes), and Faultier's PBR Skyrim AIO 2k.
  - **Tools and frameworks:** Base Object Swapper (the 1.5.97 build, for IcyFixes' swaps) and AutoBlend, with its output in `AutoBlend - Outputs` before PGPatcher's.
- **Generated:** AutoBlend, then PGPatcher, for the new set. Both logs show no errors.
  - AutoBlend wrote `AutoBlend.esp` and blended 85 landscape meshes.
  - PGPatcher found 2,365 PBR entries and wrote `PGPatcher.esp` and `PG_1.esp`. The 3,707 loose files it patched match the winning mod's copy, so it didn't read its own old output.
  - All three plugins are ESL-flagged. The order already matches LOOT's rule that PGPatcher's plugins load after `AutoBlend.esp`.
- **Moved:** the files new in Overwrite to their homes. PGPatcher's and AutoBlend's settings and log went into their tool mods, Pandora's `Settings.json` into Pandora's mod, and the shader cache into `ShaderCache - Outputs`. Only `Root` is left.
- **Moved:** Assorted Mesh Fixes from Fixes to just after SMIM, because its author says it already includes SMIM's changes and should load after it.
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
