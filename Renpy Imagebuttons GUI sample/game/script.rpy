init:
    # Here is where you tell renpy what images are inside renpy.
    # This is also place where you put anything you wanted to run at the start of renpy.
    
    # The Background images used in the game 
    image street_morning = "graphics/background_street_morning.jpg"
    image street_evening = "graphics/background_street_evening.jpg"

    
#    image credit = "graphics/credit.jpg"
    
    $ mugen = Character(' ',color="#ffffff",window_left_padding=302,window_top_padding=-5,show_side_image=Image("side_image/uncle_mugen_smile.png", xalign=0.0, yalign=1.0), )
    $ mugen_shocked = Character(' ',color="#ffffff",window_left_padding=302,window_top_padding=-5,show_side_image=Image("side_image/uncle_mugen_schocked.png", xalign=0.0, yalign=1.0), )

    $ lucy_01 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_surprized.png", xalign=0.0, yalign=1.0), )
    $ lucy_02 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_happy.png", xalign=0.0, yalign=1.0), )
    $ lucy_03 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_smile.png", xalign=0.0, yalign=1.0), )
    $ lucy_04 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_blank.png", xalign=0.0, yalign=1.0), )
    $ lucy_05 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_sad.png", xalign=0.0, yalign=1.0), )
    $ lucy_06 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_pout.png", xalign=0.0, yalign=1.0), )
    $ lucy_07 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_proud.png", xalign=0.0, yalign=1.0), )
    
    $ lucy_casual_01 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_casual_smile.png", xalign=0.0, yalign=1.0), )
    $ lucy_casual_02 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_casual_shocked.png", xalign=0.0, yalign=1.0), )
    $ lucy_casual_03 = Character(' ',color="#ffffff",window_left_padding=288,window_top_padding=-5,show_side_image=Image("side_image/lucy_casual_very_happy.png", xalign=0.0, yalign=1.0), )
    
label splashscreen:
    return
    
# The game starts here.
label start:
    # This will give your save name a name so you can see the name in your save and load file
    $ save_name = "Nothing to see here... "
    # Tells renpy to play the file "sunshine_a.mp3" located inside the music folder
    play music "music/sunshine_a.mp3"
    scene street_morning with dissolve
    #Show the in-game text dialogue box with transition dissolve
    window show dissolve
    if persistent.extra_unlocked:
        # alt. intro script when extras unlocked...
        jump tutorial
    else:
        # intro script
        lucy_03 "This is a demo of an Imagebuttons Based GUI for Ren'py."
label tutorial:
        lucy_02 "OHIO GO SAY MUST!"
        lucy_03 "I'm Lucy!"
        mugen "And I'm Uncle Mugen..."
        lucy_02 "And welcome to the Ren'py Imagebutton GUI sample!"
        mugen_shocked "Wait...{w}Imagebutton?"
        mugen_shocked "I thought we are going to talk about imagemaps..."
        lucy_07 "Not today..."
        lucy_03 "Anyway... Let's begin by turning on the quickmenu."
        $ show_quick_menu1 = True
        show example quick_menu1
        mugen_shocked "Uh... what are those?..."
        lucy_03 "Relax... These are just textbuttons. "
        mugen "Shesh!... They look so generic and boring..."
        lucy_03 "While we could customize this quickmenu with styles, there is a limit to what we can do..."
        lucy_03 "If we want something more fancy we need to use imagemaps or imagebuttons. Like this..."
        $ show_quick_menu1 = False
        show example quick_menu2
        $ show_quick_menu2 = True
        mugen "Yeah! Now that looks much better!"
        lucy_03 "Imagemaps are a quick method. An imagemap can contain several buttons, which means you need to export less images. But they have a lot limitations too."
        $ show_quick_menu2 = False
        hide example
        lucy_03 "Now let's see the quick menu made with imagebuttons..."
        show example quick_menu3
        $ show_quick_menu3 = True
        mugen "Eh?... This just look pretty much the same thing..."
        lucy_03 "It may look the same, but this one is actually made with imagebuttons. And imagebuttons are so much cooler!"
        mugen "No they're not..."
        lucy_07 "Yes they are..."
        lucy_03 "Besides... the code is very similar. Instead of defining an action and clickable area for each hotspot, we define an imagebutton for each... button. Simple!"
        lucy_03 "You define the position of each imagebutton with the xpos and ypos properties - just like with sprites. You can also use other methods, such as xalign and yalign."
        lucy_03 "Since the image has width and height, you don't need to define these, like you do with imagemaps. You just need to position the imagebuttons and you are done."
        lucy_03 "We defined these imagebuttons with \"focus_mask True\" property. This way only the opaque areas respond to mouse hover and are clickable."
        lucy_03 "Because our buttons are not rectangles, we want to make sure only the actual buttons are clickable, but not the trasparent area around them."
        
        show example add_image
        lucy_03 "There's also no \"ground\" image with imagebuttons. Instead you use the \"add\" screen language command if we need to add a background image."
        show example quick_menu3
        lucy_03 "Just like with imagemaps we can use the \"auto\" property to automatically define the images used by a button."
        
        lucy_03 "Imagebuttons also use a little less disk space. The GUI folder in this demo used to be 5,24 Mb, when it was using imagemaps. It's just 1,63 MB now."
        
        lucy_03 "If you want to change positions, you can just change the coordinates in the code. You don't need to export all of the variations from your graphics editor again."
        
        lucy_03 "You can even do it in the middle of the game. In fact, let's do it right now."
        
        $ show_quick_menu3 = False
        show example quick_menu4
        $ show_quick_menu4 = True
        
        mugen_shocked "What the!?...The buttons!... They are moving!"

        lucy_03 "See? You can apply ATL (Animation and Transformation Language) effects to imagebuttons. With this you can do all sort of stuff to imagebuttons."
        
        $ show_quick_menu4 = False
        $ show_quick_menu3 = True
        
        lucy_03 "Move, rotate, zoom, animate..."
        lucy_07 "Let's see if your imagemap can do these..."
        
        $ show_quick_menu3 = False
        show example quick_menu5
        $ show_quick_menu5 = True

        mugen_shocked "...{w}...{w}..."
        
        $ show_quick_menu5 = False
        hide example quick_menu5
        $ show_quick_menu3 = True
        
        mugen_shocked "Lucy... how did you do these fancy animated things?"
        
        show example main_eff
        lucy_03 "Simple... to use ATL with imagebuttons, you first define the transformations like this."
        mugen_shocked "Ohh..."
        show example at_atl
        lucy_03 "Then you add \"at (transformation)\" to the imagebutton definition like this."


        
        mugen_shocked "That simple?"
        lucy_07 "Yep!"
        show example nav_eff
        lucy_03 "If you want something to happen when a button changes it's state, such as \"hover\", \"selected\" or \"idle\", you use the ATL \"on\" statement."

        lucy_03 "You might want to check the script for this demo to see how the imagebuttons based Ren'Py GUI works."
        mugen "I know I would..."
        lucy_03 "Anyway... that's it for now. Bye!"
        
        # Hide the in-game text dialogue box with transition dissolve
        window hide dissolve
        $ persistent.extra_unlocked = True

        call credits
        # Stops the BG music with a 2 second fade out
        stop music fadeout 2.0
        return

