﻿## This file contains some of the options that can be changed to customize your Ren'Py game. It only contains the most common options... there is quite a bit more customization you can do.
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment them. Lines beginning with a single '#' mark are commented-out code, and you may want to uncomment them when appropriate.
         
init -1 python hide:
    ## Should we enable the use of developer tools? This should be set to False before the game is released, so the user can't cheat using developer tools.
    config.developer = True

    ## These control the width and height of the screen.
    config.screen_width = 1024
    config.screen_height = 576

    ## This controls the title of the window, when Ren'Py is running in a window.
    config.window_title = u"Renpy Imagebuttons GUI Sample"
    
    ## These control the name and version of the game, that are reported with tracebacks and other debugging logs.
    config.name = "Renpy Imagebuttons GUI Sample"
    config.version = "1.0"

    #########################################
    # Themes
    ## We then want to call a theme function. themes.roundrect is a theme that features the use of rounded rectangles. It's the only theme we currently support.
    ## The theme function takes a number of parameters that can customize the color scheme.

    theme.roundrect(
        ## Theme: Roundrect
        ## Color scheme: Cotton Candy                                    
        ## The color of an idle widget face.
        widget = "#ECC7D0",
        ## The color of a focused widget face.
        widget_hover = "#E1D4C9",
        ## The color of the text in a widget.
        widget_text = "#805C40",
        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#805C40",
        ## The color of a disabled widget face. 
        disabled = "#C8AFA1",
        ## The color of disabled widget text.
        disabled_text = "#E1D4C9",
        ## The color of informational labels.
        label = "#805C40",
        ## The color of a frame containing widgets.
        frame = "#FCF5F2",
        ## The background of the main menu. This can be a color beginning with '#', or an image filename. The latter should take up the full height and width of the screen.
        mm_root = "#D0B4BA",
        ## The background of the game menu. This can be a color beginning with '#', or an image filename. The latter should take up the full height and width of the screen.
        gm_root = "#D0B4BA",
        ## If this is True, the in-game window is rounded. If False, the in-game window is square.
        rounded_window = False,
        ## And we're done with the theme. The theme will customize various styles, so if we want to change them, we should do so below.            
        )
        
    #########################################
    ## These settings let you customize the window containing the dialogue and narration, by replacing it with an image.
    ## The background of the window. In a Frame, the two numbers are the size of the left/right and top/bottom borders, respectively.
    style.window.background = Frame("gui/frame.png", 0, 0)

    ## Margin is space surrounding the window, where the background is not drawn.
    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6

    ## Padding is space inside the window, where the background is drawn.
    style.window.left_padding = 60
    style.window.right_padding = 60
    style.window.top_padding = 10
    # style.window.bottom_padding = 6

    ## This is the minimum height of the window, including the margins and padding.
    # style.window.yminimum = 250

    #########################################
    ## This lets you change the placement of the main menu.

    ## The way placement works is that we find an anchor point
    ## inside a displayable, and a position (pos) point on the
    ## screen. We then place the displayable so the two points are
    ## at the same place.

    ## An anchor/pos can be given as an integer or a floating point
    ## number. If an integer, the number is interpreted as a number
    ## of pixels from the upper-left corner. If a floating point,
    ## the number is interpreted as a fraction of the size of the
    ## displayable or screen.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5


    #########################################
    ## These let you customize the default font used for text in Ren'Py.
    ## The file containing the default font.
    # style.default.font = "DejaVuSans.ttf"

    ## The default size of text.
    style.default.size = 24

    #########################################
    ## These settings let you change some of the sounds that are used by
    ## Ren'Py.

    ## Set this to False if the game does not have any sound effects.
    config.has_sound = True

    ## Set this to False if the game does not have any music.
    config.has_music = True

    ## Set this to False if the game does not have voicing.
    config.has_voice = True

    ## Sounds that are used when button and imagemaps are clicked.
    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"
    # style.imagemap.hover_sound = "sfx/tok.ogg"

    ## Sounds that are used when entering and exiting the game menu.
    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## A sample sound that can be played to check the sound volume.
    # config.sample_sound = "click.wav"

    ## Music that is played while the user is at the main menu.
    # config.main_menu_music = "main_menu_theme.ogg"
    
    #########################################
    ## Help.
    ## This lets you configure the help option on the Ren'Py menus.
    ## It may be:
    ## - A label in the script, in which case that label is called to show help to the user.
    ## - A file name relative to the base directory, which is opened in a web browser.
    ## - None, to disable help.   
    config.help = "None"

#██▓▒░ TRANSITIONS ░▒▓█████████████████████████████████████ 
# This block is responsible for transitions.
    ## Used when entering the game menu from the game.
    config.enter_transition = dissolve

    ## Used when exiting the game menu to the game.
    config.exit_transition = dissolve

    ## Used between screens of the game menu.
    config.intra_transition = dissolve

    ## Used when entering the game menu from the main menu.
    config.main_game_transition = dissolve

    ## Used when returning to the main menu from the game.
    config.game_main_transition = dissolve

    ## Used when entering the main menu from the splashscreen.
    config.end_splash_transition = dissolve

    ## Used when entering the main menu after the game has ended.
    config.end_game_transition = dissolve

    ## Used when a game is loaded.
    config.after_load_transition = dissolve

    ## Used when the window is shown.
    config.window_show_transition = dissolve

    ## Used when the window is hidden.
    config.window_hide_transition = dissolve

    #########################################
    ## This is the name of the directory where the game's data is
    ## stored. (It needs to be set early, before any other init code
    ## is run, so the persisten information can be found by the init code.)
python early:
#    config.save_directory = "GUI Template Imagemap - PEACH-1283057230"
    config.save_directory = "Renpy Imagebuttons GUI Sample - PEACH-02934857390"

init -1 python hide:
    #########################################
    ## Default values of Preferences.
    ## Note: These options are only evaluated the first time a game is run. To have them run a second time, delete game/saves/persistent
    ## Should we start in fullscreen mode?
    config.default_fullscreen = False

    ## The default text speed in characters per second. 0 is infinite.
    config.default_text_cps = 60

    #########################################
    ## Size of the thumbnails for save games.
    config.thumbnail_width = 167
    config.thumbnail_height = 94

    #########################################
    ## More customizations can go here.