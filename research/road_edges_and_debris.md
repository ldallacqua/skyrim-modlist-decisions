# Road edges and road debris

Checked 2026-11-03. Two questions from the owner, after the PBR conversion of Omen Apollo's road texture went in (see [the roads note](roads.md)):
- **Edges:** the road now has much more depth than the ground beside it, and the change at its edge looks wrong. Which ground textures pair best with it?
- **Debris:** the roads have no leaves, pebbles or other debris on them.

Sources:
- **This profile's plugins:** all 217 active plugins were read in load order, which covers 52,364 landscape records.
- **The height maps** of the winning textures, decoded locally.
- **Community Shaders 1.9.1's** terrain shader source.
- **Wabbajack's reports**, read on 2026-11-03, and the earlier copies of seventeen lists' `status.json`.
- **Nexus Mods' public API.**

Nothing was downloaded.

## Takeaway

**Outcome:** the ground stayed TomatoRim's and a debris plugin went in. The road's depth went down to 0.5 first, but the owner found it flat, so it went back to 1.0. Deepening the ground instead smeared it in game, so the ground is back to TomatoRim's own maps. See [What was chosen](#what-was-chosen-2026-11-03) and [Deeper ground](#deeper-ground-instead-of-a-shallower-road) below.

- **The mismatch is measured.**
  - Northern Roads paints the converted dirt road in 506 landscape records (1,100 quadrants).
  - Most of the ground beside it is TomatoRim's pine forest, fall forest dirt, rocks, field grass and Dirt02.
  - Their relief is 0.015 to 0.06. That's the height map's spread times its `displacementScale`, with a weighted median of about 0.04. The road's is 0.118.
- **The cheapest fix is to meet in the middle, inside this setup.**
  - Lower the road's `displacementScale` to about 0.5. That gives 0.059, still rougher than any common neighbour except rocks and snow.
  - If the edges still look off, raise TomatoRim's two flattest neighbours.
  - Both are JSON edits, undone by disabling a mod. No download, no regeneration.
- **The ground that lists actually pair with deep roads is Vanaheimr Landscapes.**
  - In ten of the twelve lists that run Vanaheimr's Northern Roads, Vanaheimr Landscapes comes with it.
  - It runs in 18 of the 32 lists with a deep Northern Roads texture.
  - Only Dovahmeme is shown to run its PBR files on Community Shaders.
  - Whether its PBR heights are deeper than TomatoRim's wasn't measured.
  - Switching would replace TomatoRim, the ground this list was built on.
- **Debris:**
  - Northern Roads' road textures carry no grass records at all, so nothing ever grows on them, debris included. No Northern Roads add-on changes that.
  - The models are already installed. DrJacopo's library has pebbles, small rocks, pine needle debris and fallen aspen leaves, and Merethic already uses its pine debris in the pine forests.
  - A small patch could give the dirt road a sparse debris mix. It would be the same everywhere, because one road texture can't carry different grass by region.

## The edge, measured

What borders the converted dirt road. Northern Roads paints it with 10 landscape textures, all using the same texture set. Share is coverage in the quadrants it occupies, and relief is the height map's spread times `displacementScale`:

| Share | Ground texture | Won by | `displacementScale` | Height spread | Relief |
|---|---|---|---|---|---|
| 12.7% | Pine forest 02 (two variants) | TomatoRim | 0.325 | 0.047 | 0.015 |
| 9.9% | Fall forest dirt | TomatoRim | 1.0 | 0.038 | 0.038 |
| 13.7% | Rocks (two variants) | TomatoRim | 1.0 | 0.057 | 0.057 |
| 11.9% | Field grass 01 (two variants) | TomatoRim | 1.0 | 0.022 | 0.022 |
| 6.6% | Dirt02 | TomatoRim | 1.0 | 0.030 | 0.030 |
| 5.6% | Snow | TomatoRim | 1.0 | 0.124 | 0.124 |
| 5.7% | Tundra rocks (two variants) | TomatoRim | 1.88 | 0.057 | 0.107 |
| 6.4% | Fall forest grass (three variants) | TomatoRim | 1.0 | 0.034 | 0.034 |
| 4.2% | Tundra 01 (two variants) | TomatoRim | 1.0 | 0.055 | 0.055 |
| 3.6% | Field grass 02 (two variants) | TomatoRim | 1.0 | 0.094 | 0.094 |
| 3.7% | No texture (the default ground) | none | none | none | 0 |
| | **The converted road** | this list | 1.0 | 0.118 | **0.118** |

