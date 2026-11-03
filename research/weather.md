# Weather for a Lux CS list

Checked 2026-11-03. Question: which weather mod fits this list, given [the lighting note](../research/lighting.md)'s recommendation of Lux with Lux CS. The game still runs vanilla weathers. Community Shaders 1.9.1 includes Cloud Shadows and Sky Sync in its core, and Skylighting is installed, which the weather add-ons for Community Shaders require.

The evidence is the same kind as in the lighting note: Wabbajack's published reports, the Nexus page of each candidate, and the pages of the landscape mods already installed. Counting lists measures adoption, not quality. Where a family of lists shares a template, it's counted once in the "independent" column. Wanderer's Way and its six siblings are one family. Gate to Sovngarde's two editions are another.

## Takeaway

Three weather mods cover most Community Shaders lists. Each has an add-on that retunes it for Community Shaders' filmic tone mapping:

| Weather | Add-on for Community Shaders | CS lists with the weather | With the add-on |
|---|---|---|---|
| [NAT.ENB III](https://www.nexusmods.com/skyrimspecialedition/mods/27141)'s weather plugin | [NAT.CS III](https://www.nexusmods.com/skyrimspecialedition/mods/139567) | 18 | 16 |
| [Azurite Weathers III](https://www.nexusmods.com/skyrimspecialedition/mods/42731) | [Azurite III CS](https://www.nexusmods.com/skyrimspecialedition/mods/162153) | 15 | 8 |
| [Obsidian Weathers and Seasons](https://www.nexusmods.com/skyrimspecialedition/mods/12125) | [Obsidian CS](https://www.nexusmods.com/skyrimspecialedition/mods/162627) | 11 | 6 |

Another 14 Community Shaders lists use no weather mod we could detect.

The pairings follow authors. Bottle wrote Lux CS, NAT.CS III and Obsidian CS, as well as True Light, CS Light and ISL Helper SKSE. Dlizzio wrote Azurite III CS and co-wrote Window Shadows Ultimate. So the 15 Lux CS lists run NAT or Obsidian, and 7 of the 8 Azurite III CS lists run the ATLM lighting set.

**Recommendation: Obsidian Weathers and Seasons with Obsidian CS.** Four things point to it:
- Its add-on was tuned by Lux CS's author.
- The author of Merethic Grasslands, our grass, says it works well. They name Azurite III as the best for grass colors and don't mention NAT.CS.
- Lalaland, the list closest to ours (Nature of the Wild Lands, Merethic, Lux CS), uses it.
- Lux and Obsidian have long been paired. Rudy's ENB preset for the two has 41,776 endorsements.

Beyond that it's taste. Obsidian is moody, with fog that hides distant land. NAT is brighter and more colorful. Azurite aims at a realistic atmosphere.

## What Community Shaders lists install

Weathers:

| Weather | All 117 SE lists | 58 CS lists | Independent CS lists | 15 Lux CS lists | 15 ATLM lists |
|---|---|---|---|---|---|
| NAT, weather plugin | 51 | 18 | 12 | 9 | 2 |
| NAT.CS III | 21 | 16 | 10 | 8 | 1 |
| Azurite Weathers | 22 | 15 | 14 | 1 | 8 |
| Azurite III CS | 9 | 8 | 7 | 0 | 7 |
| Obsidian Weathers and Seasons | 17 | 11 | 11 | 3 | 5 |
| Obsidian CS | 9 | 6 | 6 | 3 | 3 |
| Wonders of Weather, alongside another weather | 8 | 3 | 3 | 1 | 0 |
| Mythical Ages | 2 | 2 | 2 | 0 | 0 |
| Cathedral Weathers and Seasons | 7 | 1 | 1 | 1 | 0 |

Counted the same way, the Lux CS lists split evenly. The 9 NAT lists are three independent ones: the Wanderer's Way family, LalupK in the Woods and CSVO. The 3 Obsidian lists are Lalaland, Nordic Souls and Arkay's Commandment.

Sky and storm add-ons, by the weather they're paired with:

| Add-on | 58 CS lists | 18 NAT | 15 Azurite | 11 Obsidian |
|---|---|---|---|---|
| Moons and Stars - Sky Overhaul SKSE | 40 | 15 | 9 | 8 |
| Aurora Fix | 31 | 11 | 7 | 4 |
| Splashes of Storms | 27 | 12 | 5 | 4 |
| Lightning VFX Edit | 24 | 11 | 8 | 4 |
| Unique Map Weather | 23 | 7 | 8 | 1 |
| Water Effects Brightness and Reflection Fix | 18 | 13 | 2 | 2 |
| No More Blinding Fog | 18 | 6 | 3 | 6 |
| Distant Rolling Thunder | 17 | 10 | 3 | 4 |
| Rainbows Remade | 15 | 9 | 3 | 3 |
| Storm Lightning | 14 | 4 | 3 | 5 |
| Praedy's Night Sky AIO | 13 | 4 | 4 | 4 |

The three Obsidian CS lists closest to ours:

| List | Weather and sky |
|---|---|
| Lalaland (NOTWL, Merethic, Lux CS) | Obsidian, Obsidian CS, Darker Nights Redone, Moons and Stars, Praedy's Night Sky, Realistic Galaxy, No More Blinding Fog, Azurite Mists |
| Nordic Souls (Lux CS) | Obsidian, Obsidian CS, its MCM patch, Moons and Stars, Praedy's Night Sky, Aurora Fix, Lightning VFX Edit, Splashes of Storms, Distant Rolling Thunder |
| Everwild | Obsidian, Obsidian CS, and Obsidian's Vigilant patch |

## The candidates

- **[Obsidian Weathers and Seasons](https://www.nexusmods.com/skyrimspecialedition/mods/12125)** by DrJacopo and Arindel.
  - Version: v1.07a, last updated 2021-05-09. The plugin is about 400 kB.
  - What it does: about 90 weathers, DLC included, that keep vanilla weather IDs. The seasons change lighting and climate, and take effect when the player sleeps. A power toggles season effects, filters and a weaker sun.
  - Compatibility, by its author:
    - It works with every interior lighting overhaul, and adjusts torches and magelight for its darker nights.
    - Mods that darken nights or add storms need patches made for it.
    - Its seasons edit regions, so audio overhauls that add region sounds need a patch. None is installed here.
- **[Obsidian CS](https://www.nexusmods.com/skyrimspecialedition/mods/162627)** by Bottle.
  - Version: v1.1.2, updated 2025-10-28.
  - What it does: filmic tone mapping through Community Shaders, new volumetric lighting and retuned image spaces, with nights brightened for playability.
  - Load order: it should overwrite Moons and Stars and Volumetric Mists.
  - It recommends Realistic Galaxy, Rally's Celestial Canvas and Moons and Stars.
- **[NAT.CS III](https://www.nexusmods.com/skyrimspecialedition/mods/139567)** by Bottle.
  - Versions: v2.0.0, updated 2025-10-28. It goes over NAT.ENB III's weather plugin, v3.1.1C from 2023-06-04, which is the only file needed from that page.
  - What it does:
    - It redoes the image spaces and adds an HDR sun texture.
    - It applies filmic tone mapping and changes many weather colors.
    - It replaces rain and snow textures for Community Shaders.
  - Requirements: Cloud Shadows and Skylighting. Its water shadow option also needs Water Effects Brightness and Reflection Fix.
  - Its author calls it the essential weather mod for Community Shaders.
- **[Azurite Weathers III](https://www.nexusmods.com/skyrimspecialedition/mods/42731)** by JonnyWang, with **[Azurite III CS](https://www.nexusmods.com/skyrimspecialedition/mods/162153)** by Dlizzio.
  - Versions: Azurite v3.35, updated 2026-03-25, the most recently maintained of the three. Azurite III CS v1.2.1, updated 2026-07-20.
  - What Azurite does: it ships its own storm audio, precipitation, clouds and night sky. A power sets seasons and night and interior brightness. Audio overhauls need a patch.
  - Azurite III CS: it needs Cloud Shadows, Skylighting and Sky Sync. It's incompatible with Azurite's Darker Nights, HDR, Enhanced and Alluring Sunsets add-ons.
  - Fit with our landscape: its screenshots use Nature of the Wild Lands' Nordic Cut and Tomato's Riften, both installed here, and Merethic's author ranks it first for grass colors. But no list pairs it with Lux CS.
- **Not recommended:**
  - Cathedral Weathers (last updated 2023) and Mythical Ages (2019) are each in one or two Community Shaders lists, with no Community Shaders tuning.
  - Wonders of Weather adds weather variety on top of another weather mod; that's a separate choice.
  - Bottle's own Faithful Weathers is in no list.

## Fit with this list

- **Requirements:** Cloud Shadows and Sky Sync are part of Community Shaders 1.9.1, and Skylighting is installed. Obsidian and Obsidian CS have no SKSE plugins.
- **Lux:** Lux Orbis's author says it works with every weather mod and recommends using one. Lux itself edits some interior cells' sky and weather settings. Whether Obsidian touches the same cells wasn't checked.
- **Grass:** Merethic Grasslands has a grass brightness range of 0.700 to 0.950 that depends on the weather. Set it in Community Shaders' Grass Lighting menu after the weather is in.
- **Snow:** Better Dynamic Snow was installed with its brighter snow option. That may need another look under a new weather.
- **Seasons:** Obsidian's seasons live in its own plugin. They're unrelated to Seasons of Skyrim, which isn't installed.
- **Generators:** a weather mod changes no meshes or landscape, so AutoBlend and PGPatcher don't need to run for it.
- **Separator:** weather goes with the lighting kit. A `Lighting & Weather` separator between Architecture and Gameplay would hold both, about 16 mods.

## Recommendation

**Obsidian Weathers and Seasons with Obsidian CS, installed with the lighting kit in `Lighting & Weather`.**

| Order | Mod | Installer choices |
|---|---|---|
| 1 | Obsidian Weathers and Seasons | Main file |
| 2 | Moons and Stars - Sky Overhaul SKSE | Optional. In 2 of the 3 Obsidian CS lists closest to ours. It supports 1.5.97 |
| 3 | Obsidian CS | Main file, overwriting Moons and Stars |

The owner chose Obsidian on 2026-11-03. That's under 20 MB. Sort with LOOT afterwards. In game, set Merethic's grass brightness, and look at days, nights, storms and snow.

**Alternatives:**
- NAT.CS III, for a brighter and more colorful look. It's the most used weather in Community Shaders lists and also tuned by Lux CS's author. Its water shadow option needs Water Effects Brightness and Reflection Fix.
- Azurite III CS, if grass color matters most, or with the True Light lighting set instead of Lux.

The Nexus pages' screenshots are the quickest way to compare the three looks.

## Not verified

- No visual comparison was made, and none of these has been seen in this list's game.
- Whether Lux's interior cell edits and Obsidian's records overlap. LOOT or SSEEdit would show it after install.
- How Obsidian CS's and Lux CS's tone mapping settings combine. 3 lists combine them.
- Whether Obsidian CS and NAT.CS III, both last updated 2025-10-28, need changes for Community Shaders 1.9.
- How Better Dynamic Snow's brighter option looks under Obsidian.
- The add-ons' builds for 1.5.97, except Moons and Stars, whose page covers it.
