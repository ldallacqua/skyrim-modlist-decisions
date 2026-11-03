# 0006. Render with Community Shaders

- **Status:** accepted (recorded after the fact)
- **Date:** 2026-11-02
- **Summary:** Community Shaders 1.9.1 with its feature mods is the renderer, with no ENB.

## Context

The list uses Community Shaders with SSGI, Skylighting, Terrain Blending, Terrain Variation, Wetness Effects, Hair Specular and an upscaling add-on, plus a local DLSS 5, ReShade and RenoDX setup. The original comparison with ENB wasn't written down.

## Options considered

- **Community Shaders:** the current choice.
- **ENB:** not compared in depth here.

## Decision

Keep Community Shaders. New visual mods must work with it, and ENB presets aren't considered.

## Consequences

- Shader caches land in `ShaderCache - Outputs` and Overwrite. Keep them out of this repository.
- PGPatcher output depends on meshes and textures, so changing those means regenerating it.

## Confirmation

`tools/check.py` requires Community Shaders to be enabled.

## Revisit when

A wanted effect is only available on ENB, or Community Shaders stops supporting 1.5.97.

## Evidence

The mod list itself: [list/mods.csv](../list/mods.csv).