These rows cover 89% of the neighbour coverage. The rest is riverbeds, mud, other forest grounds and snow rocks, at 0.03 to 0.15. Weighted by coverage, the median relief is 0.038.

What the shader does with it, from `ExtendedMaterialsTerrain.hlsli` and `ExtendedMaterialsParallaxCore.hlsli`:
- **Height blending is on here** (`EnableHeightBlending`). Where two layers meet, the higher one shows. The road's height averages 0.40 and its main neighbours' 0.43 to 0.68, so the neighbours take the edge and the road reads as sunk below them. That part is natural. What isn't is the relief changing three times over in a few steps.
- **Self-shadowing** is the height difference toward the light, times 4 or 8. A deep layer next to a shallow one is lit very differently.
- **The parallax march** scales with the deepest layer in the blend, so the road's depth also shifts the neighbour's texture at the edge.

TomatoRim set the pine forest's `displacementScale` to 0.325 itself. The field grass and fall forest maps have a spread of only 0.022 to 0.038. Raising them amplifies maps with little real height in them, so it may add little but swimming.

## What lists pair with deep roads

Lists that install a deep Northern Roads texture: Omen Apollo's, Rugge's, Alternate Complex Parallax, HD Remastered, Vanaheimr's, YXZ's or 0ctoProcessor's PBR. Grouped by their ground:

| Ground | Lists | Of them on Community Shaders |
|---|---|---|
| Vanaheimr Landscapes AIO | Authoria, CSVP, Diaries of Dibella, Dovahmeme, Hymns of Hircine, Journals of Jyggalag, Krentoraan, LoreRim, Lyra Requiem, Mantras of Mara, NGVO, ReSkyrimed, SUP, Tomes of Talos, Visions of Vaermina, Whispers of Mara, Wunduniik, tightarse | 7 |
| Tomato's Complex Landscapes, TomatoRim's non-PBR sibling | Diaries of Dibella, Hymns of Hircine, Journals of Jyggalag, Mantras of Mara, Tomes of Talos, Visions of Vaermina, CSVP, Chaos Mage, Eldergleam, Kirbylite, Krentoraan, Skyrim Odyssey, Viir Suum, apostasy | 7 |
| TomatoRim PBR Landscapes | Lumina, ReaperGleam, Whispers of Mara | 1 |
| Faultier's PBR Skyrim, mostly under another ground | Dovahmeme, FILFY, the two Kirbykings lists, Lumina, ReaperGleam, Whispers of Mara | 2 |
| Vyrthland Landscapes (YXZ) | the two Kirbykings lists, Mages and Vikings | 0 |
| Skyland, Majestic, HD Remastered | Ainulindale, Ascended Fates, Chaos Mage, Eldergleam, ReaperGleam, apostasy | 2 |

Some lists run two grounds, so the rows overlap. The first six of the Tomato's Complex lists are one family, and they run Vanaheimr too.

Which Vanaheimr file, where the lists' files were checked:
- **Dovahmeme:** PBR 2k.
- **Diaries of Dibella and Tomes of Talos:** the plain 2k file from version 2.5, with no complex material or PBR.
- **Wunduniik and NGVO:** complex material 2k.

So of the seven Community Shaders lists with Vanaheimr, Dovahmeme is the only one shown to use its PBR files.

- **The most common matched set** is Vanaheimr's: Vanaheimr Landscapes plus Vanaheimr - Northern Roads, both by Cl3mus. Ten of the twelve lists with Vanaheimr's roads take both.
- **Dovahmeme** is the one PBR Community Shaders list doing it. It runs Vanaheimr Landscapes PBR 2k, Vanaheimr - Northern Roads PBR 2k, and TMD Dirt Roads made for Vanaheimr PBR, over Faultier's.
- **Lumina,** the list closest to this one, keeps TomatoRim's PBR ground and pairs it with Vanaheimr's PBR roads.

## Candidates for the ground

