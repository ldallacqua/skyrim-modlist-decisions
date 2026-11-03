# 0011. Clean plugins in batch, with backups, and judge warnings against our own masters

- **Status:** accepted
- **Date:** 2026-11-02
- **Summary:** [Clean Load Order](https://github.com/ldallacqua/clean-load-order-mo2) runs Quick Auto Clean on the active plugins, including official masters, and keeps the originals.

## Context

LOOT flagged many official masters and Creation Club plugins. Cleaning them one at a time was impractical, and the existing batch tools didn't take a backup first.

## Options considered

- **Clean with backups, masters included:** Step also cleans masters, though this is contested.
- **Leave masters alone:** avoids touching official files, and keeps LOOT's warnings.
- **Clean by hand:** the same result, one plugin at a time.

## Decision

Clean with backups. The first run processed 72 plugins and changed 44, removing 1,691 ITMs and undeleting 255 references, with no failures.

## Consequences

- **Deleted navmeshes remain.** Update.esm has 3, Dawnguard.esm 57, HearthFires.esm 5, Dragonborn.esm 1 and `cckrtsse001_altar.esl` 5. Quick Auto Clean doesn't fix them, and LOOT may stop warning because the CRC changed. We log them and move on for official masters, and treat them as real defects in mods.
- **One warning stays on purpose.** LOOT reports 1 ITM in `cceejsse005-cave.esm`. SSEEdit finds it against 1.7.104 masters (`REFR:020153C2`) but not against this list's 1.5.97 masters, cleaned or not. Here it's a real change, so it stays.
- **Not yet confirmed in game.** The game hasn't been launched since the cleaning.
- **Saves:** not assessed. Test with a new character first.

## Confirmation

LOOT's dirty count should only list `cceejsse005-cave.esm`. The originals are in `cleaning-backups`.

## Revisit when

The game shows a problem traceable to cleaned masters, or the game version changes.

## Evidence

- [xEdit, mod cleaning](https://tes5edit.github.io/docs/7-mod-cleaning-and-error-checking.html): Quick Auto Clean.
- [LOOT, dirty edits and CRCs](https://loot.github.io/docs/help/dirty-edits-mod-cleaning--crcs/): detection by CRC, with possible false positives.
- [Load order and outputs](../research/load_order_and_outputs.md): the debate on masters and navmeshes.
