init -1 python:
    #import renpy.store as store
    #import renpy.exports as renpy 
    from operator import attrgetter 

    #inv_page = 0 # initial page of the inventory screen
    #item = None
    strikes = 0
    class Evidence():
        def __init__(self, name, description, image, useFn):
            self.name = name
            self.description = description
            self.image = image
            self.useFn = useFn
        def use(self):
            if useFn == null:
                self.name = "ok"#display text... and image? same? different?
            else:
                self.name = "ok"#useFn

    #should this be "evidence", just placed in a different list?
    class Profile():
        def __init__(self, name, description, image=""):
            self.name = name
            self.description = description
            self.image = image

    evidence = []
    profiles = []

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

    "{w=1}{i}My heart is pounding.{/i}"

    "{i}I've been training to be a DA for the past several years...{/i}"

    "{i}But now I'm about to step into the court for the first time.{/i}"

    scene outside
    show mentor
    with fade

    mentor "Focus, Sana."

    mentor "Just remember what I've taught you."

    mentor "After some preamble, how about we try a practice cross-examination?"

    
    return
