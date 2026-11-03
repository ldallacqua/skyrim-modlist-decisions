# Documenting and Governing Decisions While Building a Skyrim SE Modlist

Research date: 2026-11-02. Dated items are marked where a source is older than 2025. Claims from a search summary, where the page itself was not opened, are marked "(search summary)".

Note on the name "Viva": Viva New Vegas is a Fallout: New Vegas guide. I found no "Viva Skyrim". The Skyrim guide from the same organisation (ModdingLinked) is A Dragonborn's Fate (DBF), so both were examined.

## How do curated modlists document themselves, and what is widely copied versus genuinely useful?

### Takeaway
Nearly every list has a version number, a changelog and grouped sections, and the save-compatibility flag is close to universal among recent lists. The most useful practices are much rarer: a written mandate, a stated reason for each removal, and a "why not this mod" page. None of the lists inspected publish formal decision records, so that part of the repository would be new rather than copied.

### Cited Findings

**Step**
- The SE v2.3 guide was released on 2024-08-19. It requires runtime v1.6.1170, SKSE 2.2.8 and the Anniversary Upgrade, and warns that Steam updates can break builds — [Step SE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- Each mod row has a name linked to its download, a wiki link, a forum topic link, a Baseline column for the recommended option, and an Instructions column. Instructions include FOMOD choices, main and optional files, plugins to disable and files to hide — [Step SE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- Colored flags show which plugins each Step patch requires, and a separate changelog lists patch masters — [Step SE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- The changelog has layers: Post-Release Changes, Highlights, Guide-Level Changes, and Mod-Level Changes per ModGroup. Its legend defines Added, Moved, Updated (reinstall), Incorporated (now in the patch, so remove) and Dropped — [Step 2.3 changelog](https://stepmodifications.org/wiki/SkyrimSE:2.3/changelog)
- Dropped entries usually give a reason. One example says the mod is unsupported and "known to cause issues that bake into saves". Added and Updated entries do not always say why — [Step 2.3 changelog](https://stepmodifications.org/wiki/SkyrimSE:2.3/changelog)
- The changelog admits the live guide can change between releases, so it may not capture every edit — [Step 2.3 changelog](https://stepmodifications.org/wiki/SkyrimSE:2.3/changelog)
- Step publishes a mandate listing what its guides are and are not about. This is the clearest written scope I found. Last edited 2024-08-28 — [STEP:Mandate](https://stepmodifications.org/wiki/STEP:Mandate)
- Status of newer versions: the 2.4 page is marked as in development and not supported ([Step 2.4](https://stepmodifications.org/wiki/SkyrimSE:2.4), search summary). A 3.0 WIP changelog was last edited 2026-05-08 and warns it does not apply to 2.3 ([Step 3.0 changelog](https://stepmodifications.org/wiki/SkyrimSE:3.0/changelog)).

**Lexy's LOTD**
- The site has a "Current Changelog" and a "Changelog Archive". It is usually updated about monthly, and larger updates can take three or four months to plan, test and release — [Lexy's LOTD](https://lexyslotd.com/)
- It advises installing and play-testing the whole guide "AS WRITTEN" before changing anything. Modified installs get no official troubleshooting support, and it suggests a separate MO2 instance for playing — [Lexy's LOTD](https://lexyslotd.com/)
- It defines SE as 1.5.97 or later without paid Creation Club content, and AE as 1.6+ with it. The extra DLC items are not part of the guide — [Lexy's LOTD](https://lexyslotd.com/)

**Nolvus**
- The Awakening mod list is a flat table of Mod, Version and Option, grouped in numbered sections. Option is an install condition such as "Always Install", "Graphics Only" or "Nude". Version strings are not standardized — [Nolvus Awakening list](https://www.nolvus.net/awakening)
- Changelog releases use a `6.0.x` scheme. Each opens with a bold notice on whether a new game (or new install) is required, then lists changes by guide chapter. Most lines read "Added new mod X version Y" or "Mod X updated to version Y", and reasons are given only sometimes. Latest entry seen: 6.0.21, 2026-10-20, requiring a new game — [Nolvus change log](https://www.nolvus.net/appendix/history)
- A LOOT rules appendix for Ascension (v5, titled 2023, so older) tabulates which plugins load after which, with Version and guide-section columns. It also states that all mods belong to their authors and hosts no mods — [Nolvus rules](https://www.nolvus.net/appendix/rules)

**Wildlander**
- Each changelog entry has version, date (DD/MM/YY), a stability label, a "Save Safe" or "Not Save Safe. New Game Needed." label, and bullets. Latest seen: V1.1.14, dated 09/09/26, described as compatible with Skyrim update 1.7.104 — [Wildlander changelog](https://wiki.wildlandermod.com/14ModlistVersions/CHANGELOG/). An older search snippet showed V1.1.11 as latest, which appears to be a stale crawl.

**Viva New Vegas and A Dragonborn's Fate (ModdingLinked)**
- Changelog entries are grouped by year and date, carry "Safe Mid-game" or "NOT Safe Mid-game" tags, and are split by guide section with short reasons. One Viva removal cites that the mod "massively increases the conflict profile of the guide" (Aug 2025) — [Viva changelog](https://vivanewvegas.moddinglinked.com/changelog.html)
- DBF uses the same format. Its latest entry seen is 2026-10-18, and one removal cites annoying conflicts despite SkyPatcher — [DBF changelog](https://dragonbornsfate.moddinglinked.com/changelog.html)
- DBF states that it includes essential stability fixes and "no placebo/dangerous mods". It requires the English Steam or GOG release and does not support the Anniversary Edition DLC — [DBF intro](https://dragonbornsfate.moddinglinked.com/intro.html)
- Viva has a "Gameplay Mods to Avoid" page addressing why some mods are not in the guide — [Viva avoid page](https://vivanewvegas.github.io/gameplay-avoid) (search snippet only; the fetch returned 404)
- The guide lives in a public GitHub repository: HTML pages, a changelog, MIT license, 1,767 commits at time of viewing — [Viva repo](https://github.com/ModdingLinked/Viva-New-Vegas)

**Other**
- CSVO uses headings like "1.4.1 Changelog 7/16/2025 (Save Safe)". Reasons are rare. Release 1.7.0 explains that body mods were removed because they were out of scope. Latest seen: 2.3.1, 2026-08-04 — [CSVO changelog](https://inthebottle.github.io/CSVO/changelog)
- Wabbajack's author docs tell authors to write a thorough README, keep the changelog in a separate `CHANGELOG.md`, and version clearly ("Good versioning is essential") — [Wabbajack Post-Compilation](https://wiki.wabbajack.org/modlist_author_documentation/Post-Compilation.html)
- A community compatibility table lists SKSE plugin support per runtime (1.5.97, 1.6.640, 1.6.1130, 1.6.1170) — [modding.wiki SKSE plugins](https://modding.wiki/en/skyrim/users/skse-plugins) (search summary)

### Inferences

| Practice | Seen in | Assessment |
|---|---|---|
| Version number | All | Copied everywhere; needed. The number alone says little: Nolvus has new-game releases inside 6.0.x. |
| Save-compatibility flag | Nolvus, Wildlander, Viva, DBF, CSVO | Widely copied and truly useful. Keep it as a required field. |
| Changelog by section/group | Step, Nolvus, Viva, DBF | Useful once the list has stable groups. |
| Long "added X / updated X" lines | Nolvus, partly others | Common but weak. A generated diff does this better. |
| Per-mod install instructions | Step, Nolvus, Lexy | Essential for a guide others follow, overkill for a personal snapshot. Record only non-default FOMOD choices. |
| Pinned runtime stated up front | Step, DBF, Lexy (definition) | Very useful, cheap. |
| Written scope or mandate | Step (explicit), DBF (short) | Rare and very useful. It settles most later arguments. |
| Reason for each removal | Step (usually), Viva/DBF (often), Nolvus/CSVO (rare) | Valuable; this is what a decision repo should do consistently. |
| "Why not this mod" page | Viva | Rare and valuable. It stops the same evaluation being repeated. |
| Compatibility tables | Step patch flags, Nolvus LOOT table, modding.wiki | Useful only when machine-checkable or kept current. |

- The inspected lists answer "what changed" well and "why" unevenly. They almost never record the alternatives considered. That is the gap a public decision repository can fill.

### Gaps
- Lexy's changelog format is unconfirmed: the changelog pages were not retrieved. An older URL on thephoenixflavour.com returned 404.
- I could not read the Viva avoid page in full, so its entry format is unknown.
- Wildlander's "1.7.104" runtime and modding.wiki's "1.6.1179 current" ([guide 2.1.0, 03/05/2026](https://modding.wiki/en/skyrim/users/infernalryan/skyrim-initial-setup-steam/), search summary) both post-date Step's 1.6.1170 pin. I did not verify the latest Skyrim runtime, so check the actual executable version before writing the game-version decision.
- Absence of formal ADRs is based on the lists inspected, not an exhaustive survey.

## What are the established decision record formats, which fields are worth keeping, and how are superseded decisions handled?

### Takeaway
Use a trimmed MADR with Nygard's plain status handling, and add a one-line Y-statement summary to each record. Keep Context, Options, Decision, Consequences and Confirmation. Drop stakeholder fields, Jekyll navigation fields, and tooling such as Log4brains. Never delete a superseded record: change its status and link both ways.

### Cited Findings

**Nygard (2011, older but still the origin of the format)**
- Fields are title (short noun phrase with a number), Context, Decision ("We will..."), Status, and Consequences (positive, negative and neutral) — [Nygard](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- Numbers are sequential and never reused. Records stay short, ideally one or two pages, and live in the repo as lightweight markup — [Nygard](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)
- A reversed decision is kept and marked superseded so readers know it was once the decision — [Nygard](https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions)

**MADR (4.0.0, released 2024-09-17)**
- Required sections: Title, Context and Problem Statement, Considered Options, Decision Outcome ("Chosen option: ..., because ..."). Optional: Decision Drivers, Consequences, Confirmation, Pros and Cons of the Options, More Information — [MADR](https://adr.github.io/madr/)
- Confirmation records how compliance with the decision will be verified — [MADR](https://adr.github.io/madr/)
- Optional front matter: `status`, `date`, `decision-makers`, `consulted`, `informed`. The template also has Jekyll fields `parent`, `nav_order` and `title` — [MADR](https://adr.github.io/madr/)
- Files are named `NNNN-title-with-dashes.md`, lowercase, in a `decisions/` folder. Superseding is expressed as a status such as "superseded by ADR-0123". Bare and minimal templates also exist — [MADR](https://adr.github.io/madr/)

**Y-statements**
- Olaf Zimmermann introduced them at SATURN 2012 — [Zimmermann via Medium](https://medium.com/olzzio/y-statements-10eb07b5a177) (search summary; direct fetch returned 403)
- The form has an upper part ("In the context of, facing") and a lower trade-off part ("to achieve, accepting that"), with an optional "because" clause. Its stated purpose is to give decision rationale, and it suggests splitting into two or three sentences if the single sentence gets unwieldy — [Design Practice Repository](https://raw.githubusercontent.com/socadk/design-practice-repository/master/artifact-templates/DPR-ArchitecturalDecisionRecordYForm.md)

**Log4brains**
- A docs-as-code tool with local preview, CLI creation, search, a timeline and static publishing. It uses MADR by default, treats ADRs as immutable except for status, and uses date-based filenames such as `20200101-your-first-adr.md` to avoid git merge issues — [Log4brains](https://github.com/thomvaill/log4brains)
- Last push 2024-12-17, not archived, 57 open items as of this check — [GitHub API](https://api.github.com/repos/thomvaill/log4brains)

**General**
- adr.github.io defines an ADR as capturing a single decision with its rationale, plus trade-offs and consequences. It says the practice can extend beyond architecture to design decisions — [adr.github.io](https://adr.github.io/)

### Inferences

| Field | Keep? | Why |
|---|---|---|
| Number + title | Yes | Stable references from rules and changelog |
| Status | Yes | Superseding depends on it |
| Date | Yes | Modding facts age quickly |
| Y-statement summary | Yes, one sentence | Also feeds the index |
| Context | Yes, short | Include runtime and tool versions at the time |
| Options considered | Yes, even in one line each | This is what lists omit |
| Decision | Yes | |
| Consequences | Yes | Include save impact and regeneration impact |
| Confirmation | Yes | Links the record to automated rules; MADR's most useful field for this project |
| Revisit when | Add | MADR puts this under More Information; make it explicit, because mods and runtimes change |
| Evidence links | Add | Guards against repeated folklore |
| decision-makers / consulted / informed | Drop | One owner |
| Full pros and cons per option | Only for large choices | Overkill for most mod choices |
| Jekyll fields, Log4brains | Drop | GitHub renders Markdown; a generated index is enough |

- Use sequential numbers rather than dates. Log4brains' date naming solves merge conflicts between multiple authors, which a solo project lacks, and short numbers are easier to cite in rule files.
- Superseding procedure: (1) write a new record with `supersedes: [NNNN]`; (2) in the old record change only `status` and add `superseded_by`; (3) keep the file and number. A correction for a typo or broken link is allowed; a change of meaning requires a new record.
- Add statuses beyond MADR's examples: `proposed`, `accepted`, `rejected`, `deprecated`, `superseded`. A `rejected` record is a good home for large "why not" choices.
- Not every mod deserves a record. Use a record for structural choices that are costly to reverse, and a one-line entry in a catalog for routine mods (see last section).

### Gaps
- I did not read the MADR bare and minimal template text directly.
- I could not retrieve Zimmermann's full template sentence from a primary source. The commonly quoted wording ("we decided for ... and neglected ...") is from memory and unverified.

## What kinds of decisions matter for a modlist, and which criteria do curators apply when accepting a mod?

### Takeaway
Decisions that deserve records are those that constrain many later choices or require a new save or regeneration to change. Curators' published criteria come down to scope fit, stability and save safety, conflict profile, maintenance, redundancy, performance, availability and permissions. Adult-content policy differs by list, so write it down explicitly.

### Cited Findings

**Evidence of structural decisions in real lists**
- Runtime and DLC: Step exclusively supports v1.6.1170 with the Anniversary Upgrade ([Step changelog](https://stepmodifications.org/wiki/SkyrimSE:2.3/changelog)), while DBF does not support Anniversary Edition DLC ([DBF intro](https://dragonbornsfate.moddinglinked.com/intro.html)).
- Version split: SKSE DLL plugins had to be rewritten for 1.6, some were never rewritten, and a downgrade limits you to 1.5.97 DLLs — [Nexus forum](https://forums.nexusmods.com/topic/13510557-should-i-downgrade-game-version-to-1597-in-2025) (search summary; forum opinion, 2025 or earlier)
- Stock game: to be featured, Wabbajack lists must install from the latest storefront version, and manual downgrades are rejected, though the Stock Game Folder feature can handle downgrades. For Skyrim SE the base game folder must stay unmodified — [Wabbajack featured criteria](https://wiki.wabbajack.org/wabbajack_cdn_and_gallery_access/Criteria%20for%20'Featured%20Mod%20List'%20status.html)
- Patching: Bethesda lists must include custom patching, and running Synthesis or another automated patcher alone is insufficient — [Wabbajack featured criteria](https://wiki.wabbajack.org/wabbajack_cdn_and_gallery_access/Criteria%20for%20'Featured%20Mod%20List'%20status.html)
- INI tool and LOD pipeline: Step's 3.0 WIP moved from BethINI to BethINI Pie and tuned TexGen and DynDOLOD settings, and its ENB section is empty at this stage — [Step 3.0 changelog](https://stepmodifications.org/wiki/SkyrimSE:3.0/changelog)
- Pipelines named as generated output: DynDOLOD, xLODGen, TexGen, grass cache, BodySlide, Nemesis/Pandora. ParallaxGen and VRAMR are named separately — [Wabbajack featured criteria](https://wiki.wabbajack.org/wabbajack_cdn_and_gallery_access/Criteria%20for%20'Featured%20Mod%20List'%20status.html)
- Body mods as a scope question: CSVO removed them as out of scope — [CSVO changelog](https://inthebottle.github.io/CSVO/changelog)
- Master cleaning is contested. One guide calls it optional unless using DynDOLOD's large reference bugs workaround ([Nexus article](https://nexusmods.com/skyrimspecialedition/articles/6568), search summary), and Steam commenters oppose it as outdated ([Steam thread](https://steamcommunity.com/app/489830/discussions/0/4334232130644246074), search summary; attribution to this exact thread not verified).

**Acceptance criteria**
- Scope: Step's about-list covers bug fixes, PC interface improvements, consistency and new content fitting style and lore. Its not-about list covers sex, skimpy clothing or nudity, lore conflicts, departures from the vanilla style, mods needed only by a specific user base, and mods with a high performance penalty — [STEP:Mandate](https://stepmodifications.org/wiki/STEP:Mandate)
- Testing: mandate check first, then archive validation, plugin inspection in xEdit, install and uninstall checks, MO and LOOT checks, then vanilla and modded in-game testing — [STEP:Mod Testing](https://stepmodifications.org/wiki/STEP:Mod_Testing) (marked WIP, edited 2024-09-08)
- Maintenance and bugs: "Too many bugs may disqualify a mod", and ongoing author interaction is preferred as a sign it is not abandoned. Similar mods are compared to find the best solution — [STEP:Mod Testing](https://stepmodifications.org/wiki/STEP:Mod_Testing)
- Save safety and maintenance as removal reasons — [Step 2.3 changelog](https://stepmodifications.org/wiki/SkyrimSE:2.3/changelog)
- Conflict profile as a removal reason — [Viva changelog](https://vivanewvegas.moddinglinked.com/changelog.html), [DBF changelog](https://dragonbornsfate.moddinglinked.com/changelog.html)
- Redundancy, compatibility with tools, and unavailability as removal reasons — [Step LE 2.10.0 changelog](https://stepmodifications.org/wiki/SkyrimLE:2.10.0/changelog) (LE-era; search summary)
- Paid mods cannot be required by a Wabbajack list — [Wabbajack paid mods policy](https://wiki.wabbajack.org/policies_and_license/Paid%20Mods%20Policy.html) (search summary)
- Adult content: Step's intended install has no NSFW content, though linked pages may show NSFW images ([Step SE guide](https://stepmodifications.org/wiki/SkyrimSE:2.3), search summary). Nolvus exposes "Nude" only as an option value and has no adult category on its list page ([Nolvus list](https://www.nolvus.net/awakening)). DBF's introduction states no NSFW policy ([DBF intro](https://dragonbornsfate.moddinglinked.com/intro.html)).

### Inferences

**Proposed decision catalog (first records to write)**
1. Scope and mandate of the list, including adult-content policy
2. Game runtime, storefront, language and DLC/Creation Club stance
3. Stock game versus clean game folder; MO2 instance layout
4. Script extender and core frameworks
5. Update policy and save-compatibility policy
6. Character pipeline (body, BodySlide, face and NPC appearance)
7. Animation engine and behavior generation (for example Pandora or Nemesis)
8. Shader and lighting pipeline (Community Shaders or ENB; weather stack)
9. Parallax/PBR pipeline and any generated outputs
10. LOD pipeline and regeneration triggers
11. Patching strategy (hand patches, Synthesis, order of generators)
12. Plugin sort method and master-cleaning stance
13. Separator taxonomy and order
14. INI management

**Acceptance checklist for each mod** (combines the published criteria; the performance and adult fields are my extension)
- In scope under the mandate?
- Supports the pinned runtime, with correct DLL builds?
- Maintained, or if abandoned, stable and low-risk?
- Conflict profile: which records and files does it touch, and are patches available?
- Script load and save impact: can it be removed later?
- Performance cost, noted relative to the target hardware?
- Better or redundant compared with what exists?
- Still downloadable, free, and with permissions recorded where the list relies on them?
- Adult flag set, and consistent with the content policy?
- Tested in-game, with date and list version?

- Rejections should record the specific context ("rejected for this list on this date because..."), because an adverse verdict can go stale after a mod update.

### Gaps
- No published numeric performance thresholds were found. Step lists performance testing without metrics.
- Curator rationale for character, animation and shader pipelines was not found as formal documents. Pipeline names above come from change entries and rules, not design rationales.

## How should a public repository snapshot a personal list safely, and what are the licensing concerns?

### Takeaway
Publish a whitelist of plain-text list files plus derived metadata, and never publish saves, mod content, generated output, MO2's global configuration or any credentials. Referencing mods by name matches how Nexus, Wabbajack and Load Order Library already operate, but I found no ruling that specifically addresses a GitHub repository. Separately from the owner's acceptance of publicity, GitHub's policy on sexual content should be considered for adult mod names.

### Cited Findings

**File formats**
- MO2 profile folders hold text files and optionally saves. `modlist.txt` lists all mods with `+` or `-` state, `loadorder.txt` all plugins, `plugins.txt` the enabled plugins — [Step forum, MO profiles](https://stepmodifications.org/forum/topic/3420-mod-organizers-profiles-directory-technical-details) (old source)
- `plugins.txt` cannot define the positions of inactive plugins, so `loadorder.txt` is more complete — [libloadorder docs](https://docs.rs/crate/libloadorder/latest/source/doc/src/textfile_standard.md) (search summary)
- Observed locally: the owner's profile contains `modlist.txt`, `plugins.txt`, `loadorder.txt`, `lockedorder.txt`, `archives.txt`, `settings.ini`, `initweaks.ini`, the `skyrim*.ini` files and a `saves/` folder with `.ess` and `.skse` files. A search of its `.txt` and `.ini` files for drive paths, `Users\`, keys, passwords and tokens found none, while `ModOrganizer.ini` did match path or key patterns — [local profile](C:/Modding/MO2/profiles/Default)
- Observed locally: `modlist.txt` has a generated header and uses separators like `-Outputs_separator` and `-Recently Added_separator`. Output mods sit at the top of the file, consistent with top of file meaning highest priority — [local modlist.txt](C:/Modding/MO2/profiles/Default/modlist.txt)
- Observed locally: a mod's `meta.ini` has `modid`, `version`, `newestVersion`, `installationFile`, `repository`, `url`, `nexusFileStatus`, `category`, `comments` and `notes` — [local meta.ini](C:/Modding/MO2/mods/BodySlide%20and%20Outfit%20Studio/meta.ini)

**Secrets and personal data**
- MO2 stores Nexus credentials in Windows Credential Manager rather than an INI file, according to its release notes — [MO2 releases](https://github.com/ModOrganizer2/modorganizer/releases?page=4) (search summary)
- `ModOrganizer.ini` holds `gameName` and `gamePath` — [Step forum post](https://stepmodifications.org/forum/topic/12242-installing-mo2-version-2083b-inside-skyrimskyrim-se-folders-breaks-mo2/) (search summary; anecdote)
- Nexus's API policy tolerates personal keys for personal use and prohibits them in public-facing applications — [Nexus API AUP](https://help.nexusmods.com/article/114-api-acceptable-use-policy) (search summary)

**How others handle sharing**
- Wabbajack reproduces a setup "without bundling any assets or re-distributing any mods", and warns that using `WABBAJACK_INCLUDE` on downloaded mods would distribute them — [Wabbajack docs](https://wiki.wabbajack.org/modlist_author_documentation/Introduction.html) (search summary)
- It identifies archives from `.meta` files with `fileID`, `modID` and `gameName`, and treats generated output as No Match Include rather than uploaded separately — [Wabbajack Pre-Compilation](https://wiki.wabbajack.org/modlist_author_documentation/Pre-Compilation.html)
- Files you may not rehost cannot be used, including by inlining. DynDOLOD, xLODGen, TexGen, grass cache, BodySlide and Nemesis/Pandora outputs are allowed. ParallaxGen and VRAMR outputs are not and should use delta patching. Proof is required for any claimed permission — [Wabbajack featured criteria](https://wiki.wabbajack.org/wabbajack_cdn_and_gallery_access/Criteria%20for%20'Featured%20Mod%20List'%20status.html)
- Modlists produced by Wabbajack fall under CC BY-NC-SA 4.0 and may not be paywalled — [Wabbajack License](https://wiki.wabbajack.org/policies_and_license/Wabbajack%20License.html)
- Load Order Library hosts and compares lists, including `loadorder.txt`, `modlist.txt` and `plugins.txt`. Upload needs no account, private lists are link-only, and files no longer tied to a list are deleted weekly — [LOL frontend](https://github.com/phinocio/loadorderlibrary-frontend) and [a comparison page](https://loadorderlibrary.com/compare/personal-modlist-3/simplicity-of-skyrim) (search summary)

**Nexus rules**
- Collections are meta files that reference mods. "No actual mods or mod files may be included". Lists and their metadata are public domain on upload, curating gives no rights over included mods, and nobody can control whether others include their mod in a list — [Nexus Collections guidelines](https://help.nexusmods.com/article/115-guidelines-for-collections)
- Collections must not use disparaging names, misrepresent a mod, contradict an author's instructions, or place mods as trolling — [Nexus Collections guidelines](https://help.nexusmods.com/article/115-guidelines-for-collections)
- Only the original author can set a file's distribution permissions, and stated permissions are enforced — [Nexus File Submission Guidelines](https://help.nexusmods.com/article/28-file-submission-guidelines)
- Bundled collection assets are meant for tool-generated files such as DynDOLOD output, and must not be mods or mod files — [Nexus Collections guidelines](https://help.nexusmods.com/article/115-guidelines-for-collections)
- A collection with an adult mod is marked adult permanently, and curators must tag external adult resources manually — [Nexus Collections guidelines](https://help.nexusmods.com/article/115-guidelines-for-collections)

**GitHub**
- GitHub prohibits content that exists mainly to solicit an erotic or shocking response, including graphic sexual depictions in text. It may allow textual or visual depictions in artistic, educational, historical or journalistic contexts, and says a disclaimer can help explain context. It may place such content behind an opt-in — [GitHub policy](https://docs.github.com/en/site-policy/acceptable-use-policies/github-sexually-obscene-content)

### Inferences

| Item | Publish? | Notes |
|---|---|---|
| `modlist.txt`, `plugins.txt`, `loadorder.txt` | Yes | Core snapshot; same files LOL already handles |
| Separator names | Yes | Part of `modlist.txt` |
| `lockedorder.txt`, `archives.txt` | Yes, if non-empty and useful | Scan first |
| Derived `mods.csv` (name, modid, version, repository, URL) | Yes | Generate from `meta.ini`; exclude `comments` and `notes` unless reviewed |
| `skyrim.ini`, `skyrimcustom.ini`, `initweaks.ini` | Reviewed copies only | Record the intent. `skyrimprefs.ini` is largely hardware-specific; publish a diff at most |
| LOOT `userlist.yaml` | Yes | Scan first; contains order decisions |
| Patches or plugins authored by the owner | Only if entirely original | Patch files derived from others' assets need permission |
| `ModOrganizer.ini` | No | Holds local paths and settings |
| `saves/`, `.ess`, `.skse` | No | Personal and useless to others; names contain character data |
| `mods/`, `downloads/`, `overwrite/`, Stock Game, tool outputs | No | Redistribution and size |
| DynDOLOD, BodySlide, Pandora, PGPatcher outputs | No | Allowed for some Wabbajack contexts, but not needed in a git repo |
| Crash logs, screenshots | Not by default | Logs often carry user paths. Adult screenshots raise GitHub policy risk |
| API keys, cookies, `.env` | Never | Add a secret scan |

- Use a snapshot script with an explicit whitelist, not a `.gitignore`-only approach. Also ignore the dangerous folders as a second layer.
- Scan every snapshot for `[A-Z]:\\`, `Users\\`, the owner's username and key-like strings, and fail if any match.
- Publishing names and order appears low risk because it is what Nexus treats as a reference, and it matches existing public practice. Avoid copying mod descriptions, images, or FOMOD text. Treat this as practical reasoning, not legal advice.
- "Why not" notes should follow the spirit of Nexus's collection conduct rule even though the rule applies to collections: use technical reasons and evidence, and avoid attacks on authors. Do not contradict author instructions without saying so.
- Adult mods: keep names factual and do not include images or sexual descriptions. Add a short `CONTENT_NOTICE.md` explaining that the repo is modding documentation and text-only, and flag entries with `adult: true`. This is a mitigation only. Whether it satisfies GitHub's carve-outs is undetermined, so keep an offline backup of the repo.
- Suggested licensing: MIT for scripts (as Viva does), CC BY 4.0 for original documentation, and a statement that mods belong to their authors and that no license is claimed over them. If the list later becomes a Wabbajack list, revisit this because of CC BY-NC-SA 4.0.

### Gaps
- Nexus's main Terms of Service returned 403, so no clause was read directly on personal mod lists published off-site.
- I found no legal ruling or platform statement on publishing mod names and load orders on GitHub specifically.
- I did not locate a public personal repo that combines a raw MO2 snapshot with decision records, so there is no direct precedent. The closest found were Wabbajack-list repos such as [SSS](https://github.com/spacky1/SSS) (search summary).
- The local check covered one profile at one time. It must be repeated at each snapshot.

## What is a useful automated check comparing a list with its decisions, and are there precedents?

### Takeaway
No CI linter for MO2 modlists was found. LOOT's metadata is the best vocabulary to borrow from, MADR's Confirmation field gives the link back to decisions, and a small custom script of around a dozen checks would suffice. Each rule should name the decision it enforces.

### Cited Findings
- LOOT plugin metadata provides `group`, `after`, `req` (error if missing), `inc` (error if present), `msg`, `tag`, `url`, `dirty`, `clean`. Names can be regexes — [LOOT metadata](https://loot-api.readthedocs.io/en/latest/metadata/data_structures/plugin.html)
- Metadata files have top-level `prelude`, `bash_tags`, `globals`, `groups`, `plugins` — [LOOT file structure](https://loot-api.readthedocs.io/en/latest/metadata/file_structure.html)
- LOOT's editor applies Load After, Requirements and Incompatibilities with optional conditions — [LOOT editor](https://loot.readthedocs.io/en/latest/app/usage/plugin_editor.html)
- LOOT Warning Checker is an MO2 plugin that shows LOOT warnings as notifications without sorting, and can ignore warnings by regex. It runs in-app rather than in CI — [LOOT Warning Checker](https://www.github.com/JonathanFeenstra/modorganizer-loot-warning-checker) (search summary)
- Load Order Library's compare view diffs lists to see missing or added files and contents, mainly to help support — [LOL API repo](https://github.com/phinocio/loadorderlibrary-api) (search summary)
- MO2 Tracker is a VS Code syntax highlighter for `modlist.txt` and `plugins.txt`, describing separators and comments in a backup list; it does no validation — [MO2 Tracker](https://www.nexusmods.com/site/mods/2024) (search summary)
- MADR's Confirmation section records how compliance is verified — [MADR](https://adr.github.io/madr/)
- DynDOLOD output is a snapshot of the load order at generation time, and only mods outside the LOD patch can be removed without regenerating. The docs advise regenerating from scratch if in doubt — [DynDOLOD Updating](https://dyndolod.info/Updating) (search summary)
- A search for MO2 modlist CI linting found no such project. MO2's own repository CI concerns its C++ source — [MO2 workflow](https://github.com/ModOrganizer2/modorganizer/actions/runs/5500659112/workflow) (search summary)

### Inferences

**Recommended checks, in priority order**

| # | Check | Input | Severity |
|---|---|---|---|
| 1 | Secret and path scan of all tracked files | Repo | Error |
| 2 | Forbidden tracked paths or extensions (`.ess`, `.skse`, `.bsa`, `.esp` unless whitelisted, large binaries) | Git index | Error |
| 3 | Separators exist and appear in the declared order | `modlist.txt`, rules | Error |
| 4 | Staging separator (the owner's `Recently Added`) empty for a release | `modlist.txt` | Error at release, warning otherwise |
| 5 | Required mods present and enabled | `modlist.txt` | Error |
| 6 | Forbidden pairs not both enabled | `modlist.txt`, `plugins.txt` | Error |
| 7 | Mod priority rules (A above B) | `modlist.txt` | Error |
| 8 | Plugin order rules and group expectations | `loadorder.txt` | Error |
| 9 | Each mod sits in its declared separator | `modlist.txt`, catalog | Warning |
| 10 | Every enabled mod has a catalog entry; no rejected mod is enabled | Catalog | Warning, then error |
| 11 | Decision integrity: valid status, supersede links match both ways, rules do not cite superseded records, accepted records with `confirmation: auto` have a rule | `decisions/`, rules | Error |
| 12 | List changed without a `CHANGELOG.md` entry; release lacks a save-safety flag | Git diff | Error at release |
| 13 | Generated-output freshness: LOD, behavior or body outputs older than the last relevant mod change | Manifest | Warning |
| 14 | Optional: run LOOT masterlist warnings as an in-app check | MO2 | Advisory |

**Implementation details that will matter**
- Parse the `modlist.txt` first-line header as a comment, and read lines as `+`/`-`/`*`. Normalize line endings: a `_separator$` search against the local file found nothing, which suggests CRLF.
- Remember that MO2 stores `modlist.txt` in reverse order relative to the left pane. State this in the rule semantics, or convert everything to "priority" terms to avoid mistakes.
- Encoding: an older source says `plugins.txt` used local 8-bit encoding ([Step forum](https://stepmodifications.org/forum/topic/3420-mod-organizers-profiles-directory-technical-details), old), so detect encoding rather than assume UTF-8.
- GitHub CI can only validate the snapshot, not the live install. Run the snapshot and check together locally, and rerun the check in CI.
- Do not reimplement LOOT sorting. Check only rules that encode the owner's decisions.

**Rule file example** (`rules/list-rules.yaml`):

```yaml
version: 1
separators:
  order: [Foundation, Frameworks, Fixes, Visuals, Character, Animation, Adult, Patches, Outputs]
  staging: Recently Added
required:
  - name: "SKSE - Outputs"
    decision: 4
forbidden_pairs:
  - a: "Example Mod A"
    b: "Example Mod B"
    decision: 12
    reason: "Both replace the same behavior graph."
mod_order:
  - higher: "Example Patch"
    lower: "Example Mod A"
    decision: 11
plugin_order:
  - after: "DynDOLOD.esp"
    load_after: "Synthesis.esp"
    decision: 10
```

The names above are placeholders apart from the structure itself; real rules should be written from the owner's accepted decisions.

### Gaps
- The absence of a linter is based on limited search, so a small private or niche tool may exist.
- I did not verify a headless LOOT CLI for CI use. Treat CI integration with LOOT as unconfirmed.
- I did not check the current DynDOLOD docs page directly, only a search summary.

## What do experienced curators consider the most common mistakes?

### Takeaway
No authoritative "top mistakes" list was found. The points below are assembled from curators' documents and support forums, in descending confidence. Most can be turned into a decision or a check.

### Cited Findings

**Stronger evidence (curator documentation or tool authors)**
- Treating generated output as permanent: LOD is a snapshot of the load order at generation, so removals inside the LOD patch require regeneration — [DynDOLOD Updating](https://dyndolod.info/Updating) (search summary)
- Modifying a list before confirming the base works: Lexy advises testing "AS WRITTEN" and declines official support for modified installs — [Lexy's LOTD](https://lexyslotd.com/)
- Chasing updates during a playthrough: Lexy suggests a separate MO2 instance for playing — [Lexy's LOTD](https://lexyslotd.com/). Curators flag many updates as new-game-only or not mid-game safe — [Nolvus change log](https://www.nolvus.net/appendix/history), [DBF changelog](https://dragonbornsfate.moddinglinked.com/changelog.html)
- Ignoring the runtime: Step warns that Steam updates can break builds — [Step SE 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- Adding mods with save-baking or abandoned behavior: Step dropped one for that — [Step 2.3 changelog](https://stepmodifications.org/wiki/SkyrimSE:2.3/changelog)
- Overlooking conflict cost: Viva and DBF removed mods for conflict profile alone — [Viva changelog](https://vivanewvegas.moddinglinked.com/changelog.html), [DBF changelog](https://dragonbornsfate.moddinglinked.com/changelog.html)
- Installing placebo or dangerous fixes: DBF's stated avoidance — [DBF intro](https://dragonbornsfate.moddinglinked.com/intro.html)
- Relying on automated patching alone: Wabbajack does not accept Synthesis alone as patching for featured status — [Wabbajack featured criteria](https://wiki.wabbajack.org/wabbajack_cdn_and_gallery_access/Criteria%20for%20'Featured%20Mod%20List'%20status.html)
- Leaving stale downloads and old versions: Wabbajack tells authors to delete them, since they can cause wrong archive matches — [Wabbajack Pre-Compilation](https://wiki.wabbajack.org/modlist_author_documentation/Pre-Compilation.html)
- Scope creep: CSVO removed body mods as out of scope, which also simplified use for others — [CSVO changelog](https://inthebottle.github.io/CSVO/changelog)

**Weaker evidence (forum moderators and users, some older)**
- Removing mods from a live save: a Step forum moderator says you cannot generally disable mods mid-playthrough and continue the same save — [Step forum](https://stepmodifications.org/forum/topic/12119-adding-a-mod-and-not-re-running-dyndolod/) (search summary; exact thread attribution not verified)
- Wrong DLL builds: DLL dependencies mismatched to the game version cause crashes — [Nexus forum](https://forums.nexusmods.com/topic/13510557-should-i-downgrade-game-version-to-1597-in-2025) (search summary; exact thread attribution not verified)
- Debugging by disabling LOD plugins or meshes is described by Step staff as wrong or outdated advice — [Step forum](https://stepmodifications.org/forum/topic/14591-skyrim-se-ctd-before-main-menu-when-dyndolod-enabled/) (search summary; exact thread attribution not verified)

### Inferences

| Mistake | Repository control |
|---|---|
| No stated scope | Decision 0001 and acceptance checklist |
| Unknown runtime | Runtime decision and `MANIFEST.json`; check against it |
| Regenerating outputs inconsistently | Pipeline decision with triggers; freshness warning |
| Undocumented removal | Changelog reason required; catalog status |
| Same mod re-evaluated repeatedly | `mods/rejected.md` with date and revisit trigger |
| Mid-save changes | Save-safety field on every release |
| Unnoticed conflicts | Order and pair rules linked to decisions |
| Everything added at once | Staging separator, small commits, a test note per batch |

### Gaps
- "Start small and test incrementally", "learn xEdit" and "pick a central concept first" recur in r/skyrimmods mirrors returned by search, but I could not tie them to a specific verifiable post. Treat as anecdotal.
- I found no quantitative data on the frequency of any mistake, and no 2026 curator survey.
- Advice not to blindly clean ITMs on LOOT's prompt appeared in Steam guides, but its attribution could not be verified and the question is contested.

## What should the repository contain: layout, record template and naming?

### Takeaway
A small repository with six parts is enough: policy, decisions, a mod catalog, generated list snapshots, machine-checkable rules, and a changelog. Records explain why, rules enforce it, snapshots show the current state, and the changelog connects them over time.

### Cited Findings
- Precedents for this structure: `decisions/` naming ([MADR](https://adr.github.io/madr/)), separate README and `CHANGELOG.md` ([Wabbajack](https://wiki.wabbajack.org/modlist_author_documentation/Post-Compilation.html)), written mandate ([Step](https://stepmodifications.org/wiki/STEP:Mandate)), save-safe flags ([Wildlander](https://wiki.wildlandermod.com/14ModlistVersions/CHANGELOG/)), a public docs repo with workflows ([Viva](https://github.com/ModdingLinked/Viva-New-Vegas))

### Inferences

**Directory layout**

```text
<list-name>/
  README.md               # scope, status, runtime, how to read, how to reproduce
  CHANGELOG.md            # one section per list release
  CONTENT_NOTICE.md       # text-only adult-mod notice
  LICENSE                 # MIT for tools/
  LICENSE-docs            # CC BY 4.0 for original docs
  .gitignore
  .gitattributes
  policy/
    mandate.md            # what the list is and is not about
    acceptance.md         # checklist from this document
    update-policy.md      # save safety, cadence, runtime updates
  decisions/
    README.md             # generated index with status + Y-statement
    template.md
    0000-record-decisions-in-this-repo.md
    0001-define-list-scope-and-adult-policy.md
    0002-pin-game-runtime.md
    ...
  mods/
    catalog.yaml          # one entry per mod: why it is here
    rejected.md           # why not, with date and revisit trigger
    patches.md            # owner-authored patches and their permissions
  list/                   # generated only; never edit by hand
    modlist.txt
    plugins.txt
    loadorder.txt
    mods.csv
    MANIFEST.json         # snapshot time, runtime, SKSE, MO2, tool versions, list version
  rules/
    list-rules.yaml
  tools/
    snapshot.py           # whitelist copy, normalize, scan
    check_list.py         # the checks above
    build_index.py
  .github/workflows/
    check.yml
```

**Naming conventions**
- Decisions: `NNNN-short-action-phrase.md`, lowercase English with dashes, numbers never reused: `0007-use-pandora-for-behavior-generation.md`. Name them after the choice, or after the question while still proposed, and let the title reflect both problem and outcome.
- Release versions: `MAJOR.MINOR.PATCH`, git tags `list-v1.4.0`. Suggested meaning: MAJOR means a new game is required or the foundation changes; MINOR means save-safe content changes; PATCH means fixes and regenerated output. Keep the explicit save flag anyway.
- Commits: `list:`, `decision:`, `rules:`, `tools:` prefixes, with `Refs: 0007` where relevant.

**Decision record template** (`decisions/template.md`)

```markdown
---
id: 0000
title: Short title with problem and choice
status: proposed        # proposed | accepted | rejected | deprecated | superseded
date: YYYY-MM-DD        # last status change
area: runtime           # scope | runtime | framework | character | animation | shaders | lod | patching | order | selection | tooling
supersedes: []
superseded_by: null
list_version: null      # first list release containing it
save_impact: none       # none | new-game-recommended | new-game-required
confirmation: auto      # auto | manual | none
revisit_when: "Example: SKSE or a key DLL mod updates for a new runtime"
---

# 0000. Short title

**Summary.** In the context of <situation>, facing <concern>, we chose <option> over
<alternatives>, to achieve <goal>, accepting <downside>.

## Context
What forced this decision. Include versions and dates of relevant tools and mods.
Keep this factual.

## Options considered
- **Option A**: one line on the main benefit and cost.
- **Option B**: one line.
- **Do nothing**: when realistic.

## Decision
We will use Option A because ...

## Consequences
- Good: ...
- Bad: ...
- Required upkeep: regeneration, patches, order constraints, save impact.

## Confirmation
Rules in `rules/list-rules.yaml` that cite this ID, or a manual test
(what was done, where in-game, on which list version).

## Evidence
- Links to mod pages, docs, xEdit findings, or test notes.
```

**Catalog entry** (`mods/catalog.yaml`, for routine mods that do not need a record)

```yaml
- name: "Example Mod"
  nexus_id: 12345
  separator: Visuals
  status: active          # active | testing | dropped
  added: 2026-11-02
  reason: "Fixes X, chosen over Y."
  decision: 8             # optional link
  adult: false
  removal_safe: unknown   # yes | no | unknown
  notes: "Non-default FOMOD: option Z."
```

**Rejected entry** (`mods/rejected.md`)

```markdown
## Example Mod (rejected 2026-11-02, list 0.3.0)
- Reason: conflicts with the chosen weather stack; no patch available.
- Evidence: <link or short test note>
- Revisit when: an update or compatibility patch appears.
```

**Changelog entry**

```markdown
## 1.4.0 (2026-11-02), Save safe: no (new game required)
Runtime: <exact version>. Decisions: 0012 accepted; 0005 superseded by 0012.
### Added / Removed / Moved / Updated
- Removed Example Mod: unmaintained and bakes data into saves.
### Regenerate
- LOD, behavior.
```

Step's categories (Added, Moved, Updated, Incorporated, Dropped) are worth adopting. A generated diff can fill the mod names, leaving the human to write only reasons.

**Governance workflow**
1. Add a new mod under the staging separator, with a catalog entry marked `testing`.
2. If it changes a structural choice, write or supersede a decision record first.
3. Test in-game, then move it to its final separator and mark it `active`, or record it in `rejected.md`.
4. Regenerate outputs as the pipeline decisions require.
5. Run `snapshot.py` and `check_list.py`, then commit list, catalog, rules and changelog together.
6. Tag a release with a save-safety flag when the build has been played.

**.gitignore baseline**

```gitignore
# Second layer only: the snapshot script's whitelist is the main control.
mods/*/
!mods/catalog.yaml
!mods/rejected.md
!mods/patches.md
downloads/
overwrite/
profiles/
saves/
*.ess
*.skse
*.bsa
*.ba2
*.7z
*.zip
*.rar
ModOrganizer.ini
nxmhandler.ini
.env
*.log
```

Simplification notes: start with ten or so records and the first five checks. If `catalog.yaml` feels like too much at first, require reasons only for mods added after the repo's start date, and backfill as mods are touched.

### Gaps
- This layout is a synthesis from the sources above, not a tested community standard. No equivalent public example was found.
- `nxmhandler.ini` is listed from general MO2 knowledge, not verified in a source. `.gitignore` patterns should be adjusted once the repo sits in its final relation to the MO2 folder; the safest arrangement is keeping the repo outside the MO2 directory entirely.