- **Keep TomatoRim and tune the depth.** No download. Change the road's `displacementScale` in its own mod, and if needed a small JSON-only mod that raises chosen TomatoRim sets. It's reversible by disabling. Nothing to regenerate, since the paths don't change.
- **[Vanaheimr - Landscapes - AIO](https://www.nexusmods.com/skyrimspecialedition/mods/145439)** by Cl3mus.
  - Version and popularity: v7.1, updated 2026-10-14, 2,383 endorsements, 1.25 million downloads.
  - PBR files: 0.77 GB at 1k, 2.09 GB at 2k, 6.64 GB at 4k.
  - Requirements:
    - Already here: ERM, Icy Mesh Remaster and PGPatcher. Terrain Helper is built into Community Shaders.
    - New since 7.0: [XPMF](https://www.nexusmods.com/skyrimspecialedition/mods/192698), an SKSE plugin for snow and ash materials. It's v0.8.0, supports 1.5.97, and Lumina runs it.
    - Snow: Simplicity of Snow Sulfur Ash Moss is recommended, and Better Dynamic Snow is supported through XPMF.
  - Designed around Freak's Floral Fields. Merethic, installed here, has a "Vanaheimr Cut" file (v1.1, 0.15 GB), so the grass can stay PBR.
  - It covers ground, ice and mountains. Farmhouses, mines, ore veins and Northern Roads are separate mods.
  - It would replace TomatoRim PBR Landscapes, and TomatoRim's Northern Roads add-on with it. The converted road could stay, or give way to Vanaheimr's own.
- **[Vanaheimr - Northern Roads - PBR](https://www.nexusmods.com/skyrimspecialedition/mods/152575)**, v2.7, 0.42 GB at 2k. It's the road made for Vanaheimr's ground. Rugge's PBR Rocky Mossy also installs over it.
- **[Vyrthland - Landscapes - AIO](https://www.nexusmods.com/skyrimspecialedition/mods/190416)** with **[YXZ True Diverse Northern Roads Reforged](https://www.nexusmods.com/skyrimspecialedition/mods/182981)** by YXZvyr.
  - Vyrthland: v2.0, 150 endorsements, created 2026-09-04, 3.40 GB at 2k.
  - YXZ's roads: regional variants painted into the landscape, among them an "Autumnal Leaves Byway" with leaves in the texture.
  - YXZ's plugin repaints terrain over Northern Roads and its patches. Its page asks for an SSEEdit script run to re-sync the edges after every patch change.
  - No Community Shaders list uses either. Too new and too invasive for now.
- **Not for this list:** Tomato's Complex Landscapes, Skyland, Majestic and Cathedral Landscapes are non-PBR.

## Debris

What's there now:
- **The road textures:** Northern Roads' 10 dirt road textures, its dry dirt and its mud carry no grass records. On purpose, roads stay clear.
- **Next to the road:** Merethic gives pine forest 02 two debris records, `PineDebrisA` and `B`, which use DrJacopo's `DeadPineDrJ03` and `04`. The field grass and fall forest grass get grass and flowers. Rocks and Dirt02 get nothing.
- **Nature of the Wild Lands** places forest debris (logs, stumps, branches) as objects in the forests, not on roads. Lumina even installs a mod to reduce it.

Debris mods found:

| Mod | Lists | What it does | For the roads |
|---|---|---|---|
| [DrJacopo's 3D Landscapes and Grass Library](https://www.nexusmods.com/skyrimspecialedition/mods/80687) | installed | Grass models, among them `PebbleGrass01`-`07`, `RockGrass01`-`04` in small and medium, `DeadPineDrJ03`/`04`, `DeadAspenDrJ01`-`14` and aspen leaves | The assets for a road debris patch, already here |
| [the Pebbles SE](https://www.nexusmods.com/skyrimspecialedition/mods/49413) | 6 (LoreRim) | Replaces the vanilla pebble meshes | Only better pebbles where pebbles already are |
| [More Pebbles Please](https://www.nexusmods.com/skyrimspecialedition/mods/82720) | under 6 | Adds rock grass to vanilla landscape textures | Not to Northern Roads' textures |
| [Immersive 3D Leaves](https://www.nexusmods.com/skyrimspecialedition/mods/170242) | under 6, LoreRim among them | 3D fallen leaves | Not checked further; it would also need assigning to the road |
| [Skyrim 3D Landscapes](https://www.nexusmods.com/skyrimspecialedition/mods/18247) | 7 | Groundcovers for vanilla textures, from 2020 | Overlaps Merethic, and doesn't touch the roads |
| [Forest Fragments](https://www.nexusmods.com/skyrimspecialedition/mods/113528) | under 6 | Nature of the Wild Lands' debris, standalone | Already here through Nature of the Wild Lands |
| Footprints / [Dynamic Footprints SKSE](https://www.nexusmods.com/skyrimspecialedition/mods/175254) | 42 / 12 | Footprints where actors walk | Not debris, but life on the road |

No Northern Roads add-on adds debris. Among the 124 Nexus mods named after it there are clutter-only, decluttered and no-clutter versions, all about its objects, not about debris on the surface.

**A road debris patch** would be a small ESL-flagged plugin:
- **New grass records:** about four, using DrJacopo's small pebbles, small rocks and pine needle debris, at low density so the road still reads as a road.
- **The road textures:** Northern Roads' 10 dirt road textures point at those records, and so could its dry dirt.
- **Limits:**
  - One mix for every region, from the Whiterun tundra to the Rift. Aspen leaves would be wrong in the tundra, so leaves stay out.
  - Real regional debris needs separate road textures per region painted into the terrain, which is YXZ's approach.
- **Grass cache:** none needed. This list doesn't cache grass ([0014](../decisions/0014-extended-grass-without-cache.md)), so new grass shows straight away.
- **Settings:** density, slope limits and size can be tuned in the plugin after a look in game.

## Recommendation

1. **Edges: tune first, here.**
   - Set the road's `displacementScale` to 0.5 in `Northern Roads - Omen Apollo Dirt PBR (converted)`. That's 10 small JSON edits, done with MO2 closed.
   - Look at the Riverwood and Whiterun roads again.
   - If the edge still jars, add a JSON-only mod that raises pine forest 02 from 0.325 to 0.7 and fall forest dirt from 1.0 to 1.5, then look again.
   - No downloads. Disabling undoes it.
2. **Only if the tuned road still looks out of place, consider Vanaheimr's ground.**
   - Before deciding, download Vanaheimr Landscapes PBR 1k (0.77 GB) and measure its height maps the same way, without installing it.
   - If it is deeper, the switch means: Vanaheimr Landscapes PBR, Merethic's Vanaheimr Cut, and XPMF. TomatoRim's landscapes and its road add-on come out, and AutoBlend and PGPatcher run again.
   - The pine trees, towns and farmhouses stay.
3. **Debris: a road debris patch built here from DrJacopo's installed models.** No download. Pebbles, small rocks and pine needles at low density on the dirt roads, tuned after a look in game.

## What was chosen, 2026-11-03

The owner left the choice open: TomatoRim or Vanaheimr for the ground, and back to Blended Roads if debris could never look right on Northern Roads. The record is [0015](../decisions/0015-keep-tomatorim-ground-and-northern-roads.md).

- **The ground stays TomatoRim's.**
  - Depth is a per-set setting here, and the brightness was already matched, so one author for road and ground isn't needed for a clean edge.
  - Switching would cost the PBR grass. [Merethic Grasslands PBR](https://www.nexusmods.com/skyrimspecialedition/mods/193219) converts only Merethic's Vanilla and Exist files, and the Vanaheimr Cut isn't among them.
  - Vanaheimr's PBR heights are still unmeasured, so a switch might not fix the edge anyway.
  - Lumina mixes authors the same way. Vanaheimr's own roads page suggests Rugge's road textures to players who don't like its own.
- **The roads stay Northern Roads.** Blended Roads lays meshes over the ground. Grass can't grow on a mesh, and height blending can't blend one into the terrain. Northern Roads' roads are landscape textures, which can carry grass records.
- **Done:**
  - The converted road's 10 texture set files went to `displacementScale` 0.5, a relief of 0.059. Reverted the same day, below.
  - **`Northern Roads - Road Debris`**, a new mod in `Landscape`, placed last there. It has no files that conflict. It holds `Northern Roads - Road Debris.esp`, ESL-flagged, built by `tools/road_debris.py`:

    | Grass record | Model (DrJacopo's) | Density |
    |---|---|---|
    | `NRDebris_Pebbles01` | `PebbleGrass01.nif` | 6 |
    | `NRDebris_Pebbles03` | `PebbleGrass03.nif` | 5 |
    | `NRDebris_Pebbles06` | `PebbleGrass06.nif` | 4 |
    | `NRDebris_SmallRocks02` | `RockGrass02_Small.nif` | 2 |

    - Density is the share of points on the 40-unit grass grid (`iMinGrassSize=40`). Together, about one clump per 1.4 m of road, on average.
    - Placement copies vanilla `RockGrass01`: slopes 0 to 40, offset up to 32 units, a 25% size spread, uniform scaling and fit to slope.
    - It overrides the 10 dirt road textures and Whiterun's outer road, which only Northern Roads.esp defined before, and adds four grass entries to each.
    - All the models use the vanilla `RocksGrass01.dds` texture, so the debris is grey stone and not PBR. Grass doesn't need to be PBR to sit next to PBR ground.
  - LOOT placed the plugin after Northern Roads.esp and moved nothing else.

## Deeper ground instead of a shallower road

The owner's second look, the same day: the debris helped, and the edge looked better at 0.5, but the road read as a flat texture. The depth is what makes the illusion. They asked to raise the ground instead.

Raising the ground's `displacementScale` alone would backfire. In `ExtendedMaterialsTerrain.hlsli`, height blending multiplies each layer's weight by 3 to the power of 8 × `(height - 0.5) * displacementScale`, then cubes it. Most of the road's neighbours sit high on average (fall forest dirt and field grass average 0.67, the road 0.40). Tripling their scale would triple that lead too. The ground would then swallow the road wherever its vertex weight is above a few percent, and fade faint trails out entirely.

So `tools/terrain_depth.py` stretches each height map's contrast around its own average instead:
- **Target relief 0.09**, three quarters of the road's 0.118. The stretch is at most 3 times, and backs off until under 0.5% of pixels clip.
- **The averages stay put**, so the edges fall where they did. Sets under `displacementScale` 1 rise toward 1, only as far as needed, with the average re-centred so `(average - 0.5) * scale` doesn't change. TomatoRim's pine forest 02 goes from 0.325 to 1.0 this way.
- **A light 3x3 blur** goes under any stretch above 1.5, so BC4 block noise isn't amplified.
- **Left alone:** the converted road, the reference, and 15 maps already at or above the target, among them snow, tundra rocks, river beds and the volcanic gravels.

What was written, to `Terrain Depth - Outputs` in the `Outputs` separator, since it had to win over Faultier's and Tomato's town packs too:
- **59 height maps**, all 1K BC4 like their sources, every mip checked.
- **9 texture set files** with a raised scale: pine forest 02, Reach grass and seven Soul Cairn sets.

The road's main neighbours, before and after:

| Ground | Relief before | After |
|---|---|---|
| Pine forest 02 | 0.015 | 0.086 |
| Fall forest dirt | 0.038 | 0.088 |
| Rocks | 0.057 | 0.089 |
| Field grass 01 | 0.022 | 0.061 (capped by the 3 times limit) |
| Dirt02 | 0.030 | 0.085 |
| Fall forest grass | 0.034 | 0.089 |
| Tundra 01 | 0.055 | 0.088 |
| Snow, tundra rocks, field grass 02 | 0.094 to 0.124 | unchanged |

The full table is what the tool prints.

**In game it failed.** The owner's screenshot showed the ground smeared into vertical streaks, the look of a parallax march overshooting. The files were as intended, so the cause is the approach:
- TomatoRim's height maps are mostly fine surface detail, not real height. Stretched 1.6 to 3 times, their small bumps became slopes too steep for the shader's 16-step march with its one refinement pass.
- The road's map is Omen Apollo's real height, smooth at large scale, which is why it carries 0.118 without smearing.

`Terrain Depth - Outputs` is disabled, and the ground is back to TomatoRim's own maps and settings. The road stays at 1.0. Deeper ground would need height maps made deep from the start, not stretched ones.

## Not verified

- How the debris looks on the road: pebble size, density, and whether it floats over the parallax ruts.
- How deep Vanaheimr's PBR heights are. None of its files were downloaded.
- How DrJacopo's debris models look on a road, and what density reads as debris rather than grass.
- Immersive 3D Leaves and More Pebbles Please, beyond their pages.
- Whether TomatoRim's pine forest has a reason for its 0.325 beyond taste. Its height map is now at 1.0, stretched 1.9 times.
