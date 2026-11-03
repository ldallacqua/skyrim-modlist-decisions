# 0004. Build characters on CBBE 3BA, BodySlide and OBody NG

- **Status:** accepted (recorded after the fact)
- **Date:** 2026-11-02
- **Summary:** The body is CBBE 3BA with XPMSE, CBPC and Faster HDT-SMP for physics, built with BodySlide and distributed with OBody NG.

## Context

The list was already built this way, so the original comparison wasn't written down. High Poly Head and BnP skin complete the look.

## Options considered

No alternatives were formally compared at the time. Add them here if this is ever reopened.

## Decision

Keep this pipeline. Armor and outfits must have CBBE 3BA conversions.

## Consequences

- Changing the body, a preset or an outfit means rebuilding BodySlide into `Bodyslide - Outputs`.
- Build with Zeroed Sliders and Build Morphs on, which is how the current output was produced.
- A body change on an existing save mainly means regenerating outputs, though this hasn't been tested on a long-running save.

## Confirmation

`tools/check.py` requires CBBE 3BA, BodySlide and OBody NG to be enabled.

## Revisit when

A new body standard offers something this one can't, or conversions for wanted armor stop appearing.

## Evidence

The mod list itself: [list/mods.csv](../list/mods.csv).
