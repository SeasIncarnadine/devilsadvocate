#########################################
# ____  ____  _  _  ____  _  _ 
#(  _ \( ___)( \( )(  _ \( \/ )
# )   / )__)  )  (  )___/ \  / 
#(_)\_)(____)(_)\_)(__)   (__) 
# ____  __  __    __    ___  ____  ____  __  __  ____  ____  _____  _  _  ___ 
#(_  _)(  \/  )  /__\  / __)( ___)(  _ \(  )(  )(_  _)(_  _)(  _  )( \( )/ __)
# _)(_  )    (  /(__)\( (_-. )__)  ) _ < )(__)(   )(    )(   )(_)(  )  ( \__ \
#(____)(_/\/\_)(__)(__)\___/(____)(____/(______) (__)  (__) (_____)(_)\_)(___/
#  ___  __  __  ____    ___    __    __  __  ____  __    ____ 
# / __)(  )(  )(_  _)  / __)  /__\  (  \/  )(  _ \(  )  ( ___)
#( (_-. )(__)(  _)(_   \__ \ /(__)\  )    (  )___/ )(__  )__) 
# \___/(______)(____)  (___/(__)(__)(_/\/\_)(__)  (____)(____)
#
# This file is in the public domain. Feel free to modify it as a basis for your own screens.
#
#########################################
# Note: comments like #begin foo and #end foo at the start of lines are used to display code examples. See example.rpy for more details.
#

## ■██▓▒░ MAIN MENU ░▒▓█████████████████████████████████████■
## Screen that's used to display the main menu, when Ren'Py first starts
## http://www.renpy.org/doc/html/screen_special.html#main-menu
screen main_menu:
    tag menu # This ensures that any other menu screen is replaced.
    # begin-end comments like the one in the next line are used to display code examples in the game
#begin add_image
    add "gui/main_menu_ground.jpg" # Add a background image for the main menu.
