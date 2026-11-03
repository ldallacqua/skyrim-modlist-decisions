# Plants for a PBR list

Checked 2026-11-03. Question: which mods replace the vanilla plants that now stand out against the PBR landscape, for this list (Community Shaders 1.9.1, Faultier's PBR Skyrim, TomatoRim PBR Landscapes, Nature of the Wild Lands with Nordic Cut, Merethic Grasslands, PGPatcher, Base Object Swapper, no Seasons of Skyrim).

The evidence comes from the same sources as [the PBR note](../research/pbr_trees_and_grass.md): Wabbajack's published reports for what lists install, and Nexus Mods' public API for descriptions, requirements and file lists. Counting lists measures adoption, not quality. Two kinds of evidence are new here:
- **What still looks vanilla** was measured from this profile with `tools/coverage.py`, which reads the game's own BSAs and every enabled mod.
- **What a candidate replaces** comes from the archive previews Nexus publishes for each file, so nothing was downloaded.

## Takeaway

Almost every plant in the game is still vanilla. Apart from Faultier's food crops, our mods replace 1 of the 204 vanilla plant and grass textures. Nearly all the plant meshes in PGPatcher's output are vanilla meshes it only re-patched. That's why they stand out next to Faultier's and TomatoRim.

The PBR lists that look like ours converge on one kit:
- DrJacopo's Cathedral 3D plant meshes;
- **Cathedral PBR Plants** for their textures;
- **PBR Flora Overhaul** for the plants the 3D set doesn't touch;
- Tomato's PBR Vanilla Ivy.

jepster, who made both PBR mods, adds a third, **Diverse high-quality PBR shrubs**, and says the three "together shall cover most of Skyrim's Flora without overlap and conflicts". By path, the kit covers 62 of the 103 vanilla plant textures still in use. The shrub mod replaces 22 more shrub types through Base Object Swapper, which a path count can't see. What it leaves is mostly grass, which is Merethic's job.

## What still looks vanilla

Counted over the base game and DLC plant and grass folders. A vanilla file counts as replaced when an enabled mod ships it, or ships a PBR texture at the same path. PGPatcher's and AutoBlend's outputs don't count.

| | Count |
|---|---|
| Vanilla plant and grass files (meshes and textures) | 679 |
| Diffuse textures still vanilla | 103 |
| Meshes still vanilla | 384, many of them planter and harvested-state variants |
| Plant meshes replaced today | 46, of four kinds:<br>• 25 are Faultier's food crops (cabbage, leek, gourd, garlic, potato)<br>• 13 are USSEP fixes<br>• 7 are Particle Patch's glowing plants<br>• 1 is a mesh fix |

## What PBR lists install

30 Skyrim SE lists use a PBR-only base, the same set as the PBR note. 13 of them also run Nature of the Wild Lands.

| Mod | All 117 SE lists | 30 PBR lists | 13 PBR with NOTWL |
|---|---|---|---|
| DrJacopo's 3D Snow Berries | 72 | 25 | 12 |
| DrJacopo's 3D Tundra Cotton | 69 | 25 | 11 |
| DrJacopo's 3D Dragons Tongue | 65 | 24 | 11 |
| DrJacopo's 3D Nightshade | 56 | 24 | 10 |
| DrJacopo's 3D Deathbell | 58 | 23 | 11 |
| DrJacopo's 3D Tundra Shrubs | 50 | 23 | 11 |
| DrJacopo's 3D Thistle, Sword Ferns | 56 each | 22 each | 10 each |
| DrJacopo's 3D Lavender | 64 | 20 | 8 |
| DrJacopo's 3D Stonecrop | 46 | 20 | 8 |
| DrJacopo's 3D Pine Shrubs | 34 | 19 | 11 |
| Cathedral - Mushrooms | 31 | 19 | 10 |
| Cathedral - 3D Mountain Flowers | 45 | 18 | 8 |
| High Quality Ivy Replacer (Base Object Swapper) | 48 | 17 | 9 |
| **Cathedral PBR Plants** | 17 | 16 | 10 |
| Snowy mountain flowers (Base Object Swapper) | 37 | 14 | 6 |
| DrJacopo's 3D Clover | 58 | 14 | 6 |
| **PBR Flora Overhaul** | 13 | 13 | 7 |
| A Nirnroot | 26 | 10 | 8 |
| PBR Waterplants | 9 | 9 | 5 |
| Tomato's PBR Vanilla Ivy | 7 | 7 | 3 |
| Diverse high-quality PBR shrubs | 6 | 6 | 3 |
| Mari's flora | 35 | 5 | 0 |
| Skyrim Flora Overhaul | 6 | 2 | 1 |

The lists closest to this one install nearly the same thing:

| List | Plants |
|---|---|
| CSVO (NOTWL, Merethic) | 14 DrJacopo meshes, Cathedral Mushrooms, snowy mountain flowers, Cathedral PBR Plants, PBR Flora Overhaul, Tomato's PBR Vanilla Ivy, Animated Ivy |
| Lalaland (NOTWL, Merethic) | The same, plus A Nirnroot with its PBR version, Smaller Cathedral 3D Plants, and Remove All Ugly Dead Shrubs |
| morningstar (Merethic) | The same core, plus Smaller Cathedral 3D Plants |
| Wanderer's Way (Merethic) | The same core, with the PBR Clover and PBR Lavender files, ValArt hanging moss and its PBR version |
| Morkeskygge (NOTWL, Merethic) | Cathedral PBR Plants, PBR Flora Overhaul, snowy mountain flowers, High Quality Ivy, Flora Additions willows |

## The candidates

- **DrJacopo's 3D plants** ([Mountain Flowers](https://www.nexusmods.com/skyrimspecialedition/mods/41312) by Jonny Wang, and Dr Jacopo's own [Snow Berries](https://www.nexusmods.com/skyrimspecialedition/mods/69415), [Tundra Cotton](https://www.nexusmods.com/skyrimspecialedition/mods/68068), [Dragons Tongue](https://www.nexusmods.com/skyrimspecialedition/mods/85694) and the rest).
  - What they are: 3D meshes made from photographs, replacing the flat vanilla cards. The authors pitch them as performance-friendly.
  - Coverage: 14 mods cover deathbell, dragon's tongue, mountain flowers, nightshade, pine shrubs, snowberries, stonecrop (tundra scrub), sword ferns, thickets and dead shrubs, thistle, tundra cotton, tundra shrubs, lavender and clover.
  - Plugins: only Mountain Flowers ships one. The rest are mesh and texture replacers.
  - Shared library: the grass library Merethic uses comes from the same Cathedral project.
- **[Cathedral PBR Plants](https://www.nexusmods.com/skyrimspecialedition/mods/135836)** by jepster and Tomatokillz.
  - Version: v2.10, updated 2026-09-24, 0.4 GB.
  - Coverage: PBR textures for all 14 of those, plus [Cathedral - Mushrooms](https://www.nexusmods.com/skyrimspecialedition/mods/26103). It ships no meshes, so it requires the originals and a PGPatcher run.
  - Options:
    - Faultier made some textures, with "Faultier" options for sword ferns and mushrooms.
    - There are options for glow, colors, Seasons, and [Kabu's nightshade](https://www.nexusmods.com/skyrimspecialedition/mods/102273).
    - A new optional file covers the maple vine.
- **[PBR Flora Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/148782)** by jepster.
  - Version: v2.8.3, updated 2026-07-18, about 0.86 GB.
  - Coverage: everything the Cathedral set skips. That means creep clusters, fungal pods, giant lichen, glowing mushrooms, hanging moss, frost mirriam and elves ear, jazbay, canis and jarrin root, nordic barnacles, spiky grass, scathecraw, vines, wheat, potato plants, groundcover, and the Dawnguard and Dragonborn plants.
  - Conflict with Nature of the Wild Lands: its installer also has Reach tree, juniper and driftwood options that ship tree meshes. NOTWL replaces trees, and its author doesn't support other tree mods.
  - Load order: the author says to load it after other plant texture mods and run PGPatcher.
- **[Diverse high-quality PBR shrubs](https://www.nexusmods.com/skyrimspecialedition/mods/154489)** by jepster.
  - Version: file v2.3.1 from 2026-07-18; the page was last updated on 2026-08-06.
  - What it does: swaps 22 vanilla shrub types for over 100 3D variants through Base Object Swapper. Those are tundra, reach, yellow and fall forest shrubs, thickets, dead shrubs and the vine maple.
  - Assets: native PBR textures, shared between variants so they cost no extra VRAM. Leaves are animated, and the meshes are already patched, so it needs no PGPatcher run.
  - Plugins and pine shrubs: it ships one plugin. It leaves pine shrubs to Cathedral PBR Plants.
  - Load order: nothing should overwrite it.
  - Overlap with DrJacopo's set: it swaps tundra shrubs, thickets and dead shrubs too. Its installer is modular, so one of the two has to own those.
- **[Tomato's PBR Vanilla Ivy](https://www.nexusmods.com/skyrimspecialedition/mods/176636)** by Tomatokillz.
  - Version: v1.1, updated 2026-10-24.
  - What it does: remakes the vanilla ivy, including farmhouse and dungeon ivy, with specular highlights and subsurface scattering.
  - It highly recommends [Animated Ivy](https://www.nexusmods.com/skyrimspecialedition/mods/82048), and needs a PGPatcher run.
  - Alternative: [High Quality Ivy Replacer](https://www.nexusmods.com/skyrimspecialedition/mods/113578), with jepster's [High Quality PBR Ivy](https://www.nexusmods.com/skyrimspecialedition/mods/129934). It's more used overall and recommended by NOTWL's author, but the lists closest to ours chose Tomato's.
- **[Every Mountain Flowers - Base Object Swapper](https://www.nexusmods.com/skyrimspecialedition/mods/60756)**: swaps in the snowy mountain flower where the ground is snowy, with no worldspace edits. Its plugin replaces Cathedral Mountain Flowers' plugin.
- **[A Nirnroot](https://www.nexusmods.com/skyrimspecialedition/mods/80281)**: a new nirnroot, with a PBR version on the [PBR Waterplants](https://www.nexusmods.com/skyrimspecialedition/mods/129928) page.
- **Not recommended:**
  - [Mari's flora](https://www.nexusmods.com/skyrimspecialedition/mods/45952) is popular overall, but it isn't PBR, was last updated in 2021, and says it's incompatible with other plant replacers. No PBR list with NOTWL uses it.
  - [Skyrim Flora Overhaul](https://www.nexusmods.com/skyrimspecialedition/mods/2154) replaces trees too, which clashes with NOTWL.

## Fit with this list

- **Nothing here touches Faultier's files.** Faultier's PBR plants are food crops (gourd, leek, cabbage, mammoth cheese, slaughterfish eggs), and no candidate ships those. Skip PBR Flora Overhaul's cabbage option, since Faultier's covers it. Its potato option is the farm plant, which Faultier's doesn't cover.
- **Trees stay with NOTWL.** Skip PBR Flora Overhaul's Reach tree and driftwood options. Its juniper option touches only the harvestable juniper plant, not NOTWL's juniper trees, which are separate files.
- **Every requirement is installed.** Base Object Swapper is in (the 1.5.97 build), and so are Community Shaders and PGPatcher. Seasons of Skyrim isn't, so pick the non-seasonal options.
- **Generators:** PGPatcher runs again afterwards. AutoBlend doesn't need to, since the landscape doesn't change.
- **LOD:** none of these are LOD objects, so DynDOLOD isn't affected while PBR Flora Overhaul's tree options stay out.
- **Plugins:** it adds two to four, depending on options. There are plenty of plugin slots for that.

## Recommendation

**The convergent kit, in a new `Plants` separator between Trees & Grass and Architecture.** Trees & Grass would pass 25 mods if they joined it, which is when [0003](../decisions/0003-function-based-unnumbered-separators.md) says to split.

| Order | Mod | Installer choices |
|---|---|---|
| 1 | DrJacopo's 3D plants: Deathbell, Dragons Tongue, Mountain Flowers, Nightshade, Pine Shrubs, Snow Berries, Stonecrop, Sword Ferns, Thicket and Dead Shrub, Thistle, Tundra Cotton, Tundra Shrubs, Lavender, Clover | Main files; the Full 3D PBR file for clover |
| 2 | Cathedral - Mushrooms | Main file |
| 3 | Every Mountain Flowers - Base Object Swapper | The Cathedral option |
| 4 | A Nirnroot, then A PBR Nirnroot | Main files |
| 5 | Cathedral PBR Plants | Every plant, default or Faultier textures, no Seasons |
| 6 | PBR Flora Overhaul | Every plant except Reach trees, driftwood, cabbage and clover; no Seasons. Its juniper option only changes the harvestable juniper plant, and its potato option the farm plant, so both stay |
| 7 | Diverse high-quality PBR shrubs | Reach, yellow and fall forest shrubs and the vine maple. DrJacopo's keeps tundra shrubs, thickets and dead shrubs, as 23 of 30 PBR lists do |
| 8 | Animated Ivy, then Tomato's PBR Vanilla Ivy | The Base Object Swapper version of Animated Ivy |

That's about 1.5 GB of downloads, including 0.19 GB for the shrub mod. Then sort with LOOT, run PGPatcher, and check the result with `tools/coverage.py`.

This kit was installed on 2026-11-03, as the [changelog](../CHANGELOG.md) records. Afterwards, 44 of the 108 vanilla plant and grass textures in those folders are still in use by path, down from 103. Most of the 44 are vanilla grass. Many of the rest are shrubs that Base Object Swapper now swaps for new models, and crops Faultier's covers under other file names. The real gaps left are nests and Solstheim's ash shrubs.

**More shrub variety:** let Diverse PBR shrubs own tundra shrubs, thickets and dead shrubs as well, and skip those three DrJacopo mods and their Cathedral PBR options.

**Water plants, later:** [Waterplants](https://www.nexusmods.com/skyrimspecialedition/mods/6092) and [Flora Additions - Waterplants](https://www.nexusmods.com/skyrimspecialedition/mods/116324), with PBR Waterplants, add new plants to rivers and lakes rather than replacing vanilla ones. That's a separate choice.

## Not verified

- No visual comparison was made, and none of these mods had been seen in this list's game when this was written.
- The installer option names come from the archive previews, which follow the option folders. The exact choices get read with `tools/fomod.py show` at install time.
- The previews for PBR Flora Overhaul and the shrub mod are from 2.8.1 and 2.3, the newest versions Nexus has previews for. Contents may have moved slightly since.
- How Base Object Swapper settles Diverse shrubs against DrJacopo's meshes when both cover a shrub wasn't tested. The recommendation avoids it by giving each shrub type one owner.
- 20 vanilla grass textures still show as vanilla by path. Merethic adds its own grass types, but whether it replaces every vanilla grass in every region wasn't checked.
- Nests, Solstheim's ash shrubs and thickets, and the Soul Cairn and ash grasses remain vanilla after this kit.
