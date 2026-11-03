# 0001. Pin the game at Skyrim SE 1.5.97 with Anniversary Edition content

- **Status:** accepted (recorded after the fact)
- **Date:** 2026-11-02
- **Summary:** The list runs SkyrimSE.exe 1.5.97 with SKSE 2.0.20, loads AE Creation Club content, and uses BEES to read it.

## Context

The list was already built this way when this repository started, so the original reasoning wasn't written down. The Steam install is on 1.7.104, and the list runs from a separate copy ([0002](0002-separate-stock-game-folder.md)).

## Options considered

- **Downgraded 1.5.97 with AE content:** keeps the older SKSE plugin ecosystem, but every SKSE plugin must offer a 1.5.97 build, and some tools assume newer masters.
- **Current Steam version:** matches what most authors and LOOT data target, but Steam updates can break SKSE plugins.

## Decision

Stay on 1.5.97. Every SKSE plugin is chosen for this runtime, and a plugin's version is checked against it before installing.

## Consequences

- **Plugin limits:** plan for 254 full plugins plus 4096 light ones. BEES lets 1.5.97 read 1.71 headers and the extended ESL range, which raises new records per light plugin from 2048 to 4096. It doesn't raise the plugin count.
- **LOOT data:** some warnings refer to newer masters and don't apply here. See [0011](0011-clean-plugins-with-backups.md).
- **Form 43 warnings:** treat them as a prompt to review, not an order to convert.
- **Saves:** changing runtime isn't save-safe.

## Confirmation

`tools/check.py` requires SKSE, Address Library and BEES to be enabled. The runtime version itself is checked by hand from `skse64.log`.

## Revisit when

A mod the list needs has no 1.5.97 path, or the runtime's plugin support visibly declines.

## Evidence

- [BEES](https://github.com/Nukem9/skyrimse-backported-esl-support): what it enables on 1.5.97.
- [LOOT, introduction to load orders](https://loot.github.io/docs/help/introduction-to-load-orders/): the plugin limits.
- [Research notes](../research/load_order_and_outputs.md): the full comparison.
