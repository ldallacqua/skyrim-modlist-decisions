# Agent guide

Read this before working here. It says what the project is, how the owner likes to work, where things live on the machine, how to do the common jobs, and what has gone wrong before. Update "Where things stand" at the end of every session.

## What this is

The owner plays a personal Skyrim SE modlist through Mod Organizer 2. This repository keeps the list's reasoning next to the list itself:

- `research/` holds what the best lists and tool authors do.
- `decisions/` holds the structural choices, with the options considered and what would reopen each one.
- `PLAYBOOK.md` holds the rules in force.
- `list/` is a snapshot of the real MO2 profile, and `tools/check.py` checks it against `rules/rules.json`.

The repository is public on GitHub, and `site/` publishes it as a browsable site.

The job is usually one of these: research a mod choice, install and order mods, run the generators, check logs, and record what changed.

## Working with the owner

- **Language:** they write in Portuguese or English. Reply in their language. The repository is written in English, in plain, short sentences, like the existing files.
- **Research comes first.** For a new area (PBR, trees, plants), survey what Wabbajack lists install and what authors say, write a note in `research/` and recommend. Install after they agree. Within an agreed install, they expect you to read each mod's description, pick installer options, and install every requirement without asking about each one.
- **Downloads and money:** they have Nexus Premium. A download beyond what they asked for needs their OK. Their personal API key is saved in Windows Credential Manager as `nexusmods-api-key`, and `tools/nexus.py` reads it from there. Never print it, and never write it to a file. If they hand over a new key, save it with `nexus.py store-key`.
- **Hands off:** never touch `overwrite/Root` in MO2, which holds their own screenshots and DLSS and ReShade files. Commit or push only when asked. AutoBlend has no command line, so ask them to click "Start Patching".
- **Report honestly:** what was verified, what wasn't, and what hasn't been seen in game.

## The machine

| Path | What it is |
|---|---|
| `C:\Modding\MO2` | Portable MO2 2.5.2. Profile `Default`, with local saves and INIs. |
| `C:\Modding\MO2\mods\<name>` | One folder per mod; `meta.ini` holds its Nexus ids and notes. |
| `C:\Modding\MO2\downloads` | Archives, each with a `.meta` file MO2 reads. |
| `C:\Modding\MO2\profiles\Default` | `modlist.txt`, `plugins.txt`, `loadorder.txt` and the profile's INIs. |
| `C:\Modding\STOCK` | The game MO2 runs: Skyrim SE 1.5.97 with SKSE 2.0.20 ([0001](decisions/0001-pin-skyrim-se-1597-with-cc.md), [0002](decisions/0002-separate-stock-game-folder.md)). The Steam install is a separate 1.7.104 copy; never point a tool at it. |
| `C:\Modding\TOOLS` | LOOT 0.29.2, SSEEdit, Bethini. |
| `%LOCALAPPDATA%\LOOT` | LOOT's `settings.toml` and its masterlist under `games\Skyrim Special Edition`. |
| `C:\Modding\clean-load-order-mo2`, `C:\Modding\ardosia-mo2` | The owner's MO2 plugin and theme, separate repositories. |

MO2's executables, by the title used to launch them: `Skyrim Special Edition`, `SKSE`, `skse64_loader`, `LOOT`, `PGPatcher`, `AutoBlend`, `Pandora Behaviour Engine+`, `BodySlide`, `SSEEdit`, `SSEEditQuickAutoClean`, `Bethini`, `Explore Virtual Folder`.

## Tools in this repository

All are standard-library Python except `terrain_to_pbr.py` and `terrain_depth.py`, which need numpy. Run them from the repository root with `python -X utf8`.

