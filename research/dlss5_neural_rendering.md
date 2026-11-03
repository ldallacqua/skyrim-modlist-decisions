# DLSS 5 Neural Rendering through ReShade and RenoDX

Checked 2026-11-03. Question: how DLSS 5 Neural Rendering (NR) is set up in this list, what each file and setting does, and what to try when NR seems to do nothing. NR is NVIDIA's DLSS 5 feature that reworks the rendered image with a neural model. Skyrim has no support for it, so a ReShade add-on adds it on top of the DLSS upscale that Community Shaders already runs ([0006](../decisions/0006-community-shaders-renderer.md)).

How to read the evidence:
- **Local** means read on this machine on 2026-11-03: the mod's files with their versions and signatures, `reshade.ini`, `ModOrganizer.ini`, Root Builder's source, the Upscaling archive's file list, and Skyrim's last `ReShade.log`.
- **Add-on text** means a label, tooltip or message read from inside `renodx-dlss5.addon64`. It shows what the add-on says it does, not what was seen.
- **Conan Exiles** means tested in that game on the same RTX 4090 on 2026-11-03, by the session that swapped the runtime. It isn't Skyrim.
- Anything else is marked not verified.

## Takeaway

NR runs through ReShade and the RenoDX "DLSS5 Generic" add-on. They sit with their files in one Root Builder mod, `DLSS 5 - ReShade and RenoDX`. The add-on catches Community Shaders' DLSS upscale and runs NR on its output, through its own Direct3D 11 bridge. The runtime is ShortFuse's compat build, patched for RTX 20, 30 and 40 cards. NR starts off, and F6 turns it on.

**The compat runtime hasn't run in Skyrim yet.** The last Skyrim session was an hour before the swap, and NR was off in it. Two capture pairs from earlier that day show NR changing the image in Skyrim, on the old runtime.

If NR seems to do nothing, change the Style and the scene first. This `reshade.ini` is on Style Model A, the style that looked like no change at all in Conan Exiles.

## How a frame gets NR

1. Skyrim renders in Direct3D 11. Community Shaders' Upscaling add-on runs DLSS through NVIDIA Streamline, from 1920x1080 to 3840x2160 (local, `ReShade.log`).
2. Root Builder has copied ReShade's `dxgi.dll` and the add-on next to `SkyrimSE.exe`. ReShade loads from there and loads the add-on from the same folder (local, `ReShade.log`).
3. The add-on hooks NGX, the NVIDIA library that DLSS runs in, and leaves Streamline's own modules alone (`EnableHooks=2`, local log). The log lists three hooked copies: the driver's `_nvngx.dll` and `nvngx_dlssd.dll`, and Community Shaders' `nvngx_dlss.dll`.
4. When the game creates DLSS, the add-on records what DLSS gets: the flags IsHDR, MVLowRes and AutoExposure, a 1920x1080 render and a 3840x2160 output (local log).
5. With `DX11Source=native`, its built-in bridge serves the game's Direct3D 11 DLSS to NR, which runs on Direct3D 12 (local log, which names the bridge's mode `copy`). That NR gets a private Direct3D 12 device is the add-on's description; the log doesn't show it.
6. With `NRHookPoint=0`, NR works on DLSS's output. That's before the game's HUD, which only the Present hook point includes (add-on text).

## The mod

`DLSS 5 - ReShade and RenoDX` sits in `Shaders`, just below `Upscaling - Community Shaders` in MO2's left pane. Its MO2 note reads "Root Builder mod: ReShade and Lecram RenoDX DLSS 5". Everything is in its `Root` folder (local):

| File | What it is | File version | Signed |
|---|---|---|---|
| `dxgi.dll` | ReShade | 6.8.0.2155 | No |
| `renodx-dlss5.addon64` | RenoDX DLSS5 Generic v10.8.0, built 2026-10-20. ReShade lists it as "DLSS 5 Neural Rendering". | 0.2026.1020.1459 | No |
| `nvngx_dlssnr.dll` | The NR runtime, ShortFuse's compat build | 310.9.16 | No |
| `nvngx_dlss.dll` | DLSS upscaling | 310.8.0 | NVIDIA |
| `reshade.ini` | ReShade's settings, with the add-on's under `[RenoDX.DLSS5]` | | |
| `ReShadePreset.ini` | ReShade's effect preset. No effect is on. | | |
| `reshade-shaders` | Lilium's HDR shaders. A marker file says RenoDX Commander (RDXC) manages the folder. None is on. | | |

