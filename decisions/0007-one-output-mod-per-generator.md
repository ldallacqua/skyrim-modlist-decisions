# 0007. Give each generator its own output mod at the end of the pane

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** Pandora, BodySlide, AutoBlend, PGPatcher, SKSE, Root and shader cache output each live in their own mod under `Outputs`, and Overwrite stays empty.

## Context

BodySlide wrote into the source mods of this list, which needed a reinstall of 5 mods to undo. Every list studied that has an output section keeps it in the end zone.

## Options considered

- **One mod per generator:** any output can be deleted and rebuilt alone.
- **A single outputs mod:** fewer entries, but outputs can't be rebuilt separately.
- **Leave files in Overwrite:** nothing tracks them, and they're easy to lose.

## Decision

One mod per generator, under `Outputs`. Disable an output before regenerating it, so the tool doesn't read its own result.

The run order is LOOT and personal patches, BodySlide, Pandora, optional Wrye Bash and Synthesis, LOOT, xLODGen, AutoBlend, PGPatcher, TexGen, DynDOLOD. No single source states this; it's combined from each tool's documentation, and placing xLODGen before PGPatcher is our own call. AutoBlend goes right before PGPatcher because PGPatcher patches AutoBlend's meshes and masters its plugin.

## Consequences

- Terrain LOD, TexGen and DynDOLOD will need their own mods if the list starts changing the world. They aren't installed today.
- Overwrite still holds leftovers in `Root` that need sorting. The `SKSE` and `ShaderCache` files went to their output mods. Tool settings that land there go into the tool's own mod.

## Confirmation

`tools/check.py` requires each output mod to exist under `Outputs`. Overwrite is checked by hand.

## Revisit when

A tool's documentation changes its required order or location.

## Evidence

- [PGPatcher](https://github.com/hakasapl/PGPatcher/wiki/Basic-Usage-%28PGPatcher%29): BodySlide, PGPatcher, TexGen, DynDOLOD.
- LOOT's masterlist (checked locally on 2026-11-03): `PG_<n>.esp` loads after `AutoBlend.esp`, and both are in the late changes group.
- [DynDOLOD](https://dyndolod.info/Help/Load-Overwrite-Orders): final order first, its plugins last, and old TexGen removed before regenerating.
- [Load order and outputs](../research/load_order_and_outputs.md): the full notes.
