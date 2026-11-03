# 0014. Extend grass with Grass Optimizations and NGIO, without a cache

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** NGIO draws grass out to 40000 units, Community Shaders' Grass Optimizations keeps that cheap, and there is no grass cache.

## Context

Grass Optimizations replaces vanilla grass rendering in Community Shaders, which cuts the CPU cost of grass. Its author recommends pairing it with NGIO's extended grass distance. The Dragonborn's Fate extended grass guide adds Grass Cache Helper NG, a generated grass cache and an optional BSA of that cache.

Two things were missing here. Grass Optimizations 1.0.0 was installed, but the Community Shaders core was 1.8.4, and the feature only exists from 1.9.0, so it did nothing. NGIO 2.0.3 was installed with no configuration, because it only writes `GrassControl.ini` the first time the game runs.

## Options considered

- **Simplest setup, no cache:** the author's recommendation. It changes four NGIO settings.
- **The full guide, with a cache:** the author says a cache has no effect on visuals and is optional. It helps load times, but it has to be regenerated after any change to landscape, grass or object placement.
- **New grass LODs from DynDOLOD:** better performance at long distances, but DynDOLOD isn't part of this list.

## Decision

Use the simplest setup. Community Shaders was updated to 1.9.1, and `SKSE/Plugins/GrassControl.ini` was created inside the NGIO mod with:

| Setting | Value |
|---|---|
| `Extend-grass-distance` | `true` |
| `Overwrite-grass-distance` | `40000` |
| `Overwrite-grass-fade-range` | `0` |
| `DynDOLOD-Grass-Mode` | `0` |

The setting names and the `[GrassConfig]` section come from NGIO's source. NGIO fills in every other setting with its default.

## Consequences

- Load times may grow, because grass is generated outside loaded cells without a cache. The cache from the guide is the fix if that becomes a problem.
- Reinstalling NGIO with "Replace" would delete `GrassControl.ini`. Use "Merge" or recreate it.
- Grass Optimizations' own settings live in the Community Shaders menu in game. Its author suggests adjusting distance there.
- Not yet seen in game.

## Confirmation

By hand: in game, Grass Optimizations shows as loaded in the Community Shaders menu, and NGIO's log has no configuration errors.

## Revisit when

Load times become a problem, the list adds DynDOLOD or a grass mod with LODs, or a landscape mod arrives that would make a cache worth regenerating.

## Evidence

- [Grass Optimizations](https://www.nexusmods.com/skyrimspecialedition/mods/188628): the recommended settings, read through Nexus Mods' public API.
- [Community Shaders 1.9.0 release](https://github.com/community-shaders/skyrim-community-shaders/releases/tag/v1.9.0): where grass optimizations was added.
- [NGIO's settings](https://github.com/DwemerEngineer/No-Grass-In-Objects-NG/blob/main/include/GrassControl/Config.h): names, section and defaults.
- [Dragonborn's Fate, extended grass](https://dragonbornsfate.moddinglinked.com/extendedgrass.html): the full guide, with the cache steps skipped here.
