# 0008. Set each generator's output in the tool, not only in MO2

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** Configure the output location the way each tool documents, because MO2's "create files in mod" only catches new files.

## Context

MO2's redirect catches new files, while existing files are changed where they are. That's how BodySlide ended up writing into source mods here. The profile redirected Pandora and BodySlide through `custom_overwrites`, and neither executable had arguments. BodySlide's own Output Path was already set to `Bodyslide - Outputs`, so its redirect was redundant, and Pandora relied on the redirect alone.

## Options considered

- **Per-tool configuration:** matches each tool's documentation and survives existing files.
- **MO2 redirect only:** simple, and Step uses it with Nemesis, but it depends on the tool only creating new files.

## Decision

Follow each tool's documentation. Pandora runs with `-o "<absolute path to Pandora - Outputs>" --tesv:"<game root>"`. The game root matters here: without it, Pandora finds the game through the Windows registry, which points to the Steam install rather than the separate folder ([0002](0002-separate-stock-game-folder.md)). BodySlide keeps its own Output Path. Both `custom_overwrites` entries were removed.

## Consequences

- Pandora needs a rerun to confirm the new arguments. It's save-safe as long as the animations don't change.
- Pandora hadn't changed any source mod: none of the files in `Pandora - Outputs` exist in another mod.

## Confirmation

By hand: run Pandora and confirm that only `Pandora - Outputs` changed.

## Revisit when

MO2 changes how the redirect handles existing files.

## Evidence

- [Pandora README](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus): `-o` and `--tesv`.
- [PGPatcher](https://github.com/hakasapl/PGPatcher/wiki/Basic-Usage-%28PGPatcher%29): set the output in BodySlide's preferences, not MO2.
- [Step 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3): uses the MO2 option with Nemesis, so the rule is per tool.
