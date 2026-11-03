# 0015. Keep TomatoRim's ground and Northern Roads at their own depths, and add road debris

- **Status:** accepted
- **Date:** 2026-11-03
- **Summary:** The ground stays TomatoRim PBR Landscapes, the roads stay Northern Roads with the converted Omen Apollo dirt, road and ground keep their texture sets' own depth values after two tuning attempts failed in game, and a small plugin adds debris to the dirt roads.

## Context

The converted Omen Apollo road has about three times the parallax depth of the TomatoRim ground beside it (relief 0.118 against a median of 0.038), and the edge looked wrong in game. The roads also had no debris on them. [The research](../research/road_edges_and_debris.md) measured both.

The owner left the choice open: keep TomatoRim's ground or move to Vanaheimr's, and go back to Blended Roads if debris could never look right on Northern Roads. The aim is realism, close to a modern game.

## Options considered

- **Keep TomatoRim and tune.** Lower the road's `displacementScale`, or raise the ground's. No download, undone by disabling.
- **Move to Vanaheimr Landscapes PBR with Vanaheimr's own Northern Roads.** One author for road and ground, and the ground most lists pair with deep roads. But:
  - about 2.5 GB of downloads at 2k, and XPMF as a new SKSE requirement;
  - Merethic Grasslands PBR converts only Merethic's Vanilla and Exist files, so the Vanaheimr Cut would leave the grass without PBR;
  - TomatoRim's road add-on and the conversion would go, and AutoBlend and PGPatcher would run again;
  - only one Community Shaders list, Dovahmeme, is shown running Vanaheimr's PBR files, and their heights weren't measured, so the depth mismatch might not even go away.
- **Go back to Blended Roads.** Its roads are meshes laid over the ground. Nothing can grow on a mesh, and Community Shaders' height blending can't blend a mesh into the terrain. It's worse on both counts.

## Decision

Keep TomatoRim and Northern Roads.
- **Depth is a setting, not an author's style.** Community Shaders reads each texture set's depth from its own `PBRTextureSets` file, and the conversion already matched TomatoRim's road brightness. A road from another author can be made to fit.
- **The lists closest to this one mix authors too.** Lumina keeps TomatoRim's ground under Vanaheimr's PBR roads. Vanaheimr's own roads page suggests Rugge's road textures to players who don't like its own.
- **Northern Roads is the better base for debris.** Its roads are landscape textures, and landscape textures can carry grass records, which is how the engine places debris.

Done on 2026-11-03:
- **First, the road came down.** Its 10 texture set files went from `displacementScale` 1.0 to 0.5, a relief of 0.059. In game the edge improved, but the owner found the road flat: the depth is what sells it. So it went back to 1.0, and the ground came up instead.
- **Then the ground came up, by contrast rather than by scale.** Height blending weighs layers by `(height - 0.5) * displacementScale`, so a bigger scale would also lift the ground's average and let it swallow the road's edges. `tools/terrain_depth.py` stretched 59 PBR ground height maps around their own averages toward a relief of 0.09, into `Terrain Depth - Outputs`. In game the ground smeared into streaks: TomatoRim's maps hold too little real height detail to stretch, and the shader's 16-step march can't follow the steeper slopes. That mod is now disabled.
- **What stays:** every texture set at its own value. The ground is TomatoRim's as shipped, and the converted road keeps the 1.0 that TomatoRim's own files give it. The edge stays deeper on the road side; the debris softens it.
- `Northern Roads - Road Debris.esp`, built by `tools/road_debris.py`, gives the 10 dirt road textures and Whiterun's outer road four sparse grass records: three of DrJacopo's pebble models and one small rock model.

## Consequences

- **Saves:** safe to add to an existing save. Grass isn't saved, and the plugin is ESL-flagged and only overrides landscape textures and adds grass records.
- **Regenerate:** nothing. There's no grass cache ([0014](0014-extended-grass-without-cache.md)), the debris plugin has no meshes or textures, and no texture path changed, so PGPatcher and AutoBlend don't need to run for this.
- **Debris is the same everywhere.** One road texture runs from the tundra to the Rift, so the mix is pebbles and rocks only. Leaves and pine needles come only from the ground beside the road, where Merethic already places them.
- **Debris is spread evenly across the road.** The engine places it by the road texture's coverage, so the middle of the road gets as much as the edges.
- The owner saw the debris with the road at 0.5 and found the edge better. It hasn't been seen with the road back at 1.0.
- `Terrain Depth - Outputs` stays in `Outputs`, disabled. Delete it, or rerun the tool with a much milder `--max-gain`, only after a look in game.

## Confirmation

- In SSEEdit, the 11 road landscape textures' winning override is `Northern Roads - Road Debris.esp`, with four grass entries each. `tools/road_debris.py --dry-run` prints the list it builds.
- `list/plugins.txt` has `Northern Roads - Road Debris.esp` enabled, and `list/modlist.txt` has `Terrain Depth - Outputs` disabled.
- The converted road's texture set files say `"displacementScale": 1.0`.
- By hand, in game: the road keeps its depth, the ground doesn't smear, and the road shows scattered pebbles without reading as gravel.

## Revisit when

- The edge between the deep road and the ground still bothers the owner. Measure Vanaheimr's PBR heights next, which needs a 0.77 GB download, or look for ground textures with real height detail.
- Merethic Grasslands PBR adds the Vanaheimr Cut, which removes the main cost of switching.
- A Northern Roads add-on arrives with regional road textures, so debris can differ by region.

## Evidence

- [research/road_edges_and_debris.md](../research/road_edges_and_debris.md): the edge measured from this profile's plugins and height maps, what lists pair, and the debris options.
- [Merethic Grasslands PBR](https://www.nexusmods.com/skyrimspecialedition/mods/193219): its description names the Vanilla and Exist versions only.
- [Vanaheimr - Northern Roads - PBR](https://www.nexusmods.com/skyrimspecialedition/mods/152575): its description suggests Rugge's road textures to players who don't like its own, and names PBR Hub and PGPatcher as requirements.
- [research/pbr_trees_and_grass.md](../research/pbr_trees_and_grass.md): why TomatoRim was chosen as the ground in the first place.
