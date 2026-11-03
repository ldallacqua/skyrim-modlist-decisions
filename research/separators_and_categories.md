# Separators, naming and categories in Mod Organizer 2 (Skyrim SE, MO2 2.5.x)

Evidence labels used in these notes:
- **[Source]**: read from the MO2 C++ source on the `master` branch (fetched 2026-11-02) through a fetch tool that summarises and quotes. It is not pinned to the 2.5.2 tag, and nothing was tested at runtime. Treat behaviour as "how the current code reads".
- **[Local]**: read directly from the user's install at `C:\Modding\MO2` (`version=2.5.2`).
- **[Issue]**: GitHub issue or PR. The title and state are facts, but a reporter's diagnosis is not.
- **[Guide]**: Step wiki. An editorial recommendation from an established project.
- **[Opinion]**: forum, Reddit or mod page text. Community opinion.
- **[Snippet]**: seen only as search result text. The Nexus pages returned HTTP 403 on direct fetch, so the full page was not read.

## Should separators be numbered?

### Takeaway
No, not for this list. Order comes from `modlist.txt`, not from names, so numbers add nothing to correctness while MO2 is managing the list. Numbers pay off mainly for distributable separator packs and guides, and they restore only the order of the headers, never which mods sit under them. If the user wants them anyway for reference or scripting, use equal-width numbers with gaps (05, 10, 15...).