The mod's files land in the game folder and Upscaling's land in `Data`, so the two don't conflict.

## Root Builder

Root Builder deploys the mod. Its settings in `ModOrganizer.ini` use copy mode (`copyfiles=**`), with backup, cache and hash checks on (local).
- **At launch** it copies `Root` into `C:\Modding\STOCK`, next to `SkyrimSE.exe` ([0002](../decisions/0002-separate-stock-game-folder.md)).
- **When the game closes** it syncs, then clears. A copied file that changed goes back to the mod it came from. A new file goes to Overwrite's `Root` (local, Root Builder's `rootbuilder_builder.py`).
- **So** a setting changed in the ReShade overlay is saved back into the mod's `reshade.ini`. Screenshots go to `overwrite\Root`, which is the owner's to sort. `ReShade.log` goes back to `ROOT - Outputs\Root`, where a copy already lives.
- With the game closed, `STOCK` holds none of these files (local).

## The runtime

`nvngx_dlssnr.dll` is ShortFuse's `compat-fp16-310.9.16-cuda13.4.3`. ShortFuse posted it on the RenoDX Discord on 2026-10-16, titled "Patched DLSS-NR for RTX20, RTX30, and RTX40". It replaced a modified 310.8.0 on 2026-11-03.

| | Now | Before |
|---|---|---|
| Build | `compat-fp16-310.9.16-cuda13.4.3` | 310.8.0, modified |
| Size | 276 MB | 166 MB |
| Signature | None | NVIDIA's, but it no longer matches the file |
| sha256 | `cdfa6c1e…` | `8270b350…` |
| GPU time per frame at 4K, in Conan Exiles | About 7 ms | 10 to 12 ms |

- **Full hash** of the compat file, to check a copy: `cdfa6c1ec784867182164c7836f324f087b5c9f374d0c9fe46f54999feabf3ed` (local).
- **Why a patched build.** This PC has an RTX 4090 (local log). The post's title says the build is for RTX 20 to 40 cards. The add-on also warns about runtimes "built for GeForce RTX 50-series (Blackwell) GPUs" on older cards (add-on text). Whether NVIDIA's own build refuses this card wasn't tested.
- **Where it loads from.** The add-on looks next to itself or the game's exe (add-on text), which is where Root Builder puts it. The session that swapped the runtime also named `%LOCALAPPDATA%\DLSS5-NR\runtime` as a second place. The add-on's text names a DLSS5-NR runtime folder only for its Studio, and that folder doesn't exist here, so this isn't verified.
- **A second copy** of the same file sits in `Upscaling - Community Shaders\Shaders\Upscaling\Streamline`. It replaced an NVIDIA-signed 310.8.0 there (sha256 `e16bcf15…`).
  - The Upscaling 1.4.0 archive ships no NR runtime. Its own `nvngx_dlss.dll` is 310.5.2, while the installed one is 310.8.0 (local, archive listing). So both files were added or swapped after install, and what did it isn't recorded.
  - No Community Shaders DLL names `nvngx_dlssnr.dll` (local).
- **Which copy runs isn't known.** The last log shows an `nvngx_dlssnr.dll` loaded, but not from which folder.
- **Backups** of both 310.8.0 files are in `C:\Modding\_cleanup-backup\2026-11-03-dlssnr-compat`, under their mod paths.
- The compat build is unsigned, so only its source vouches for it.
- `nvngx_dlss.dll`, the upscaler, stays at NVIDIA's signed 310.8.0 in both mods (local).

## Settings

The add-on's settings are in `reshade.ini` under `[RenoDX.DLSS5]`. The ReShade overlay edits them under Add-ons, then DLSS 5 Neural Rendering. The overlay opens with Home (`KeyOverlay=36`).

