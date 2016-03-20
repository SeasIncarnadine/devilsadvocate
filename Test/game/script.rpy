init -1 python:
    strikes = 0

# Declare characters used by this game.
define crucius = Character('Inquisitor Crucius', color="#c8ffc8")
define mentor = Character('Lysander', color="#c8ffc8")
define da = Character('Sana', color="#c8ffc8")

image crucius = "images/inquisitor.png"
image mentor = "images/mentor.png"
image black = "#000000"

image bg outside = "images/outside.png"

define fade = Fade(0.0, 0.0, 2.0)



# The game starts here.
label start:

    #play music "music/intro.ogg" fadein 1
    scene black

    "{w=1}{i}I've been training to be a DA for the past several years...{/i}"

    "{i}But now I'm about to step into the court for the first time.{/i}"

    scene outside
    show mentor
    with fade

    show screen inventory_button

    show screen profiles_button

    mentor "Here, have an evidence button."

    extend " And a profiles button of course."

    $ chocolate = Evidence("Chocolate", "A bar of dark chocolate, 80% cocoa", "gui/inv_chocolate.png")

    $ tinymap = Evidence("Courtroom Map", "A map of the rooms immediately around where the victim's body was found.", "gui/tinymap.png", "gui/biggermap.png")

    $ evidence.append(chocolate)

    $ evidence.append(tinymap)

    mentor "I've just added some example evidence, take a look."

    mentor "Ok, there isn't any more script to see!"

    # Empty evidence lists after the case:
    $ del evidence[:] 
    $ del profiles[:]

    
    return