label extras:
    # Tells renpy to play the file "poofy_reel.mp3" located inside the music folder
    play music "music/poofy_reel.mp3"
    
    scene street_evening with dissolve
    # Show the in-game text dialogue box with transition dissolve
    window show dissolve
    $ save_name = "If you see this... then there's something wrong with your project... Lol!..."
    # To prevent right clicking and opening the save/load screen while inside the Extra's screen
    $ _game_menu_screen = None 
    # To prevent game from Rolling back into Main Menu
    $ renpy.block_rollback()
    
    mugen "Welcome to the extra's section which contains... {p}nothing"
    mugen_shocked "W... What happened?... {w}Where's the content?"
    lucy_casual_02 "You do know that this is just a GUI demo to demonstrate Imagebutton based GUI..."
    lucy_casual_02 "Of course there won't be anything in here..."
    mugen_shocked "...Really?"
    lucy_casual_01 "Yep!"
    lucy_casual_03 "Anyway, this is the unlockable extra's section where you can do anything you wanted with it."
    lucy_casual_03 "You can put image galleries, and music jukebox or a sprite viewer..."
    lucy_casual_03 "Even perhaps some unlockables whenever a player reaches a milestone or something."
    lucy_casual_03 "Same thing, you might want to check the script for this demo to see how the imagebutton based Ren'Py GUI works."
    lucy_casual_03 "We look forward to what you can create using screen based imagebutton."
    
    # To re-enable right clicking
    $ _game_menu_screen = "save_screen"
    # Hide the in-game text dialogue box with transition dissolve
    window hide dissolve
    # Stops the BG music with 2 second fade out
    stop music fadeout 2.0
    return
    
label credits:
    $ credits_speed = 10 #scrolling speed in seconds
    scene street_evening
    with dissolve

    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    show thanks:
        yanchor 0.5 ypos 0.5
        xanchor 0.5 xpos 0.5
    with dissolve
    with Pause(3)
    hide thanks
    return

init python: # 
    credits = ('GUI and Graphics', 'Mugenjohncel'), ('Music', 'Kevin Macleod'), ('Programming', 'Leon Zavšek')
    credits_s = "{size=80}Credits\n\n"
    c1 = ''
    for c in credits:
        if not c1==c[0]:
            credits_s += "\n{size=40}" + c[0] + "\n"
        credits_s += "{size=60}" + c[1] + "\n"
        c1=c[0]
    credits_s += "\n{size=40}Engine\n{size=60}" + renpy.version()

init:
    image cred = Text(credits_s, text_align=0.5, drop_shadow = (4, 4), drop_shadow_color = "#000000")
    image thanks = Text("{size=80}Thank You!", text_align=0.5, drop_shadow = (4, 4), drop_shadow_color = "#000000")