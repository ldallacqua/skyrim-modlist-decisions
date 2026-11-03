# 0008. Set each generator's output in the tool, not only in MO2

- **Status:** proposed
- **Date:** 2026-11-02
- **Summary:** Configure the output location the way each tool documents, because MO2's "create files in mod" only catches new files.

## Context

MO2's redirect catches new files, while existing files are changed where they are. That's how BodySlide ended up writing into source mods here. The profile still redirects Pandora and BodySlide through `custom_overwrites`, and neither executable has arguments. BodySlide's own Output Path was since set to `Bodyslide - Outputs`, so its redirect is now redundant. Pandora relies on the redirect alone.

## Options considered

- **Per-tool configuration:** matches each tool's documentation and survives existing files.
- **MO2 redirect only:** simple, and Step uses it with Nemesis, but it depends on the tool only creating new files.

## Decision

Follow each tool's documentation. Give Pandora `-o "<absolute path to Pandora - Outputs>"`, plus `--tesv` as its README asks for Stock Game setups so it finds FNIS mods. Keep BodySlide's Output Path. Then remove both `custom_overwrites` entries and regenerate.

## Consequences

- Pandora needs a rerun. It's save-safe as long as the animations don't change.
- It hasn't been verified whether Pandora has already changed any source mod. Check the Conflicts tab and reinstall anything suspect.

## Confirmation

By hand: run Pandora and confirm that only `Pandora - Outputs` changed.

## Revisit when

MO2 changes how the redirect handles existing files.

## Evidence

- [Pandora README](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus): `-o` and `--tesv`.
- [PGPatcher](https://github.com/hakasapl/PGPatcher/wiki/Basic-Usage-%28PGPatcher%29): set the output in BodySlide's preferences, not MO2.
- [Step 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3): uses the MO2 option with Nemesis, so the rule is per tool.