#end add_image
    $ y=114 # To make things easier, we define a variable y and use it to set positions for our imagebuttons
    imagebutton auto "gui/main_start_%s.png" xpos 773 ypos y focus_mask True action Start() hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_start.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at main_eff1
    # Imagebutton documentation: http://www.renpy.org/doc/html/screens.html#imagebutton
    
    # auto - is used to automatically define the images used by this button. We could also use:
    # imagebutton idle "main_start_idle.png" hover "main_start_hover.png"
    
    # xpos 773 ypos y - are used set the coordinates to position the button at 773, 114 (y has a value of 114)
    
    # focus_mask True ensures that only non-transparent areas of the button can be focused. focus_mask defines which parts of the image can be focused, and hence clicked on. http://www.renpy.org/doc/html/style.html#button-style-properties
    
    # action - action to run when the button is activated. This also controls if the button is sensitive, and if the button is selected.
    
    # hovered - action to run when the button gains focus. Square brackets are used to run multiple actions. In this case we play a sound effect and show a tooltip.
    
    # unhovered - action to run when the button loses focus. In this case we hide a tooltip.
    
    $ y+=71 # We increase y position for the next menu item. y has a value of 185(114+81=185) now. We could also use: xpos 773 ypos 185
    imagebutton auto "gui/main_load_%s.png" xpos 773 ypos y focus_mask True  action ShowMenu('load') hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_load.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at main_eff2
    $ y+=71
    imagebutton auto "gui/main_config_%s.png" xpos 773 ypos y focus_mask True action ShowMenu('preferences') hovered [ Play ("test_three", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_config.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at main_eff3
    $ y+=71
    if persistent.extra_unlocked: # We only show the extras, if they have been unlocked. Because we are using a variable (y) for ypos, we don't need to worry about positioning the rest of the button(s).
        imagebutton auto "gui/main_extras_%s.png" xpos 773 ypos y focus_mask True action Start('extras') hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_extra.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at main_eff4
        $ y+=71
    imagebutton auto "gui/main_quit_%s.png" xpos 773 ypos y focus_mask True action Quit(confirm=False) hovered [ Play ("test_five", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_main_menu_quit.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at main_eff5

screen example: #this screen isn't used. It's just used as an example in the script.
#begin at_atl
    imagebutton auto "gui/main_start_%s.png" xpos 773 ypos 114 focus_mask True action Start() at main_eff1
#end at_atl

# The code below defines the ATL transform effects for each button on the main menu. These effects are triggered when the buttons are shown.
# ATL transform properties: http://www.renpy.org/wiki/renpy/doc/reference/Animation_and_Transformation_Language#Transform_Properties
#begin main_eff
init -2:
    transform main_eff1:
        zoom 0.5
        easein 0.4 zoom 1.0
    transform main_eff2:
        zoom 0.5
        easein 0.8 zoom 1.0
    transform main_eff3:
        zoom 0.5
        easein 1.2 zoom 1.0
    transform main_eff4:
        zoom 0.5
        easein 1.6 zoom 1.0
    transform main_eff5:
        zoom 0.5
        easein 2.0 zoom 1.0
#end main_eff

## ■██▓▒░ NAVIGATION ░▒▓████████████████████████████████████■
## This screen is responsible for the game menu/navigation. It's included in other screens to display the game menu navigation.
## http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation:
    imagebutton auto "gui/game_menu_save_%s.png" xpos 810 ypos 99 focus_mask True action ShowMenu('save') hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_save.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/game_menu_load_%s.png" xpos 810 ypos 164 focus_mask True action ShowMenu('load') hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_load.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/game_menu_config_%s.png" xpos 810 ypos 227 focus_mask True action ShowMenu('preferences') hovered [ Play ("test_three", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_config.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/game_menu_main_%s.png" xpos 810 ypos 291 focus_mask True action MainMenu() hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_main.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/game_menu_return_%s.png" xpos 810 ypos 355 focus_mask True action Return() hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_return.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at nav_eff
    imagebutton auto "gui/game_menu_quit_%s.png" xpos 810 ypos 419 focus_mask True action Quit() hovered [ Play ("test_three", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_geme_menu_quit.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")] at nav_eff

# The code below defines the ATL transform effects for the buttons on the game menu. These effects are triggered when we hover the mouse over them (hover and selected_hover). Effects that are triggered by idle and selected_idle events (when we stop hovering the mouse over them) ensure that the buttons are moved back to the initial state.
#begin nav_eff
init -2:
    transform nav_eff:
        on idle:
            easein 0.5 xpos 810
        on selected_idle:
            easein 0.5 xpos 810
        on hover:
            easein 0.3 xpos 830
            easein 0.3 xpos 790
        on selected_hover:
            easein 0.3 xpos 830
            easein 0.3 xpos 790
#end nav_eff

## ■██▓▒░ PREFERENCES ░▒▓███████████████████████████████████■
## Screen that allows the user to change the preferences.
## http://www.renpy.org/doc/html/screen_special.html#prefereces
screen preferences:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/config_ground.jpg" # We add the image that is shown in the background of the preferences screen.
    use navigation # We include the navigation screen (game menu)
    # Display windowed/full screen:
    imagebutton auto "gui/config_display_window_%s.png" xpos 300 ypos 186 focus_mask True action Preference('display', 'window') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_windowed.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "gui/config_display_fullscreen_%s.png" xpos 388 ypos 186 focus_mask True action Preference('display', 'fullscreen') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_fullscreen.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    # Transitions on/off:
    imagebutton auto "gui/config_transitions_none_%s.png" xpos 502 ypos 186 focus_mask True action Preference('transitions', 'none') at config_eff hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_enable_transition.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "gui/config_transitions_all_%s.png" xpos 591 ypos 186 focus_mask True action Preference('transitions', 'all') at config_eff hovered [ Play ("test_four", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_enable_transition.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    # Stop/continue skipping after choices
    imagebutton auto "gui/config_afterchoices_stop_%s.png" xpos 300 ypos 345 focus_mask True action Preference('after choices', 'stop') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_stop_skip.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "gui/config_afterchoices_skip_%s.png" xpos 388 ypos 345 focus_mask True action Preference('after choices', 'skip') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_go_skip.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    # Skip all/seen text
    imagebutton auto "gui/config_skip_seen_%s.png" xpos 501 ypos 345 focus_mask True action Preference('skip', 'seen') at config_eff hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_stop_skip.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    imagebutton auto "gui/config_skip_all_%s.png" xpos 591 ypos 345 focus_mask True action Preference('skip', 'all') at config_eff hovered [ Play ("test_two", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_go_skip.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    # Button to begin skipping. Only active/visible if the game is started. Image config_begin_skipping_insensitive.png is used when the button is not active.
    imagebutton auto "gui/config_begin_skipping_%s.png" xpos 420 ypos 117 focus_mask True action Preference('begin skipping') hovered [ Play ("test_one", "sfx/click.wav"), Show("gui_tooltip", my_picture="gui/tooltip_config_skipping.png", my_tt_xpos=46, my_tt_ypos=518) ] unhovered [Hide("gui_tooltip")]
    # bar sliders for volume control, text speed and auto-forward time
    frame xpos 57 ypos 136:
        style_group "pref"
        has vbox
        bar value Preference("music volume")
    frame xpos 57 ypos 202:
        style_group "pref"
        has vbox
        bar value Preference("sound volume")
    frame xpos 57 ypos 268:
        style_group "pref"
        has vbox
        bar value Preference("voice volume")
    frame xpos 57 ypos 354:
        style_group "pref"
        has vbox
        bar value Preference("text speed")
    frame xpos 57 ypos 420:
        style_group "pref"
        has vbox
        bar value Preference("auto-forward time")
      
init -2 python: 
    # Styling for the bar sliders:
    # Aleema's Customizing Menus tutorial: http://lemmasoft.renai.us/forums/viewtopic.php?f=51&t=9812
    # Bar style properties documentation: http://www.renpy.org/doc/html/style.html#bar-style-properties
    style.pref_frame.background = None
    style.pref_slider.left_bar = "gui/config_bar_full.png"
    style.pref_slider.right_bar = "gui/config_bar_empty.png"
    style.pref_slider.thumb = None
    style.pref_slider.xmaximum = 223
    style.pref_slider.ymaximum = 36    
    
init -2:
    transform config_eff:
        on idle:
            easein 0.5 rotate 0
        on selected_idle:
            easein 0.5 rotate 0
        on hover:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat
        on selected_hover:
            easein 0.3 rotate 5
            easein 0.3 rotate -5
            repeat

            
## ■██▓▒░ SAVE / LOAD SLOT ░▒▓██████████████████████████████■
## This represents a load/save slot. You should customize this to ensure that the placement of the thumbnail and the slot text are as desired. Positions (x1, y1, x2 and y2) are relative to the x, y parameters, that are passed when the screen is called. To set the screenshot thumbnail size see options.rpy.
init -2 python: #we initialize x and y, so the load_save_slot screen below works at startup
    x=0
    y=0
screen load_save_slot:
    $ file_text = "% s\n  %s" % (FileTime(number, empty="Empty Slot."), FileSaveName(number))
    $x1=x+321
    $y1=y+10
    add FileScreenshot(number) xpos x1 ypos y1
    $x2=x+10
    $y2=y+11
    text file_text xpos x2 ypos y2 size 20

## ■██▓▒░ SAVE SCREEN ░▒▓███████████████████████████████████■
screen save:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/file_picker_ground.jpg" # We add the file picker background image. This image is the same for save and load screens.
    add "gui/title_save.png" # We add the save title image on top of the background
    use file_picker # We include the file_picker screen

## ■██▓▒░ LOAD SCREEN ░▒▓███████████████████████████████████■
screen load:
    tag menu # This ensures that any other menu screen is replaced.
    add "gui/file_picker_ground.jpg"
    add "gui/title_load.png"
    use file_picker

## ■██▓▒░ SAVE / LOAD FILE PICKER ░▒▓███████████████████████■
## Since saving and loading are so similar, we combine them into a single screen, file_picker. We then use the file_picker screen from simple load and save screens.
screen file_picker:
    use navigation # We include the navigation/game menu screen
    # Buttons for selecting the save/load page:
    imagebutton auto "gui/filepage1_%s.png" xpos 46 ypos 104 focus_mask True action FilePage(1) hover_sound "sfx/click.wav"
    imagebutton auto "gui/filepage2_%s.png" xpos 46 ypos 228 focus_mask True action FilePage(2) hover_sound "sfx/click.wav"
    imagebutton auto "gui/filepage3_%s.png" xpos 46 ypos 353 focus_mask True action FilePage(3) hover_sound "sfx/click.wav"
    $ y=104 # ypos for the first save slot
    for i in range(0, 3): # This repeats the block below 3 times (counts from 0 to 2), for the 3 save slots. We could also copy/paste the block below 3 times, but we are too lazy to do that.
        imagebutton auto "gui/fileslot_%s.png" xpos 195 ypos y focus_mask True action FileAction(i)
        use load_save_slot(number=i, x=195, y=y) # This calls the load_save_slot screen defined above. We pass variable i as the slot number and x, y coordinates.
        $ y+=124 # We increase the y variable so every next save slot is moved 124px lower.
        
## ■██▓▒░ YES/NO PROMPT ░▒▓█████████████████████████████████■
## Screen that asks the user a yes or no question. You'll need to edit this to change the position and style of the text.
## http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt:
    on "show" action Play("sound", "sfx/alert.wav")
    modal True # A modal screen prevents the user from interacting with displayables below it, except for the default keymap.

    add "gui/yesno_ground.png"
    imagebutton auto "gui/yesno_yes_%s.png" xpos 267 ypos 369 action yes_action hover_sound "sfx/click.wav"
    imagebutton auto "gui/yesno_no_%s.png" xpos 526 ypos 369 action no_action hover_sound "sfx/click.wav"
    
    if message == layout.ARE_YOU_SURE:
        add "gui/yesno_are_you_sure.png"
    elif message == layout.DELETE_SAVE:
        add "gui/yesno_delete_save.png"
    elif message == layout.OVERWRITE_SAVE:
        add "gui/yesno_overwrite_save.png"
    elif message == layout.LOADING:
        add "gui/yesno_loading.png"
    elif message == layout.QUIT:
        add "gui/yesno_quit.png"
    elif message == layout.MAIN_MENU:
        add "gui/yesno_main_menu.png"

## ■██▓▒░ CUSTOM MOUSE POINTER ░▒▓██████████████████████████■
##This block is responsible for the custom mouse pointer
# init python:
    # config.mouse = { }
    # config.mouse["default"] = [
         # ("gui/mouse_pointer.png", 8.8, 0.0),
    # ]
# Configuration variables: http://www.renpy.org/doc/html/config.html
# Custom mouse pointer is commented out, to disable it for the time being, because of an issue in all recent versions of Ren'Py.
# PyTom: "There's also an issue where display latency introduced by newer Nvidia drivers makes config.mouse noticeably slow, when Maximum Pre-Rendered Frames is set (which is the default for the driver). As far as I know, this isn't fixable in the short term. For now, I strongly recommend disabling custom mouse cursors (config.mouse)." (Mar 29, 2013) http://lemmasoft.renai.us/forums/viewtopic.php?f=8&t=19703&start=45#p259263

## ■██▓▒░ TOOLTIP ░▒▓███████████████████████████████████████■
screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

## ■██▓▒░ CUSTOM SOUND CHANNEL ░▒▓██████████████████████████■
# This is the block where we declare the individual sound channels. This enables us to play several sound FX's without overlapping
init python:
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)

## ■██▓▒░ THE TEXTBOX ░▒▓███████████████████████████████████■
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say

screen say:
    default side_image = None
    window:
        id "window"
        has vbox:
            style "say_vbox"
        if who:
            text who id "who"
        text what id "what"              
    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Which quick menu should we use? We use 5 different quick menues for presentation purposes in the script.
    if show_quick_menu1:
        use quick_menu1    
    if show_quick_menu2:
        use quick_menu3
    if show_quick_menu3:
        use quick_menu3
    if show_quick_menu4:
        use quick_menu4
    if show_quick_menu5:
        use quick_menu5

init -2 python:   
    show_quick_menu1=False
    show_quick_menu2=False
    show_quick_menu3=False
    show_quick_menu4=False
    show_quick_menu5=False

## ■██▓▒░ TEXTBOX DROP SHADOW ░▒▓███████████████████████████■
## This block is responsible for the text drop shadow effect for the textbox dialogue.
init:
    $ style.say_dialogue.drop_shadow = (2, 2)
    $ style.say_dialogue.drop_shadow_color = "#000000"

## ■██▓▒░ QUICK MENU ░▒▓████████████████████████████████████■
## Screens for the quick menus above the textbox. We use several different quick menus for presentation purposes.
#begin quick_menu1
screen quick_menu1:    
    hbox:
        style_group "quick"
        xpos 650
        ypos 410
        textbutton _("Save") action ShowMenu('save')
        textbutton _("Load") action ShowMenu('load')
        textbutton _("Prefs") action ShowMenu('preferences')
        textbutton _("Menu") action MainMenu()
#end quick_menu1

# Note that we actually never display the imagemap-based quick menu below; we cheat and display the imagebutton-based quick menu and say it's imagemap-based. There actually isn't even an image for the imagemap. DEATH TO ALL IMAGEMAPS! MUAHAHAHAHA!
#begin quick_menu2
screen quick_menu2:
    imagemap:
        xpos 660 ypos 390
        auto "GUI/quick_imagemap_%s.png"
        hotspot (0,0,80,36) action ShowMenu("save")
        hotspot (162,0,80,36) action ShowMenu("load")
        hotspot (162,0,80,36) action ShowMenu("preferences")
        hotspot (243,0,80,36) action MainMenu()
#end quick_menu2

#begin quick_menu3
screen quick_menu3:
    imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') xpos 690 ypos 390 focus_mask True
    imagebutton auto "gui/quick_save_%s.png" action ShowMenu('save') xpos 760 ypos 390 focus_mask True
    imagebutton auto "gui/quick_load_%s.png"action ShowMenu('load') xpos 830 ypos 390 focus_mask True
    imagebutton auto "gui/quick_main_%s.png" action MainMenu() xpos 900 ypos 390 focus_mask True
#end quick_menu3

#begin quick_menu4
screen quick_menu4:
    imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') xpos 690 ypos 390 focus_mask True at q_move1
    imagebutton auto "gui/quick_save_%s.png" action ShowMenu('save') xpos 760 ypos 390 focus_mask True at q_move2
    imagebutton auto "gui/quick_load_%s.png"action ShowMenu('load') xpos 830 ypos 390 focus_mask True at q_move3
    imagebutton auto "gui/quick_main_%s.png" action MainMenu() xpos 900 ypos 390 focus_mask True
init -2:
    transform q_move1:
        xpos 690
        linear 5.0 xpos 830
    transform q_move2:
        xpos 760
        time 3
        linear 5.0 xpos 690
    transform q_move3:
        xpos 830
        time 4
        linear 5.0 xpos 760        
#end quick_menu4

#begin quick_menu5
screen quick_menu5:
    imagebutton auto "gui/quick_config_%s.png" action ShowMenu('preferences') xpos 690 ypos 390 focus_mask True at q_move4
    imagebutton auto "gui/quick_save_%s.png" action ShowMenu('save') xpos 760 ypos 390 focus_mask True at q_move5
    imagebutton auto "gui/quick_load_%s.png"action ShowMenu('load') xpos 830 ypos 390 focus_mask True at q_move6
    imagebutton auto "gui/quick_main_%s.png" action MainMenu() xpos 900 ypos 390 focus_mask True at q_move7
init -2:
    transform q_move4:
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        repeat
    transform q_move5:
        linear 5.0 rotate 180
        linear 5.0 rotate 0
        repeat
    transform q_move6:
        linear 2.0 zoom 0.5
        linear 2.0 zoom 2
        repeat
    transform q_move7:
         xalign 0.0 yalign 1.0
         linear 1.0 xalign 0.0
         ease 1.0 truecenter
         pause 1.0
         alignaround (.5, .5)
         linear 2.0 yalign 0.0 clockwise circles 3
         linear 2.0 align (0.5, 1.0) knot (0.0, .33) knot (1.0, .66)
         linear 1.0 xalign 0.0 yalign 1.0
         repeat
#end quick_menu5