| Script | Use |
|---|---|
| `tools/snapshot.py "C:\Modding\MO2" Default` | Refresh `list/` from the profile. Never edit `list/` by hand. |
| `tools/check.py` | Check `list/` against the rules, and the repository for secrets and mod files. Run before committing. |
| `tools/wabbajack.py` | Count which published Wabbajack lists install a mod. This is the main evidence for research. |
| `tools/nexus.py` | Search Nexus, read a mod's files, requirements and description, and download files into MO2 with their `.meta`. |
| `tools/fomod.py` | Show a FOMOD installer's options, and install with explicit choices. |
| `tools/coverage.py` | Show which vanilla assets still look vanilla in the profile, and how much candidate Nexus files would replace, without downloading them. |
| `tools/mo2.py` | Install a download into a mod folder, add separators, place mods, turn mods on and off, enable plugins, set an executable's arguments, read plugin headers, find file conflicts, check download flags, and confirm PGPatcher's inputs. |
| `tools/road_debris.py` | Build `Northern Roads - Road Debris.esp`: sparse pebbles and small rocks on Northern Roads' dirt road textures. Tune the mix in its table, or `--scale` every density, then run it again with the game closed. |
| `tools/terrain_depth.py` | Stretch each winning PBR ground height map around its own average toward `--target` relief, into `Terrain Depth - Outputs`. Its first output (target 0.09, gain up to 3) smeared TomatoRim's ground in game and is disabled. Needs numpy and Texconv. |
| `tools/terrain_to_pbr.py` | Turn an ENB complex parallax landscape texture into a Community Shaders PBR set, matched to the brightness of the PBR texture it replaces. It uses Texconv from SSEEdit's scripts folder. |
| `tools/mo2-run.ps1` | Run a tool through MO2 with nobody at the keyboard: LOOT sorts, PGPatcher regeneration, or any executable with temporary arguments. |

Each script's docstring has its full usage. The scripts that write to MO2 read `MO2_DIR` and `MO2_PROFILE`, and refuse to write profile files while MO2 is open.

## How to do the common jobs

### Research a mod choice

1. Find candidates with `python tools/nexus.py search <words>`, and see what lists actually use with `python tools/wabbajack.py count "<regex>"`. Lists that also use Community Shaders matter most, since this list uses it ([0006](decisions/0006-community-shaders-renderer.md)). For visual mods, `python tools/coverage.py "<regex>" --candidate <mod>:<file>` measures what still looks vanilla and what each candidate would replace.
2. Read each candidate's description with `nexus.py description <id>` and requirements with `nexus.py info <id>`. Check fit with what's installed: Community Shaders and PBR, 1.5.97 builds of SKSE plugins, and DynDOLOD support, because LOD will be generated later.
3. Write `research/<topic>.md`. [`research/pbr_trees_and_grass.md`](research/pbr_trees_and_grass.md) is the model: takeaway first, evidence tables, candidates, fit with this list, recommendation, then what wasn't verified. Mark claims as verified or not.

### Install mods

1. `python tools/nexus.py files <mod id>` to pick files, then `python tools/nexus.py get <mod>:<file> ...`. It uses the stored key. Big files download in parallel parts, and every file is checked by MD5.
2. Read the description, then `python tools/mo2.py install "<Nexus mod name>" --mod <id> --version <v> --part <file id>`. If the archive has a FOMOD, it prints the options and stops. Run it again with `--part "<file id>:Group=Option;Step/Group=Option"`. The choices go into the mod's MO2 notes.
3. Close MO2. Then `python tools/mo2.py place "<separator>" "<mod>" ...` in the order the authors ask, and `python tools/mo2.py enable-plugins "<mod>" ...`.
4. Sort with `tools\mo2-run.ps1 -Sort`, and check conflicts with `mo2.py conflicts <mods> --all`. Then run the generators. For PGPatcher, `tools\mo2-run.ps1 -RegeneratePGPatcher` disables its output, runs it, re-enables the output and its plugins, sorts again, and checks its inputs.
5. Refresh the snapshot, run the checks, and add the change to `CHANGELOG.md`. Add a new separator to `rules/rules.json` too.

### Run a tool through MO2 without the interface

Use `tools\mo2-run.ps1`, with MO2 closed:

| Command | What it does |
|---|---|
| `-Sort` | LOOT auto-sort |
| `-RegeneratePGPatcher` | The full PGPatcher cycle |
| `-Title <executable> -Arguments '<args>'` | Any MO2 executable |

