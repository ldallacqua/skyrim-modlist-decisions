# 0012. Keep the inbox separator last

- **Status:** proposed
- **Date:** 2026-11-02
- **Summary:** Move `Recently Added` below `Outputs` and require it to be empty at release.

## Context

The separator currently sits above `Outputs`. With no row selected, a new mod should land at top priority, which today means inside `Outputs`. This comes from reading MO2's `master` source and should be tested with a small mod.

## Options considered

- **Last in the pane:** new mods land inside the inbox, and many lists keep one, such as `99. ___ NEW & UNSORTED ___`.
- **Above Outputs:** keeps outputs winning conflicts, but new mods land in the wrong section.

## Decision

Move it to the end. A mod in the inbox wins every conflict until it's sorted, which is a reason to sort it quickly and keep the inbox empty at release.

## Consequences

Regenerate outputs after sorting a mod that affects them.

## Confirmation

`tools/check.py` checks that the inbox is empty and last. It only warns while this decision is proposed, and fails once it's accepted. Adopting it also means updating the separator order in `rules/rules.json`.

## Revisit when

MO2 changes where new mods land.

## Evidence

- [Reference list structures](../research/reference_list_structures.md): inbox separators in real lists.
- [Separators and categories](../research/separators_and_categories.md): the source reading.
