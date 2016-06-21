init -1 python:
    strikes = 0

    #currentCallStack = "Default text"

    renpy.music.register_channel("talkblips", mixer="voice", loop=True);
    renpy.music.register_channel("shout", mixer="voice", loop=False);

    def talksound(soundfile):
        def talkfunc(event, **kwargs):
            renpy.music.set_volume(0.25, channel="talkblips");
            if event == "show":
                renpy.music.play(soundfile, channel="talkblips")
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="talkblips")
        return talkfunc

    defaultTalksound = talksound("sfx/blip.wav")

# Declare characters used by this game.
define narrator = Character(callback=defaultTalksound, color="#c8ffc8")
define crucius = Character('Inquisitor Crucius', callback=defaultTalksound, color="#c8ffc8")
define mentor = Character('Lysander', callback=defaultTalksound, color="#c8ffc8")
define da = Character('Sana', callback=defaultTalksound, color="#c8ffc8")

image crucius = "images/inquisitor.png"
image mentor = "images/mentor.png"
image black = "#000000"

image bg outside = "images/outside.png"

define fade = Fade(0.0, 0.0, 2.0)





label start:

    #play music "music/intro.ogg" fadein 1
    play music "music/trial.mp3" fadein 1.5

    scene outside
    show mentor
    with fade

    show screen inventory_button

    show screen profiles_button

    $ chocolate = Evidence ("Chocolate", "A bar of dark chocolate, 80% cocoa", "gui/inv_chocolate.png")

    $ tinymap = Evidence("Courtroom Map", "A map of the rooms immediately around where the victim's body was found.", "gui/tinymap.png", "gui/biggermap.png")

    $ evidence.append(chocolate)

    $ evidence.append(tinymap)

    narrator "About to call from main label."

    $ currentCallStack = renpy.get_return_stack()

    narrator "Call stack: [currentCallStack]"




    $ beginCrossExamination("test", 3, chocolate, 2)

label test_1:
    narrator "First Statement"
    return

label test_2:
    narrator "Second Statement"
    return

label test_3:
    narrator "Third Statement"
    return

label test_advice:
    narrator "this is the advice segment"
    return

label test_1_press:
    narrator "test 1 press"
    return

label test_2_press:
    narrator "test 2 press"
    return

label test_3_press:
    narrator "test 3 press"
    return
    
label test_present:
    mentor "yep"
    mentor "okay that's the end"



    $ del evidence[:]
    $ del profiles[:]
    return






    call test1 from firstcall



label test1:

    $ currentCallStack = renpy.get_return_stack()

    narrator "Call stack: [currentCallStack]"

    call test2 from test1call

label test2:

    $ currentCallStack = renpy.get_return_stack()

    narrator "Call stack: [currentCallStack]"

    call test2 from test2call


    return;

    narrator "{w=1}{i}I've been training to be a DA for the past several years...{/i}"

    narrator "{i}But now I'm about to step into the court for the first time.{/i}"

    play music "music/trial.mp3" fadein 1.5

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

    play music "music/examination.mp3" fadeout 1.5 fadein 1.5

    scene black
    show mentor
    with fade

    $ setupCrossExamination("cross_examination_example")
    #$ beginCrossExamination("cross_examination_example")

label cross_examination_example_1:

    #$ currentCrossExaminationStatement = 1
    mentor "Cross-examinations consist of several statments."
    return

label cross_examination_example_2:

    #$ currentCrossExaminationStatement = 2
    mentor "You can press a statment if you want more information."
    return

label cross_examination_example_3:

    #$ currentCrossExaminationStatement = 3
    mentor "Or you can present evidence if you think you've found a contradiction."
    return

label cross_examination_example_4:

    #$ currentCrossExaminationStatement = 4
    mentor "I can firmly state that chocolate does not exist."
    return

label cross_examination_example_base:

    mentor "uh... I don't think you're supposed to be here."
    return

label cross_examination_example_advice:

    $ endCrossExamination()
    mentor "When you reach the end of a cross-examination, you'll loop back to the beginning again. See if you can find a statement that contradicts something in your Evidence or Profiles."
    $ beginCrossExamination("cross_examination_example")
    jump cross_examination_example_1

label cross_examination_example_1_press:

    mentor "Well, I guess there could just be one?"
    mentor "Not sure what more you want to know about this."
    $ beginCrossExamination("cross_examination_example")
    play music "music/examination.mp3" fadeout 1.5 fadein 1.5
    jump cross_examination_example_1

label cross_examination_example_2_press:

    mentor "Yes, like that!"
    mentor "Press any statement you want to know more about."
    $ beginCrossExamination("cross_examination_example")
    play music "music/examination.mp3" fadeout 1.5 fadein 1.5
    jump cross_examination_example_2

label cross_examination_example_3_press:

    mentor "Basically, if you think the statment includes a {i}lie{/i}, or is otherwise in conflict with something you can {i}prove{/i} using Evidence."
    $ beginCrossExamination("cross_examination_example")
    play music "music/examination.mp3" fadeout 1.5 fadein 1.5
    jump cross_examination_example_3

label cross_examination_example_4_press:

    mentor "You know. Chocolate. {i}Theobroma cacao{/i} seeds, roasted, ground, flavored, and made into bars, beverages, etc. Definitely no such thing."
    $ beginCrossExamination("cross_examination_example")
    play music "music/examination.mp3" fadeout 1.5 fadein 1.5
    jump cross_examination_example_4

label cross_examination_example_1_present:

label cross_examination_example_2_present:

label cross_examination_example_3_present:

    call wrong_evidence_generic
    $ beginCrossExamination("cross_examination_example")
    play music "music/examination.mp3" fadeout 1.5 fadein 1.5
    jump cross_examination_example_1

label cross_examination_example_4_present:

    if selectedEvidence is chocolate:
        jump cross_examination_example_success
    else:
        call wrong_evidence_generic
        $ beginCrossExamination("cross_examination_example")
        play music "music/examination.mp3" fadeout 1.5 fadein 1.5
        jump cross_examination_example_1

label wrong_evidence_generic:

    mentor "No, I don't think that evidence is relevant to that statment."
    return

label return_to_cross_examination:
    $ beginCrossExamination(currentCrossExaminationTag) # or - "begin" without setting this var? ("resumeCrossExamination")
    play music "music/examination.mp3" fadeout 1.5 fadein 1.5

label cross_examination_example_success:

    play music "music/cornered.mp3"

    mentor "Well done! You caught the contradiction!"

    mentor "That's about all that's currently written."

    mentor "Best of luck with the rest of the game!"



    # Empty evidence lists after the case:
    $ del evidence[:]
    $ del profiles[:]


    return