What it does underneath, for when something goes wrong:
- **Launch:** it starts `ModOrganizer.exe "moshortcut://:<title>"`, which runs the tool inside MO2's virtual file system and exits MO2 when the tool closes.
- **Arguments:** they live in `ModOrganizer.ini` as `<n>\arguments=` under `[customExecutables]`. `mo2.py exe-args` sets them for the run and restores them, but only after MO2 has exited, because MO2 saves its settings on exit.
- **LOOT:** it sorts with `--game="Skyrim Special Edition" --auto-sort` and its masterlist update off (`mo2.py loot-update`).
- **PGPatcher:** it runs with `--autostart`.
- **Leftover windows:** PGPatcher's "Generation Complete" and LOOT's "Sorting made no changes" each wait for OK, and the script clicks it through UI Automation.

### After any generator or game run

- Read the tool's log: PGPatcher's is in its mod folder under `PGPatcher\log`, AutoBlend's in `AutoBlend - Outputs`, Pandora's in `Pandora - Outputs`.
- Check that Overwrite holds nothing but `Root`. Move anything else to its home ([0007](decisions/0007-one-output-mod-per-generator.md)):
  - tool settings into the tool's own mod;
  - caches and generated files into their `- Outputs` mod.
- After PGPatcher, run `python tools/mo2.py pgpatcher-check`.

## Pitfalls already hit

- **MO2 rewrites the profile on exit.** Edit `modlist.txt`, `plugins.txt`, `loadorder.txt` or `ModOrganizer.ini` only while it's closed.
- **`modlist.txt` is upside down.** The first line is the highest priority, and a separator's line comes after its own mods.
- **The `installed` flag in a download's `.meta` is also the end of `uninstalled`.** A plain text replace once flipped both and made MO2 show 25 installed archives as Uninstalled. `mo2.py` anchors to the line start.
- **LOOT's masterlist update can time out and leave an empty `masterlist.yaml`.** Restore it with:

  ```
  curl -o masterlist.yaml https://raw.githubusercontent.com/loot/skyrimse/v0.29/masterlist.yaml
  ```

  Then sort with the update turned off.
