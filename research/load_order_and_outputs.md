# Load order, conflict resolution, generated outputs and list maintenance for Skyrim SE in MO2

Target setup: Skyrim SE 1.5.97 with Anniversary Edition Creation Club content, MO2 2.5.2, SKSE 2.0.20, BEES, Pandora Behaviour Engine+, BodySlide output in its own mod, PGPatcher. Researched 2026-11-02.

Evidence tags: **[R]** = the page itself was fetched. **[S]** = search-result summary only; the passage was not read in context, and where several links are grouped the exact passage-to-link mapping is unverified. Treat [S] as a lead. Forum and Reddit items are opinion or anecdote unless stated. Nexus mod pages and one Nexus forum thread returned HTTP 403, and Reddit was only reachable through mirrors. The Step 2.3 guide was read for characters 0-100,000 and 290,000-390,000 of about 390,000; the middle was not read.

## LOOT versus manual ordering

### Takeaway
LOOT is the baseline for Skyrim lists, but it is not the final authority. Curated lists sort with LOOT, encode exceptions as LOOT metadata (`Load After` for specific pairs, groups for whole sets), and check the result in xEdit. Sort before each generator that reads the load order, sort again once its plugin exists, then confirm the placement by eye.

### Cited Findings
- **[R]** Step 2.3 (released 2024-08-19, targets 1.6.1170) relies on LOOT alone: its patches "are designed to work with a default, LOOT-sorted plugin order", which "eliminates the need to set rules on the load order". It says to sort whenever plugins are added or removed and to keep LOOT and its masterlist updated — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[S]** Lexy's guide uses LOOT plus user rules: a Conflict Resolution group with additional rules and separate `Load After` rules for individual mods (page date not checked, treat as older) — [Lexy's LOTD Finishing Line](https://stepmodifications.org/wiki/User:DarkladyLexy/Lexys_LOTD_SE_Finishing_Line). A reply in the support thread says you cannot expect to match another person's order 100%, because every added mod changes it — [Step forum, Lexy's thread](https://stepmodifications.org/forum/topic/13092-lexys-legacy-of-the-dragonborn-special-edition/page/618)
- **[S]** The Nolvus guide tells the user to run LOOT from MO2, sort, then apply the sorted order — [Nolvus LOD page](https://www.nolvus.net/guide/asc/visuals/lods)
- **[S]** Viva New Vegas rejects LOOT and ships a premade `loadorder.txt` per module, placed in the MO2 profile folder. This is a Fallout: New Vegas guide, and its reason is that LOOT's FNV masterlist is "heavily outdated", so it does not carry over to Skyrim — [Viva, Tools to Avoid](https://vivanewvegas.moddinglinked.com/avoid-tools.html); [Viva, Base Finish](https://vivanewvegas.moddinglinked.com/basefinish.html)
- **[R]** LOOT's FAQ says it "can sort most plugins correctly, sometimes it gets things wrong", that it "isn't omniscient", that more than one load order can be correct, and that it does not know which plugins belong to which mod. To check a suspected misorder, look for the conflicts in TES5Edit and decide for yourself — [LOOT FAQs](https://loot.github.io/docs/help/loot-faqs/)
- **[R]** The FAQ gives two override tools: `Load After` entries for specific plugins, and groups "when the plugin needs to load before or after many other plugins" — [LOOT FAQs](https://loot.github.io/docs/help/loot-faqs/)
- **[R]** Group ordering is transitive even when a middle group has no installed plugins. Masterlist-defined groups and edges cannot be removed. Cycles are possible, and LOOT breaks them by ignoring a plugin's group membership, so the docs advise avoiding them — [LOOT Groups Editor](https://loot.readthedocs.io/en/latest/app/usage/groups_editor.html)
- **[R]** DynDOLOD: "Sort and finalize the load order before generating the LOD patch" — [DynDOLOD Load/Overwrite Orders](https://dyndolod.info/Help/Load-Overwrite-Orders)
- **[R]** Step runs Nemesis with all plugins ticked and LOOT-sorted, and sorts with LOOT again after enabling the DynDOLOD plugins — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[R]** The PGPatcher wiki says LOOT sorts `PG_X.esp` correctly — [PGPatcher Basic Usage](https://github.com/hakasapl/PGPatcher/wiki/Basic-Usage-%28PGPatcher%29)
- **[S]** A user reported LOOT placing `DynDOLOD.esp` too early, fixed by moving it manually to the end. Another reply says to run LOOT before generating LOD because DynDOLOD Resources adds plugins. Anecdotal and older — [Step forum, LOOT after DynDOLOD](https://stepmodifications.org/forum/topic/13969-should-i-run-loot-after-dyndolod-installation/)

### Inferences
- Working rule: sort, generate, enable the output, sort, verify. Each generator should read a sorted order, and its plugin then needs placing.
- Record every exception as LOOT metadata rather than a manual drag. LOOT recalculates the order from its metadata, so an undocumented drag is likely to be lost at the next sort.
- Use `Load After` first, because it states a specific reason. Use a group only when one plugin or set must sit relative to many plugins, such as a personal patch group loading after everything except the LOD plugins.
- After the final sort, confirm the end of the list by eye: `PG_X.esp`, then `DynDOLOD.esp`, then `Occlusion.esp`. `DynDOLOD.esm` should be the last ESM.

### Gaps
- No primary source was read showing how Wabbajack-distributed Skyrim lists (Nolvus excepted) ship their final order, or whether they tell users not to re-sort. The Nolvus evidence is a search summary of the manual guide.
- I found no source stating a formal curated-list policy on when to prefer a group over `Load After`, beyond LOOT's FAQ wording.

## Plugin limits, ESL, compacting, BEES and Form 43

### Takeaway
Plan for 254 full plugins plus up to 4096 light plugins. BEES does not raise either count. It lets 1.5.97 load plugins with 1.71 headers and the extended light range (4096 new records per light plugin instead of 2048), which AE gets natively from 1.6.1130. Do not "upgrade" Form 43 plugins blindly: the form version alone rarely breaks anything, and a careless conversion can.

### Cited Findings
| Item | 1.5.97 without BEES | 1.5.97 with BEES | AE 1.6.1130+ |
|---|---|---|---|
| Full plugins | 255 active ESM/ESP per LOOT; 254 per Smash | Unchanged | Same as 1.5.97 |
| Light plugins | 4096 | Unchanged | 4096 |
| New records per light plugin | 2048 | 4096 | 4096 |
| 1.71 headers | Likely crash | Loads | Native |
| FormIDs 001-7FF as new records | Not allowed | Allowed | Allowed |

- **[R]** LOOT documents up to 255 active `.esm`/`.esp` plugins and up to 4096 additional `.esl` plugins on SSE, with positions shown as 00-FE and light masters shown as FE — [LOOT, Introduction to Load Orders](https://loot.github.io/docs/help/introduction-to-load-orders/)
- **[S]** Mator Smash describes the limit as 254 "full modules", meaning anything not ESL or ESL-flagged, including ESMs — [Mator Smash on Nexus](https://www.nexusmods.com/skyrim/mods/90987); [Nexus forum, Smash and ESL](https://forums.nexusmods.com/topic/7987948-is-mator-smash-useless-for-se-without-esl-support)
- **[R]** The BEES README says it "adds support for the extended plugin (ESL) range introduced in game version 1.6.1130" and backports compatibility for 1.71 headers. The header change was made "to expand the maximum number of new records in an ESL from 2048 to 4096". A 1.71 plugin on an old build "will likely crash". Supported: "1.5.97, 1.6.659, and anything in between". Its log, `BackportedESLSupport.log` under `Documents\My Games\Skyrim Special Edition\SKSE`, lists relevant plugins — [BEES GitHub](https://github.com/Nukem9/skyrimse-backported-esl-support)
- **[R]** A Step thread (started 2023-12-09) says BEES applies to 1.5.97 through 1.6.640, which differs slightly from the README's 1.6.659. It is unnecessary for gameplay on 1.6.1130+, but is still needed when generating an NGIO grass cache on the 1.5.97 runtime — [Step forum, BEES](https://stepmodifications.org/forum/topic/19259-backported-extended-esl-support-by-nukem/)
- **[S]** The Nexus file page was reported as listing BEES 1.4 as the latest main file (August 2026). The same search flagged inconsistent dates, and I could not open the page to confirm — [BEES Nexus files](https://www.nexusmods.com/skyrimspecialedition/mods/106441?tab=files)
- **[S]** Builds 1.5.97-1.6.640 did not allow forms in 001-7FF as new records (community testing, not official) — [Nexus 106283 posts](https://www.nexusmods.com/skyrimspecialedition/mods/106283?tab=posts). A December 2023 post says old executables (downgraded, VR, GOG) crash immediately on the new plugins, and that 1.6.1130 opened 0x0-0x7FF to plugins other than `Skyrim.esm` — [r/skyrimmods mirror, Dec 2023](https://reddit.rtrace.io/r/skyrimmods/comments/18btob5/updated_information_about_the_new_skyrim_update)
- **[S]** Compacting: xEdit's "Compact FormIDs for ESL" renumbers all records and fails if there are too many. xEdit refuses to save an ESL flag when FormIDs are invalid. An ESP-FE is an ESP with the ESL flag and is not a master. Common practice is not to flag plugins that create new CELL records — [Nexus article, making an ESPFE](https://www.nexusmods.com/skyrimspecialedition/articles/1776); [Nexus forum, compacting](https://forums.nexusmods.com/topic/7979533-need-some-help-figuring-out-the-compacting-process-for-eslifying-plugins)
- **[S]** Compacting does not update FaceGen files, so NPC face assets keyed to old FormIDs break — [FaceGenEslify README](https://github.com/Michael-wigontherun/FaceGenEslify/blob/main/README.md). A forum poster advises checking scripts for `GetFormFromFile`/`GetFormID` first — [Nexus forum, ESP to ESL](https://forums.nexusmods.com/topic/10613998-questions-about-converting-esp-to-esp-with-esl-flag-for-skyrim-se)
- **[S]** Form 43, opinion: usually harmless, "very unlikely to crash your game", and many base game files are still Form 43 — [Nexus forum, mods at Form 43](https://forums.nexusmods.com/topic/12537304-lots-of-mods-for-sse-are-form-43)
- **[S]** Form 43 conversion: one poster warns never to change 43 to 44 in xEdit by editing the header, because record layout differs and weapon damage and duration values can be lost. The usual method is loading the plugin as active in the SE Creation Kit and saving. One user's mod crashed on startup after this conversion, though the cause was not established. A claim that the SE CK no longer saves ESPs that have ESP masters is old and unverified — [Nexus forum, Form 44 via SSEEdit](https://forums.nexusmods.com/topic/8760158-correcting-old-form-to-44-using-sse-edit)

### Inferences
- "BEES raises the plugin limit" is a misreading. Neither the README nor the Step thread mentions any increase in plugin count, only in the record range and header support. The table's "unchanged" cells are drawn from that absence.
- The 255 and 254 figures probably reconcile through the FE slot: with any light plugin active, FE is taken. Use 254 as the planning number.
- With BEES present, 1.5.97 and AE should behave alike for 1.71 and extended-range plugins. The remaining 1.5.97 risk is SKSE DLL compatibility, not plugin headers.
- For any plugin you flag yourself: confirm it has no new CELLs, no FaceGen dependency and no scripted lookups by FormID. If other plugins use it as a master, compact only with them loaded so that xEdit can update them, then test. If unsure, leave it as a full plugin while slots remain.
- Treat Form 43 as a review prompt. Convert only when there is a concrete symptom or a data-layout reason, on a backed-up copy, and compare records in xEdit afterwards.

### Gaps
- I could not read the MO2 Form 43 warning thread ([Nexus forum, 403](https://forums.nexusmods.com/topic/13510797-mo2-form-43-or-lower-plugin-detected)), so I have no first-hand description of MO2 2.5.2's warning text.
- I found no reliable source on whether 1.5.97 has distinct behaviours for specific Form 43 record types.
- I found no source on handling an already-compacted plugin that other mods use as a master after an upstream update.
- The BEES page's August 2026 version needs a direct check by the user.

## Plugin cleaning, vanilla masters, deleted navmeshes and CC plugins on 1.5.97

### Takeaway
Clean what LOOT or your own xEdit run flags, using Quick Auto Clean on one plugin at a time. Step cleans vanilla and CC masters and stores them in a mod. Deleted navmeshes reported in official masters can be left alone. In a mod they are a real fault for the author or a manual fix. A LOOT warning on a CC plugin is evidence, not a verdict, and on 1.5.97 your own xEdit result against your own masters decides.

### Cited Findings
- **[R]** xEdit docs: ITMs "can be cleaned automatically", and deleted references "are a significant cause of crashes and game bugs" and can also be cleaned automatically. Deleted navmeshes "cannot be automatically corrected, and require manual cleaning". Wild edits must be cleaned manually. Quick Auto Clean is "the preferred and recommended method" and runs three passes, saving between each — [xEdit, Mod Cleaning](https://tes5edit.github.io/docs/7-mod-cleaning-and-error-checking.html)
- **[R]** xEdit docs: clean one file at a time with nothing else loaded, because extra modules make the process "utterly pointless". "There are errors in the official DLCs. Do not attempt to correct them." — [xEdit, Mod Cleaning](https://tes5edit.github.io/docs/7-mod-cleaning-and-error-checking.html)
- **[R]** Step 2.3 cleans "exactly 44 'dirty' vanilla masters" across the base game, DLC and CC, using xEditQuickAutoClean, citing large reference bugs. Cleaned files go in a "Cleaned Vanilla Masters" mod, and originals are restored to Data so Steam does not see the change. Anything Bethesda updates must be cleaned again. The count was written for 1.6.1170 — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[R]** Step's default rule: "Always follow LOOT's advice in regards to mod cleaning and sorting unless otherwise noted" — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[R]** LOOT's dirty information rests on CRC: "It can't detect unknown unclean plugins" or "plugins that have been edited but not cleaned". False ITM positives can occur when a plugin is checked against different dependency versions, such as other localisations — [LOOT, Dirty Edits & CRCs](https://loot.github.io/docs/help/dirty-edits-mod-cleaning--crcs/)
- **[R]** January 2024 (older): after the 1.6.1170 update, Mousetick said LOOT's metadata lagged, so it could not reliably show whether masters were clean, and advised running QuickAutoClean whenever the game or CC updates. z929669 (admin) said he trusts LOOT's metadata while acknowledging the delay. The thread does not discuss navmeshes — [Step forum, cleaning vanilla masters](https://stepmodifications.org/forum/topic/19347-step-cleaning-vanilla-masters)
- **[S]** Older (2019-2021): a guide says not to clean deleted navmeshes in the official ESMs because it "will do more harm than good". A user was told to ignore three deleted navmeshes reported in `Update.esm`, as they generally need the Creation Kit. Deleted navmeshes in a mod's own plugin are treated as a real crash risk — [Nexus 89312](https://www.nexusmods.com/skyrimspecialedition/mods/89312); [Step forum, vanilla masters problem](https://stepmodifications.org/forum/topic/16336-problem-with-cleaning-vanilla-masters); [Nexus forum, LOOT deleted navmeshes](https://forums.nexusmods.com/topic/9509433-vortex-loot-found-deleted-navmeshes). A manual method exists — [CK wiki, Fixing Navmesh Deletion](https://ck.uesp.net/wiki/Fixing_Navmesh_Deletion_Tutorial)
- **[S]** A Steam user says the free CC files arrive with the 1.6+ update, so downgrading can remove them, and another suggests copying them out and back — [Steam discussion](https://steamcommunity.com/app/489830/discussions/0/4211497623313274801). A forum user warns a downgrade means using 1.5.97 SKSE DLLs only — [Nexus forum, 1.5.97 in 2025](https://forums.nexusmods.com/topic/13510557-should-i-downgrade-game-version-to-1597-in-2025)

### Inferences
- **Clean:** plugins LOOT flags with a matching CRC, unless the mod author says otherwise; and vanilla and CC masters if you follow the Step approach.
- **Do not clean:** plugins whose author warns against it; anything just to remove masters (the xEdit docs say not to remove masters from others' mods); intentional-looking edits you have not inspected. A QAC report of deleted navmeshes in a master is not a failed clean.
- **Deleted navmesh rule:** in official masters and CC, note it and move on, since no reviewed source shows these causing trouble in practice. In a mod, check for an updated version or author fix, then use the manual CK method only if you can test that area.
- **CC plugin with a LOOT warning generated against newer masters (target setup):**
  1. Read the warning as "this file's CRC was once reported dirty by someone", not as a measurement of your own install. The record count may come from different masters.
  2. Back up the plugin, then load it in xEdit with your 1.5.97 masters and run QAC or an ITM check. xEdit compares against the masters actually loaded, so its result applies to your setup.
  3. If xEdit finds ITMs or deleted references, QAC is reasonable. Keep the cleaned copy in its own mod and the original as a backup. If it finds nothing, leave it and consider a LOOT user metadata note.
  4. Check the plugin's header version. If it is 1.71, it depends on BEES, which logs relevant plugins.
  5. If you later change masters (for example `Update.esm`), repeat the check, because a cleaned CC plugin is only valid against the masters it was cleaned with.
- Step's "restore originals" step protects a Steam-managed Data folder. A separate Stock Game copy is outside Steam's reach, so this should matter less there, though a cleaned-masters mod remains the tidier and more reversible approach.
- Do not reuse Step's "44" as a target. Count from your own install, since a 1.5.97 setup with added AE content may differ.

### Gaps
- No primary source covers cleaning CC plugins specifically on 1.5.97, or which CC plugins LOOT currently flags. Checking the current LOOT masterlist for your plugin names, or LOOT's own output, would answer this.
- The current best evidence on vanilla navmesh risk is old (2019-2021) and partly forum opinion. I found no controlled test.
- A dissenting "do not clean masters" position exists, but I did not read a current, reasoned statement of it. [This older Nexus thread](https://forums.nexusmods.com/topic/10858303-to-clean-or-not-to-clean) was only seen in search results. I also did not verify whether a mismatched `Update.esm` is present in common 1.5.97 + AE setups.

## Conflict resolution with xEdit and asset conflicts

### Takeaway
Conflicts are normal. Act only when the winning record drops something you want. Use a small personal patch that loads after its sources, keep it in its own mod, and fix asset conflicts by deliberate left-pane order, not by file deletion.

### Cited Findings
- **[R]** Colours and meaning: overrides show yellow background with green text and usually need no action. Conflict losers show red background and red text. A green background with grey text means identical to master, usually an unintentional dirty edit. After patching, the text turning green shows the conflict is resolved — [xEdit, Conflict Detection](https://tes5edit.github.io/docs/5-conflict-detection-and-resolution.html)
- **[R]** "The game will count the last record loaded as the winner of any conflict between files" — [xEdit, Conflict Detection](https://tes5edit.github.io/docs/5-conflict-detection-and-resolution.html)
- **[R]** Workflow: right-click, "Apply Filter to show Conflicts", which can take minutes on large lists; review in the View tab. To patch, right-click the record, "Copy as override", create a new file; save with Alt-S and confirm in Messages. The patch should load last among related plugins. The old Merged Patch tool is obsolete and unsupported — [xEdit, Conflict Detection](https://tes5edit.github.io/docs/5-conflict-detection-and-resolution.html)
- **[R]** Four options: do nothing, change load order, add the records to a patch, or remove a mod. "Often times conflicts are not harmful to the game", and some red-background conflicts are intentional, such as a deliberate compatibility patch loading last — [xEdit, Conflict Detection](https://tes5edit.github.io/docs/5-conflict-detection-and-resolution.html)
- **[S]** A January 2026 Reddit thread favours manual xEdit mini patches over Smash (opinion) — [r/skyrimmods snapshot](https://reddit.sentinel-team.org/posts/1qkn2k4/snapshots/2026-01-23T21%3A21%3A30.982898Z)
- **[R]** Asset rules from tools: TexGen output "needs to overwrite DynDOLOD Resources and also any other assets", and "Generated output should always overwrite everything else". "Do not disable any LOD assets (meshes and textures) after generation" — [DynDOLOD Load/Overwrite Orders](https://dyndolod.info/Help/Load-Overwrite-Orders)
- **[R]** Step: mods are arranged in listed order so later mods override earlier ones — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[R]** PGPatcher reads MO2 conflict results by being pointed at the instance folder; the wiki says the default is correct in most cases — [PGPatcher Basic Usage](https://github.com/hakasapl/PGPatcher/wiki/Basic-Usage-%28PGPatcher%29)

### Inferences
**Personal patch recipe**
1. Load the sorted list through MO2 into xEdit and apply the conflict filter.
2. Triage in this order: leveled lists, NPCs, quests, cells and worldspaces, then the rest. This priority is my judgment, not from a source.
3. Copy the winning record into a new ESP-FE patch, then forward wanted values from the losers. Do not change anything you have no reason to change.
4. Put it in its own mod, such as `Personal Patch - <topic>`, and add a LOOT `Load After` for each of its sources.
5. Run this before the generators, so they read the final records, and rerun affected generators afterwards.

**Treat as harmless:** identical values, cosmetic differences you do not care about, deliberate patch wins, and a higher mod winning when it was meant to.

**Investigate:** a lost keyword or script, a lost navmesh or location edit, NPC record and FaceGen mismatches, and worldspace or cell conflicts in places that affect LOD.

**Asset rule:** decide the winner per mod, record why in a separator or mod note, and hide individual files only when a whole-mod order cannot give the result you want.

### Gaps
- I did not read a primary guide on MO2's conflict tabs and hidden-file workflow.
- I found no source giving an authoritative triage order for record types.

## Generated outputs: run order, left-pane placement and keeping Overwrite empty

### Takeaway
Run from the bottom of the dependency chain up: patches built from plugins first, then visual patchers, then LOD last. Each output goes in its own mod, and each tool's own output setting is preferred over MO2's "create files in mod" option, since that only captures new files. LOD plugins go last, and any later plugin change means updating LOD.

### Cited Findings
- **[R]** PGPatcher order: "BodySlide, PGPatcher, TexGen, then DynDOLOD", with "Keep PGPatcher output enabled for the rest of this list". The mod should win over everything except TexGen and DynDOLOD outputs. `PG_X.esp` "MUST BE LOADED LAST, except for DynDoLOD/TexGen Outputs". VRAMr order "doesn't technically matter", with enable or disable rules depending on whether it runs before or after — [PGPatcher Basic Usage](https://github.com/hakasapl/PGPatcher/wiki/Basic-Usage-%28PGPatcher%29)
- **[R]** PGPatcher output folder: use an empty mod such as `PGPatcher_Output`, with the zip option off and the mod disabled before running. A later run offers "Update Output", patching only what changed — [PGPatcher Basic Usage](https://github.com/hakasapl/PGPatcher/wiki/Basic-Usage-%28PGPatcher%29)
- **[R]** BodySlide: "To output to a mod use the preferences within the Bodyslide GUI NOT the MO2 output to mod option", because MO2's option only adds new files, so existing meshes are overwritten in the original mod ("an unsolvable limitation of the MO2 USVFS"). The output must be active before PGPatcher runs — [PGPatcher Basic Usage](https://github.com/hakasapl/PGPatcher/wiki/Basic-Usage-%28PGPatcher%29)
- **[R]** Pandora: create an empty `Pandora Output` mod and set `-o "absolute path"` in MO2's executable arguments. The README prefers this over MO2's option because "files produced by Pandora with MO2 VFS will overwrite existing files at their origin". Do not install Pandora directly in Data. It supports Nemesis and FNIS patch formats. For a Stock Game, use `--tesv` to point at the game root so FNIS mods are found — [Pandora GitHub](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus)
- **[S]** Nemesis may stay installed for its patches, but its output must be disabled or deleted — [Pandora Nexus](https://nexusmods.com/skyrimspecialedition/mods/133232)
- **[R]** Step runs Nemesis with "Create files in mod instead of overwrite" and an output mod. This contrasts with Pandora's README, which warns against that MO2 setting for Pandora — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[R]** DynDOLOD: `DynDOLOD.esm` should be "the ESM with the highest priority possible or just before the first non-ESM". `DynDOLOD.esp` and then `Occlusion.esp` should be the last plugins. Previous TexGen output "should be removed before running TexGen again". After adding plugins, regenerate, or patch conflicting records in xEdit, or sort the new plugin after the DynDOLOD plugins — [DynDOLOD Load/Overwrite Orders](https://dyndolod.info/Help/Load-Overwrite-Orders)
- **[R]** Step order: terrain first, then object LOD, meaning xLODGen, TexGen, DynDOLOD. Empty output mods sit at the bottom of the left pane in that order. Disable the temporary `(TEMP) Cathedral Landscapes - xLODGen` mod after terrain generation. The grass cache goes in the SKSE output mod — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[R]** Step's regeneration triggers: xLODGen for landscape textures or LAND/LTEX changes; TexGen and DynDOLOD for object, grass, tree or landscape-height changes or a master order change; Nemesis for animation or skeleton changes — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[S]** Bashed Patch first, with `Synthesis.esp` and `DynDOLOD.esp` deactivated while it builds; Synthesis then runs after it. The OWL example order is Bashed Patch, OWL, Synthesis, and calls Smash "completely optional" — [Nexus guide, OWL](https://www.nexusmods.com/skyrimspecialedition/articles/3166); same sequence from a user — [Steam discussion](https://steamcommunity.com/app/489830/discussions/0/3806155532855864955)
- **[S]** The Mator Smash page says Bashed Patch runs before the Smashed Patch, and the Smashed Patch must be regenerated whenever the load order changes — [Mator Smash on Nexus](https://www.nexusmods.com/skyrim/mods/90987)
- **[S]** A January 2026 thread says Smash "hasn't been relevant in years" (opinion) — [r/skyrimmods snapshot](https://reddit.sentinel-team.org/posts/1qkn2k4/snapshots/2026-01-23T21%3A21%3A30.982898Z). A DynDOLOD thread states LOD should be generated last, but that thread's own load-order sketch places Synthesis after DynDOLOD, which is unresolved — [Step forum, DynDOLOD 3 alpha, p.614](https://stepmodifications.org/forum/topic/17510-dyndolod-300-alpha-180/page/614)
- **[S]** Nolvus points DynDOLOD output at the Overwrite folder during generation, which differs from Step's empty output mods — [Nolvus DynDOLOD page](https://nolvus.net/guide/asc/output/dyndolod)
- **[R]** Step says a config file "should appear in Overwrite (or the SKSE Output if the guide was followed)". It does not state a keep-Overwrite-empty rule outright — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)

### Inferences
**Recommended run order for the target setup.** This combines the sources above; no single source states it.

| Step | Tool | Output mod | Left-pane position (bottom = wins) | Plugin position | Rerun when |
|---|---|---|---|---|---|
| 0 | LOOT and personal patches | Own patch mods | After their sources | After sources | Any plugin change |
| 1 | BodySlide batch build | `BodySlide Output` (BodySlide's own setting) | Below body and outfit mods | None | Body, preset or outfit change |
| 2 | Pandora | `Pandora Output` (`-o`) | Below animation mods | None | Animation, behaviour or skeleton change |
| 3 | Wrye Bash, optional | `Bashed Patch` | Late | After what it patches | Leveled-list or tagged plugin change |
| 4 | Mator Smash, optional, usually skip | `Smashed Patch` | Late | After Bashed Patch | Any load order change |
| 5 | Synthesis | `Synthesis Output` | Late | After Bashed or Smash | Inputs change |
| 6 | LOOT sort, then xLODGen terrain | `xLODGen Output` | Near bottom | None | Landscape changes |
| 7 | PGPatcher (BodySlide output enabled, own output disabled while running) | `PGPatcher_Output` | Below all but TexGen and DynDOLOD | `PG_X.esp` last, except LOD plugins | Mesh, texture or relevant plugin change |
| 8 | TexGen (old output removed, PGPatcher enabled) | `TexGen Output` | Below PGPatcher | None | Tree or object texture change |
| 9 | DynDOLOD (LOOT sorted first) | `DynDOLOD Output` | Very bottom | ESM last among ESMs; ESP then Occlusion last | Object, tree, grass or order change |

- Disable the previous output of a step before rerunning it, so a tool does not read its own old result. Sort after enabling the new plugin, then check its position.
- Pandora's place in the sequence is loose. It does not depend on plugin order in any reviewed source, so running it at step 2 simply avoids forgetting it. A skeleton change should trigger it.
- **Why each output gets its own mod:** the output can be disabled or deleted in one move, it has an explicit left-pane priority, and it can be regenerated without mixing into source mods. A tool cannot then read its old output by accident.
- **The shared lesson from BodySlide and Pandora:** MO2's "create files in mod" does not reliably capture every file, since existing ones are changed where they live. Prefer each tool's own output path, and do not assume MO2's redirect protects source mods.
- **Keeping Overwrite empty:** treat a non-empty Overwrite as a to-do after each tool or game run. Move each file to the correct output mod: tool outputs to their mod, SKSE logs and generated config to an SKSE Output mod. This is a practice inferred from Step's output mods, not a quoted rule. Nolvus's use of Overwrite is a temporary path, not a counterexample, assuming its output is moved afterwards.
- **Synthesis versus DynDOLOD:** keep Synthesis before LOD generation. DynDOLOD's sort-and-finalize rule and last-plugin rule support this over the contrary sketch in the forum.

### Gaps
- **xLODGen versus PGPatcher order:** the PGPatcher wiki does not mention xLODGen, and Step does not use PGPatcher. Step 6 and the left-pane position relative to PGPatcher are my placement, not a sourced rule. A direct check in current PGPatcher or DynDOLOD support threads is warranted.
- I could not confirm from Synthesis's own docs where its output should go. The ordering comes from community guides. The Synthesis docs were not read in this round.
- I did not read Wrye Bash documentation directly.
- I did not confirm whether specific Synthesis patchers read meshes or depend on PGPatcher output. If one does, order matters and differs from the table.
- Pandora's README gives no formal version list. Its support for 1.5.97 is implied by SE targeting and common use, not stated.

## Stock Game, profiles, version pinning and downgraded setups

### Takeaway
Stock Game (a game copy inside the MO2 folder) is the strongest pin, because Steam updates cannot reach it. Root Builder saves space and allows per-profile root files but can be broken by an update. Use profile-local saves and INIs, but check MO2's INI Editor label, since reports on that behaviour conflict.

### Cited Findings
- **[R]** Wabbajack wiki comparison: Stock Game uses about 12 GB more storage, is locked to one platform and allows only one ENB preset, but "game updates can't break it". Root Builder needs less storage and allows per-profile binaries and ENB presets, but "if the game updates, the binaries for that version may not exist anymore" — [Wabbajack, Keeping the Game Folder clean](https://wiki.wabbajack.org/modlist_author_documentation/Keeping%20the%20Game%20Folder%20clean.html)
- **[R]** Stock Game steps: copy all game files into the folder, change `GamePath=` in `Mod Organizer.ini`, and edit executable paths to the new location. For Root Builder, flag `plugins\data\RootBuilder` so Wabbajack ignores the cache — [Wabbajack, Keeping the Game Folder clean](https://wiki.wabbajack.org/modlist_author_documentation/Keeping%20the%20Game%20Folder%20clean.html)
- **[S]** A multi-version Root Builder guide runs 1.5.97 and 1.6.1170 side by side, moving stock files into a `root` folder inside a mod — [Nexus article 6682](https://www.nexusmods.com/skyrimspecialedition/articles/6682). A related 2024 guide collection covers downgrading and preventing updates — [Nexus 113681](https://nexusmods.com/skyrimspecialedition/mods/113681). Neither page was opened.
- **[S]** A user's copied 1.5.97 folder survived a Steam update to the original — [Nexus forum, stopping updates](https://forums.nexusmods.com/topic/11022483-how-to-stop-skyrim-from-updating/page/4). Generic advice is to set Steam to update only on launch — [Skyrim SE guide, workspace](https://sites.google.com/view/skyrimsemoddingguide/the-guide/setup-workspace)
- **[R]** Step 2.3 requires a clean 1.6.1170 and is not a 1.5.97 guide — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3). **[S]** Lists do still target 1.5.97, for example Secunda — [Secunda](https://sites.google.com/view/secundatheskyrimsemodlist/secunda-the-skyrim-se-1-5-97-modlist)
- **[S]** MO2 profile behaviour: Local Savegames and Local Game Settings are checkboxes in profile options. One user reports MO2 ignoring profile INIs; another reports they are used and disabling reverts to `Documents\My Games`. Another saw Local Game Settings switching itself off, with the INI Editor showing "Editing Global INIs" — [Step forum, MO2 SSE](https://stepmodifications.org/forum/topic/11805-mod-organizer-2sse-is-there-something-i-may-have-missed/); [Step forum, INI Editor](https://stepmodifications.org/forum/topic/11868-ini-editor-and-configurator-not-working); [Step forum, local saves](https://stepmodifications.org/forum/topic/11827-local-save-games/). MO2's Python API documents a per-profile game settings query — [mobase.IProfile](https://www.modorganizer.org/python-plugins-doc/api/mobase.IProfile.html)
- **[S]** Wildlander required an up-to-date Skyrim at install in a 2022 Q&A, with a downgrade afterwards for custom mods. This is old and should be verified — [r/wildlander mirror](https://cal1.lr.ggtyler.dev/r/wildlander/comments/rz4qkc/got_questions_read_me_first)

### Inferences
- For the target setup, a Stock Game copy is the simplest pin, since it keeps 1.5.97, the AE content and any cleaned masters out of Steam's reach. Launch only through MO2, with SKSE pointing into that copy.
- Keep a zipped backup of the pinned folder, because a verified download may not be able to reproduce a downgraded state.
- Set `--tesv` on Pandora whenever the managed game is not the registry path. Check that MO2's Managed Game setting points at the copy.
- A second profile with its own saves is a cheap test environment. Verify the MO2 INI Editor's label after enabling local settings, given the conflicting reports.

### Gaps
- I did not read a current MO2 primary document on profile INI handling. The forum reports are older and in conflict, so a local test on 2.5.2 is the only reliable check.
- I did not verify a current recommended downgrade path or how the patcher handles AE content.
- I did not read an authoritative procedure for stopping updates on a Steam-managed install. Nexus guide 113681 is the best lead.

## Backup, update discipline and mid-save safety

### Takeaway
Before any change: back up saves, the profile folder and any hand-made patches, then read the changelog. Lists version themselves through changelogs that state save compatibility. Assets are usually safe mid-save. Scripted mods, and removing anything baked into the save, are not. New plugins can also force LOD updates.

### Cited Findings
- **[S]** Wildlander's guidance warns some updates force a fresh playthrough and that a newly added plugin usually means a new game — [Wildlander, customising (mirror URL, 404 on redirect)](https://wildlander-mod.github.io/09-How-Do-i/ModdingGuide/). 2022 changelogs state save compatibility per version: from 1.0 a new game is needed; 1.1+ saves are safe — [Wildlander change log](https://github-wiki-see.page/m/Wildlander-mod/Support/wiki/Change-Log); [Wildlander 1.1.2 hotfix](https://www.patreon.com/posts/68087803)
- **[S]** Lorerim's readme: check the changelog and back up saves before updating — [Lorerim read-me](https://www.lorerim.com/read-me). Another list warns that manually added mods may be deleted in a Wabbajack update unless prefixed `[NoDelete]` — [Winds of the North, installation](https://colinswrath.github.io/WindsOfTheNorth/installation)
- **[S]** Viva New Vegas (FNV, as a pattern only) records mod version and load-order backup updates in a dated changelog and says existing saves cannot be used — [Viva changelog](https://vivanewvegas.moddinglinked.com/changelog.html); [Viva FAQ](https://vivanewvegas.moddinglinked.com/faq.html)
- **[R]** DynDOLOD: "a clean save should be created" when updating output from scratch or switching between PapyrusUtil and the DLL. Papyrus script changes also require a clean save before removing old scripts. A DLL-only update needs nothing else. Updating the tool or resources does not by itself require new LOD. "Only mods or plugins that are not part of the LOD patch can truly be removed without having to generate a new LOD patch". "Tree LOD easily breaks visually if the plugin load order priority changes". Partial updates exist in expert mode; if in doubt, generate from scratch — [DynDOLOD Updating](https://dyndolod.info/Updating)
- **[S]** Opinion split on removal: a Steam guide argues Skyrim bakes script data into saves and has no real removal method. Others say the risk depends on the mod, and that texture and mesh replacers and non-scripted items are generally safe, while script-heavy or quest-editing mods carry the most risk. Going back to a pre-mod save is the safe way. Load order changes shift the order for other mods. Check the mod's description for removal notes — [Nexus forum, mid-game changes](https://forums.nexusmods.com/topic/4853155-adding-mods-removing-mods-and-changing-load-order-mid-game); [Nexus forum, removing and adding](https://forums.nexusmods.com/topic/6485231-removing-and-adding-mods-mid-playthrough); [Steam discussion](https://steamcommunity.com/app/489830/discussions/0/3196992771946274852). These threads are older.
- **[R]** Step: mods updated by Bethesda need re-cleaning, and regeneration triggers apply after content changes — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)

### Inferences
**What to back up**
- `saves` (profile-local or global)
- the whole MO2 profile folder (`modlist.txt`, `plugins.txt`, `loadorder.txt`, INIs)
- personal patches
- the LOOT `userlist.yaml`
- cleaned masters and their originals
- generated output mods as zips, since LOD and PGPatcher runs are slow
- MO2's INI
- the pinned Stock Game folder once

**Personal versioning:** treat each stable state as a version: copy the profile with a date, keep a short changelog of each mod change with its reason and whether it is save-safe, and zip output mods at each release.

**Testing a change:** clone the profile, change one group at a time, regenerate only what the trigger list requires, then run the smoke test in the next section. Promote to the main profile only after it passes.

**Mid-save risk tiers** (a synthesis of the above; verify against each mod's page)

| Tier | Examples | Add | Remove or update |
|---|---|---|---|
| Usually safe | Textures, meshes, ENB presets, sound replacers, assets with no plugin | Safe | Safe, unless LOD or PGPatcher output depends on them; then update those |
| Generally safe with care | Non-scripted plugins, new items | Generally safe; update LOD or Bashed Patch as needed | Risky if items or references are already in the save |
| Risky | Script-heavy mods, MCM mods, SKSE plugins that write to the co-save, animation frameworks, followers | Check the mod page and test | Assume unsafe; use a pre-install save |
| Avoid mid-save | Quest overhauls, core skill and combat overhauls, major master or cell changes, Worldspace edits, new-land mods | New save preferred | Do not remove |
| Tool updates | DynDOLOD per the docs above, with a clean save where required | - | Follow the docs |

### Gaps
- I could not read Wildlander's current customisation page (the redirect target returned 404). Its guidance here is from a search summary and may be outdated; the changelog evidence is from 2022.
- I found no list-authored document on SPID or KID distributor additions, or a current Nolvus update policy.
- I found no reliable, current source on whether save cleaning (e.g., with Fallrim Tools) is advised. This should not be presented as safe without evidence.
- The tier table's specific categories (MCM, co-save, frameworks) are my judgment from the general pattern, not sourced lists.
- I did not read Step's own upgrade thread ([Updating from release v210](https://stepmodifications.org/forum/topic/18943-updating-from-release-v210)) or the [Skyrim Unification Project update page](https://skyrimunificationproject.github.io/01HowDoI/UpdatingModlist), both of which are leads for concrete procedures.

## Stability testing routines

### Takeaway
The best-documented routine is Step's: test a fresh build on a new character and never from an existing save, then benchmark a repeatable outdoor route. Crash logging plus a log analyser is the common diagnostic pair, but I found no documented curated-list `coc` test script, so the routine below is a proposal.

### Cited Findings
- **[R]** Step: test a fresh build by starting a new character; "don't load from a save after a fresh Guide install", to avoid false flags from save incompatibility. It benchmarks from Breezehome out to the Whiterun tundra and repeats after ENB — [Step SkyrimSE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **[S]** Community threads recommend Crash Logger SSE/AE/VR for diagnosis, plus Phostwood's web log analyser, which is reported as useful but not covering every case — [r/skyrimmods snapshot, Jun 2026](https://reddit.sentinel-team.org/posts/1tw326r/snapshots/2026-06-04T02%3A36%3A17.93282Z); [r/skyrimmods snapshot, Mar 2026](https://reddit.sentinel-team.org/posts/1rlzi6l/snapshots/2026-03-06T02%3A34%3A22.545813Z)
- **[S]** Tullius CTD Logger / SkyrimDiag: v0.2.62 and v0.2.63 crash right after launch on 1.5.97, fixed from v0.2.64; it also picks up CrashLogger logs — [Nexus 172272](https://www.nexusmods.com/skyrimspecialedition/mods/172272)
- **[S]** An AutoModerator note says crashes immediately at launch with address 05E1F22 on 1.5.97 point to a missing master or similar load-time problem — [r/skyrimmods snapshot, Jan 2026](https://reddit.sentinel-team.org/posts/1qdxgzq/snapshots/2026-01-15T23%3A31%3A11.808898Z)
- **[R]** BEES writes a log naming relevant plugins — [BEES GitHub](https://github.com/Nukem9/skyrimse-backported-esl-support)

### Inferences
**Proposed smoke test after any change (a test design, not a sourced routine)**
1. Check the BEES log, xEdit error reports for changed plugins, and LOOT warnings.
2. Start a new character on the test profile, with no prior saves.
3. From the main menu or start, load into a known exterior, then an interior via `coc`.
4. Exercise the changed feature: walk or fast travel across cell boundaries, and enter and leave a city.
5. Save, quit to desktop, reload, and confirm plugins and scripts load without warnings.
6. Check the Crash Logger folder, Papyrus logs if enabled, and MO2 Overwrite for new files.
7. Run a longer session only after the short test passes, then retest on a copy of the real save if the change is meant to be save-compatible.

For crashes: read the log's top frames and plugin list before changing anything, use an analyser as a second opinion, and bisect by group using the cloned profile. On 1.5.97, confirm the logger's version supports it before blaming the list.

### Gaps
- I found no source documenting a `coc qasmoke` routine or a specific curated-list test script. Its use is widely assumed, but this round produced no citation, so it should not be attributed to any list.
- I did not read the Crash Logger, Phostwood or Nolvus/Wildlander troubleshooting pages directly. Crash Logger's 1.5.97 compatibility for the user's exact build should be checked on its Nexus page.
- I found no source on recommended soak-test durations or quantified pass thresholds, other than Step's optional FPS guidance.
