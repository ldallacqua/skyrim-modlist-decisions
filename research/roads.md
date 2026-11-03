# Northern Roads on a PBR landscape

Checked 2026-11-03. Question: the owner wants [Northern Roads](https://www.nexusmods.com/skyrimspecialedition/mods/77530) in place of Blended Roads, with good parallax on the roads. What do lists pair it with, and how does it fit this list? The relevant parts of this list are TomatoRim PBR Landscapes, Faultier's, Tomato's towns, Nature of the Wild Lands with Nordic Cut, and Merethic, plus Lux with Lux Via and Lux CS, all on Community Shaders 1.9.1.

Sources:
- **What lists install:** Wabbajack's reports. That's the index of mod names, and each list's `status.json`, which names the exact files it downloads. Both were read on 2026-11-03.
- **Mod details:** each mod's description, read through Nexus Mods' public API.
- **What archives contain:** the file listings Nexus publishes.
- **Local checks:** the installed mods, their plugins, and Community Shaders' own shader source.

Nothing was downloaded. Counting lists measures adoption, not quality.

## Takeaway

- **What it does:** Northern Roads removes every vanilla road mesh and paints the roads into the landscape. It also replaces every bridge except Dragon Bridge, and adds signposts, totems and other clutter. Because the roads become terrain, their parallax comes from the terrain shader, not from road meshes.
- **Road textures must be PBR here:** Faultier's page says Community Shaders can't render PBR and non-PBR terrain together, and this list's terrain is all PBR. That rules out the popular complex parallax road retextures: Northern Concept, Nordic Northern Roads, Rugge's, and Alternate Complex Parallax Textures.
- **PBR terrain already has parallax:** in Community Shaders 1.9.1, PBR terrain gets parallax from each texture's height map whenever Extended Materials' Parallax is on, and it's on here. TomatoRim's landscapes already ship 108 height maps.
- **The TomatoRim lists agree:** three of the four TomatoRim lists that run Northern Roads (ElderTeej, Wanderer's Way and HexRim) use the same road set: TomatoRim's own Northern Roads add-on, loaded over PBR Hub's Northern Roads PBR. Both give every Northern Roads road texture a PBR set with a height map.
- **Lux Via is a well-trodden pairing:** 25 of the 38 Northern Roads lists also install Lux Via's patch hub. Northern Roads' Patch Collection has patches for Lux, Lux Orbis and Lux Via.

**Recommendation:**
- Northern Roads, with its Patch Collection and Patches Compendium.
- PBR Hub's Northern Roads PBR, then TomatoRim PBR - Northern Roads.
- The fixes most Northern Roads lists with Lux Via add.
- Blended Roads, and Lux Via's option for it, come out.

That's about 0.7 GB of downloads. AutoBlend and PGPatcher run again afterwards.

## What lists install

Road choices by group. A PBR list here is one that installs Faultier's PBR Skyrim, Vanilla PBR AIO or TomatoRim PBR Landscapes by name:

| Roads | All 117 SE lists | 58 CS lists | 27 PBR lists | 13 TomatoRim lists |
|---|---|---|---|---|
| Northern Roads | 38 | 15 | 8 | 4 |
| Blended Roads | 70 | 40 | 18 | 7 |
| Both | 18 | 9 | 3 | 1 |
| Neither | 27 | 12 | 4 | 3 |

Notes on the counts:
- **TomatoRim lists** are lists that install any file from TomatoRim's page. Wanderer's Way takes only its add-ons.
- **Family counting:** the 15 Community Shaders lists with Northern Roads come to about 7 once list families are counted once. Wanderer's Way and its six siblings are one family, and Gate to Sovngarde's two editions are another.
- **Dovahmeme** installs Northern Roads' "no roads, no bridges" variant next to Blended Roads, so it doesn't use Northern Roads' roads.
- **Lumina and HexRim** install Lux CS and PGPatcher, which only work with Community Shaders. The index doesn't count them as Community Shaders lists because neither downloads Community Shaders from Nexus.

The four TomatoRim lists with Northern Roads, file by file:

| List | Road textures | Other Northern Roads files |
|---|---|---|
| ElderTeej 5.0.3.4 | TomatoRim PBR - Northern Roads, PBR Hub Northern Roads PBR | Patch Collection 1.40.1, its Addons, Patches Compendium 7.6.1 with Fixes and Optimization 7.5.2 |
| Wanderer's Way 2.0.0 | the same two | Patch Collection 1.40, Patches Compendium 7.6.0 with Fixes and Optimization 7.5.2 |
| HexRim 1.3.1 | the same two, and it keeps Blended Roads | Patch Collection 1.41.1, Patches Compendium 8.0.0 with Fixes and Optimization 8.0.0, Valhalla Bridges' Northern Roads version |
| Lumina 0.4.0.1 | Vanaheimr - Northern Roads PBR 2k, PBR Hub Northern Roads PBR, Nordic Northern Roads 2K, Northern Concept 2K | Patch Collection 1.41.1, Patches Compendium 7.6.1, Collision and Placement Fix, Landscape Fix and Improvement, Tents Animated |

Lumina is the list closest to this one. It runs:
- Faultier's, TomatoRim, Tomato's Whiterun, Riften and Farmhouses, and Vanaheimr's Mines and Caves.
- Nature of the Wild Lands 3.14, though not Nordic Cut.
- Lux, Lux Orbis and Lux Via, with Lux Via's updates and patch hub, and Lux CS.

Wanderer's Way is the closest list that the index counts as Community Shaders. It runs Northern Roads with Merethic, Lux and Lux CS. Its ground is Sloppy Vanilla Landscapes with Vanilla PBR AIO, and it takes only TomatoRim's Northern Roads and ECSS add-ons, not TomatoRim's main landscapes. It installs Lux Via's resource pack but not Lux Via itself.

Fixes in the six large lists that pair Northern Roads with Lux Via: LoreRim, Wunduniik, NGVO, Diaries of Dibella, Tomes of Talos and Viir Suum. All six also install the Patch Collection and the Patches Compendium.

| Fix | Lists of the 6 | What it is |
|---|---|---|
| [Floating Objects Fix](https://www.nexusmods.com/skyrimspecialedition/mods/112127), with its Lux Via file | 6 | 200+ floating flora and clutter references moved. Now also a Base Object Swapper file, with no plugin |
| [Whiterun stone texture fix](https://www.nexusmods.com/skyrimspecialedition/mods/111609) | 6 | A 342-byte plugin that swaps the texture set on Whiterun's outer road, for parallax with non-PBR textures |
| [Tents Animated](https://www.nexusmods.com/skyrimspecialedition/mods/108532) | 6 | Swaps Northern Roads' tents for animated ones through Base Object Swapper |
| [Patch Collection Addons](https://www.nexusmods.com/skyrimspecialedition/mods/91969) | 6 | Combination patches with other location mods |
| [Collision and Placement Fix](https://www.nexusmods.com/skyrimspecialedition/mods/112554) | 5 | Missing collision, one of which traps the player, plus world gaps and floating objects |
| [Landscape Fix and Improvement](https://www.nexusmods.com/skyrimspecialedition/mods/112130) | 5 | Landscape fixes around Raven Rock, outside Whiterun and in some wilderness |
| [Collision Box Fix in Whiterun](https://www.nexusmods.com/skyrimspecialedition/mods/137238) | 5 | A collision box at Whiterun that gets in the way |
| [Ivarstead Bridge](https://www.nexusmods.com/skyrimspecialedition/mods/97560) | 3 | Less bumpy ground at Ivarstead's bridge |
| [Stairs Fixes](https://www.nexusmods.com/skyrimspecialedition/mods/137711) | 2 | Two meshes whose stairs didn't work |

Their road textures are Northern Concept, Vanaheimr's non-PBR file, Rugge's, Alternate Complex Parallax and Nordic Northern Roads. All are non-PBR, so none suits this list.

## The candidates

### The base and its patches

- **[Northern Roads](https://www.nexusmods.com/skyrimspecialedition/mods/77530)** by JPSteel2.
  - Version and popularity: v1.3.1, last updated 2023-05-25, with 10,836 endorsements. 207 mods list it as a requirement. One 0.17 GB file with a 13.4 MB plugin, loose assets and LOD models for the bigger pieces.
  - What it does: roads by region, with dirt in villages and the wild, stone near cities, and snow and mud in the cold. New bridges, buildings and clutter, with the east of Skyrim Scandinavian and the west Celtic and Slavic.
  - Save safety: the author says it can go into an existing game, since it touches no persistent reference.
  - Its LOD models show up only after DynDOLOD runs, and the roads show on the map and in the distance only after xLODGen.
  - A one-size grass patch is offered for grass growing on roads.
  - A `seasons` folder serves Seasons of Skyrim, which isn't installed.
- **[Northern Roads Patch Collection](https://www.nexusmods.com/skyrimspecialedition/mods/77386)**: v1.41.1, updated 2026-09-29, 0.05 GB, every patch ESL-flagged.
  - It fixes landscape seams and erased roads where other mods edit the same land.
  - It covers about 160 mods. These are installed here: Lux, Lux Orbis and Lux Via, and six Creation Club items: Farming, Fishing, Myrwatch, Saints and Seducers, The Cause and Tundra Homestead.
  - Its page gives an 11-step load order, with town overhauls and combination patches last.
- **[Northern Roads - Patches Compendium](https://www.nexusmods.com/skyrimspecialedition/mods/77893)** by Alaxouche: v8.0.0, updated 2026-08-24. It has two main files.
  - **Patches Compendium:** about 270 patches in v7.6.1, picked by automatic detection and all ESP-FE. Those that could apply here are USSEP Additions, a Floating Plants Fix, and a Rocks patch. Its page says the Rocks patches aren't needed with ENB's terrain blending; whether Community Shaders' Terrain Blending and AutoBlend make it unneeded too wasn't checked.
  - **Lux Via Clutter:** the Compendium's Lux Via option. Its page says not to use it with the Patch Collection's "Lux Via patch - NR bridge", so the two Lux Via approaches are a choice to make at install.
  - **Fixes and Optimization:** fixed and optimized copies of Northern Roads' meshes, with no plugin. In v7.5.2 that was 129 files.
  - The page also asks for `MaxStdio = 8192` in Engine Fixes and `fShadowDirectionalBiasScale=0.24` against square shadow artifacts on the landscape.

### PBR road textures

- **[TomatoRim PBR - Northern Roads](https://www.nexusmods.com/skyrimspecialedition/mods/177621)**, an optional file on TomatoRim's page.
  - Version: v1.0, 2026-04-21, 0.12 GB.
  - Contents: 7 PBR landscape sets, each with a height map and a roughness, metal and AO map. They cover all of Northern Roads' road textures: dry dirt, the dirt road with its 8 trail directions, mud, stone, glacier snow and volcanic tundra, plus a rubble texture.
  - It also has 29 Community Shaders texture set files and a 4.6 kB plugin.
  - TomatoRim calls it fully standalone. It matches TomatoRim's own ground, which is the point.
- **[PBR Hub - Northern Roads PBR](https://www.nexusmods.com/skyrimspecialedition/mods/139889)** by Leo.
  - Version: v1.0.3, 2026-10-19, 0.31 GB.
  - Coverage: Northern Roads' landscape, and also its architecture, bridges, totems, stones and banners. That's why the TomatoRim lists keep it under TomatoRim's file.
  - v1.0.2 had 231 files, among them a 7.2 kB plugin and 5 meshes: two Reach bridges, two stone spikes and `dragonbridge01.nif`. Its 29 texture set files have the same names as TomatoRim's.
  - It needs PGPatcher and Community Shaders, and should overwrite Northern Roads.
- **[Vanaheimr - Northern Roads - PBR](https://www.nexusmods.com/skyrimspecialedition/mods/152575)** by Cl3mus.
  - Version: v2.7, 0.42 GB at 2k.
  - It's made to match Vanaheimr Landscapes, not TomatoRim, with mesh tweaks for vanilla integration.
  - Its PBR version needs PBR Hub. Lumina and Dovahmeme use it.
- **[YXZ True Diverse Northern Roads Reforged](https://www.nexusmods.com/skyrimspecialedition/mods/182981)**.
  - Version: v1.2, 2026-07-04, with 58 endorsements.
  - Hand-painted regional variants for forests, tundra, the Rift and other areas, in PBR or complex parallax.
  - It's new. Only the two Kirbykings lists use it, and neither is a Community Shaders list.

### Not for this list

- Northern Concept, Nordic Northern Roads, Rugge's two packs and Alternate Complex Parallax Textures are all non-PBR terrain textures.
- The Terrain Helper patch for Northern Roads is for older non-PBR retextures.
- "Let me guess someone stole your sweetROADS" keeps the clutter and drops the roads.

## Fit with this list

- **Parallax.**
  - What's verified: Community Shaders 1.9.1's `Lighting.hlsl` enables PBR terrain parallax with Extended Materials' Parallax switch, and takes the height from each texture set's displacement.
  - The settings here: `SettingsUser.json` has `EnableParallax` and `EnableShadows` on. `EnableTerrain` is off, but it only affects non-PBR terrain, so nothing needs changing.
  - Strength: TomatoRim's own texture set files set the height strength per texture, mostly at 1.0.
- **TomatoRim and Faultier's.**
  - TomatoRim asks for Blended Roads' plugin "or Northern Roads".
  - Faultier's page says Northern Roads will probably work and needs no Blended Roads plugin, as long as its terrain gets a PBR retexture.
- **Removing Blended Roads.**
  - No installed plugin has `BlendedRoads.esp` as a master.
  - Its 96 meshes go with it: 30 road pieces and their 30 snow versions, 30 Dwemer road pieces, 4 bridges, the Solitude bridge and Dragon Bridge.
  - TomatoRim's own 60 road meshes stay, unused once Northern Roads has removed the road pieces.
- **Lux Via.**
  - It was installed with "Via Bridges for Blended Roads version": a texture set plugin and 6 bridge meshes. That option comes out, leaving Lux Via's own bridges from its archive.
  - Lux Via reworks bridges and Northern Roads replaces them, so its 14 landscape and 48 navmesh edits now meet Northern Roads.
  - The Patch Collection's Lux Via patch settles which bridge stays, and the Floating Objects Fix has a Lux Via file.
- **Lux CS and Orbis CS.** The Northern Roads patches for Lux and Lux Orbis were made against those mods alone. Where they share references with Lux CS or Lux Orbis CS, they may undo those edits. The lighting install found that kind of reversion between Orbis CS and the Orbis patches. Check the overlaps at install.
- **Nature of the Wild Lands with Nordic Cut.**
  - Nordic Cut's Patch Collection has a Northern Roads patch, which its installer recommends once `Northern Roads.esp` is active. Its masters are NOTWL, Nordic Cut and Northern Roads.
  - The same archive has a Lux Via patch, recommended once `Lux Via - plugin.esp` is active. It was never installed, because Nordic Cut went in before Lux Via. Both patches come from the archive already in downloads.
- **Merethic.** Its plugin overrides the grass on 29 vanilla landscape textures. Northern Roads paints with its own landscape textures, so Merethic shouldn't grow grass on them. That wasn't checked. Northern Roads' Grass Patch and the Compendium's grass remover script are the fallbacks.
- **Tomato's towns and forts, TomatoRim Farmhouses, Vanaheimr's caves.**
  - None has a plugin, so none conflicts on landscape.
  - Northern Roads replaces five vanilla-path meshes: Riften's guardhouse and inner gate wall, the Solitude bridge, a lobster cage and a rope coil.
  - Tomato's Riften ships no meshes. PGPatcher applies its textures to whichever mesh wins, so they'd reach Northern Roads' Riften meshes if those keep the vanilla texture paths.
- **Bridge meshes to settle at install.**
  - Solitude bridge: TomatoRim's copy wins today, over Blended Roads, Assorted Mesh Fixes and SMIM. Northern Roads and its fixes ship their own, and one of them has to meet the painted road.
  - Dragon Bridge: Northern Roads leaves it alone. Blended Roads ships one, and so does PBR Hub's Northern Roads file.
- **Other landscape editors:**
  - Lux.esp edits 8 landscape records, which the Lux patch covers.
  - Dead Man's Dread and Hendraheim each edit 4 landscape records, and no patch covers them. Whether Northern Roads touches those cells is unknown until install.
  - No patch was found for Skyrim Unbound, IcyFixes or Better Dynamic Snow's DisableRefs.
- **Plugins and version.**
  - Northern Roads is one plugin. The Patch Collection's and Compendium's authors say all their patches are ESL-flagged.
  - Everything is plugins and assets, with no SKSE plugin, and BEES covers newer plugin headers on 1.5.97.
- **LOOT.**
  - The masterlist has no group for Northern Roads, only a rule to load after Vanilla Landscape Corrections. The Compendium wants Northern Roads and its patches at the very bottom.
  - LOOT will sort the patches by their masters. Expect a few userlist rules, recorded as [0010](../decisions/0010-loot-with-metadata.md) asks: TomatoRim's road plugin after PBR Hub's, for one.
- **Generators and LOD.**
  - AutoBlend and PGPatcher must run again, each with its output disabled first (rule 14).
  - Until xLODGen runs, distant terrain keeps vanilla LOD with the old road shapes, and the map shows the old roads too. When LOD is done, rule 15 puts xLODGen before AutoBlend.
- **Settings.** Engine Fixes already raises the file limit with `bMaxStdIO = true`. This profile has `fShadowDirectionalBiasScale=0.47`. Try the Compendium's 0.24 only if square shadows show on roads.

## Recommendation

**Northern Roads with the TomatoRim lists' PBR road set, its two patch packs, and the fixes the Lux Via lists use.** In the `Landscape` separator, in this order:

| Order | Mod | File | Choices |
|---|---|---|---|
| 1 | Icy Mesh Remaster, Enhanced Rocks and Mountains | installed | none |
| 2 | Northern Roads | Main 1.3.1, 0.17 GB | Leave out `seasons\` |
| 3 | Northern Roads - Patches Compendium | Fixes and Optimization 8.0.0, and Patches Compendium 8.0.0, 0.02 GB | Detected patches for installed mods. Its Lux Via Clutter or the Collection's Lux Via patch, not both |
| 4 | Northern Roads - Collision and Placement Fix | 2.1.1 | Must overwrite Northern Roads and the Compendium |
| 5 | Northern Roads - Floating Objects Fix | Floating Objects Fix BOS 1.4, and its Lux Via BOS 1.2 | none |
| 6 | Northern Roads - Collision Box Fix in Whiterun | 1.0.0 | none |
| 7 | Northern Roads Patch Collection | 1.41.1, 0.05 GB | Lux, Lux Orbis, Lux Via and the six Creation Club patches |
| 8 | TomatoRim PBR Landscapes | installed | none |
| 9 | PBR Hub - Northern Roads PBR | 1.0.3, 0.31 GB | none |
| 10 | TomatoRim PBR - Northern Roads | 1.0, 0.12 GB | Wins over PBR Hub for the roads |

Changes to what's installed:
- **Drop** Blended Roads.
- **Lux Via:** remove its "Bridges for Blended Roads" option, which is its texture set plugin and 6 meshes.
- **Nordic Cut's Patch Collection:** add its Northern Roads patch, and the Lux Via patch the lighting install missed. Both come from the archive already in downloads.
- **Then:** sort, check conflicts and overlaps, run AutoBlend and PGPatcher again, read their logs, and test on a cloned profile (rule 18).

The downloads come to about 0.7 GB.

This set was installed on 2026-11-03, as the [changelog](../CHANGELOG.md) records. What the install settled:
- **Installer choices:**
  - The Patch Collection's Lux patches keep Lux Via's bridges where both mods have one. Its experimental "NR bridges" patch was left out, and so was the Compendium's "Lux Via Clutter".
  - The Collection's Blended Roads Solitude Bridge Fix went in, because TomatoRim's Blended Roads-based Solitude bridge stays.
  - PBR Hub's Dragon Bridge, whose deck uses Northern Roads' stone road, wins over TomatoRim's.
- **Lux CS:** checked. Northern Roads' Lux and Lux Orbis patches share no references with Lux CS, Lux Orbis CS or CS Light, so none of their light edits is undone.
- **Load order:**
  - LOOT first put Northern Roads before Nature of the Wild Lands and Lux Via's plugin. In that order Nordic Cut kept a tree on the new road, and Lux Via's plugin put its own terrain back over two Northern Roads blocks.
  - A userlist rule now loads Northern Roads after both, as its patch packs ask. Their shared cells carry the same regions, so the move changes no cell data.
  - After it, only 10 of the 13,087 records Northern Roads and its patches edit end up won by a plugin that doesn't list Northern Roads as a master: Obsidian's six clouds, kept on purpose, and the four below.
- **Not patched:** no patch covers Nordic Cut, Lux Via and Northern Roads together. In 4 references Nordic Cut's Lux Via patch wins over the Northern Roads one: two trees stay where Lux Via moved them, and one Lux Via object stays that the Northern Roads patch disables. A rule to reverse that moved five other patches, so it was dropped.
- **PBR Hub's gaps:** its plugin points a Windhelm wall texture set at maps that only a Windhelm PBR mod provides. ElderTeej, HexRim and Lumina all run Tomato's Windhelm. It also points a dragon totem set at textures nobody ships. Nothing places either object, so neither shows.
- **Nordic Cut's patches:** its Northern Roads patch went in, along with the Lux Via and Lux patches that the lighting install had missed.

**Left out, to add only if the game shows the problem:**
- Landscape Fix and Improvement, for seams outside Whiterun or at Raven Rock.
- The Whiterun stone texture fix, if Whiterun's outer road looks flat. It was made for non-PBR textures.
- Stairs Fixes and Ivarstead Bridge.
- Northern Roads' Grass Patch, if grass grows on the roads.
- The Patch Collection Addons. Every patch in it targets a mod this list doesn't have.
- Tents Animated, which is taste.

**Alternatives:**
- Vanaheimr - Northern Roads PBR for a different road look, as Lumina does. It's made for Vanaheimr's landscapes, not TomatoRim's.
- YXZ for regional variety. It's too new to have a track record.

## Not verified

The install settled the archive questions this note first left open: plugins, installer options, Lux CS, and the record overlaps. What's still open:
- **Grass.** Whether Merethic grows grass on Northern Roads' roads.
- **Snow.** How Better Dynamic Snow looks on the new bridges.
- **The four unpatched references** above, and how they look.
- **The look.** The owner has seen Northern Roads in game and likes it, then asked for rougher dirt roads (the last section). Still to look at:
  - roads near towns and in snow and mud, and the parallax up close;
  - bridges, especially Solitude's, Dragon Bridge and Lux Via's;
  - grass on roads, and floating lanterns and plants along them.
- **Distance.** Distant roads and the map show the old roads until xLODGen runs.

## Rougher dirt roads

Checked 2026-11-03. Question: the owner wants rougher, trampled dirt roads with deep parallax, like [Complex Parallax Texture for Northern Roads](https://www.nexusmods.com/skyrimspecialedition/mods/93860) by Omen Apollo or [Rugge's Rocky Mossy Complex Parallax](https://www.nexusmods.com/skyrimspecialedition/mods/134716). Neither showed any parallax when the owner tried them before. Nothing was downloaded. Sources: their pages and file listings, and the installed Community Shaders and PGPatcher.

- **Why they failed.**
  - Both are ENB complex parallax textures for `textures\cotn\landscape\grounddirt01`, Northern Roads' main dirt road, and its 8 trail variants. Omen Apollo's 2K file has only colour and normal maps. Rugge's Rocky Path III adds a height map.
  - Here, TomatoRim's road plugin points those texture sets at `textures\pbr\cotn\landscape\`, so the game never loads files at the old path.
  - Without a PBR road plugin they'd load, but as non-PBR terrain. Community Shaders gives that parallax only with Extended Materials' Terrain Parallax switch, which is off here. And Faultier's page says it can't render non-PBR terrain next to PBR ground, which is all of TomatoRim's.
- **PGPatcher doesn't convert them.**
  - Version 2.3.1 has one shader transform, "Upgrade Parallax to Complex Material".
  - It patches meshes, from model records such as STAT and TREE. Terrain textures come from landscape records, which it doesn't touch.
  - Its TruePBR patcher applies existing PBR textures to meshes. It makes none.
- **The ready-made PBR version:** Rugge's own [R - PBR Rocky Mossy](https://www.nexusmods.com/skyrimspecialedition/mods/170204).
  - v1.0, 2026-01-19, 42 endorsements, 0.31 GB at 4K.
  - It uses the same paths and texture set file names as TomatoRim's road file, so it would simply override it.
  - It also ships separate normal, height and RMAOS maps for each trail. Both installed road plugins point the trails at the base maps, so those would go unused.
  - Its screenshots show grey, flat stones with moss between them, not sandy dirt.
  - Its other file, Dirt02, retextures vanilla `landscape\dirt02`, not Northern Roads.
- **Other PBR Northern Roads textures:** Vanaheimr's, YXZ's and 0ctoProcessor's [PBR Northern Roads](https://www.nexusmods.com/skyrimspecialedition/mods/140565) (v3.0.2, 131 endorsements, 0.90 GB). Each retextures every road for a different landscape. Their looks weren't compared.
- **Converting by hand.**
  - Omen Apollo credits Quixel Megascans, and Rugge credits Megascans and Poly Haven, so both started as PBR scans. Rebuilding PBR maps from them is mechanical:
    - The colour map becomes the albedo.
    - The normal map is kept.
    - The height map becomes the `_p` map.
    - Roughness comes from the normal map's alpha if that holds gloss, or else is a flat value near TomatoRim's, with metal at 0. These go into `_rmaos`.
  - The results go at TomatoRim's paths, in a new texture-only mod after `TomatoRim PBR - Northern Roads`. With no plugin, there's no LOOT change, and AutoBlend and PGPatcher don't run again. TomatoRim's `displacementScale` sets the depth.
  - The tools are already here: Texconv in SSEEdit's scripts folder, and Python with numpy.
  - The converted files are for this setup only and aren't to be shared.
  - Whiterun's outer road changes too, because TomatoRim points `COTN_LandscapeWRStone` at the same textures.
  - Unknown until download:
    - Where Omen Apollo stores the height. ENB terrain parallax normally reads it from the colour map's alpha.
    - Whether its 8 trail maps differ from the base. Here the trails share the base's normal and height maps.

**Recommendation:** convert Omen Apollo's 4K file, 0.19 GB.
- It's the look the owner asked for, and only this one texture set changes.
- It has 1,622 endorsements, against 528 for Rugge's.
- If a stonier road will do, Rugge's PBR Rocky Mossy needs no conversion.
- Rugge's Rocky Path III, 0.18 GB, converts the same way, for the look in Rugge's screenshots.

The owner approved, and it was converted and installed on 2026-11-03, as `Northern Roads - Omen Apollo Dirt PBR (converted)` at the top of `Landscape`. It hasn't been seen in game yet.
- **The source,** verified after download:
  - The 4K file has two maps. The colour map is BC7 and not sRGB, with the height in its alpha: a smooth spread from 0.17 to 0.71.
  - The normal map's alpha is empty, so it holds no gloss.
  - All 8 trail colour maps are byte-for-byte copies of the base. Sharing the base's normal and height loses nothing.
- **How Community Shaders 1.9.1 reads a full PBR terrain layer,** from `LightingLandscape.hlsli`:
  - The colour is used as linear, so it must be flagged sRGB.
  - RMAOS is roughness times `roughnessScale`, metal, AO, and specular times `specularLevel`.
  - The height is centred at 0.5 and scaled by `displacementScale`.
  - The colour and normal alphas aren't used on PBR terrain.
- **The conversion** was done by [`tools/terrain_to_pbr.py`](https://github.com/ldallacqua/skyrim-modlist-decisions/blob/main/tools/terrain_to_pbr.py):
  - **Albedo:** 4K, BC7 sRGB. The source is far darker than TomatoRim's road, with a mean linear brightness of 0.035 against 0.100. It was raised 2.86 times in linear light to match TomatoRim's road, and the top 0.8% of values roll off instead of clipping.
  - **Normal:** 4K BC7, the source's RGB.
  - **Height:** 2K BC4, from the alpha, unchanged apart from the size. Its spread (std 0.118) is about three times that of TomatoRim's road (0.036), so the new road has much deeper parallax at the same `displacementScale`.
  - **RMAOS:** 2K BC1. Roughness runs from 0.96 on dark dirt to 0.86 on the brightest stones, averaging 0.95 (TomatoRim's averages 0.94). Metal is 0, AO is 1 because the colour map already has its shading, and specular is 1.
  - Each map was decoded after compression and matched what was written. That check read only the full-size level, which missed the fault below.
- **First in-game test, same day: the road went black.** It was black at a distance and at low angles, with dark patches close up from above.
  - **Cause:** every albedo mip below full size was solid black. The tool had left the albedo's alpha at 0, which PBR terrain ignores, but Texconv weights colour by alpha when it builds mips. The normal, height and RMAOS mips were fine.
  - **Fix:** the albedo is now opaque. The tool also checks every mip of every map against the full-size level and stops if one strays. The 12 files were rebuilt and replaced, and all pass.
  - **Ruled out:** the depth. Terrain self-shadowing in `ExtendedMaterialsTerrain.hlsli` does multiply height differences by 8 and saturate. But TomatoRim's own rock, snow and dirt maps have as much relief (up to std 0.18 against 0.118 here), mostly at `displacementScale` 1.0, and they look fine. Across TomatoRim's 123 PBR terrain height maps the median std is 0.038.
- **In the mod:**
  - The four maps, plus the albedo again under the 8 trail names.
  - Copies of TomatoRim's 10 texture set files for the sets that use these maps, values unchanged. They're there so `displacementScale` can be tuned in this mod.
  - It conflicts only with TomatoRim's and PBR Hub's road files, and wins over both.
  - No plugin, so LOOT stays as it was. AutoBlend baked nothing from Northern Roads' textures, and PGPatcher's meshes point at the same paths, so neither runs again.
- **What changes in game:** every non-winter Northern Roads dirt road, its trails, and Whiterun's outer road. Northern Roads' three winter sets are Seasons of Skyrim's, used only by the `seasons` file this list leaves out.
- **Not verified:**
  - The look in game since the fix.
  - The depth. If it's too deep or swims at grazing angles, lower `displacementScale` in this mod's texture set files. About 0.3 matches TomatoRim's depth.
  - The brightness next to TomatoRim's ground. `--brightness` reruns the conversion brighter or darker.

After the fix the owner found the road good, but deeper than the ground beside it, and bare of debris. [The road edges and debris note](../research/road_edges_and_debris.md) measures both and recommends a fix. On 2026-11-03 a small plugin added pebbles and small rocks to the dirt roads, and the ground stayed TomatoRim's ([0015](../decisions/0015-keep-tomatorim-ground-and-northern-roads.md)). The road's depth went down to 0.5 and back to 1.0, because the owner found it flat. Deepening the ground's height maps instead smeared them, so the ground stays as TomatoRim ships it.

The same look showed the stone spike pillars broken, smeared and furry. PBR Hub's copies of the spikes and the Reach bridges swap their textures for the vanilla mountain slab, and PGPatcher then gave them TomatoRim's whole-mountain material. Those four meshes are hidden now, so the Patches Compendium meshes win and take PBR Hub's own spike and bridge PBR textures.