- **MO2 asks whether to start Steam** before running some tools, which blocks a launch nobody is watching. `[DialogChoices]` in `ModOrganizer.ini` stores "no" for LOOT, PGPatcher and AutoBlend.
- **A Nexus CDN link's `md5=` signs the link.** It isn't the file's hash. `nexus.py` checks the real MD5 against Nexus's `md5_search`.
- **Tools that find the game through the registry open the Steam copy.** SSEEdit once cleaned a plugin there. Pass the data folder explicitly (SSEEdit `-D:`), or check the tool's settings.
- **Tools whose executable lives inside a mod write their settings into Overwrite.** PGPatcher writes `PGPatcher\cfg` and `PGPatcher\log`, AutoBlend writes `AutoBlend\settings.json`, and Pandora writes `Settings.json`. Move them into the tool's mod.
- **PGPatcher refuses to run while `PGPatcher - Outputs` is enabled.** It shows a critical error instead. Disable the output first, as playbook rule 14 says. `mo2-run.ps1 -RegeneratePGPatcher` does that.
- **A run script must stop if its setup fails.** Once, a failed preparation step still launched LOOT, with normal settings and its masterlist update on. Check the exit code before launching anything.
- **PGPatcher's output replaces 81 BodySlide meshes.** After rebuilding BodySlide, run PGPatcher again. After changing landscape mods, run AutoBlend and then PGPatcher.
- **Nature of the Wild Lands - Nordic Cut needs a new game.**
- **Python on this machine:** run anything that reads downloaded files with `-I` from a folder of your own. Python 3.11 can't open paths over 260 characters, such as deep scratch folders.
- **Windows answers in Portuguese here.** `tasklist`'s "no tasks" message isn't valid UTF-8, which crashed `mo2.py`'s check that MO2 is closed until it learned to replace undecodable bytes.
- **Git Bash's `sed -i` turns CRLF into LF.** The profile's INIs use CRLF, so edit them in Python, in binary mode.
- **PGPatcher's "Generation Complete" OK is a pane, not a button.** UI Automation finds it but can't click it. `mo2-run.ps1` now closes that window with `WindowPattern.Close()`, which lets MO2 exit; a full unattended run on 2026-11-03 went through with it. If a run still stops, close the window that way and finish by hand: `mo2.py exe-args PGPatcher --set=`, enable `PGPatcher - Outputs` and its plugins, `-Sort`, then `mo2.py pgpatcher-check`.
- **Some archives unpack read-only folders.** Northern Roads' Patch Collection did, and `mo2.py install` stopped while cleaning up staging, before writing `meta.ini`. It now clears the flag.
- **LOOT may meet a rule by moving the wrong plugin.** A rule only says "after". Re-run the overlap check after every sort that follows a new rule.
- **Non-PBR road and terrain retextures show nothing here.** The PBR road plugins point Northern Roads' texture sets at `textures\pbr\`, so files at the old path never load, and Community Shaders can't draw non-PBR terrain next to PBR ground anyway. PGPatcher won't convert them, because it patches meshes, not terrain. Convert them with `terrain_to_pbr.py` into a texture-only mod above the PBR road files.
- **Texconv weights colour by alpha when it builds mips.** An albedo with alpha 0 came out with a fine full-size level and every mip below it black. In game, that showed as a black road at a distance and dark patches up close. Keep alpha opaque, and check every mip, not just the top one; `terrain_to_pbr.py` does both.
- **Raising a ground texture's `displacementScale` also lifts its average height.** Community Shaders' height blending weighs layers by `(height - 0.5) * displacementScale`, so the ground then swallows the edges of the layers beside it. Stretching the height map around its average avoids that, but TomatoRim's maps smeared when stretched 1.6 to 3 times: they hold surface detail, not real height. Leave TomatoRim's ground at its defaults.
- **PBR Hub's Northern Roads copies of the stone spikes and Reach bridges use the vanilla mountain slab texture.** PGPatcher then gave them TomatoRim's whole-mountain material, which looked furry and smeared on them. They're hidden in MO2 so the Patches Compendium meshes win, which PBR Hub's own spike and bridge PBR textures fit. A PBR Hub reinstall brings them back.
- **Bethini's window mode switches Community Shaders' Frame Generation on.** CS 1.9.1 ships Frame Generation on, but it needs windowed mode, so exclusive fullscreen hid it. Bethini's borderless setting brought it out, with a Direct3D 12 proxy swap chain, and the RenoDX DLSS 5 add-on stopped seeing DLSS. Bethini's own game path also points at the Steam copy, though it writes the profile's INIs when launched through MO2.
- **Installer instructions can fight this list.** Lux CS asks for its Orbis plugin after every Orbis patch, but here that undid their cell fixes. Check record overlaps before writing a LOOT rule an author asks for.

## Where things stand

Updated 2026-11-03.

- **PBR visual set:** installed on 2026-11-03 and seen in game, and the owner reports it working well. See the changelog and [the research](research/pbr_trees_and_grass.md). AutoBlend and PGPatcher ran cleanly after it.
- **Plants:** the kit from [research/plants.md](research/plants.md) was installed on 2026-11-03 in a new `Plants` separator, followed by a PGPatcher run and a LOOT sort. It hasn't been seen in game yet. The changelog lists every installer choice.
- **Lighting and weather:** installed on 2026-11-03 in a new `Lighting & Weather` separator, from [research/lighting.md](research/lighting.md) and [research/weather.md](research/weather.md). That's Lux, Lux Orbis and Lux Via with their patch hubs and Lux CS, CS Light, Embers XD, Obsidian with Obsidian CS, and Moons and Stars, plus Light Placer and ISL Helper SKSE. AutoBlend and PGPatcher ran cleanly after it. It hasn't been seen in game yet. The changelog lists every installer choice, the meshes removed from Lux and Lux Orbis, and the list's first LOOT rules.
- **Open from the lighting install:**
  - Three Lux Via lantern posts point at meshes that don't exist. Look for them near Whiterun and Riften in game.
