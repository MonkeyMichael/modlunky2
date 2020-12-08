from pathlib import Path

KNOWN_FILEPATHS = [
    # Fonts
    "Data/Fonts/fontdebug.fnb",
    "Data/Fonts/fontfirasans.fnb",
    "Data/Fonts/fontmono.fnb",
    "Data/Fonts/fontnewrodin.fnb",
    "Data/Fonts/fontrodincattleya.fnb",
    "Data/Fonts/fontyorkten.fnb",
    # Level Files
    "Data/Levels/abzu.lvl",
    "Data/Levels/Arena/dm1-1.lvl",
    "Data/Levels/Arena/dm1-2.lvl",
    "Data/Levels/Arena/dm1-3.lvl",
    "Data/Levels/Arena/dm1-4.lvl",
    "Data/Levels/Arena/dm1-5.lvl",
    "Data/Levels/Arena/dm2-1.lvl",
    "Data/Levels/Arena/dm2-2.lvl",
    "Data/Levels/Arena/dm2-3.lvl",
    "Data/Levels/Arena/dm2-4.lvl",
    "Data/Levels/Arena/dm2-5.lvl",
    "Data/Levels/Arena/dm3-1.lvl",
    "Data/Levels/Arena/dm3-2.lvl",
    "Data/Levels/Arena/dm3-3.lvl",
    "Data/Levels/Arena/dm3-4.lvl",
    "Data/Levels/Arena/dm3-5.lvl",
    "Data/Levels/Arena/dm4-1.lvl",
    "Data/Levels/Arena/dm4-2.lvl",
    "Data/Levels/Arena/dm4-3.lvl",
    "Data/Levels/Arena/dm4-4.lvl",
    "Data/Levels/Arena/dm4-5.lvl",
    "Data/Levels/Arena/dm5-1.lvl",
    "Data/Levels/Arena/dm5-2.lvl",
    "Data/Levels/Arena/dm5-3.lvl",
    "Data/Levels/Arena/dm5-4.lvl",
    "Data/Levels/Arena/dm5-5.lvl",
    "Data/Levels/Arena/dm6-1.lvl",
    "Data/Levels/Arena/dm6-2.lvl",
    "Data/Levels/Arena/dm6-3.lvl",
    "Data/Levels/Arena/dm6-4.lvl",
    "Data/Levels/Arena/dm6-5.lvl",
    "Data/Levels/Arena/dm7-1.lvl",
    "Data/Levels/Arena/dm7-2.lvl",
    "Data/Levels/Arena/dm7-3.lvl",
    "Data/Levels/Arena/dm7-4.lvl",
    "Data/Levels/Arena/dm7-5.lvl",
    "Data/Levels/Arena/dm8-1.lvl",
    "Data/Levels/Arena/dm8-2.lvl",
    "Data/Levels/Arena/dm8-3.lvl",
    "Data/Levels/Arena/dm8-4.lvl",
    "Data/Levels/Arena/dm8-5.lvl",
    "Data/Levels/Arena/dmpreview.tok",
    "Data/Levels/babylonarea_1-1.lvl",
    "Data/Levels/babylonarea.lvl",
    "Data/Levels/basecamp_garden.lvl",
    "Data/Levels/basecamp.lvl",
    "Data/Levels/basecamp_shortcut_discovered.lvl",
    "Data/Levels/basecamp_shortcut_undiscovered.lvl",
    "Data/Levels/basecamp_shortcut_unlocked.lvl",
    "Data/Levels/basecamp_surface.lvl",
    "Data/Levels/basecamp_tutorial.lvl",
    "Data/Levels/basecamp_tv_room_locked.lvl",
    "Data/Levels/basecamp_tv_room_unlocked.lvl",
    "Data/Levels/beehive.lvl",
    "Data/Levels/blackmarket.lvl",
    "Data/Levels/cavebossarea.lvl",
    "Data/Levels/challenge_moon.lvl",
    "Data/Levels/challenge_star.lvl",
    "Data/Levels/challenge_sun.lvl",
    "Data/Levels/cityofgold.lvl",
    "Data/Levels/cosmicocean_babylon.lvl",
    "Data/Levels/cosmicocean_dwelling.lvl",
    "Data/Levels/cosmicocean_icecavesarea.lvl",
    "Data/Levels/cosmicocean_jungle.lvl",
    "Data/Levels/cosmicocean_sunkencity.lvl",
    "Data/Levels/cosmicocean_temple.lvl",
    "Data/Levels/cosmicocean_tidepool.lvl",
    "Data/Levels/cosmicocean_volcano.lvl",
    "Data/Levels/duat.lvl",
    "Data/Levels/dwellingarea.lvl",
    "Data/Levels/ending_hard.lvl",
    "Data/Levels/eggplantarea.lvl",
    "Data/Levels/ending.lvl",
    "Data/Levels/generic.lvl",
    "Data/Levels/hallofushabti.lvl",
    "Data/Levels/hundun.lvl",
    "Data/Levels/icecavesarea.lvl",
    "Data/Levels/junglearea.lvl",
    "Data/Levels/lake.lvl",
    "Data/Levels/lakeoffire.lvl",
    "Data/Levels/olmecarea.lvl",
    "Data/Levels/palaceofpleasure.lvl",
    "Data/Levels/sunkencityarea.lvl",
    "Data/Levels/templearea.lvl",
    "Data/Levels/testingarea.lvl",
    "Data/Levels/tiamat.lvl",
    "Data/Levels/tidepoolarea.lvl",
    "Data/Levels/vladscastle.lvl",
    "Data/Levels/volcanoarea.lvl",
    # Textures
    "Data/Textures/base_eggship2.DDS",
    "Data/Textures/base_eggship3.DDS",
    "Data/Textures/base_eggship.DDS",
    "Data/Textures/base_skynight.DDS",
    "Data/Textures/base_surface2.DDS",
    "Data/Textures/base_surface.DDS",
    "Data/Textures/bayer8.DDS",
    "Data/Textures/bg_babylon.DDS",
    "Data/Textures/bg_beehive.DDS",
    "Data/Textures/bg_cave.DDS",
    "Data/Textures/bg_duat2.DDS",
    "Data/Textures/bg_duat.DDS",
    "Data/Textures/bg_eggplant.DDS",
    "Data/Textures/bg_gold.DDS",
    "Data/Textures/bg_ice.DDS",
    "Data/Textures/bg_jungle.DDS",
    "Data/Textures/bg_mothership.DDS",
    "Data/Textures/bg_stone.DDS",
    "Data/Textures/bg_sunken.DDS",
    "Data/Textures/bg_temple.DDS",
    "Data/Textures/bg_tidepool.DDS",
    "Data/Textures/bg_vlad.DDS",
    "Data/Textures/bg_volcano.DDS",
    "Data/Textures/border_main.DDS",
    "Data/Textures/char_black.DDS",
    "Data/Textures/char_blue.DDS",
    "Data/Textures/char_cerulean.DDS",
    "Data/Textures/char_cinnabar.DDS",
    "Data/Textures/char_cyan.DDS",
    "Data/Textures/char_eggchild.DDS",
    "Data/Textures/char_gold.DDS",
    "Data/Textures/char_gray.DDS",
    "Data/Textures/char_green.DDS",
    "Data/Textures/char_hired.DDS",
    "Data/Textures/char_iris.DDS",
    "Data/Textures/char_khaki.DDS",
    "Data/Textures/char_lemon.DDS",
    "Data/Textures/char_lime.DDS",
    "Data/Textures/char_magenta.DDS",
    "Data/Textures/char_olive.DDS",
    "Data/Textures/char_orange.DDS",
    "Data/Textures/char_pink.DDS",
    "Data/Textures/char_red.DDS",
    "Data/Textures/char_violet.DDS",
    "Data/Textures/char_white.DDS",
    "Data/Textures/char_yellow.DDS",
    "Data/Textures/coffins.DDS",
    "Data/Textures/credits.DDS",
    "Data/Textures/deco_babylon.DDS",
    "Data/Textures/deco_basecamp.DDS",
    "Data/Textures/deco_cave.DDS",
    "Data/Textures/deco_cosmic.DDS",
    "Data/Textures/deco_eggplant.DDS",
    "Data/Textures/deco_extra.DDS",
    "Data/Textures/deco_gold.DDS",
    "Data/Textures/deco_ice.DDS",
    "Data/Textures/deco_jungle.DDS",
    "Data/Textures/deco_sunken.DDS",
    "Data/Textures/deco_temple.DDS",
    "Data/Textures/deco_tidepool.DDS",
    "Data/Textures/deco_tutorial.DDS",
    "Data/Textures/deco_volcano.DDS",
    "Data/Textures/floor_babylon.DDS",
    "Data/Textures/floor_cave.DDS",
    "Data/Textures/floor_eggplant.DDS",
    "Data/Textures/floor_ice.DDS",
    "Data/Textures/floor_jungle.DDS",
    "Data/Textures/floormisc.DDS",
    "Data/Textures/floorstyled_babylon.DDS",
    "Data/Textures/floorstyled_beehive.DDS",
    "Data/Textures/floorstyled_duat.DDS",
    "Data/Textures/floorstyled_gold_normal.DDS",
    "Data/Textures/floorstyled_gold.DDS",
    "Data/Textures/floorstyled_guts.DDS",
    "Data/Textures/floorstyled_mothership.DDS",
    "Data/Textures/floorstyled_pagoda.DDS",
    "Data/Textures/floorstyled_palace.DDS",
    "Data/Textures/floorstyled_stone.DDS",
    "Data/Textures/floorstyled_sunken.DDS",
    "Data/Textures/floorstyled_temple.DDS",
    "Data/Textures/floorstyled_vlad.DDS",
    "Data/Textures/floorstyled_wood.DDS",
    "Data/Textures/floor_sunken.DDS",
    "Data/Textures/floor_surface.DDS",
    "Data/Textures/floor_temple.DDS",
    "Data/Textures/floor_tidepool.DDS",
    "Data/Textures/floor_volcano.DDS",
    "Data/Textures/fontdebug.DDS",
    "Data/Textures/fontfirasans.DDS",
    "Data/Textures/fontmono.DDS",
    "Data/Textures/fontnewrodin.DDS",
    "Data/Textures/fontrodincattleya.DDS",
    "Data/Textures/fontyorkten.DDS",
    "Data/Textures/fx_ankh.DDS",
    "Data/Textures/fx_big.DDS",
    "Data/Textures/fx_explosion.DDS",
    "Data/Textures/fx_rubble.DDS",
    "Data/Textures/fx_small2.DDS",
    "Data/Textures/fx_small3.DDS",
    "Data/Textures/fx_small.DDS",
    "Data/Textures/hud_controller_buttons.DDS",
    "Data/Textures/hud.DDS",
    "Data/Textures/hud_text.DDS",
    "Data/Textures/items.DDS",
    "Data/Textures/items_ushabti.DDS",
    "Data/Textures/journal_back.DDS",
    "Data/Textures/journal_elements.DDS",
    "Data/Textures/journal_entry_bg.DDS",
    "Data/Textures/journal_entry_items.DDS",
    "Data/Textures/journal_entry_mons_big.DDS",
    "Data/Textures/journal_entry_mons.DDS",
    "Data/Textures/journal_entry_people.DDS",
    "Data/Textures/journal_entry_place.DDS",
    "Data/Textures/journal_entry_traps.DDS",
    "Data/Textures/journal_pageflip.DDS",
    "Data/Textures/journal_pagetorn.DDS",
    "Data/Textures/journal_select.DDS",
    "Data/Textures/journal_stickers.DDS",
    "Data/Textures/journal_story.DDS",
    "Data/Textures/journal_top_entry.DDS",
    "Data/Textures/journal_top_gameover.DDS",
    "Data/Textures/journal_top_main.DDS",
    "Data/Textures/journal_top_profile.DDS",
    "Data/Textures/loading.DDS",
    "Data/Textures/lut_backlayer.DDS",
    "Data/Textures/lut_blackmarket.DDS",
    "Data/Textures/lut_icecaves.DDS",
    "Data/Textures/lut_original.DDS",
    "Data/Textures/lut_vlad.DDS",
    "Data/Textures/main_body.DDS",
    "Data/Textures/main_dirt.DDS",
    "Data/Textures/main_doorback.DDS",
    "Data/Textures/main_doorframe.DDS",
    "Data/Textures/main_door.DDS",
    "Data/Textures/main_fore1.DDS",
    "Data/Textures/main_fore2.DDS",
    "Data/Textures/main_head.DDS",
    "Data/Textures/menu_basic.DDS",
    "Data/Textures/menu_brick1.DDS",
    "Data/Textures/menu_brick2.DDS",
    "Data/Textures/menu_cave1.DDS",
    "Data/Textures/menu_cave2.DDS",
    "Data/Textures/menu_chardoor.DDS",
    "Data/Textures/menu_charsel.DDS",
    "Data/Textures/menu_deathmatch2.DDS",
    "Data/Textures/menu_deathmatch3.DDS",
    "Data/Textures/menu_deathmatch4.DDS",
    "Data/Textures/menu_deathmatch5.DDS",
    "Data/Textures/menu_deathmatch6.DDS",
    "Data/Textures/menu_deathmatch.DDS",
    "Data/Textures/menu_disp.DDS",
    "Data/Textures/menu_generic.DDS",
    "Data/Textures/menu_header.DDS",
    "Data/Textures/menu_leader.DDS",
    "Data/Textures/menu_online.DDS",
    "Data/Textures/menu_titlegal.DDS",
    "Data/Textures/menu_title.DDS",
    "Data/Textures/menu_tunnel.DDS",
    "Data/Textures/monsters01.DDS",
    "Data/Textures/monsters02.DDS",
    "Data/Textures/monsters03.DDS",
    "Data/Textures/monstersbasic01.DDS",
    "Data/Textures/monstersbasic02.DDS",
    "Data/Textures/monstersbasic03.DDS",
    "Data/Textures/monstersbig01.DDS",
    "Data/Textures/monstersbig02.DDS",
    "Data/Textures/monstersbig03.DDS",
    "Data/Textures/monstersbig04.DDS",
    "Data/Textures/monstersbig05.DDS",
    "Data/Textures/monstersbig06.DDS",
    "Data/Textures/monsters_ghost.DDS",
    "Data/Textures/monsters_hundun.DDS",
    "Data/Textures/monsters_olmec.DDS",
    "Data/Textures/monsters_osiris.DDS",
    "Data/Textures/monsters_pets.DDS",
    "Data/Textures/monsters_tiamat.DDS",
    "Data/Textures/monsters_yama.DDS",
    "Data/Textures/mounts.DDS",
    "Data/Textures/noise0.DDS",
    "Data/Textures/noise1.DDS",
    "Data/Textures/OldTextures/ai.DDS",
    "Data/Textures/saving.DDS",
    "Data/Textures/shadows.DDS",
    "Data/Textures/shine.DDS",
    "Data/Textures/splash0.DDS",
    "Data/Textures/splash1.DDS",
    "Data/Textures/splash2.DDS",
    # Shaders
    "shaders.hlsl",
    # FMOD Audio
    "soundbank.bank",
    "soundbank.strings.bank",
    # Strings
    "strings00.str",
    "strings01.str",
    "strings02.str",
    "strings03.str",
    "strings04.str",
    "strings05.str",
    "strings06.str",
    "strings07.str",
    "strings08.str",
]

