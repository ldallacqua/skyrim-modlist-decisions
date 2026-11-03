# Lighting for a Community Shaders list

Checked 2026-11-03. Question: which lighting setup fits this list. It runs Community Shaders 1.9.1 with its core lighting features, Skylighting and SSGI. It has no lighting mod and no weather mod, so interiors, town lights and image spaces are still vanilla.

The evidence is the same kind as in [the plant note](../research/plants.md): Wabbajack's published reports for what lists install, the Nexus page of each candidate, and the source code of two SKSE plugins on GitHub. The reports cover 117 Skyrim SE lists, 58 of them with Community Shaders. Counting lists measures adoption, not quality. Several lists also share a template: 7 of the 15 Lux CS lists are one family (Wanderer's Way and its siblings), and Gate to Sovngarde and Tuxborn each publish two editions.

## Takeaway

Community Shaders lists light the game in one of two ways, with 15 lists each:
- **Lux, converted with Lux CS.** GGUNIT's [Lux](https://www.nexusmods.com/skyrimspecialedition/mods/43158) relights interiors, [Lux Orbis](https://www.nexusmods.com/skyrimspecialedition/mods/56095) the lights outside, and [Lux Via](https://www.nexusmods.com/skyrimspecialedition/mods/63588) the roads between towns. Bottle's [Lux CS](https://www.nexusmods.com/skyrimspecialedition/mods/153919) adapts all three to Community Shaders: tone mapping, image spaces, and inverse square falloff for every Lux bulb. The three lists closest to ours use it.
- **A modular set built for Community Shaders.** [Ambient Templates for Lighting Mods](https://www.nexusmods.com/skyrimspecialedition/mods/153425) (ATLM) sets interior ambient light, [CS Light](https://www.nexusmods.com/skyrimspecialedition/mods/138443) puts real bulbs on light sources, and [Window Shadows Ultimate](https://www.nexusmods.com/skyrimspecialedition/mods/150494) casts shadows from windows. [True Light](https://www.nexusmods.com/skyrimspecialedition/mods/135488) builds on them. Most of these lists pair it with Azurite III CS weather.

Both sets use po3's [Light Placer](https://www.nexusmods.com/skyrimspecialedition/mods/127557) and CS Light for bulbs. The other 15 Community Shaders lists install neither, or nothing we could detect.

**Recommendation: Lux with Lux CS.** The lists most like ours use it. It covers interiors, exterior lights and roads, and Lux has more patches than any other lighting mod: 354 mods on Nexus list it as a requirement.

## What the game has now

Community Shaders 1.9.1 already includes the engine side:
- Light Limit Fix and Inverse Square Lighting;
- volumetric lighting and shadows, and cloud shadows;
- Interior Sun, image-based lighting and Sky Sync.

Skylighting, SSGI and Particle Patch are installed separately. What's missing is content. Nothing changes the vanilla bulbs, lighting templates or image spaces, and there's no weather mod.

The separate [Inverse Square Lighting](https://www.nexusmods.com/skyrimspecialedition/mods/153542) mod is deprecated, because Community Shaders 1.4.7 and later include it. Lighting mods still need tuning for it, which is what Lux CS and True Light do.

## What Community Shaders lists install

| Mod | All 117 SE lists | 58 CS lists | 15 Lux CS lists | 15 ATLM lists |
|---|---|---|---|---|
| Light Placer | 51 | 37 | 15 | 14 |
| CS Light | 46 | 36 | 14 | 14 |
| Embers XD | 86 | 36 | 15 | 9 |
| First person magic hand light fix | 31 | 25 | 12 | 11 |
| Lux Via | 67 | 24 | 15 | 2 |
| Lux | 64 | 22 | 15 | 0 |
| XEMI Utility | 39 | 22 | 5 | 14 |
| ISL Helper SKSE | 29 | 21 | 11 | 9 |
| Lux Orbis | 57 | 19 | 14 | 0 |
| **Lux CS** | 25 | 15 | 15 | 0 |
| **ATLM** | 17 | 15 | 0 | 15 |
| Luma Utility | 28 | 15 | 3 | 11 |
| Placed Light | 14 | 12 | 0 | 11 |
| Helios | 18 | 11 | 3 | 7 |
| Window Shadows Ultimate | 11 | 9 | 0 | 8 |
| Dynamic Interior Ambient Lighting (DIAL) | 10 | 7 | 1 | 4 |
| Enhanced Lights and FX (ELFX) | 6 | 4 | 0 | 2 |
| Modern Lighting Overhaul 2 | 8 | 2 | 0 | 0 |
| Luminosity, Relighting Skyrim | 3 each | 2 each | 0 | 0 |

True Light doesn't appear in Wabbajack's index under its name, though two lists install fixes made for it. Its Light Placer files are hosted on CS Light's page, so some of the CS Light counts may be True Light setups.

The weather each set is paired with:

| Weather | 15 Lux CS lists | 15 ATLM lists |
|---|---|---|
| NAT: NAT.CS III, or NAT.ENB III's weather plugin alone | 9, of which 8 run NAT.CS III | 2 |
| Obsidian Weathers with Obsidian CS | 3 | 3 |
| Azurite Weathers with Azurite III CS | 0 | 7 |

The lists closest to this one:

| List | Lighting | Weather |
|---|---|---|
| CSVO (NOTWL, Merethic) | Lux, Lux Orbis, Lux Via, the Lux and Orbis patch hubs, Lux CS, ISL Helper SKSE, Light Placer, CS Light, Embers XD | NAT.ENB III's weather plugin |
| Lalaland (NOTWL, Merethic) | The same, plus Helios with Luma Utility | Obsidian CS |
| Wanderer's Way (Merethic) | The same core, plus small Light Placer add-ons | NAT.CS III |
| Morkeskygge (NOTWL, Merethic) | ATLM, Lux Via, Light Placer, CS Light, ISL Helper SKSE | Obsidian CS |

## The candidates

- **[Lux](https://www.nexusmods.com/skyrimspecialedition/mods/43158)** by GGUNIT.
  - Version: v7.1, updated 2025-12-08. The main file is 0.28 GB.
  - What it does: a complete rework of interior lighting. It was built for ENB, which is why it needs Lux CS under Community Shaders.
  - Requirements: [Lux - Patch Hub](https://www.nexusmods.com/skyrimspecialedition/mods/113002) (v7.2, updated 2026-09-25), and Lux Via or its lantern resource pack.
  - Patches: its list covers Skyrim Unbound Reborn and USSEP, both installed. Tomato's Whiterun Remake ships Lux shadow masks for its windows.
- **[Lux Orbis](https://www.nexusmods.com/skyrimspecialedition/mods/56095)** by GGUNIT.
  - Version: v4.5, updated 2024-11-29, with [its patch hub](https://www.nexusmods.com/skyrimspecialedition/mods/114169) at v4.7 from 2026-08-28.
  - What it does: reworks artificial light outdoors, in towns, forts and camps. The installer detects installed mods and picks patches.
  - Weather: the author says it works with every weather mod.
- **[Lux Via](https://www.nexusmods.com/skyrimspecialedition/mods/63588)** by GGUNIT.
  - Version: v2.2, last updated 2025-02-01, 1.3 GB.
  - What it does: lights the main roads between towns, and reworks many bridges and crossroads. It adds points of interest along the way.
  - Load order: it edits vanilla objects, navmesh and landscape. The author loads it as low as possible, below landscape mods, and says Orbis should win where the two overlap.
- **[Lux CS](https://www.nexusmods.com/skyrimspecialedition/mods/153919)** by Bottle.
  - Version: v2.6.0, updated 2026-08-04.
  - What it does: edits Lux's image spaces for Community Shaders' tone mapping, and fixes bloom and eye adaptation that relied on ENB. Its SKSE plugin converts every Lux bulb to inverse square falloff, including the patches, Orbis and Via.
  - Requirements: Community Shaders, Lux, ISL Helper SKSE. Light Placer is needed if its Light Placer add-on is chosen.
  - Compatibility: it works with nothing but Lux. It isn't compatible with Window Shadows Ultimate or ALTM. It works with CS Light if the matching installer options are chosen.
  - Install notes:
    - Lux's optimized meshes aren't needed with Community Shaders' Light Limit Fix.
    - For Lux Orbis, only the meshes with a "Lux" prefix need to stay.
- **[ISL Helper SKSE](https://www.nexusmods.com/skyrimspecialedition/mods/179132)** by Bottle.
  - Version: v1.0.6, updated 2026-09-13.
  - What it does: converts each light to inverse square falloff as the game loads it. It skips spotlights, window and magic lights, and Light Placer bulbs. Sliders for global intensity and a shadow light boost need SKSE Menu Framework, which is installed.
  - Game version: its source builds on CommonLibSSE-NG, which supports 1.5.97 and later in one DLL.
- **[Light Placer](https://www.nexusmods.com/skyrimspecialedition/mods/127557)** by powerofthree.
  - Version: v5.0.0, updated 2026-09-25.
  - What it does: attaches real lights to objects and actors through JSON files. Light Limit Fix, built into Community Shaders, keeps them from flickering.
  - Requirements: powerofthree's Tweaks, which is installed.
  - Game version: its source builds the SE and AE versions separately, and Nexus has one archive. Whether it carries the SE build has to be checked at install.
- **[CS Light](https://www.nexusmods.com/skyrimspecialedition/mods/138443)** by Bottle and the Community Shaders Discord.
  - Version: v2.0.1, updated 2026-05-27.
  - What it does: Light Placer settings that put bulbs on candles, lanterns, fires, potions, ingredients, windows, plants, insects and effects. It works with any lighting mod.
  - ENB lights: its author notes that Community Shaders stopped supporting them in 1.4, so ENB light mods do nothing here.
  - Requirements: it wants [First person magic hand light fix](https://www.nexusmods.com/skyrimspecialedition/mods/142757) for the light from spells in the player's hand.
- **[Embers XD](https://www.nexusmods.com/skyrimspecialedition/mods/37085)** by mindfIux.
  - Version: v3.3.0, updated 2026-10-17.
  - What it does: overhauls campfires and other fires.
  - Lux support: its installer has a Lux Orbis plugin, and there's a Light Placer add-on.
  - Settings: it needs `iMaxDesired=10000` under `[Particles]` in SkyrimPrefs.ini. This profile has 2000.
- **The alternative set: True Light with ATLM.**
  - The mods: [True Light](https://www.nexusmods.com/skyrimspecialedition/mods/135488) v3.6.5 by Bottle, now maintained by SkrubbySkrubInAShrub, with ATLM v3.1, [Luma Utility](https://www.nexusmods.com/skyrimspecialedition/mods/177961), CS Light, Light Placer and Window Shadows Ultimate.
  - Its strengths:
    - It was built for Community Shaders and inverse square lighting from the start.
    - It edits cells through Luma Utility's JSON files instead of plugins, so it doesn't conflict there.
    - It casts window shadows.
  - Its weaknesses:
    - It doesn't rework roads or exterior lights the way Lux Via and Orbis do. True Light's exterior bulbs are optional, and 2 of these lists add Lux Via anyway.
    - It has fewer patches.
    - True Light can't be counted in Wabbajack's index.
  - Time of day: [Helios](https://www.nexusmods.com/skyrimspecialedition/mods/181533), or the older DIAL, can make interiors follow the weather and the time of day. Helios also appears with Lux in 3 lists.
- **Not recommended:** Enhanced Lights and FX (last updated 2017), Luminosity (2021), Relighting Skyrim and Modern Lighting Overhaul 2. Few Community Shaders lists use them, and none of them is tuned for inverse square lighting. Mixing Lux CS with Window Shadows Ultimate or ATLM is out too: Lux CS's author calls them incompatible.

## Fit with this list

- **Requirements are installed:** SKSE Menu Framework, powerofthree's Tweaks, and Community Shaders with Inverse Square Lighting in its core.
- **1.5.97:** ISL Helper SKSE and Lux CS's plugin share one source, built for SE and AE alike. Light Placer needs checking at install. Lux, Orbis, Via, CS Light and Embers XD have no DLLs.
- **Landscape:** Lux Via carries landscape and navmesh edits. Run AutoBlend again afterwards, then PGPatcher.
- **Patches:** the patch hubs' installers pick patches for what's installed. They don't say whether they cover Tomato's Riften, the Imperial Forts or the farmhouses, or Vanaheimr's caves. Check with `tools/fomod.py show` and `tools/mo2.py conflicts` at install.
- **Weather:** there's none yet. Lux Orbis works with any weather. The Lux CS lists pair it with NAT.CS III or Obsidian CS, and that's a separate choice.
- **Particles:** Embers XD needs `iMaxDesired` raised to 10000. Particle Patch is already installed, as it is in 10 of the 15 Lux CS lists.
- **LOD:** Lux Via and Orbis add objects to the world. DynDOLOD, planned for later, would take them into account.
- **Separator:** a new `Lighting & Weather` separator between Architecture and Gameplay, so that Lux Via and Orbis load after the landscape and town mods. The weather mod goes there too. Light Placer belongs in SKSE & Frameworks and ISL Helper SKSE in Shaders.

## Recommendation

**Lux, Lux Orbis and Lux Via, converted with Lux CS, in a new `Lighting & Weather` separator.**

| Order | Mod | Separator | Installer choices |
|---|---|---|---|
| 1 | Light Placer | SKSE & Frameworks | The SE build |
| 2 | ISL Helper SKSE | Shaders | Main file |
| 3 | Lux Via, then Lux via - Patch Hub | Lighting & Weather | Main file, with the patches its installer detects |
| 4 | Lux, then Lux - Patch Hub | Lighting & Weather | No optimized meshes; the detected patches |
| 5 | Lux Orbis, then Lux Orbis - Patch Hub | Lighting & Weather | The detected patches; keep the meshes with a "Lux" prefix |
| 6 | Lux CS | Lighting & Weather | SKSE plugin, Light Placer add-on, CS Light compatibility |
| 7 | CS Light, First person magic hand light fix | Lighting & Weather | The options that match Lux CS |
| 8 | Embers XD 2K | Lighting & Weather | The Lux Orbis plugin, with its Light Placer add-on |

The owner chose this kit on 2026-11-03. That's about 2.4 GB of downloads, most of it Lux Via. Then raise `iMaxDesired`, sort with LOOT, and have the owner run AutoBlend before PGPatcher. Look at it in game in interiors and in towns at night.

This kit was installed on 2026-11-03, as the [changelog](../CHANGELOG.md) records, with the official update files from Lux's and Lux Via's pages. What the install settled:
- **1.5.97:** Light Placer's installer has an SE 1.5.97 option, and its DLL exports the entry point SKSE needs on 1.5.97. ISL Helper SKSE's DLL exports both entry points.
- **Lux CS 2.6.0** has no separate SKSE plugin option any more: that plugin is now ISL Helper SKSE, which it requires. Its Light Placer add-on is the `LightPlacer` folder that comes with its main option. It lights candles, chandeliers, lanterns, torches, Nordic halls, furniture and vanilla fires. CS Light 2.0 no longer lights the first five, so the only overlap is furniture: CS Light's Furniture option stays out, as its own installer suggests for Lux CS.
- **The "Lux" prefix:** Lux Orbis's installer makes you pick a set of "optimized meshes". Of the 113 meshes it installs, 108 sit at vanilla paths, cut up for the old light limit that Light Limit Fix in Community Shaders removes. They would have overridden Assorted Mesh Fixes, Faultier's, SMIM, Particle Patch, TomatoRim, Blended Roads and AutoBlend's output, so they were removed. The 5 with a "Lux" prefix are new assets, not replacements, and they stay. Two of them are used by Lux, Orbis and Via themselves.
- **Patches:** the three hubs add 34 patches, all for Creation Club content and Skyrim Unbound. None covers Tomato's Riften, Imperial Forts or farmhouses, or Vanaheimr's caves. Tomato's Whiterun and Faultier's ship their own Lux window masks, so Lux's vanilla masks were removed to let theirs win. Faultier's Whiterun mask is hidden too, since Tomato's mod supplies Whiterun's windows.
- **Landscape:** Lux Via's landscape and navmesh edits overlap no other landscape plugin in this list.
- **Load order:** two LOOT rules make Orbis and Lux CS's Orbis plugin win over Lux Via's plugin, as Via's author asks. No rule puts Lux CS's Orbis plugin after the Orbis patches, although its installer asks for that. It shares no references with them, and its copies of their cells would undo region and water fixes.

**Weather:** Lux Orbis doesn't depend on it, but exteriors and the overall tone change with it. [The weather note](../research/weather.md) recommends Obsidian Weathers with Obsidian CS, installed alongside this kit.

**The other way:** if window shadows and a set designed for Community Shaders matter more than roads and patch coverage, choose True Light with ATLM and Window Shadows Ultimate, and keep Lux Via for the roads, as Morkeskygge does.

## Not verified

- No visual comparison was made, and none of these mods had been seen in this list's game when this was written.
- How Lux Via's road and bridge edits look with Northern Roads, which replaced Blended Roads later on 2026-11-03. Lux Via's Blended Roads bridge option came out then. Northern Roads' Patch Collection covers Lux, Lux Orbis and Lux Via, and keeps Lux Via's bridges where both mods have one. Lux Via's optional Better Dynamic Snow patch, for version 2, was left out. [The roads note](../research/roads.md) has the details. That leaves only what the game shows.
- How Lux CS's tone mapping combines with a weather mod's own tone mapping for Community Shaders. 11 of the 15 Lux CS lists combine them.
- How many lists run True Light, which Wabbajack's index doesn't name.
- What Placed Light is. It isn't on Nexus under that name.
