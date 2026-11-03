# PBR textures, trees and grass for a Community Shaders list

Checked 2026-11-03. Question: which PBR texture base to install, and which trees and grass go with it, for this list (Skyrim SE 1.5.97, Community Shaders 1.9.1, PGPatcher, Grass Optimizations with NGIO, no grass cache). DynDOLOD isn't installed yet, but it will run once the visuals are settled, so mods that need it are in scope.

How to read the evidence:
- **What lists install** comes from Wabbajack's published validation reports (`reports/searchIndex.json` and each list's `status.json` in [wabbajack-tools/mod-lists](https://github.com/wabbajack-tools/mod-lists/tree/master/reports)), read on 2026-11-03. They name every archive a list downloads, including which file of a mod. They cover Wabbajack lists only, so Nolvus and other lists with their own installers are missing.
- **Mod details** come from each mod's description and requirements tab, read through Nexus Mods' public GraphQL API. Nexus pages themselves return 403 to automation.
- **Counting lists measures adoption, not quality.** Several lists share authors and templates, and many are small or new.

## Takeaway

Faultier's PBR Skyrim is the most adopted PBR base, and the lists built on it converge on one set: Tomato's mods fill the places Faultier skips, and TomatoRim PBR Landscapes covers the ground. For trees, Nature of the Wild Lands is the most used mod overall and has a PBR add-on. It needs USSEP, which the list now has at 4.2.5b, the same pairing Eldergleam NG runs on 1.5.97. Morkeskygge installs nearly this whole set: Faultier's AIO, TomatoRim, NOTWL with its Nordic Cut and PBR add-on, Merethic, DynDOLOD and Grass Optimizations. CSVO is close too. The lighter PBR-native set is Tomato's PBR Vanilla Trees on Enhanced Vanilla Trees, with Aspens Ablaze and its PBR conversion, as in ElderTeej and Nordic Souls PBR. For grass, Merethic Grasslands with its PBR conversion is the most used in PBR lists, and the only PBR one among them. Freak's Floral Fields is the lusher choice, built alongside Vanaheimr's landscapes rather than TomatoRim's.

## What PBR lists install

30 Skyrim SE lists install a PBR-only base (Faultier's PBR Skyrim, Vanilla PBR AIO or TomatoRim PBR Landscapes). PBR needs Community Shaders, so all 30 are Community Shaders lists.

| Choice | Lists out of 30 |
|---|---|
| **Base:** Faultier's PBR Skyrim | 22 |
| **Base:** Vanilla PBR AIO | 9 |
| **Landscape:** TomatoRim PBR Landscapes | 13 |
| **Landscape:** Sloppy Vanilla Landscapes (ICFur Exist mashup) | 7 |
| **Landscape:** Vanaheimr Landscapes AIO | 6 |
| **Trees:** Nature of the Wild Lands | 13 |
| **Trees:** Tomato's PBR Vanilla Trees | 10 |
| **Trees:** Happy Little Trees | 10 |
| **Trees:** Aspens Ablaze | 9 |
| **Grass:** Merethic Grasslands | 9 |
| **Grass:** Freak's Floral Fields | 7 |
| **Grass:** Witchy Wilderness | 5 |
| **LOD:** DynDOLOD 3 | 22 |
| **LOD:** Grass Cache Helper NG | 12 |
| **LOD:** Grass Optimizations | 6 |

A list can count in more than one row. Faultier's own landscapes can't be told apart by mod name, so they appear only in the file-level check below.

### Which Faultier's files lists actually use

From the `status.json` archive names:

| List | Faultier's files | Landscape | Trees | Grass |
|---|---|---|---|---|
| ElderTeej (featured) | AIO 2k | TomatoRim 2K | Tomato's, Aspens Ablaze, EVT, Fabled Forests | Witchy Wilderness |
| Nordic Souls PBR | Separate 2k files | TomatoRim 2K | Tomato's, Aspens Ablaze, EVT, HLT | Freak's Floral |
| Morkeskygge | AIO 2k | TomatoRim 2K | NOTWL | Merethic |
| ReaperGleam | AIO 2k + Landscapes 4k | TomatoRim 4K | NOTWL, S3DTP | Freak's Floral |
| Everwild | AIO 2k | TomatoRim 4K | none | Witchy Wilderness |
| Lalaland | AIO 2k | Sloppy Vanilla | HLT, NOTWL | Merethic |
| NG-EVO (Enderal) | AIO 1k + Landscapes 1k | Vanaheimr 1k | NOTWL | Freak's Floral |
| Tuxborn | Separate 2k files | Vanaheimr 2k | HLT, Aspens Ablaze | Cathedral, Folkvangr |

Only two lists install Faultier's landscapes, and both also install another landscape. The usual pairing is Faultier's architecture with TomatoRim's ground.

ElderTeej and Nordic Souls PBR fill Faultier's gaps with the same mods: Tomato's Whiterun Remake, Tomato's Riften and Ratway, Tomato's PBR Farmhouses, Imperial Forts Remake and Vanaheimr Mines and Caves. Both also install SMIM, Icy Mesh Remaster, ERM meshes and Better Dynamic Snow 3.6. CSVO (featured) uses the same gap fillers under Vanilla PBR AIO.

## The candidates

### Texture bases

- **[Faultier's PBR Skyrim](https://www.nexusmods.com/skyrimspecialedition/mods/125308)**: v3.0, 2,663 endorsements, 1.76M downloads.
  - The AIO covers clutter, Nordic and Dwemer ruins, Solitude, Windhelm, the College, ships, DLC architecture and more. It's 9.2 GB at 2k, 3.1 GB at 1k and 19.7 GB at 4k. Landscapes are a separate file.
  - It doesn't cover Whiterun, Riften, farmhouses, Imperial forts or caves.
  - It requires Community Shaders, SMIM and PGPatcher. The landscapes also need Blended Roads' ESP.
  - Incompatible: Terrain Parallax Blending Fix, Majestic Landscapes, double-pass snow (Simplicity of Snow, BDS 2), Icy or Snowy Windhelm, RUGNAROK and Detailed Rugs.
- **[Vanilla PBR AIO](https://www.nexusmods.com/skyrimspecialedition/mods/174091)**: v1.33.1, 1,050 endorsements, 56k downloads.
  - It covers almost everything except gear and landscapes, including cities, actors, dungeons and food, and stays faithful to vanilla.
  - It uses 2k diffuse maps and 1k normals by design. It requires SMIM and PGPatcher, and the author says not to use SMIM PBR with it.
  - The author designed it around ICFur Exist landscapes, Merethic Grasslands, Tomato's PBR Vanilla Trees and Cathedral PBR Plants.

### Landscapes

Community Shaders can't render PBR and non-PBR terrain together, so every landscape texture must be PBR (Faultier's description).

- **[TomatoRim PBR Landscapes](https://www.nexusmods.com/skyrimspecialedition/mods/177621)**: v1.7, updated 2026-09-18. It's 1.9 GB at 2K.
  - It covers the base game, DLC, mountains up to 16k, Soul Cairn, ice and bridges. Optional files cover ECSS, Northern Roads, Seasonal Landscapes and XPMF.
  - It requires Better Dynamic Snow 3.6 with "No Glacier Snow", and Blended Roads' ESP unless the list uses Northern Roads. It recommends Icy Mesh Remaster, ERM meshes and running AutoBlend.
  - It needs `bEnableProjecteUVDiffuseNormals=1` in skyrimprefs.ini, and Terrain Parallax Blending Fix is incompatible.
- **[Sloppy Vanilla Landscapes](https://www.nexusmods.com/skyrimspecialedition/mods/143767)** (ICFur Exist mashup): 2k AI upscales of the vanilla textures, with DLC in the new version. Its author pitches it to players who don't want to run DynDOLOD, because it keeps vanilla colors.
- **[Vanaheimr Landscapes AIO](https://www.nexusmods.com/skyrimspecialedition/mods/145439)**: it requires ERM, Icy Mesh Remaster and PGPatcher. It was designed around Freak's Floral Fields.

### Trees

Tree mods in the 71 Skyrim SE lists that run DynDOLOD: Nature of the Wild Lands 31, Happy Little Trees 28, Skyrim 3D Trees and Plants 15, Aspens Ablaze 14, EVT 9, Tomato's 7. Among the 19 PBR lists that run DynDOLOD: NOTWL 8, Tomato's 7, Aspens Ablaze 6, HLT 5.

- **[Tomato's PBR Vanilla Trees](https://www.nexusmods.com/skyrimspecialedition/mods/139375)**: v2.6, 0.3 GB.
  - It gives vanilla trees new bark, subsurface foliage and new moss decals, plus logs and firewood.
  - It works with vanilla tree meshes, [Enhanced Vanilla Trees](https://www.nexusmods.com/skyrimspecialedition/mods/11008) and anything else that uses vanilla tree textures. The author's screenshots use EVT's Lush option. Its snow matches Faultier's and TomatoRim's landscapes exactly.
  - The author recommends [Aspens Ablaze](https://www.nexusmods.com/skyrimspecialedition/mods/39998) and [Aspens Ablaze - PBR](https://www.nexusmods.com/skyrimspecialedition/mods/146940) loaded after it.
  - EVT requires DynDOLOD for its object LOD, and Aspens Ablaze has an official DynDOLOD 3 add-on.
- **[Nature of the Wild Lands](https://www.nexusmods.com/skyrimspecialedition/mods/63604)**: v3.14, about 3.5 GB.
  - It uses photogrammetry trees, adds over 400 new trees, plants and objects in many small regions, and makes forests much denser. It doesn't edit landscape or navmesh.
  - It has a [PBR add-on](https://www.nexusmods.com/skyrimspecialedition/mods/150319) and a [3D hybrid LOD add-on](https://www.nexusmods.com/skyrimspecialedition/mods/133619) that needs TexGen and DynDOLOD Ultra.
  - **It requires USSEP.** 46 of the 47 Wabbajack lists that install NOTWL also install USSEP. The exception, NG-EVO, is built on Enderal.
  - USSEP's current page says it isn't supported on older game versions, and every older file is archived. This list now has USSEP 4.2.5b, the last build for 1.5.97, installed by the user.
  - Eldergleam NG 4.0.2 runs NOTWL 3.14 with USSEP 4.2.5b, BEES and SKSE 2.0.20, which is the 1.5.97 setup this list uses. The Nico Experience runs an older NOTWL the same way.
  - **[Nordic Cut](https://www.nexusmods.com/skyrimspecialedition/mods/161936)** keeps vanilla placement for most trees and keeps NOTWL's shrubs and debris. It swaps pines for NOTWL's spruce.
    - It's compatible with the PBR, animation and 3D LOD add-ons, but not with NOTWL's regular patches or the LOD regions add-on.
    - It needs a new game, and its optional scaling uses Base Object Swapper.
    - Morkeskygge and CSVO use it.
- **[Happy Little Trees](https://www.nexusmods.com/skyrimspecialedition/mods/50961)**: popular overall, but mostly in ENB lists. It gets PBR only through Skyland's bark textures, which 1 of the 27 PBR lists installs.

### Grass

- **[Merethic Grasslands](https://www.nexusmods.com/skyrimspecialedition/mods/164058)**: v2.3, updated 2026-08-25.
  - Vanilla-faithful complex grass covering the base game and DLC. It needs Community Shaders with Grass Lighting and the meshes from DrJacopo's 3D Grass Library.
  - Its colors are tuned to blend with vanilla LOD, and it says it needs no grass cache with vanilla or vanilla-based LOD.
  - Files: Vanilla, Exist (for Sloppy Vanilla Landscapes), Vanaheimr Cut, and a Faultier addon covering three regions.
  - It has no TomatoRim variant, but Morkeskygge, CSVO, Wanderer's Way and In the Woods pair it with TomatoRim.
  - The Dragonborn's Fate guide installs it with the same Community Shaders features this list uses, Grass Optimizations included.
- **[Merethic Grasslands PBR](https://www.nexusmods.com/skyrimspecialedition/mods/193219)**: a PBR conversion by Leo, v1.1.0, covering the Vanilla and Exist files. It requires Merethic, DrJacopo's library, PGPatcher, Community Shaders and Grass Optimizations. It's new, with 1.8k downloads.
- **[Freak's Floral Fields](https://www.nexusmods.com/skyrimspecialedition/mods/125349)**: v3.2.3. It's the most configurable option, with 31 variants, grass on dirt cliffs through Base Object Swapper, and Seasons support.
  - Its requirements tab says Vanaheimr Landscapes "was literally made side by side" with it and its lighter sibling, Freak's Floral Meadows, and matches it everywhere.
  - Among Skyrim lists that run DynDOLOD, the Freak's family is the most common grass after Folkvangr.
- **[Witchy Wilderness](https://www.nexusmods.com/skyrimspecialedition/mods/134287)**: modular, with complex grass and non-complex versions. It has no PBR version, and ElderTeej uses it.

## Fit with this list

- Community Shaders 1.9.1 ships TruePBR, Grass Lighting and Subsurface Scattering as core features (local check of the mod folder), so nothing extra is needed for PBR, Merethic or Tomato's foliage.
- PGPatcher is already installed and must run again after any of these, with its output last (decision 0007).
- Until DynDOLOD and xLODGen run, distant terrain and trees keep vanilla LOD. Expect seams at the LOD edge while testing. 10 of the 19 PBR lists that run DynDOLOD also install xLODGen or TexGen resources.
- DynDOLOD's grass LOD needs a grass cache. That's what would reopen [decision 0014](../decisions/0014-extended-grass-without-cache.md), not the textures themselves.
- The game version matters little for textures and meshes, and BEES is already installed for newer plugin headers. USSEP 4.2.5b is installed, which NOTWL needs.

## Recommendation

**Faultier + Tomato, with PBR trees and PBR grass:**

| Role | Mod |
|---|---|
| Architecture and clutter | Faultier's PBR Skyrim AIO 2k, with SMIM |
| Gap fillers | Tomato's Whiterun Remake, Tomato's Riften and Ratway, Tomato's PBR Farmhouses, Imperial Forts Remake, Vanaheimr Mines and Caves (all PBR 2k) |
| Landscape | TomatoRim PBR Landscapes 2K and its 1.7 update, with Better Dynamic Snow 3.6, Blended Roads' ESP, ERM meshes, Icy Mesh Remaster and AutoBlend |
| Trees | Nature of the Wild Lands, its Nordic Cut, and Nature of the Wild Lands - PBR |
| Grass | Merethic Grasslands (Vanilla file) and Merethic Grasslands PBR, with DrJacopo's 3D Grass Library meshes |
| LOD pass, after testing | xLODGen terrain, TexGen and DynDOLOD Ultra with NOTWL's 3D hybrid LODs; decide then whether to cache grass for grass LOD |

That's about 18 GB of downloads, half of it the Faultier's AIO. The set was installed on 2026-11-03 for testing, as the [changelog](../CHANGELOG.md) records. Nordic Cut's CC Tundra Homestead patch, Base Object Swapper for IcyFixes, and moving Assorted Mesh Fixes after SMIM came out of the install itself. On the same day Northern Roads replaced Blended Roads, with TomatoRim's own Northern Roads textures, as [the roads note](roads.md) explains.

**Denser forests:** leave out Nordic Cut, so NOTWL uses its own tree placement, as Eldergleam NG, LoreRim, ReaperGleam and Lalaland do.

**Lighter trees:** Enhanced Vanilla Trees (Lush), Tomato's PBR Vanilla Trees with the modern snow patch, then Aspens Ablaze and Aspens Ablaze - PBR. Their snow matches TomatoRim exactly.

**Lusher grass:** swap TomatoRim for Vanaheimr Landscapes PBR and Merethic for Freak's Floral Fields, which were made together. Faultier's with Vanaheimr is used by Tuxborn, Dovahmeme and NG-EVO. The grass stops being PBR.

## Not verified

- No visual comparison was made, and none of these mods has been seen in this list's game.
- It wasn't checked whether Community Shaders' Terrain Variation and Terrain Blending features behave with PBR landscapes, or how AutoBlend interacts with Terrain Blending.
- Merethic with TomatoRim has no official variant. The pairing rests on four lists that use it.
- NOTWL 3.14's plugin wasn't opened, so whether it references anything newer than USSEP 4.2.5b rests on Eldergleam NG running that pair. xEdit's error check after install would show unresolved references.
- Base Object Swapper's support for 1.5.97 wasn't checked.
- Merethic Grasslands PBR is a month old and in no Wabbajack list yet.
- Grass Optimizations' handling of complex grass rests on the Dragonborn's Fate guide pairing them.
