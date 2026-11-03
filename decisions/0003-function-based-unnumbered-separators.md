# 0003. Use function-based separators without numbers

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** Keep the 17 separators named by function, leave them unnumbered, and fix only the two ends of the pane.

## Context

The list has 80 mods under 17 separators. The question was whether to number them, how many to use, and which categories are right.

## Options considered

- **Unnumbered:** 18 of the 24 SE lists studied do this.
- **Numbered:** 5 of 24 number nearly all separators (Nolvus, Step, Elysium, Eldergleam, Wunduniik). It helps when a guide maps chapters to the pane, or when separators are dropped into `mods/` as a pack, but numbers drift: Wunduniik's parents run 01, 02, 03, 06, 07, 05, 04, 08 and include duplicates.
- **Parents only:** Licentia numbers only its parent separators.

## Decision

Don't number. MO2 takes priority from the line's position in `modlist.txt`, so a number changes nothing functionally, and a `modlist.txt` backup recovers more than a number can.

Lists agree on the two ends and disagree in the middle, so we fix the ends and let conflicts decide the middle:

| Zone | Separators |
|---|---|
| Top | DLC & CC, SKSE & Frameworks, Fixes |
| Upper | UI & Camera |
| Middle | Shaders, Skeleton & Physics, Body, Head & Face, Skin, Presets, Hair, Animation, Armor, Gameplay |
| End | Tools, Patches (when needed), Outputs |
| After outputs | Recently Added ([0012](0012-inbox-separator-last.md)) |

When the list grows, add Textures and Models, Locations, and Lighting and Weather between Armor and Gameplay. If it gains visual mods, order them nature, then structures, then small objects, with lights late. At least 12 of 24 lists do this, though it's a habit and not a rule. MO2 categories stay a cross-cutting filter, because grouping by category replaces the separator tree.

## Consequences

- No reorder is needed today.
- Rename separators only through MO2's interface, because renaming the folder elsewhere moves it to top priority. Compare `modlist.txt` before and after.
- Evidence limit: no source measures whether structure affects stability, and several lists share templates, so "most lists" partly reflects shared lineage.

## Confirmation

`tools/check.py` compares the separators and their order with `rules/rules.json`.

## Revisit when

A section passes about 25 mods (the median across lists is near 22), or a guide or external reference needs stable section numbers.

## Evidence

- [Reference list structures](../research/reference_list_structures.md): real `modlist.txt` files from 25 lists.
- [Separators and categories](../research/separators_and_categories.md): MO2 source code and arguments.
- [MO2 profile.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/profile.cpp): priority comes from line position (read on `master`, not the 2.5.2 tag).
