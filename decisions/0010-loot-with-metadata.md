# 0010. Sort with LOOT and record every exception as metadata

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** LOOT sets the base order, and any exception is a `Load After` rule or a group, never a manual drag.

## Context

The next sort recalculates the order, so manual changes silently disappear.

## Options considered

- **LOOT only:** Step trusts it and says its patches target the default order.
- **LOOT plus user rules:** Lexy's and Nolvus do this.
- **Fully manual:** complete control, but it doesn't survive a new mod.

## Decision

LOOT plus recorded rules. Use `Load After` for specific pairs and groups for one plugin against many. The routine is: sort, generate, enable the output, sort again, and read the end of the list. LOOT itself admits it sometimes errs, so check suspect results in xEdit.

## Consequences

- `userlist.yaml` joins the backup and should join the snapshot once rules exist.
- A rule needs a reason, recorded in the rule's note.

## Confirmation

By hand: sorting twice changes nothing.

## Revisit when

The rules outgrow what LOOT metadata can express.

## Evidence

- [LOOT FAQ](https://loot.github.io/docs/help/loot-faqs/): its limits.
- [Nolvus rules](https://www.nolvus.net/appendix/rules): a real example of user rules.
- [Step 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3): LOOT only.
