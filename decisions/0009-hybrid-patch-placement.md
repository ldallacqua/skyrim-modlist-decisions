# 0009. Place patches by what they connect

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** A patch for one mod goes right below it, and a patch linking several sections goes in a late `Patches` section.

## Context

The list has few patches today, so this is the moment to set the rule cheaply.

## Options considered

- **Hybrid:** most lists studied. At the median, 82% of patch-named mods sit within six positions of a related mod, and 36% fall in the last quarter of the pane, against 25% for a uniform spread. This is a name-matching heuristic, not a conflict analysis.
- **One final section:** Wunduniik, Keizaal and Halls of Sovngarde do this. It's easy to audit, but it separates a patch from what it patches.
- **Only beside the parent:** fails for a patch that must overwrite two distant mods.

## Decision

Use the hybrid. A patch with no assets has no left-pane conflict, so its position only serves readers. A `Patch` category makes patches auditable by filter. Create the `Patches` section between Tools and Outputs when the first multi-target patch appears.

A conflict alone isn't a defect. Act when the winner drops something wanted, by copying the winning record as an override into a small patch loaded after its sources.

## Consequences

No change today.

## Confirmation

By hand, when a patch is added.

## Revisit when

Patches become hard to find, which would favor a single section.

## Evidence

- [Reference list structures](../research/reference_list_structures.md): the measurements and their method.
- [xEdit, conflict detection](https://tes5edit.github.io/docs/5-conflict-detection-and-resolution.html): many conflicts are harmless.
