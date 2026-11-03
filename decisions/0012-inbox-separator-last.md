# 0012. Keep the inbox separator last

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** `Recently Added` sits below `Outputs` and must be empty at release.

## Context

The separator sat above `Outputs`. With no row selected, a new mod should land at top priority, which meant inside `Outputs`. This comes from reading MO2's `master` source and should be tested with a small mod.

## Options considered

- **Last in the pane:** new mods land inside the inbox, and many lists keep one, such as `99. ___ NEW & UNSORTED ___`.
- **Above Outputs:** keeps outputs winning conflicts, but new mods land in the wrong section.

## Decision

It moved to the end. A mod in the inbox wins every conflict until it's sorted, which is a reason to sort it quickly and keep the inbox empty at release.

## Consequences

Regenerate outputs after sorting a mod that affects them.

## Confirmation

`tools/check.py` fails if the inbox has mods or isn't the last separator.

## Revisit when

MO2 changes where new mods land.

## Evidence

- [Reference list structures](../research/reference_list_structures.md): inbox separators in real lists.
- [Separators and categories](../research/separators_and_categories.md): the source reading.