- **In game, after lighting:** set Merethic's grass brightness in Community Shaders' Grass Lighting menu (0.70 to 0.95, depending on the weather), and ISL Helper's sliders in SKSE Menu Framework. Then look at interiors, towns at night, storms and snow.
- **Roads:** Northern Roads replaced Blended Roads on 2026-11-03, from [research/roads.md](research/roads.md), with its two patch packs, three fixes, and PBR Hub's and TomatoRim's PBR road textures. Nordic Cut's Northern Roads, Lux Via and Lux patches went in too. AutoBlend and PGPatcher ran cleanly after it. The owner has seen it in game and likes it. Blended Roads is still disabled but kept. On 2026-11-03 the main dirt road became a PBR conversion of Omen Apollo's complex parallax texture, for a rougher look. That's `Northern Roads - Omen Apollo Dirt PBR (converted)`, explained in the roads note's last section. Its first test showed black mips, since fixed; the owner saw it after the fix and liked the depth, but not the edge with the ground. Its `displacementScale` is 1.0.
- **Open from the roads install:** four references where Nordic Cut's Lux Via patch beats the Northern Roads one (Skyrim.esm 0C3936 and 0C3937, Lux Via.esp 0009AD). Also check the bridges (Solitude, Dragon Bridge, Lux Via's, and the Reach bridges since their fix) and the stone spike pillars.
- **Road edges and debris:** researched on 2026-11-03 in [research/road_edges_and_debris.md](research/road_edges_and_debris.md), and decided in [0015](decisions/0015-keep-tomatorim-ground-and-northern-roads.md): TomatoRim's ground and Northern Roads stay. `Northern Roads - Road Debris` (built by `tools/road_debris.py`) puts sparse pebbles and small rocks on the dirt roads; the owner saw it and found the edge better. The road's depth went to 0.5 and back: at 0.5 it looked flat. Deepening the ground with `tools/terrain_depth.py` smeared it in game, so `Terrain Depth - Outputs` is disabled, and the owner asked for default values: the ground is TomatoRim's as shipped, and the road keeps the 1.0 of TomatoRim's own files. The road at 1.0 with the debris hasn't been seen in game. Next, after a look: tune the debris with `--scale`; only if the edge still bothers the owner, measure Vanaheimr's PBR heights, which needs a 0.77 GB download the owner hasn't approved.
- **DynDOLOD:** planned once the visuals settle. The research plans xLODGen terrain, then TexGen and DynDOLOD Ultra with Nature of the Wild Lands' 3D hybrid LOD add-on, and a decision then on caching grass for grass LOD (which would reopen [0014](decisions/0014-extended-grass-without-cache.md)). Each generator needs its own output mod.
- **Pandora's arguments are empty.** Its MO2 executable no longer has the `-o`/`--tesv` arguments that [0008](decisions/0008-configure-outputs-in-the-tool.md) describes. Its own `Settings.json`, now in its mod folder, still sends output to `Pandora - Outputs` and reads the game from `STOCK`. Ask the owner which setup they intend before changing either.
- **DLSS 5 Neural Rendering:** it runs through ReShade and RenoDX again, with CS Frame Generation off (`frameGenerationMode=0`). The owner uses NVIDIA Smooth Motion for frame generation instead. See [the DLSS 5 note](research/dlss5_neural_rendering.md#frame-generation-with-this-route).
  - Seen in game on 2026-11-04, and the owner calls it perfect. The setup is Smooth Motion with VSync in the NVIDIA control panel, VSync off in SSE Display Tweaks, and borderless windowed. `ReShade.log` shows `api=d3d11 path=bridge` and `state=ENGAGED`. Keep CS Frame Generation off.
  - Community Shaders Neural Rendering Addon 1.2.1 was tried and fails its own version check on 1.5.97. It's kept disabled, with its runtime mod.
  - The owner's HDR - Community Shaders, Effects 11 and PI-CHO ENB are all disabled.
  - Bethini's other changes (grass fade 4096, particles 2000) weren't reverted.
- **Overwrite:** only `Root` is left, and it's the owner's to sort.
- **Nexus API key:** a new key was saved in Credential Manager on 2026-11-03, replacing the one pasted earlier.
- **Site:** it deploys by hand, with `npm run deploy` in `site/`, after a commit.
