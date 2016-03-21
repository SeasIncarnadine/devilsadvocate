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

    mentor "Now that you have some evidence, let's try a cross-examination."

    scene black
    show mentor
    with fade 


label cross_examination_example_1:

    $ beginCrossExamination("cross_examination_example")  
    $ currentCrossExaminationStatement = 1
    mentor "Cross-examinations consist of several statments."

label cross_examination_example_2:

    $ currentCrossExaminationStatement = 2
    mentor "You can press a statment if you want more information."

label cross_examination_example_3:

    $ currentCrossExaminationStatement = 3
    mentor "Or you can present evidence if you think you've found a contradiction."

label cross_examination_example_4:

    $ currentCrossExaminationStatement = 4
    mentor "I can firmly state that chocolate does not exist."

label cross_examination_example_advice:

    $ endCrossExamination()
    mentor "When you reach the end of a cross-examination, you'll loop back to the beginning again. See if you can find a statement that contradicts something in your Evidence or Profiles."
    jump cross_examination_example_1 

label cross_examination_example_1_press:

    mentor "Well, I guess there could just be one?"
    mentor "Not sure what more you want to know about this."
    $ beginCrossExamination("cross_examination_example")   
    jump cross_examination_example_2

label cross_examination_example_2_press:

    mentor "Yes, like that!"
    mentor "Press any statement you want to know more about."
    $ beginCrossExamination("cross_examination_example")   
    jump cross_examination_example_3

label cross_examination_example_3_press:

    mentor "Basically, if you think the statment includes a {i}lie{/i}, or is otherwise in conflict with something you can {i}prove{/i} using Evidence."
    $ beginCrossExamination("cross_examination_example")   
    jump cross_examination_example_4

label cross_examination_example_4_press:

    mentor "You know. Chocolate. {i}Theobroma cacao{/i} seeds, roasted, ground, flavored, and made into bars, beverages, etc. Definitely no such thing."
    jump cross_examination_example_advice

label cross_examination_example_1_present:

label cross_examination_example_2_present:

label cross_examination_example_3_present:

    call wrong_evidence_generic
    jump cross_examination_example_1

label cross_examination_example_4_present:
    
    if selectedEvidence is chocolate:
        jump cross_examination_example_success
    else:
        call wrong_evidence_generic
        jump cross_examination_example_1

label wrong_evidence_generic:

    mentor "No, I don't think that evidence is relevant to that statment."
    return

label cross_examination_example_success:

    mentor "Well done! You caught the contradiction!"

    mentor "That's about all that's currently written."

    mentor "Best of luck with the rest of the game!"



    # Empty evidence lists after the case:
    $ del evidence[:] 
    $ del profiles[:]

    
    return