### Cited Findings
- **Order comes from position in the file.** [Source] Priority comes from line position in `modlist.txt`, with the top of the file as highest priority — [profile.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/profile.cpp). [Local] The user's file confirms this: `Outputs_separator` is near the top of the file and `DLC & CC_separator` is the last line — `C:\Modding\MO2\profiles\Default\modlist.txt`.
- **Name sort changes the view only, and has real costs.** [Source] Sorting by the name column compares names case-insensitively, including separator names. Drag and drop is refused unless sorted by priority ("Drag&Drop is only supported when sorting by priority") — [modlistsortproxy.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistsortproxy.cpp).
- **Collapsing needs priority sort.** [Source] Collapsible separators apply only when the sort column is priority, the setting is on for that sort direction, and no Category or Nexus ID grouping is selected — [modlistview.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistview.cpp). [Issue] The request for collapsing under name sort is still open — [#1546](https://github.com/ModOrganizer2/modorganizer/issues/1546).
- **New folders are where numbers really act.** [Source] Mods not listed in `modlist.txt` get priorities above all listed mods, in `ModInfo` index order — [profile.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/profile.cpp). That collection is kept sorted by name (`ModInfo::ByName`) — [modinforegular.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinforegular.cpp).
- **Community arguments for numbers.** [Snippet/Opinion] Separator pack authors say numbering keeps separators in order "even when MO2's mod and install order gets out of whack", and that numbered separators arrive at the bottom of the list. One says the J3w3ls scheme lets you reorder without renumbering everything — Nexus pages [90857](https://www.nexusmods.com/skyrimspecialedition/mods/90857) and [96582](https://www.nexusmods.com/skyrimspecialedition/mods/96582). I could not confirm which snippet belongs to which page, or the exact scheme, because both returned 403.
- **Step numbers its groups but does not clearly number its separators.** [Guide] Step's ModGroups are numbered (02-Extenders to 21-Post-Processing). Its instruction is to name separators after Mod Groups, with the examples "Extensions, Resources, Lighting and Weather", which carry no numbers — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3). Step's numbers also stay stable with gaps: groups 04, 05, 06, 12, 17, 18 and 21 are listed as empty in an add-on guide — [The Road Ahead](https://stepmodifications.org/wiki/SkyrimSE:TRA-1.0).
- **Separators ignore Nexus metadata.** [Source] A separator's `nexusId()` returns -1 and its Nexus category, update and INI tweak functions are stubbed — [modinfoseparator.h](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinfoseparator.h).
- **Grouping replaces separators.** [Source] Category and Nexus ID group-by replace the by-priority proxy, so the separator tree is not used in those views — [modlistview.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistview.cpp). [Issue] Introduced in [PR #1338](https://github.com/ModOrganizer2/modorganizer/pull/1338).
- **Text filters see the number.** [Source] A text filter matches separator names like any other mod name — [modlistsortproxy.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistsortproxy.cpp).
- **Renaming to number has a stated risk.** [Source] The separator header carries the comment "TODO: Fix renaming method to avoid priority reset" — [modinfoseparator.h](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinfoseparator.h). Against that, renames through the UI emit `modRenamed` — [modlist.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlist.cpp) — and `profile.cpp` has `renameModInList` / `renameModInAllProfiles`, which rewrite the name in each profile's file — [profile.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/profile.cpp).
- **Renaming outside MO2 is unsafe.** [Source] An old name that no longer resolves is dropped from `modlist.txt`, and the renamed folder is treated as unlisted and goes to highest priority — [profile.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/profile.cpp).

### Inferences

| Scenario | Unnumbered | Numbered |
|---|---|---|
| Normal use, sorted by priority | Correct | Correct, with no added function |
| Moving a section | Move it, done | Move it, then the number is wrong unless renamed |
| Inserting a section | Create it, done | Needs a free number, or renumbering without gaps |
| Name sort view | Headers interleaved with mods | Headers cluster together, but there is no collapse or drag in this view either way |
| Dropping many new separator folders into `mods\` | Arrive in name order, wrong | Arrive in the intended order at the bottom. The real benefit, and it matters to pack authors |
| `modlist.txt` lost or rebuilt | All order lost | Header order recoverable, but membership of mods is still lost |
| Explorer view of `mods\` | Separators scattered by name | Separators still mixed with mods unless the prefix sorts first; minor benefit |
| Text filter | Clean | Number can match searches such as "10"; minor cost |
| Citing a section in notes or scripts | By name | Short, stable ID; a modest benefit |

- Use zero-padded numbers if numbering at all: the comparison reads as plain string comparison, so "10" would sort before "2" (inference from the name comparison; no natural sort code was seen).
- The recovery argument is weak because the valuable data is mod membership. Backing up `modlist.txt` is better protection than numbering.
- Numbering has no interaction with Nexus categories or Group by. Those views ignore the separator tree regardless of name.

### Gaps
- Whether renaming a separator through the UI in 2.5.2 actually resets priority was not tested. The TODO and the rename handler point in different directions. Back up `modlist.txt` and compare it after a rename.
- The exact J3w3ls scheme could not be read (403).

## How do MO2 separators work technically, and what are the limits?

### Takeaway
A separator is an empty mod folder named `<name>_separator` with a `meta.ini`, listed as a disabled entry in `modlist.txt`. It has no game effect. The collapsing tree is a view built from priority order, with one level only and several open bugs. One of them directly concerns a separator placed above Creation Club entries in 2.5.2.

### Cited Findings
**Structure**
- [Source] Creation appends `_separator` to the name, filters it through `fixDirectoryName`, refuses duplicates, and inserts at the selected row when sorted by priority — [modlistviewactions.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistviewactions.cpp).
- [Source] The display name removes every occurrence of `_separator` via `name.replace("_separator", "")`, and internal names are compared case-insensitively for collisions — [modlist.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlist.cpp).
- [Source] `ModInfoSeparator` subclasses `ModInfoRegular`. `canBeEnabled()` is false, updates are disabled and `nexusId()` is -1 — [modinfoseparator.h](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinfoseparator.h). It adds `FLAG_SEPARATOR` — [modinfoseparator.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinfoseparator.cpp).
- [Local] A real `meta.ini` holds `color=@Variant(...)`, `modid=0`, empty version fields, `category=0` and `installedFiles` size 0 — `C:\Modding\MO2\mods\Fixes_separator\meta.ini`. In `modlist.txt` separators appear with a `-` prefix.

**Color**
- [Source] `color` is a `meta.ini` key — [modinforegular.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinforegular.cpp). The dialog supports alpha and applies to all selected rows. The last color is remembered and auto-applied to new separators — [modlistviewactions.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistviewactions.cpp). [Local] `previousSeparatorColor` is in `ModOrganizer.ini`.
- [Source] Scrollbar marks depend on the `colorSeparatorScrollbar` setting — [modlist.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlist.cpp). [Local] It is on (`colorSeparatorScrollbars=true`).
- [Guide] Step's add-on guide recommends scrollbar colors and profile-specific collapse states — [The Road Ahead](https://stepmodifications.org/wiki/SkyrimSE:TRA-1.0).

**Collapsing**
- [Source] `buildTree()` walks mods in priority order. A separator becomes a top-level node and later mods become its children until the next separator. Mods before the first separator stay at top level. Backups and Overwrite are always root children, never inside a separator. In descending sort the walk runs in reverse — [modlistbypriorityproxy.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistbypriorityproxy.cpp).
- [Source] Collapsed state is stored by display name, optionally per profile (`collapsed_separators`). A collapsed separator can merge child conflict, flag and content icons and blend marker colors. Double-click and Shift+Enter toggle, and Alt+click selects children. Installing a mod expands its parent separator — [modlistview.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistview.cpp). [Issue] The icon merge came from [PR #1338](https://github.com/ModOrganizer2/modorganizer/pull/1338) and [PR #1350](https://github.com/ModOrganizer2/modorganizer/pull/1350).
- [Local] The user has `collapsible_separators_asc=true`, `collapsible_separators_dsc=true`, `collapsible_separators_per_profile=false` and all icon merge options on.

**Filters**
- [Source] Separator filter modes are Filter (tested like any mod), Show (forced visible) and Hide (forced hidden). The check runs only when a filter is active — [modlistsortproxy.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistsortproxy.cpp).
- [Source] With collapsible separators active, the separators combo is forced to Filter and disabled — [modlistview.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistview.cpp).
- [Source] A parent row is accepted if the separator itself matches, otherwise if any child matches. Text filtering covers name, author, uploader, notes and comments, categories and Nexus ID depending on columns, with `|`, `||` and `OR` as OR operators and spaces as AND — [modlistsortproxy.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistsortproxy.cpp).

**Known limits and bugs** [Issue]
- [#2420](https://github.com/ModOrganizer2/modorganizer/issues/2420), open, opened 2026-07-04: in 2.5.2 a separator at the very top, above Creation Club mods, reportedly loses its anchor and collapse state after F5. The reporter suspects the new CC parsing. A community member could not reproduce it, and no maintainer has responded.
- No nesting: [#1960](https://github.com/ModOrganizer2/modorganizer/issues/1960) closed as duplicate, [#2291](https://github.com/ModOrganizer2/modorganizer/issues/2291) open as a feature request.
- [#1615](https://github.com/ModOrganizer2/modorganizer/issues/1615), open: closing MO with a filter active affects collapse state on reopening.
- [#1817](https://github.com/ModOrganizer2/modorganizer/issues/1817), open: a report of a system freeze when dragging over separators in 2.4.4.
- [#639](https://github.com/ModOrganizer2/modorganizer/issues/639), open: no separator navigation list, and separators are not in the filter panel.
- [#1493](https://github.com/ModOrganizer2/modorganizer/issues/1493), closed as completed in 2021: moving a collapsed separator left its mods behind.
- [#2152](https://github.com/ModOrganizer2/modorganizer/issues/2152), closed as completed: separators could not be created once the list filled the window.

**Official documentation**
- The official site has no separator or category documentation. Its only documentation link is a Mod Organizer 1.3.11 wiki article that it warns may differ from MO2 — [modorganizer.org](https://www.modorganizer.org/). `modorganizer2.github.io` now redirects there.
- Older information: the Step advanced page still describes making separators by hand with folders, citing an unresolved enhancement request. This is MO1-era and obsolete — [Guide:Mod Organizer/Advanced](https://stepmodifications.org/wiki/Guide:Mod_Organizer/Advanced).

### Inferences
- Because membership is computed from neighbours, there is no stored "this mod belongs to this separator". Moving a mod across a header changes its group, and nothing else records it.
- Descending sort appears to attach a mod to a different separator than ascending does, since the tree is built in the opposite direction. A mod between S1 and S2 falls under S1 in ascending and under S2 in descending. The user should stick to one direction, preferably ascending. This reading comes from the code summary and was not tested.
- Avoid the literal text `_separator` inside a separator name, as it is stripped everywhere in display.
- Renaming a separator probably forgets its collapsed state, since state is keyed by display name. This is harmless.
- `save_filters=false` [Local] should reduce exposure to #1615.

### Gaps
- Whether moving a collapsed separator carries its children in 2.5.2 was not visible in the code read; the proof would be in `ModListDropInfo`. #1493 is closed as completed. Test once before relying on it.
- No hard limit on separator count was found in the code read, and no source states one.
- The exact character set allowed by `fixDirectoryName` was not read.

## How granular should separators be?

### Takeaway
No authoritative number exists. Available examples suggest roughly 15 to 25 top-level sections for a list up to a few hundred mods. For a list this size, a separator is justified when it marks a real priority boundary or is expected to grow, not by a target count.

### Cited Findings
- [Snippet/Opinion] One Nexus pack ships tiers: Lite with 19 separators for up to 250 mods, Intermediate with 77 for 250 to 1000, and Full with 126 for 1000+. Another author uses 19 general sections divided into smaller subsections rather than 69 sections — [Nexus 90857](https://www.nexusmods.com/skyrimspecialedition/mods/90857), [Nexus 96582](https://www.nexusmods.com/skyrimspecialedition/mods/96582) (attribution between the two pages unconfirmed).
- [Guide] Step SkyrimSE 2.3 uses 20 ModGroups. Visible counts include Extenders 10, Resources 3, Foundation 24, Animation and Physics 7 — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3). The page was read only in part, so later group counts are missing.
- [Guide] Step splits Gameplay into six parts: General, AI and Combat, Economy, Immersion, Quests, Skills and Perks — [The Road Ahead](https://stepmodifications.org/wiki/SkyrimSE:TRA-1.0).
- [Local] The user has 17 separators, 77 managed mods and 78 foreign DLC/CC entries in `modlist.txt`.

### Inferences
- Rule of thumb (my synthesis, not a cited standard): split a section past about 20 to 25 mods if it has a natural split. Keep small sections if they mark a real override boundary. Merge only sections that are both small and have no ordering meaning.
- Small sections cost little when collapsed, so the penalty for a section of 1 or 2 is low.
- With no nesting, a flat list is the only option. Subsections would need separate separators with a shared prefix, such as "Gameplay - Combat".

### Gaps
- I found no measured or survey data on section counts or mods per section. Everything here is example-based.

## Should top-level order follow function, install dependency, or conflict priority? How do left and right pane order differ?

### Takeaway
Conflict priority governs the order; function supplies the labels. In practice this means function-named groups arranged so that whatever should win sits lower. Left and right panes are independent systems, so let LOOT handle the right pane and do not try to mirror it in the left.

### Cited Findings
- [Guide] Step's order runs Extenders, Resources, Foundation, then assets, Fixes, Gameplay, Interface, Locations, Lighting, Utilities, Patches, Post-Processing. Mods "should be arranged in MO in the order that they are listed" so later overrides earlier. Foundation holds baseline mods that others should override — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3), [The Road Ahead](https://stepmodifications.org/wiki/SkyrimSE:TRA-1.0).
- [Guide] Step keeps mods alphabetical within a group, with deviations "purposeful" — [The Road Ahead](https://stepmodifications.org/wiki/SkyrimSE:TRA-1.0).
- [Guide] LOOT sets plugin order before launch, and manual rules cover exceptions — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3).
- [Opinion] Left pane manages loose file priority; right pane manages load order, which handles records and archived resources — [Steam thread](https://steamcommunity.com/app/489830/discussions/0/4354499488253058461). The same point appears in an r/skyrimmods thread: loose files override BSA contents, and plugin order controls conflicts among BSAs — [Reddit snapshot, Dec 2025](https://reddit.sentinel-team.org/posts/1ptudvt/snapshots/2025-12-24T00%3A20%3A21.850421Z).
- [Guide, undated and older] A BSA loads with its same-named plugin and wins if that plugin loads later, and loose files override BSAs — [Step forum](https://stepmodifications.org/forum/topic/5033-ramifications-of-bsa-extraction-in-mod-organizer/page/2/).
- **Conflict:** a 2017 Step forum moderator reply suggests left pane order decides this in MO — [Step forum](https://stepmodifications.org/forum/topic/5033-ramifications-of-bsa-extraction-in-mod-organizer/page/7/). This could not be pinned to an exact page, and it appears to be MO-era behaviour. Marked as older and unresolved.
- [Opinion] One poster sorts the right pane with LOOT and then matches the left by hand. Another notes that mods with several ESPs make an exact match impossible — [Steam thread](https://steamcommunity.com/app/489830/discussions/0/4354499488253058461).
- [Opinion] A Steam user warns that separators "break" load order. This has no support in the code read: separators carry no plugins, and they live only in the left pane — [Steam thread](https://steamcommunity.com/app/489830/discussions/0/4354499488253058461), [modinfoseparator.h](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinfoseparator.h).

### Inferences
- Install dependency matters less than people assume. Masters are a right pane issue, and BodySlide or Pandora outputs depend on their inputs through generation, not through left pane position.
- Dependency still shapes the outer frame: frameworks low, generated outputs last.
- Function order and priority order conflict only when a section is both functional and asset-bearing. Priority wins in that case. "Fixes" that touch assets are the typical example.

### Gaps
- No primary Bethesda or MO2 document on BSA order was found. Use the Conflicts tab and in-game testing for specific cases.

## Where should patches go?

### Takeaway
Use a hybrid. Put a patch with one parent directly below its parent. Put a patch that bridges mods from different sections in a dedicated Patches section after all content. Keep generated output last. No source settles this as a standard.

### Cited Findings
- [Guide] Step uses a dedicated 20-Patches group near the end, described as "Mods that programmatically resolve load-order conflicts" — [The Road Ahead](https://stepmodifications.org/wiki/SkyrimSE:TRA-1.0). It has required and optional modular conflict resolution patches, with "combo" patches where "Only ONE" should be used — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3).
- [Opinion] Install the patch as its own mod ("modname patch") below the main mod in the left pane, with any plugin below the main mod in the right pane — [Reddit snapshot, Dec 2025](https://reddit.sentinel-team.org/posts/1ptudvt/snapshots/2025-12-24T00%3A20%3A21.850421Z).
- [Snippet] The MO2 Modlist Manager plugin places patches after their targets, with a Patches tier for patches covering two or more mods — [Nexus 193186](https://www.nexusmods.com/skyrimspecialedition/mods/193186). The direct fetch returned 403, and a second search did not find it, so treat this as weakly verified. This is the closest published example of the hybrid.
- [Snippet] Wabbajack list convention keeps [NoDelete] user-added mods in a block at the bottom — same [Nexus 193186](https://www.nexusmods.com/skyrimspecialedition/mods/193186) snippet; see also the [Wabbajack NoDelete indexer](https://www.nexusmods.com/site/mods/669) and [MO2KeywordTagger](https://github.com/ApocryphaRealm/MO2KeywordTagger).
- [Guide] Merge-type outputs in guide lists sit late in the order: "LOTD Patches Merge" near the end — [Lexy's thread](https://stepmodifications.org/forum/topic/13092-lexys-legacy-of-the-dragonborn-special-edition/page/734). Step also places generated "xEdit Output" and "SKSE Output" at high priorities — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3).
- [Opinion] PGPatcher output should override everything else, and one user saw texture problems when it was placed low — [Steam thread](https://steamcommunity.com/app/489830/discussions/0/4354499488253058461).
- [Source] Overwrite is always highest and outside any separator — [profile.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/profile.cpp).

### Inferences
- Beside the parent: the patch moves with its parent, is visible when disabling the parent, and is easy to keep in sync. The risk is that a patch for mods A and B must outrank both, which is only guaranteed if it sits below the later one.
- Dedicated section: multi-target priority is guaranteed and it is a clear audit list. The cost is that the patch is far from its parent, so use the Notes column or the name to link them.
- Plugin-only patches have no left pane conflict at all, so their placement is purely for humans. LOOT handles the right pane.
- Suggested order at the tail: content, Tools, Patches, merged patches and compatibility packs, generated Outputs, Overwrite. A compatibility pack covering many mods belongs in Patches. Treat a Synthesis, Bashed or smashed patch or similar as generated output.

### Gaps
- Lexy's guide page itself was not read; only forum threads and snippets were reached. r/skyrimmods is blocked directly, so opinion was sampled through one snapshot and is thin.

## Naming conventions for mods in the left pane

### Takeaway
Keep the Nexus name by default and rename only to disambiguate or to mark a role, using a parent-first pattern. Renaming inside MO2 does not break update checks because they use `modid`. Avoid versions in names, since MO2 has a Version column.

### Cited Findings
- [Source] Update checks depend on `m_NexusID`, not the folder name. `m_Name` is used only in logs and in the rename logic. `meta.ini` lives in the folder and moves with it — [modinforegular.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinforegular.cpp).
- [Source] `installDownload` finds existing mods by Nexus ID and reuses the name, with the last match winning — [organizercore.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/organizercore.cpp).
- [Source] `setName` rejects `/` and `\`. `renameMod` runs `fixDirectoryName`, rejects empty and duplicate names case-insensitively, then emits `modRenamed` — [modinforegular.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinforegular.cpp), [modlist.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlist.cpp).
- [Source] `version` and `newestVersion` are `meta.ini` fields compared for the update flag — [modinforegular.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinforegular.cpp).
- [Guide] Step names helper mods descriptively ("xEdit Output", "SKSE64 Output") and uses prefixes such as "(CONFIG) SSE Display Tweaks" and "(TEMP) Cathedral Landscapes - xLODGen" — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3).
- [Opinion] Tools exist for tags in names: `[NoDelete]` for Wabbajack, `[Patch]` and similar — [MO2KeywordTagger](https://github.com/ApocryphaRealm/MO2KeywordTagger).
- [Local] The user's names mostly follow Nexus. Outputs use the pattern `<Tool> - Outputs`. `[Dint999] BDOR Hairs SSE 0.24` and `[Dint999] HairPack02 SSE 1.12 (base)` embed a version.

### Inferences
- If a renamed entry has several siblings with the same Nexus ID, the install dialog may propose the wrong one because the last match wins. Read the proposed name before choosing Replace.
- A version in the name goes stale after updating and duplicates the Version column. The exception is when the version is part of the identity, as in "RaceMenu 0.4.16 Memory Leak Hotfix (SE)", which targets a specific build. Leave that one alone.
- For the Dint999 entries, consider dropping the version and using the Version field, especially if there is no valid `modid`.
- Tags in names work as a cheap filter, since text filtering matches names. They cost readability and are unneeded on a list of 77 mods.
- Prefer a suffix to a prefix for variants ("RaceMenu - <variant>"). It keeps the parent as the search key and groups correctly under name sort.

### Gaps
- No official MO2 naming guideline exists. The official site has no such documentation.

## Is MO2's category system worth using alongside separators? Notes, flags and colors

### Takeaway
Treat categories as a low-effort, cross-cutting filter, not as a second hierarchy. Use the 2.5 Nexus mapping if it is free, and do not hand-maintain a 1:1 copy of the separators. Notes are the most useful of these, particularly for recording why a mod sits where it does and which FOMOD options were picked.

### Cited Findings
- [Source] 2.5.0 removed hard-coded defaults. New and upgraded instances prompt to import and map Nexus categories. The editor can map, import, replace or merge. Auto-reassign is on the right-click and dropdown menus, and mods with no valid mapping stay untouched. Installing can prompt for missing mappings, which can be disabled — [v2.5.0 release notes](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.0).
- [Source] `category` in `meta.ini` is comma-separated IDs, with the first valid one primary — [modinforegular.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinforegular.cpp). Foreign mods show "Non-MO" in the category column — [modlist.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlist.cpp).
- [Source] Choosing Group by Category or Nexus ID replaces the separator tree — [modlistview.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistview.cpp). Category criteria in filters work without grouping — [modlistsortproxy.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistsortproxy.cpp).
- [Snippet/Opinion] A guide suggests turning off the Category column, since Nexus categories depend on how authors classify their mods — [Nexus separators page](https://www.nexusmods.com/skyrimspecialedition/mods/96582).
- [Opinion] A Step forum reply suggests deleting default categories and creating your own based on guide sections — [Lexy's thread](https://stepmodifications.org/forum/topic/13092-lexys-legacy-of-the-dragonborn-special-edition/page/577). This is the opposite approach, with older evidence.
- [Local] Categories already auto-populate and cut across the separators: SkyUI and RaceMenu share ID 15, and CBBE 3BA and BnP female skin share ID 5. The ID names were not looked up. Several generated and manual entries have `-1`.
- **Notes.** [Source] The Notes column shows `comments`; the tooltip shows both `comments` and `notes`. A valid color paints the Notes column background — [modlist.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlist.cpp). `comments` and `notes` are searched by the text filter — [modlistsortproxy.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistsortproxy.cpp).
- **Colors on mods.** [Source] `setColor` applies to any selected row, not only separators — [modlistviewactions.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistviewactions.cpp).
- **Flags.** [Guide, MO1-era] Step documents flags and the highlights for conflicts: green for mods the selection overrides, red for mods overriding it — [Guide:Mod Organizer](https://stepmodifications.org/wiki/Guide:Mod_Organizer). That page is dated to Mod Organizer 1, and the release notes do not show a change in this area. It also says the page was only read to 100,000 of 182,242 characters.

### Inferences
- Do not use Group by as a daily view, because it loses the tree and download drops are rejected under `QtGroupingProxy` [Source: modlistsortproxy.cpp]. It is fine as a temporary audit view.
- A small category use that does pay off: a `Patch` category to filter patches when they are scattered beside their parents. This is what makes the hybrid patch rule easy to audit.
- Use colors for section families (for example one color for character sections) rather than a different color per separator. With scrollbar marks on, this aids navigation. This is a preference, not sourced.

### Gaps
- Whether Notes survive Replace on reinstall is uncertain: `createMod` resets `modid`, `version`, `category` and `installedFiles` when not merging — [organizercore.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/organizercore.cpp) — but the summary did not list comments. Test before relying on it.
- Whether internal drag between rows works under Group by in 2.5.x is unclear. Step's page is internally inconsistent on this, and it is MO1-era.

## Mod priority for optional files and handling of multiple-option mods (FOMOD)

### Takeaway
Default to separate entries (Rename at the install prompt) placed directly below the main file. Merge only for small hotfixes or when a guide instructs it. Use Replace for version updates. Reinstall to change FOMOD choices, and write the choices in Notes unless FOMOD Plus is used.

### Cited Findings
- [Opinion] The prompt appears when a mod of that name already exists. Merge overwrites conflicting files and leaves the rest. Replace removes the old version. Rename installs separately — [Step forum](https://stepmodifications.org/forum/topic/16497-mo2-and-merging-pre-downloaded-files/), [Step forum](https://stepmodifications.org/forum/topic/14721-should-i-merge-sro-files-by-hand). These links come from one search summary; attribution to each specific page was not checked.
- [Guide] Step uses both. It merges some optional files into main (SSE Display Tweaks), and installs others separately, which "preserves their version tracking to keep pace with updates" or lets them be disabled later (LODGEN textures) — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3).
- [Opinion] Merging is "generally unnecessary", mainly useful for hotfixes that replace a single file — [Reddit snapshot, Dec 2025](https://reddit.sentinel-team.org/posts/1ptudvt/snapshots/2025-12-24T00%3A20%3A21.850421Z).
- [Source] A reinstall does not change priority (`reinstallation ? -1 : priority`), and a merged or replaced install does not move the mod — [organizercore.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/organizercore.cpp).
- [Source] `installedFiles` records `modid`/`fileid` pairs — [modinforegular.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modinforegular.cpp).
- [Opinion] Reinstall via right-click and choose replace or merge at the end. FOMOD Plus can highlight earlier choices, but only for mods installed after the plugin was added — [FOMOD Plus notes](https://gio-gianny.github.io/gio_skyrim_stock_game/mo2_plugins/fomod_plus_a_mod_installation_overhaul_for_mod_organizer_2/).
- [Local] The user has already split items as separate entries, such as `BEES` and `BEES Papyrus Scripts`, `BnP female presets` and `BnP female small update`, and the two Expressive Facial Animation editions.

### Inferences
- Separate entries can be toggled and removed, show their own conflicts, and keep their own versions. Merged files cannot be separated later without reinstalling. Sibling entries have the wrong-match risk noted above when updating.
- Multi-variant mods: a single FOMOD install is fine when choices are stable. Keep variants as separate entries only if the user really switches between them.
- A patch shipped in a FOMOD of the parent stays in that entry, and is one more reason to note the choices. Patches from other pages get their own entries.
- Generated output is a different thing from FOMOD output: keep it in dedicated entries in Outputs, so it can be wiped and regenerated.

### Gaps
- No official MO2 guidance on this exists, as noted above. The Step forum notes the wiki had little beyond a warning about uninstalling merged mods (search summary only).

## How does the user's 17-separator scheme compare, and what should change?

### Takeaway
The scheme is sound. It is function-labeled and largely arranged by override order, the same model Step uses. Keep it unnumbered. Make three changes: fix the "Recently Added" position, add a Patches section once a multi-target patch exists, and watch the DLC & CC separator for issue #2420.

### Cited Findings
- [Local] Mods per separator from `modlist.txt`:

| Separator (priority ascending) | Entries |
|---|---|
| DLC & CC | 78 foreign (3 DLC, 58 labeled Creation Club, 17 labeled Unmanaged) |
| SKSE & Frameworks | 15 |
| Fixes | 6 |
| UI & Camera | 4 |
| Shaders | 11 |
| Skeleton & Physics | 3 |
| Body | 5 |
| Head & Face | 7 |
| Skin | 2 |
| Presets | 5 |
| Hair | 2 |
| Animation | 4 |
| Armor | 1 |
| Gameplay | 3 |
| Tools | 3 |
| Recently Added | 0 |
| Outputs | 6 |

- [Local] 77 managed mods, about 4.8 per non-DLC section. One profile (`Default`), which removes the multi-profile rename risk.
- **Where a new mod lands.** [Source] `findInstallPriority` returns -1 unless a valid row is selected and the view is sorted by priority. It uses the selected mod's priority; for a selected separator it targets the next one in ascending order, which is the end of that section — [modlistviewactions.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlistviewactions.cpp). Dragging a download onto the list uses `dropPriority`, and `MaximumPriority` when dropped out of range — [modlist.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/modlist.cpp). Unlisted mods get highest priority — [profile.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/profile.cpp).
- **Foreign entries.** [Source] They get pushed to the lowest priorities — [profile.cpp](https://raw.githubusercontent.com/ModOrganizer2/modorganizer/master/src/profile.cpp). [Issue] [#2420](https://github.com/ModOrganizer2/modorganizer/issues/2420) concerns this exact layout, and [#1215](https://github.com/ModOrganizer2/modorganizer/issues/1215) (2020) reported Non-MO order being reset. [Local] As of the last write, `DLC & CC_separator` is still on the last line.
- **Comparison to Step.** [Guide] Step places Fixes (09) after Models and Textures, Sounds and Character Appearance, Utilities (19) right before Patches (20), and Post-Processing last (21) — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3).
- **Step sections without an equivalent here:** Resources, Foundation, Models and Textures, Sounds and Music, Locations, Lighting and Weather — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3).
- [Local] The Lite tier comparison: 17 separators sits under the 19 pack size, for a list one third of that tier's 250 mod ceiling ([Snippet] [Nexus 90857](https://www.nexusmods.com/skyrimspecialedition/mods/90857)).

### Inferences
**Change**
1. **Move "Recently Added" to the very bottom, after Outputs.** With nothing selected, a new install should land at highest priority, which is currently inside Outputs, not under Recently Added, which is empty now. Either way the mod temporarily outranks the outputs until triaged, but moved to last it is at least visibly in the inbox. Alternative: keep the current order and always select the Recently Added separator, or drag downloads onto it. Test with one small mod, since this comes from reading `master`.
2. **Add "Patches" between Tools and Outputs when the first multi-target patch arrives.** Single-parent patches go beside the parent. Do not create it empty just for symmetry.
3. **Test the DLC & CC separator against #2420.** Collapse it, press F5, check it. If it misbehaves, delete it. It is purely cosmetic, because foreign entries are placed at the lowest priorities anyway. Only then would the 78 entries stay uncollapsed, unless the separator is retained for that purpose. This trade-off is the user's call.

**Consider**
4. **Fixes.** The SKSE plugin fixes do not conflict by position. "Assorted mesh fixes" is the exception, since it touches assets and sits low, so any later mesh mod overrides it. Check its Conflicts tab, and move it to after Armor if it is losing to mods it should fix.
5. **Tools.** BodySlide currently outranks Body and Presets. Check BodySlide's Conflicts tab for losses in CBBE 3BA or preset files.
6. **Consider small-section names when adding.** Armor (1), Hair (2) and Skin (2) are small but are real boundaries or will grow, so keep them.

**Keep**
- Unnumbered names, since there is one profile and frequent inserts are likely as the list grows.
- The body sequence, with Skeleton before Body before Skin and Presets; later sections override earlier ones.
- `Outputs` near the end and `<Tool> - Outputs` naming, which fits Step's practice.
- Ascending sort, per-direction collapse, scrollbar colors.

**Future sections, added only when needed**: Textures and Models, Lighting and Weather, Audio, Locations, NPCs and Creatures, and splits within Gameplay, using Step's six parts. Place world asset sections before Gameplay and after Armor. Keep Lighting after Locations, following Step.

### Gaps
- "About 112 plugins" was given by the caller. `plugins.txt` has 49 lines marked active, and CC plugins may be implicitly active, but the count was not reconciled and it does not affect this analysis.
- Why 17 entries show as `Unmanaged:` rather than `Creation Club:` is unknown. Only `_ResourcePack` is an obvious non-CC item. This may be relevant to the 2.5.2 CC parsing mentioned in #2420, but that link is speculative.
- No conflict data was analysed here, so the suggestions on Assorted mesh fixes and BodySlide are prompts to check, not findings of an actual problem.
