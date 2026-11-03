# MO2 plugins and companion tools for a Skyrim SE list (MO2 2.5.2, SE 1.5.97)

Checked 2026-11-02. Scope: what exists and works on MO2 2.5.2 (Qt and PyQt 6.7.1, Python 3.12.3).

How to read the evidence:
- **Nexus was not readable.** WebFetch returned 403 and the browser stopped at a Cloudflare check, which I did not try to get past. No Nexus date, description, or compatibility note was read directly. Anything from Nexus or forums seen only through search results is labeled as a search summary or snippet, and those claims are weak.
- **Dates** come from GitHub (releases and commits, read through the API on 2026-11-02) or from the manifest files in Kezyma's repo.
- **"Works on 2.5.2" has three strengths:**
  - **Proven locally:** loaded in the user's install, shown by compiled Python 3.12 files or SKSE logs.
  - **Code evidence:** the repo imports PyQt6 and/or its release notes name 2.5 or 2.5.2. This is not a test run.
  - **Unverified:** stated as such.
- **Local evidence** refers to `C:\Modding\MO2` and was inspected read-only. Plugins with both PyQt5 and PyQt6 imports most likely use a try/except fallback, but I counted imports and did not read those files.

## Which MO2 plugins are worth having, and which work on 2.5.2?

### Takeaway
MO2 2.5.2 is still the newest stable release, so the user is not behind. Most plugins named in the brief are bundled, not chosen. The most useful additions are LOOT Warning Checker, a diff path (List Exporter and/or Load Order Library), and FOMOD reinstall help. Bethesda Plugin Manager and NIF Preview are the most interesting items I could not verify.

### Cited Findings

