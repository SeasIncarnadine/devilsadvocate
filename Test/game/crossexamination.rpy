init -1 python:

    crossExaminationInProgress = False
    currentCrossExaminationNumStatements = 0
    currentCrossExaminationStatement = 0
    currentCrossExaminationTag = ""
    currentCrossExaminationMusic = "music/examination.mp3"
    useGenericWrongEvidence = True
    crossExaminationCorrectEvidence = None
    crossExaminationCorrectStatement = 0

    def beginCrossExamination(crossExaminatonTag, numStatements, correctEvidence, correctStatement, music="music/examination.mp3", doUseGenericWrongEvidence=True):
        global crossExaminationInProgress
        crossExaminationInProgress = True
        global currentCrossExaminationTag
        currentCrossExaminationTag = crossExaminatonTag
        global currentCrossExaminationNumStatements
        currentCrossExaminationNumStatements = numStatements
        global currentCrossExaminationMusic
        currentCrossExaminationMusic = music
        global crossExaminationCorrectEvidence
        crossExaminationCorrectEvidence = correctEvidence
        global crossExaminationCorrectStatement
        crossExaminationCorrectStatement = correctStatement
        global currentCrossExaminationStatement
        currentCrossExaminationStatement = 1
        global useGenericWrongEvidence
        useGenericWrongEvidence = doUseGenericWrongEvidence
        renpy.show_screen("press_button")
        renpy.jump("_crossExaminationSkeleton")

    def resumeCrossExamination():
        global crossExaminationInProgress
        crossExaminationInProgress = True
        renpy.show_screen("press_button")

    def pauseCrossExamination():
        global crossExaminationInProgress
        crossExaminationInProgress = False
        renpy.hide_screen("press_button")

screen press_button():
    textbutton "Press" action [Stop("music"), Play("shout", "sfx/Phoenix - Hold it.mp3", loop=False), Function(pauseCrossExamination), Jump("_crossExaminationPress")] align (.5,.04)

label _crossExaminationSkeleton:
    play music currentCrossExaminationMusic fadeout 1.5 fadein 1.5
    if currentCrossExaminationStatement > currentCrossExaminationNumStatements:
        "Bug - current cross examination statement is " + currentCrossExaminationStatement + ", max is " + currentCrossExaminationNumStatements "."
        return
    while currentCrossExaminationStatement <= currentCrossExaminationNumStatements:
        call expression currentCrossExaminationTag + "_" + str(currentCrossExaminationStatement)
        $ currentCrossExaminationStatement += 1
    $ pauseCrossExamination()
    call expression currentCrossExaminationTag + "_advice"
    $ resumeCrossExamination()
    $ currentCrossExaminationStatement = 1
    jump _crossExaminationSkeleton

label _crossExaminationPress:
    call expression currentCrossExaminationTag + "_" + str(currentCrossExaminationStatement) + "_press"
    $ resumeCrossExamination()
    jump _crossExaminationSkeleton

label _crossExaminationPresent:
    if selectedEvidence is crossExaminationCorrectEvidence and currentCrossExaminationStatement is crossExaminationCorrectStatement:
        $ renpy.set_return_stack([])
        jump expression currentCrossExaminationTag + "_present"
    else:
        if useGenericWrongEvidence:
            call _crossExaminationWrongEvidence
        else:
            call expression currentCrossExaminationTag + "_wrongEvidence"
        $ resumeCrossExamination()
        jump _crossExaminationSkeleton

label _crossExaminationWrongEvidence:
    mentor "No, I don't think that evidence is relevant to that statment."
    return

    #TODO handle evidence, pressing correctly
    #parameterized music??
    #see what else happens manually in script, reproduce here

    #clear return stack???