# Mapping of filenames to their file paths
# Example: {'splash1.DDS': 'Data/Textures/splash1.DDS'}
FILENAMES_TO_FILEPATHS = {Path(path).name: path for path in KNOWN_FILEPATHS}

# Most of the textures convert cleanly to .png but not all of them.
# This is the list of assets we want to convert to/from png.
PNGS = set(
    asset
    for asset in KNOWN_FILEPATHS
    if asset.endswith(".DDS")
    and asset
    not in [
        "Data/Textures/bayer8.DDS",
        "Data/Textures/fontdebug.DDS",
        "Data/Textures/fontfirasans.DDS",
        "Data/Textures/fontmono.DDS",
        "Data/Textures/fontnewrodin.DDS",
        "Data/Textures/fontrodincattleya.DDS",
        "Data/Textures/fontyorkten.DDS",
    ]
)


# Mapping of png file names to DDS file names
# Example: {'monstersbig06.png': 'monstersbig06.DDS'}
PNG_NAMES_TO_DDS_NAMES = {
    str(Path(filepath).with_suffix(".png").name): str(Path(filepath).name)
    for filepath in KNOWN_FILEPATHS
    if filepath in PNGS
}

EXTRACTED_DIR = Path("Extracted")
PACKS_DIR = Path("Packs")
OVERRIDES_DIR = Path("Overrides")

FILEPATH_DIRS = [
    Path(path).parent for path in KNOWN_FILEPATHS if Path(path).parent != Path(".")
]

DEFAULT_COMPRESSION_LEVEL = 20
BANK_ALIGNMENT = 32