**MO2 itself**
- v2.5.2 was published 2024-08-04 and is the latest non-prerelease. It lists Qt and PyQt 6.7.1, Python 3.12.3, libloot 0.23.0, and usvfs 0.5.0 — [MO2 releases](https://github.com/ModOrganizer2/modorganizer/releases)
- The main repo is still active (latest master commit 2026-10-05) with no newer release — [MO2 commits](https://github.com/ModOrganizer2/modorganizer/commits/master)
- ModdingLinked's fork last released 2.5.2-ML1.5 on 2024-08-16, and its notes say "many of the previous features in this fork are now part of mainline" — [fork release](https://github.com/ModdingLinked/modorganizer/releases/tag/2.5.2-ML1.5)

**What the user's "installed plugins" actually are**
- These files all carry the same 2024-08-04 timestamp as MO2's own DLLs, which points to the stock 2.5.2 install: `DDSPreview.py`, `FNISPatches.py`, `FNISTool.py`, `FNISToolReset.py`, `Form43Checker.py`, `pyCfg.py`, `ScriptExtenderPluginChecker.py`, `bsa_extractor.dll`, `bsa_packer.dll`, `check_fnis.dll`, `diagnose_basic.dll`, `inibakery.dll`, `inieditor.dll`, `preview_bsa.dll` — local, `C:\Modding\MO2\plugins`
- Form43Checker "Checks plugins (.ESM/.ESP files) to see if any are lower than Form 44 (Skyrim SE)"; ScriptExtenderPluginChecker "Checks script extender log to see if any plugins failed to load" — local plugin source
- **Root Builder 5.1.1 is also installed but missing from the brief.** Its compiled Python 3.12 files are present, and SKSE is installed through a `Root` folder in `mods` — local (`plugins\rootbuilder`, `rootbuilder_plugin.py`, `ModOrganizer.ini`)
- Root Builder is set to copy mode (`copyfiles=**`) with hashing on — local `ModOrganizer.ini`
- FNIS Integration Tool has never been configured (`initialised=false`, empty `fnis-path`). The only FNIS-named mod is "Dyn FNIS AA functions" — local

**Ranked shortlist of additions**

| # | Plugin | What it does | Latest verified | 2.5.2 evidence | Maintenance |
|---|---|---|---|---|---|
| 1 | [LOOT Warning Checker](https://github.com/JonathanFeenstra/modorganizer-loot-warning-checker/releases) | Shows LOOT warnings as MO2 notifications without sorting | v1.4.0, 2024-08-04 | Code: release note "Add support for Mod Organizer 2.5.2 (Python 3.12)" | Dormant since release, still compatible on paper |
| 2 | [List Exporter](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugins/listexporter.json) (Kezyma) | Exports the mod list to HTML, Markdown, CSV, JSON; multi-profile; `<LE_Exclude>` tag | 2.0.0, 2026-01-07 | Code: repo tooling targets 2.5.2; manifest max is 2.5.0 | Active |
| 3 | [Load Order Library plugin](https://github.com/phinocio/loadorderlibrary-mo2-plugin/releases) | Uploads a list directly to Load Order Library, whose main feature is list comparison | v2.0.0, 2025-06-01 | Code: PyQt5 and PyQt6 imports | Maintained, low activity |
| 4 | [Reinstaller](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugins/reinstaller.json) (Kezyma) | Backs up installers and re-runs them on demand, including large FOMOD patch installers | 2.0.1 (entry dated 2024-01-16) | Code: note "(2.0.1) Update for MO2 2.5.2" | Stable, not recently updated |
| 5 | [FOMOD Plus](https://raw.githubusercontent.com/aglowinthefield/mo2-fomod-plus/main/README.md) | FOMOD installer rewrite: remembers prior choices, FOMOD filter, non-blocking window | v1.19.1, 2026-02-18 | Code: manifest min 2.5.2, builds against 2.5.2 sources | Very active (commit 2026-11-01); README calls it "barely in alpha" |
| 6 | [Remember Installation Choices](https://github.com/miere43/remember-installation-choices) | Shows previous install choices on reinstall; a lighter alternative to #5 | 1.2.4, 2025-03-28 | Unverified on 2.5.2 | Quiet |
| 7 | [Notes Panel](https://github.com/aglowinthefield/mo2-notes) | Markdown notes panel inside MO2 | v1.0.2, 2026-01-24 | Code: built against Qt 6.7 and Python 3.12 | Active |
| 8 | [MO2 Download Manager+](https://github.com/aglowinthefield/mo2-download-manager) | Batch install and delete, removes old duplicate versions, batch metadata queries | v1.8.0, 2026-01-26 | Code: PyQt5 and PyQt6 imports | Very active |
| 9 | [BodySlide Batch Builder](https://github.com/tkoopman/MO2-BodySlide-Batch-Builder) | Runs BodySlide for up to 5 groups, presets, and output mods | v2.2.0, 2026-06-05 | Code: PyQt6 imports | Active |
| 10 | [ESLifier](https://github.com/MaskPlague/ESLifier) plus its MO2 integration plugin | Finds and compacts ESL candidates and patches dependents | v0.16.17, 2026-09-07 | Code: mostly PyQt6; tool is standalone | Very active |

**ESLifier cautions**
- It needs Backported Extended ESL Support below 1.6.1130, and it warns that compacting changes Form IDs and may affect existing saves — [ESLifier README](https://raw.githubusercontent.com/MaskPlague/ESLifier/main/README.md)
- `skse64.log` shows BackportedESLSupport.dll "loaded correctly", so the prerequisite is already in place — local `Documents\My Games\Skyrim Special Edition\SKSE`

**Requested items, evaluated**
- **Root Builder:** 5.1.1, released 2026-01-09; earlier note "(5.0.5) Updates for MO2 2.5.2" — [manifest](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugins/rootbuilder.json). Proven locally. Docs were updated 2026-04-02 — [rootbuilder.md history](https://github.com/Kezyma/ModOrganizer-Plugins/commits/main/docs/rootbuilder.md)
- **Root Builder open issues (user reports):** path containing "root" (#33), performance (#38), `NoneType` error on 5.0.3 (#26), and a proposal for deployment sessions without sync-back (#51) — [issues](https://github.com/Kezyma/ModOrganizer-Plugins/issues)
- **Profile Sync:** 2.2.0, 2026-01-07, fixed "various issues that could cause the mod list for all profiles in a group to be wiped" — [manifest](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugins/profilesync.json)
- **Plugin Finder:** newest entry labeled 2.0.0, dated 2023-12-04, with notes through 2.0.1 — [manifest](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugins/pluginfinder.json). Its directory includes both current plugins and ones the MO2 wiki marks deprecated — [directory](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugin_directory.json)
- **Shortcutter:** 2.0.0, dated 2024-01-16, "Total rewrite" — [manifest](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugins/shortcutter.json)
- **Curation Club:** 1.1.0a, 2023-01-16, "Added support for MO 2.5.0"; no 2.5.2 note — [manifest](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugins/curationclub.json)
- **Local CC content:** `STOCK\Data` holds 74 `cc*` plugins and a `Skyrim.ccc`, with game exe 1.5.97.0 — local
- **Shader Cache Tool (Kezyma): not found.** It is absent from the repo's file tree including `archive/`, from the [README list](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/README.md), from the Plugin Finder directory, and from the [MO2 wiki list](https://raw.githubusercontent.com/wiki/ModOrganizer2/modorganizer/List-of-MO2-Extension-Plugins.md). A web search also found nothing
- **Merge Plugins Hide (deorder):** release 1.3 says "Only 2.5 and up is supported", and latest is 1.4, 2024-09-29, with PyQt6 imports — [releases](https://github.com/deorder/mo2-plugins/releases)
- **Sync Mod Order** ships in the same deorder repo — [README](https://raw.githubusercontent.com/deorder/mo2-plugins/master/README.md)
- **Batch Plugin Cleaner (tkoopman):** v1.3.1, 2026-07-31; manifest max 2.5.2; PyQt6. Runs xEdit Quick Auto Clean over the load order, records results to skip processed mods, and can use LOOT's masterlist — [README](https://raw.githubusercontent.com/tkoopman/MO2-Batch-Plugin-Cleaner/master/README.md), [releases](https://github.com/tkoopman/MO2-Batch-Plugin-Cleaner/releases)
- **Own plugin compared:** CleanLoadOrder also uses Quick Auto Clean and LOOT knowledge and skips unchanged plugins, and it adds a copy to `cleaning-backups` before touching a plugin — local `CleanLoadOrder.py`
- **Newer plugins, active on GitHub in 2026 but not assessed further:** [Plugin Browser](https://github.com/Pickysaurus/MO2-Plugin-Browser) v1.1.0 (2026-07-06), [MaskPlague MO2-Plugins](https://github.com/MaskPlague/MO2-Plugins) (pushed 2026-09-15), [Kodex](https://github.com/KylerNyhagen/Kodex) (pushed 2026-02-13), and [PBR Conflict Audit](https://gitlab.com/z929669/pbr-conflict-audit) (GitLab activity 2026-07-11)
- **Prolific closed listings:** alhimik.ph has 25+ wiki entries, and none list a repo — [MO2 wiki list](https://raw.githubusercontent.com/wiki/ModOrganizer2/modorganizer/List-of-MO2-Extension-Plugins.md)

**Rootbuilder alternatives**
- Root Builder itself offers Copy, Link, USVFS, and Custom modes — [rootbuilder docs](https://github.com/Kezyma/ModOrganizer-Plugins/blob/main/docs/rootbuilder.md)
- deorder's repo has a link deployment plugin "now supporting 'root' modding", described as an alpha — [release 1.3](https://github.com/deorder/mo2-plugins/releases/tag/1.3)
- Root Linker's repo is archived, last pushed 2021-12-14, even though the wiki still lists it as active — [repo](https://github.com/Vaneixus/modorganizer-rootlinker), [MO2 wiki list](https://raw.githubusercontent.com/wiki/ModOrganizer2/modorganizer/List-of-MO2-Extension-Plugins.md)

**BSA tools and conflict viewers**
- BSA extraction, packing, and preview are bundled (`bsa_extractor.dll`, `bsa_packer.dll`, `preview_bsa.dll`) — local
- BSA Extractor 2 was last pushed 2024-02-01, and 2.5.2 compatibility is unverified — [repo](https://github.com/Ryan-rsm-McKenzie/mo2-bsa-extractor-new)
- Conflict viewing is native; see the MO2 features section below
- Load Order Miner by Hymlock reportedly compares files, folders, and text inside MO2. This comes from a search summary only: page not opened, not on the MO2 wiki list, and no link recorded because the summary did not tie the claim to one URL.

### Inferences
- **Disable the three FNIS tool plugins** (`FNISTool`, `FNISPatches`, `FNISToolReset`). They appear dormant here because Pandora does the generation and no FNIS generator is installed.
- **Keep Form43Checker and ScriptExtenderPluginChecker.** Both are cheap passive checks, and the second matters on 1.5.97, where version-mismatched SKSE DLLs are a real risk.
- **pyCfg overlaps BethINI Pie** but costs nothing to leave enabled.
- **Do not replace CleanLoadOrder.** Batch Plugin Cleaner is a close match, and CleanLoadOrder's pre-clean backup is its distinguishing feature based on the two descriptions. Batch Plugin Cleaner's code is still worth reading for ideas.
- **Profile Sync and Sync Mod Order are unnecessary today** because the install has one profile (`Default`). If the user adds profiles, take Profile Sync 2.2.0 or later because of the list-wipe fixes.
- **Curation Club is only worth considering if the 74 CC plugins should be managed as mods.** Its last note is about 2.5.0, so test it on a backup first.
- **Merge Plugins Hide is unnecessary** unless the user starts merging plugins.
- **Do not recommend Shader Cache Tool.** I could not verify it exists under Kezyma's name.
- **Choose one FOMOD aid.** FOMOD Plus replaces the installer and is self-described alpha, so Reinstaller or Remember Installation Choices is the lower-risk first try.
- **Closed-source Nexus-only plugins need a higher bar**, since their code cannot be checked the way the repos above were.

### Gaps
- Nexus last-updated dates and compatibility notes for every plugin.
- [Bethesda Plugin Manager](https://github.com/Exit-9B/modorganizer-bsplugins) (v0.1.5, 2024-02-15) and [NIF Preview](https://github.com/Exit-9B/modorganizer-preview_nif) (v0.2.0, 2024-02-16) are C++ builds that predate 2.5.2. Whether they load on 2.5.2 is unverified.
- I found no expert ranking of MO2 plugins from 2025 or 2026. The ranking above is my own, based on the user's setup and on maintenance evidence.
- No plugin above was installed and test-run on this MO2 except those already present.

## Which plugins are broken or unnecessary on MO2 2.5?

### Takeaway
A PyQt5-only plugin cannot import on this install, because the bundled runtime contains only PyQt6. Age alone does not prove breakage: several plugins untouched since 2024 target 2.5.2 explicitly.

### Cited Findings
- The 2.5.0 installer wipes third-party plugins because few 2.4.4 plugins are compatible, and most Python plugins needed updates after the Qt, Python, and pybind11 changes — [MO2 releases](https://github.com/ModOrganizer2/modorganizer/releases)
- `plugins\plugin_python\libs` contains `PyQt6` and no PyQt5 — local
- "Qt no longer natively reads DDS files and the mod info image viewer will not display them", and "There are a few graphical issues due to Qt 6, particularly when using themes" — [v2.5.0 notes](https://github.com/ModOrganizer2/modorganizer/releases/tag/v2.5.0)
- A Nexus user reportedly fixed a crash log plugin by switching imports to PyQt6 and updating calls. Another user in the same search results found MO2 ignored a plugin after editing. Both are user reports from a search summary; the posts were not opened, and the likely page for the first is [Crash Log Tools posts](https://www.nexusmods.com/skyrimspecialedition/mods/66743/?tab=posts)

**Avoid or treat as obsolete**

| Item | Evidence | Status on 2.5.2 |
|---|---|---|
| [Crash Log Tools](https://github.com/Exit-9B/ModOrganizer-CrashLogTools) | v1.0.1, 2022; PyQt5 imports only; manifest max 2.4.4 | Should fail without patching (inference from code) |
| [LOOT Config Loader](https://github.com/Exit-9B/LOOTConfigLoader) | v1.0.0, 2021; PyQt5 imports only; manifest max 2.4.4 | Should fail without patching (inference from code) |
| [Root Linker](https://github.com/Vaneixus/modorganizer-rootlinker) | Archived, last pushed 2021-12-14 | Obsolete |
| [Nexus Collection Downloader](https://github.com/Furglitch/modorganizer2-nxm-collection-dl) | Archived despite release 1.3.0 on 2026-09-23 | Not for new setups; no longer developed |
| Conflict Deleter, Fix Game Registry Key, Game Redirector, LOOT Preventifier, Mappings Dumper, Requiem Redirector, Orphaned Script Extender Save Deleter | Listed under ["no longer supported"](https://raw.githubusercontent.com/wiki/ModOrganizer2/modorganizer/List-of-MO2-Extension-Plugins.md) | Avoid, even though [Plugin Finder still lists several](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugin_directory.json) |
| [Oracle](https://github.com/Levalicious/MO2-Oracle) | v0.0.0.1a, 2025-05-01; states 2.5.2 | Works on paper; experimental ML load-order toy, no reason to use it |
| [Load Order Library plugin v1.2.0](https://github.com/phinocio/loadorderlibrary-mo2-plugin/releases) | Flagged "DO NOT USE": leaks API tokens in debug logs | Use v2.0.0 |

**Stale but not proven broken**
- [Broom](https://github.com/mihaifm/broom) 1.1.1 (2024-02-19; imports both) predates 2.5.2
- [Grass Precacher](https://github.com/Al12rs/modorganizer-GrassPrecacher) (last commit 2023-06-30; imports both) predates 2.5.2. Step's 2.3 guide uses Grass Cache Helper NG for this job — [Step 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- [Master Order Checker](https://github.com/ForgottenGlory/mo2-master-order-checker) (2023-07-19; no PyQt imports found) has unverified compatibility
- [Auto-Activator](https://github.com/JonathanFeenstra/modorganizer-auto-activator) v1.0.0 (2023-09-14; last commit 2024-09-20; PyQt6)

**Kezyma distribution change**
- Commit 2026-07-03: "No longer needed now that plugins are getting removed from nexusmods." — [commits](https://github.com/Kezyma/ModOrganizer-Plugins/commits/main)
- On 2026-07-01 and 2026-07-02, Nexus URLs were removed from the Reinstaller, Plugin Finder, and Shortcutter manifests and their download links were changed — [commits](https://github.com/Kezyma/ModOrganizer-Plugins/commits/main)
- A June 2026 Reddit thread says Nexus has been pushing MO2 plugins toward its Modding Tools section and discusses a different plugin's removal (user report) — [Reddit snapshot](https://reddit.sentinel-team.org/posts/1u88kih/snapshots/2026-06-18T06%3A18%3A17.64778Z)

**Plugin Finder trap**
- Its hosted Merge Plugins Hide and Sync Mod Order entry shows version 1.1 (2020-12-21) with max support 2.4.2 — [hosted manifest](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/hosted/mergepluginhidesyncmodorder.json), while the author's current release is 1.4 — [releases](https://github.com/deorder/mo2-plugins/releases)

### Inferences
- **Get Kezyma plugins from GitHub**, because the author appears to be moving away from Nexus and Wabbajack meta files were dropped. Root Builder's own docs still link both.
- **Check manifests before using Plugin Finder installs.** At least one entry is years behind and predates the Qt 6 move, so it may install something that cannot load.
- **Check for PyQt5 first when triaging any older plugin.** A quick search of the plugin's `.py` files for `PyQt5` without a PyQt6 fallback settles most cases on this install.

### Gaps
- Whether all Kezyma pages have actually left Nexus. The commit says "getting removed", and Root Builder, Profile Sync, Curation Club, and List Exporter still carry Nexus URLs in their manifests.
- The reason for that removal is not stated in the commits I read.

## Which external tools are standard, and what is their status?

### Takeaway
All the core tools are maintained except CAO and NifSkope, which are old but not replaced by anything I could verify. The real gaps in this setup are LOD generation and save tooling. Crash Logger and Pandora are behind their latest releases.

### Cited Findings

| Tool | Latest verified | User's copy (local) | Notes |
|---|---|---|---|
| [LOOT](https://github.com/loot/loot/releases) | 0.29.2, 2026-08-16 | 0.29.2, current | Commit 2026-10-29 |
| [xEdit](https://github.com/TES5Edit/TES5Edit/releases) | GitHub tag xedit-4.1.5f, 2024-04-28 | SSEEdit.exe 4.1.5.0 | Repo commits to 2026-10-31; the file version cannot distinguish 4.1.5 letters |
| [PGPatcher](https://github.com/hakasapl/PGPatcher/releases) (formerly ParallaxGen) | 2.3.1, 2026-10-19 | 2.3.1, current | Active; Nexus file ID 120946 matches the old ParallaxGen page |
| [Pandora Behaviour Engine+](https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/releases) | v5.0.0-beta, 2026-10-01 | v4.4.0-beta, **behind** | 5.0.0 refactors FNIS animation building and adds Nemesis format conversion |
| [Crash Logger SSE](https://github.com/alandtse/CrashLoggerSSE/releases) | v1.27.0, 2026-10-25 | 1.25.0, **behind** | 1.27.0 logs game state on crash and recovers model paths |
| [BethINI Pie](https://github.com/DoubleYouC/Bethini-Pie-Performance-INI-Editor) | Last commit 2026-01-31 | Installed | No GitHub release date captured |
| [Synthesis](https://github.com/Mutagen-Modding/Synthesis/releases) | 0.36.6, 2026-08-08 | **Not installed** | Patcher pipeline for code-based mods |
| [Wrye Bash](https://github.com/wrye-bash/wrye-bash/releases) | v315, 2026-09-14 | **Not installed** | Commit 2026-10-27 |
| [DynDOLOD and xLODGen](https://dyndolod.info/) | Docs cite an August 2026 DLL update | **Not installed** | "DynDOLOD DLL NG supports 1.5.x, 1.6.x, 1.7.x"; DynDOLOD 3 labeled alpha; old versions stop working after several months |
| BodySlide | Nexus only, unverified | Installed | |
| [NifSkope](https://github.com/hexabits/nifskope/releases) | v2.0.dev9, 2023-09-23 | **Not installed** | Still the latest release I could verify |
| [Cathedral Assets Optimizer](https://www.nexusmods.com/skyrimspecialedition/mods/23316) | Unverified | **Not installed** | A search summary cites an undated forum post saying it was hidden on Nexus; post not opened |
| ReSaver (FallrimTools) | Unverified | **Not installed** | See below |
| [Phostwood's analyzer](https://phostwood.github.io/crash-analyzer/skyrim.html) | "Last updated: May 29, 2026" | Web tool | See below |

"Not installed" means no matching folder in `mods` or `TOOLS` and no executable entry in `ModOrganizer.ini` — local.

**Crash tooling on 1.5.97**
- Proven locally: `skse64.log` shows CrashLogger `01190000` (1.25) "loaded correctly" on exe 1.5.97.0 with SKSE 2.0.20, alongside EngineFixes — local. Its README names only Address Library as a user requirement and does not state version support — [README](https://raw.githubusercontent.com/alandtse/CrashLoggerSSE/main/README.md)
- Phostwood accepts Crash Logger SSE, .NET Script Framework (SE only), and Trainwreck as a backup. It warns "Not all crash issues can be detected with this tool" — [analyzer](https://phostwood.github.io/crash-analyzer/skyrim.html)
- A Quick-Link plugin reportedly opens the analyzer automatically after a crash, for Vortex and MO2 users. This comes from a search summary; the Nexus page was not opened.

**Pandora vs FNIS (user reports from 2024 to 2025, nothing dated 2026)**
- A search summary of Reddit and Steam threads has users calling Pandora actively developed and backward compatible with FNIS and Nemesis, while another says many mods remained incompatible. The threads were not opened individually; one of them is [this r/skyrimmods thread](https://lr.eu.psf.lt/r/skyrimmods/comments/1gex2lg/why_do_people_still_use_fnis_se/ludrafi/?context=3)

**ReSaver (search summaries only, treat as weak)**
- A community fork named FallrimTools-Re-Saver, by AI-Underdog, reportedly says the original stopped working after a Java 24 upgrade and offers a restored 7.28-SNAPSHOT from July 2025. A GitHub repository search for that name returned nothing, so **the fork is unverified and not recommended**.
- Users disagree on whether orphaned scripts matter; some say SKSE catches most of them. Posts not opened.

**Step baseline (older; targets a different game version)**
- Step SkyrimSE 2.3 was released 2024-08-19 and targets 1.6.1170, not 1.5.97. Its content uses BethINI Pie, LOOT, xEdit, xEditQuickAutoClean, SKSE, xLODGen, DynDOLOD and TexGen, Grass Cache Helper NG, and No Grass In Objects — [Step 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- Pandora, Synthesis, Wrye Bash, and CAO did not appear in the portion I read (first 100,000 of about 390,000 characters) — [Step 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)

### Inferences

Gaps in this setup, in priority order:
1. **Update Crash Logger to 1.27.0.** It is low risk and improves the log the user would feed into Phostwood.
2. **Add xLODGen and DynDOLOD**, provided the list changes worldspace or object content. Keep them current because old DynDOLOD versions expire.
3. **Decide on Pandora 5.0.0-beta deliberately.** It reworks FNIS handling, and this list loads `fnis_aa.dll`, so re-test animations and do not update mid-playthrough without a backup.
4. **Add Phostwood to the routine.** It costs nothing, and the user already produces Crash Logger logs.
5. **Add a leveled-list and patching tool only on demand.** Wrye Bash or Synthesis are both healthy. Neither is needed until a concrete patch need appears. CleanLoadOrder already excludes `synthesis.esp` and `Bashed Patch, 0.esp`, so it is ready for either.
6. **Add NifSkope when debugging meshes**, especially alongside PGPatcher output.
7. **ReSaver is a diagnostic to keep on hand, not a routine step.** Check Java compatibility first.
8. **Skip CAO unless it is needed** for an old mod. I could not confirm its availability.

### Gaps
- Current official ReSaver version, and its Java requirement. Nexus was unreadable.
- BodySlide's latest version and date.
- Whether Pandora 5.0.0-beta is safe with this list. Nothing tested.
- The CAO repo I checked (Guekka, 2021, 0 stars) looks like a mirror, so I did not use it as evidence of status.
- Whether Phostwood uploads logs. The page links a privacy policy that I did not read.

## Which MO2 features are underused?

### Takeaway
The user already uses custom overwrite for two tools, profile-local saves and INIs, and output mods. The next wins are routing the remaining tools the same way, cleaning Overwrite, and using conflict filters. Forced libraries are not in use, and I could not source a reason for them here.

### Cited Findings
- **Conflicts tab:** the top pane lists what a mod overrides, and you can hide a file there with `.mohidden`; the bottom pane lists what it loses to others, where hiding is not possible — [Step MO guide](https://stepmodifications.org/wiki/Guide:Mod_Organizer)
- **Filters:** presets include `<Conflicted>`, combine with And or Or, and show a red box around the list while active — [Step MO guide](https://stepmodifications.org/wiki/Guide:Mod_Organizer)
- **Data tab:** shows the virtual Data folder with each file's source, plus "Show only conflicts" — [Step MO guide](https://stepmodifications.org/wiki/Guide:Mod_Organizer)
- **Overwrite:** check it after each tool run and use Create Mod — [Step MO guide](https://stepmodifications.org/wiki/Guide:Mod_Organizer). `check_overwrite` is on here — local `ModOrganizer.ini`
- **User's Overwrite today** holds `Root` (DLSS5 screenshots, `RenoDX-DLSS5-crash.log`, `ReShade.ini.v10-backup`), `SKSE`, and `ShaderCache` — local
- **Custom overwrite:** Step 2.3 uses "Create files in mod instead of overwrite" for tool executables with dedicated output mods — [Step 2.3](https://stepmodifications.org/wiki/SkyrimSE:2.3)
- **Custom overwrite storage:** it is stored per profile. Here `profiles\Default\settings.ini` routes only Pandora and BodySlide to output mods — local
- **Forced libraries:** MO2 2.5.2's binary contains `forced_libraries` and a "Configure Libraries" string, confirming the feature exists. No `[forced_libraries]` section exists in this profile — local
- **Profile-local settings:** `LocalSaves=true`, `LocalSettings=true`, `AutomaticArchiveInvalidation=true` — local `settings.ini`. Step says profiles independently manage INIs, enabled mods, plugins, and priority — [Step MO guide](https://stepmodifications.org/wiki/Guide:Mod_Organizer)
- **Saves tab:** shows ESPs a save needs that the current profile lacks and offers "Fix Mods..." — [Step MO guide](https://stepmodifications.org/wiki/Guide:Mod_Organizer)
- **Instance vs portable:** Step says portable has "no known issues" and is generally more compatible with third-party tools, yet "highly recommends the 'instanced' configuration" — [Step MO guide](https://stepmodifications.org/wiki/Guide:Mod_Organizer)
- **User's layout:** `ModOrganizer.ini`, `mods`, and `profiles` all live under `C:\Modding\MO2`, with no `portable.txt` — local
- **Age warning:** the Step MO guide reads as old. It mentions FOMM, TES5Edit naming, and "As of version 1.2.15". Its "Have MO manage archives" text may not match 2.5.2, so I am not relying on it

### Inferences
- **Clear Overwrite.** The `Root` files are mostly tool debris, and the screenshots belong elsewhere. Run Create Mod for anything worth keeping.
- **Decide what to do with `ShaderCache`.** It appears to be Community Shaders output, since that plugin loads in this install. Regenerable caches are poor candidates for a versioned or shared mod, so leaving them in Overwrite and ignoring the warning, or moving them to a dedicated excluded output mod, are both defensible.
- **Extend custom overwrite** to SSEEdit if it creates new plugins, and check where PGPatcher writes (its executable lives inside `mods\PGPatcher`).
- **Note the profile trap.** Custom overwrites live in the profile's `settings.ini`, so a newly created profile may not carry them unless they are copied. Verify this when adding a second profile.
- **Stay with the current layout.** A single-game modlist gains nothing obvious from changing it, and Step's preference for instances is aimed at people running several builds.

### Gaps
- No current, sourced guidance on when to use forced libraries in a Skyrim SE setup. I confirmed the feature exists, not a recommended use.
- Whether archive handling in 2.5.2 still matches the Step text.
- Official MO2 documentation on these features was not found in this pass.

## Which tools track changes or diff a modlist?

### Takeaway
The simplest reliable approach is plain text under version control, since MO2's profile files are text. Load Order Library adds a shareable comparison view. Wabbajack could not be verified as a diff tool and should not be adopted for this purpose.

### Cited Findings
- Load Order Library is a support tool for Mod Organizer lists whose "premiere feature" is list comparison, showing missing or added files and differing contents. Uploads can be anonymous, and private lists are visible only by link — [API repo](https://github.com/phinocio/loadorderlibrary-api), [frontend repo](https://github.com/phinocio/loadorderlibrary-frontend)
- Its MO2 plugin v2.0.0 (2025-06-01) supports the new API — [releases](https://github.com/phinocio/loadorderlibrary-mo2-plugin/releases)
- `loadorderlibrary.com` returned HTTP 521 when I checked on 2026-11-02, so availability was not confirmed that day — [site](https://www.loadorderlibrary.com/)
- `profiles\Default` contains `modlist.txt`, `plugins.txt`, `loadorder.txt`, `lockedorder.txt`, `archives.txt`, and the profile INIs — local
- List Exporter outputs JSON, CSV, and Markdown, with column selection and an exclusion tag — [manifest](https://raw.githubusercontent.com/Kezyma/ModOrganizer-Plugins/main/directory/plugins/listexporter.json)
- Wabbajack's Compilation index describes a chapter on the full workflow for developing and deploying a modlist, and it says nothing about diffing in the part I could read — [Wabbajack wiki](https://wiki.wabbajack.org/modlist_author_documentation/Compilation.html)

### Inferences
- **Recommended stack:** keep the profile's text files in git for exact load-order diffs, add a List Exporter JSON or CSV export when mod versions and categories matter, and upload to Load Order Library at milestones when a shareable comparison is useful.
- **A caveat for git:** `modlist.txt` and `plugins.txt` capture order and state, not mod versions or file contents, which is why the export adds value. `meta.ini` files hold versions.
- **Wabbajack is a heavy way to get a diff.** Compiling is meant for distributing a list, so it only makes sense if the user plans to publish one.

### Gaps
- Whether Wabbajack compile output can be diffed usefully. Its subpages (Meta Files, Compilation Settings, CLI) were not read, to stay within budget.
- Exact Load Order Library upload steps and current site status.