| Setting | Value here | What it does |
|---|---|---|
| `DX11Source` | `native` | Serves the game's own Direct3D 11 DLSS through the built-in bridge (log). |
| `EnableHooks` | `2` | NGX hooks only. Streamline's modules stay unpatched (log). |
| `NRHookPoint` | `0`, After Upscaling | NR works on DLSS's output. |
| `NRResolutionScale` | `0.67` | The scale NR works at (log: `resolution_scale=0.67`). What it's a fraction of wasn't checked. |
| `NRStyle` | `0`, Model A | Which of the model's three styles NR asks for. |
| `NRToggleKey` | `117`, F6 | Turns NR on and off. |
| `NRScreenshotKey` | `116`, F5 | Saves a screenshot. |
| `NRShotKey` | `118`, F7 | Saves a capture for the Studio. Shift+F7 saves one and opens the Studio. |

**Hook points** (add-on text):
- **After Upscaling**: on DLSS's 3840x2160 output. This is the one in use.
- **Before Upscaling**: on the 1920x1080 image the game hands DLSS, against the game's own depth and motion, so NR works on fewer pixels. Where that image has a shape NR can't use, the add-on keeps the game's own DLSS image.
- **Present**: on the finished frame at the swap chain, with the game's post-processing and HUD. In a Direct3D 11 game it needs `DX11Source=native`, which is set.

**Styles** (add-on text): Model A is the runtime's own choice. Version 10.7 of the add-on called the three Default, Natural and Cinematic, so B and C are probably Natural and Cinematic. The add-on also says Models B and C may darken bright highlights, which can read as no NR there.

**Model version.** The overlay also has a Model version setting (add-on text). The session that swapped the runtime reported its choices as Default, Old and New. Its key in `reshade.ini` wasn't found.

**NR starts off.** At the start of the last session the log said NR was off, and how to turn it on: tick "Enable DLSS Neural Rendering" in the overlay, or press F6. Whether that choice survives a restart wasn't checked.

**Screenshots.** NR screenshots are saved in pairs to a `DLSS5 Screenshots` folder next to the exe: the result, and the original marked `_NR_OFF` (add-on text, and the files in Overwrite). Root Builder then moves them to `overwrite\Root`. A pair is the quickest check that NR changes anything.

**The Studio is missing.** Shift+F7 needs `Offline Studio for Neural Rendering.exe` next to the add-on (add-on text). It isn't in the mod or anywhere under `C:\Modding` (local), so the Studio can't open here.

**Settings changed since 2026-11-02.** The older `reshade.ini` in that day's backup had `NRStyle=1`, `NRIntensity=2`, `NRPreset=1` and `NRAutoMask=1`. The current one has `0`, `1`, `0` and `0`, with `ConfigVersion=10`. A `ReShade.ini.v10-backup` in Overwrite suggests the v10 add-on rewrote the file when it came in (not verified). So the list left Style 1 at intensity 2 for Model A at intensity 1, maybe without anyone choosing it.

## What Skyrim has shown

**The last session.** `ROOT - Outputs\Root\ReShade.log` is from 19:11 on 2026-11-03 (local). The runtime was swapped at 20:11, by its backup folder's time, so this session had the old 310.8.0.
- ReShade 6.8.0.2155 loaded into `SkyrimSE.exe` from `STOCK` and registered the add-on.
- The add-on took the Direct3D 11 bridge route and hooked three NGX copies.
- DLSS was created with IsHDR, MVLowRes and AutoExposure, a 1920x1080 render and a 3840x2160 output.
- The swap chain is 3840x2160 at 120 Hz in `R8G8B8A8_UNORM`, plain 8-bit output, though DLSS's input is flagged HDR.
- NR was off the whole time, with zero NR evaluations. The game ran at about 115 fps, 8.7 ms a frame, in its second 30-second window.
- Every 30 seconds the add-on writes an `NR-VERDICT` line. With NR on, its `evals` count and `ratio` show whether NR ran on the frames. That's the second check, after a screenshot pair.

