# Playbook

The rules in force, on one page. Each rule links to the decision that explains it.

## Structure

1. **Name separators by function and don't number them.** Priority comes from the line's position in `modlist.txt`, not the name, and numbers drift. ([0003](decisions/0003-function-based-unnumbered-separators.md))
2. **Keep both ends fixed and let conflicts decide the middle.** Foundation and fixes go on top; tools, patches, outputs and the inbox go at the bottom. In the middle, function gives the name and conflict priority gives the position. When they disagree, priority wins. ([0003](decisions/0003-function-based-unnumbered-separators.md))
3. **Add a separator only when a section needs it.** The list averages under 6 mods per section, so there's nothing to split today. ([0003](decisions/0003-function-based-unnumbered-separators.md))
4. **New mods land in the inbox, and it's last and empty at release.** ([0012](decisions/0012-inbox-separator-last.md))
5. **Keep the Nexus name on mods.** Use the Notes field for why a mod is there and which FOMOD options were picked.

## Patches

6. **A patch for one mod sits right below that mod.** A patch linking mods from different sections goes in a late `Patches` section, created when the first one appears. ([0009](decisions/0009-hybrid-patch-placement.md))
7. **A conflict isn't a defect by itself.** Act when the winner drops something you want: a keyword, a script, a navmesh, or an NPC and FaceGen pair. ([0009](decisions/0009-hybrid-patch-placement.md))

## Plugins

8. **Start from LOOT and write every exception down as LOOT metadata.** The next sort discards anything dragged by hand. ([0010](decisions/0010-loot-with-metadata.md))
9. **Sort, generate, enable the output, sort again, and read the end of the list.** ([0010](decisions/0010-loot-with-metadata.md))
10. **Clean with backups, and judge LOOT's warnings against your own masters.** LOOT's counts belong to a specific set of masters. ([0011](decisions/0011-clean-plugins-with-backups.md))
11. **Budget 254 full plugins and 4096 light ones.** BEES enables the extended ESL range on 1.5.97; it doesn't raise the count. Don't compact plugins without a concrete need, because it changes Form IDs. ([0001](decisions/0001-pin-skyrim-se-1597-with-cc.md))

## Generated files

12. **Each generator writes to its own mod, at the end of the pane.** That makes it possible to delete and rebuild any one of them. ([0007](decisions/0007-one-output-mod-per-generator.md))
13. **Set the output in the tool, following its documentation.** MO2's "create files in mod" only catches new files; existing files are changed at their source. ([0008](decisions/0008-configure-outputs-in-the-tool.md))
14. **Disable an output before regenerating it,** so the tool doesn't read its own result. ([0007](decisions/0007-one-output-mod-per-generator.md))
15. **Run in dependency order:** LOOT and personal patches, BodySlide, Pandora, optional Wrye Bash and Synthesis, LOOT, xLODGen, AutoBlend, PGPatcher, TexGen, DynDOLOD. No source states this whole sequence; it's combined from each tool's documentation. ([0007](decisions/0007-one-output-mod-per-generator.md))
16. **Keep Overwrite empty.** Whatever lands there gets a home or gets deleted. ([0007](decisions/0007-one-output-mod-per-generator.md))

## Safety

17. **Back up what can't be downloaded again:** saves, the profile folder, personal patches, LOOT's `userlist.yaml`, cleaned masters and their originals, and a zip of the pinned game folder. ([0002](decisions/0002-separate-stock-game-folder.md))
18. **Test on a cloned profile with a new character:** `coc` to an exterior and an interior, save, quit, reload, then read the logs and Overwrite. This routine is our own design; no list documents it. ([0002](decisions/0002-separate-stock-game-folder.md))
19. **Mark every version as save-safe or not.** Assets are usually safe mid-save; removing scripted mods is risky. See the [changelog](CHANGELOG.md).

## This repository

20. **Publish by whitelist.** Only `tools/snapshot.py`'s listed files and fields leave the machine. ([0013](decisions/0013-public-snapshot-by-whitelist.md))
21. **Run `python tools/check.py` before committing.** Each check cites the decision it enforces.
22. **Never delete a decision.** Mark it superseded and link the replacement.
