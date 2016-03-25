init -1 python:

    crossExaminationInProgress = False
    currentCrossExaminationStatement = 0
    currentCrossExaminationTag = "asdasdas"

    def beginCrossExamination(crossExaminatonTag):
        global crossExaminationInProgress
        crossExaminationInProgress = True
        global currentCrossExaminationTag
        currentCrossExaminationTag = crossExaminatonTag
        renpy.show_screen("press_button")

    def endCrossExamination():
        global crossExaminationInProgress
        crossExaminationInProgress = False
        global currentCrossExaminationTag
        currentCrossExaminationTag = ""
        renpy.hide_screen("press_button")

screen press_button():
    textbutton "Press" action [Stop("music"), Play("shout", "sfx/Phoenix - Hold it.mp3", loop=False), Function(endCrossExamination), Jump(currentCrossExaminationTag + "_" + str(currentCrossExaminationStatement) + "_press")] align (.5,.04)