**Earlier captures.** Pairs in `overwrite\Root\DLSS5 Screenshots` date from 2026-08-31, 2026-11-02 and 2026-11-03 at 00:08 and 00:12 (local).
- The two from 2026-11-03 have `.meta.txt` files that name the hook `0` and a Present capture path. In both, the NR image and the `_NR_OFF` image differ in size, so NR changed something.
- In the older pairs, both images have exactly the same size, so they show nothing either way.
- The images weren't looked at for this note.

## When NR seems to do nothing

Seen in Conan Exiles on the same RTX 4090 on 2026-11-03, not in Skyrim:
- With Style Model A in the character creator, NR on and NR off looked almost the same, though NR ran on 99.9% of frames. A pixel diff of the two showed only animation.
- Switching to Model C, and to other scenes, made the effect plain. The runtime wasn't the cause.

So, in this order:
1. Try another Style, Model C first, and another scene.
2. Then the hook point and the resolution scale.
3. Swap the runtime last. The 310.8.0 backups are kept for that.

To check, compare a screenshot pair, and read the `NR-VERDICT` lines in `ReShade.log`.

## The setup before 2026-11-02

Two backups show it (local): `C:\Modding\_cleanup-backup\2026-11-02-renodx-upgrade` and `2026-11-02-dlss5-feed`. The changelog doesn't mention it, so its reasons weren't written down.
- **A separate bridge.** `dlss5-dx11-bridge.addon64` 1.0.27 ran beside an older `renodx-dlss5.addon64`, file version 0.2026.0828.0517.
- **A synthetic feed.** `dlss5-feed.addon64` 1.19.0 describes itself as a "synthetic DLSS contract from ReShade depth + estimated motion vectors". It came with `DLSS5_Feed.fx` and LumeniteFX shaders, and with an installer record that names the method "Feeder". These sat in Overwrite's `Root`, by the backup's folder name.
- **A Ray Reconstruction DLL**, `nvngx_dlssd.dll` 310.7.129, sat in `ROOT - Outputs\Root`.
- **What replaced them.** On 2026-11-02 the v10 add-on's built-in bridge replaced the separate one. It reads the game's real DLSS inputs (local log), which the synthetic feed had stood in for, so the feed went too. The `DLSS 5 - ReShade and RenoDX` mod was made the same afternoon. The profile's `modlist.txt` backed up just before doesn't list it.
- **Leftovers.** `ReShadePreset.ini` still names the feed's and Lumenite's techniques in its sort order. No technique is on and their shaders are gone, so it should be harmless (not verified).

## Fit with this list

- **Renderer.** After Upscaling needs Community Shaders' Upscaling with DLSS on, because NR hooks that DLSS call ([0006](../decisions/0006-community-shaders-renderer.md)).
- **Game folder.** Root Builder leaves `STOCK` clean while the game is closed ([0002](../decisions/0002-separate-stock-game-folder.md)).
- **Saves.** NR only changes the image. It adds no plugin or script, so it's safe for any save.
- **Generators.** Nothing to regenerate. PGPatcher, AutoBlend and Pandora read `Data`, not these files.
- **No decision record.** A decision gets one when it's structural and expensive to reverse. This is one mod, undone by disabling it, and the runtime swap has backups.

## Not verified

- How the compat runtime looks or performs in Skyrim. The cost figures come from Conan Exiles.
- Which `nvngx_dlssnr.dll` loads: the one next to the exe, or the copy in Community Shaders' Streamline folder.
- Whether the `nvngx_dlss.dll` next to the exe is used at all. The log only shows Community Shaders' copy being hooked.
- Whether the add-on also loads the runtime from `%LOCALAPPDATA%\DLSS5-NR\runtime` in a game.
- What swapped the files in Community Shaders' Streamline folder after install.
- The Model version setting's choices and its key, and whether NR's on or off state survives a restart.
- The numbers behind the Before Upscaling and Present hook points in `reshade.ini`.
- What the add-on's crash log means. `RenoDX-DLSS5-crash.log` in Overwrite marks each Skyrim session as unclean when the next one starts. That may be Skyrim's abrupt exit rather than crashes.
- How the earlier capture pairs look.
