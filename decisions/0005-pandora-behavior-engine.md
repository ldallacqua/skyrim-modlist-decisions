# 0005. Generate behaviors with Pandora, and treat version 5 as its own decision

- **Status:** accepted (recorded after the fact)
- **Date:** 2026-11-02
- **Summary:** Pandora Behaviour Engine+ 4.4.0-beta generates behaviors; updating to 5.0.0-beta requires a test first.

## Context

The list uses Pandora with Open Animation Replacer and OStim. It also loads `fnis_aa.dll` through Dyn FNIS AA functions. The original comparison with Nemesis wasn't written down.

## Options considered

- **Stay on Pandora 4.4.0-beta:** works today.
- **Update to Pandora 5.0.0-beta:** it reworks FNIS handling, which this list touches.
- **Nemesis or FNIS:** not compared in depth.

## Decision

Stay on 4.4.0-beta until 5 is tested on a cloned profile.

## Consequences

Any change to animations, behaviors or the skeleton means rerunning Pandora. Don't update Pandora in the middle of a save without a backup.

## Confirmation

`tools/check.py` requires Pandora to be enabled and `Pandora - Outputs` to exist.

## Revisit when

Pandora 5 leaves beta, or a needed animation mod requires it.

## Evidence

- [Pandora](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus): usage and arguments.
- [MO2 plugins and tools](../research/mo2_plugins_and_tools.md): version status as of 2026-11-02.
