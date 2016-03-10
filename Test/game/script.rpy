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

    mentor "Ok, let's take a look at your inventory."

    show screen inventory_button

    mentor "After some preamble, how about we try a practice cross-examination?"

    mentor "Hmm..."

    
    return
