init -1 python:
    #import renpy.store as store
    #import renpy.exports as renpy 
    from operator import attrgetter 

    class Evidence():
        def __init__(self, name, description, image, clickthruimage=None):
            self.name = name
            self.description = description
            self.image = image
            self.clickthruimage = clickthruimage
        #def use(self):
        #    if self.useFn is not None:
        #        self.useFn

    #should this be "evidence", just placed in a different list?
    class Profile():
        def __init__(self, name, description, image):
            self.name = name
            self.description = description
            self.image = image

    #def displayFullscreenFunction(image):
    #    def displayFullscreen():
    #        renpy.show_screen("display_fullscreen_evidence", image)
    #    return displayFullscreen

    evidence = []
    profiles = []
    evidence_page = 0
    profiles_page = 0
    selectedEvidence = None

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_bottom.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2
    
    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


screen inventory_button():
    textbutton "Evidence" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.04)
            
screen inventory_screen():    
    default description_textbox = Tooltip(selectedEvidence.description if selectedEvidence is not None else "")
    add "gui/inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.05,.04) spacing 20:
        textbutton "Profiles" action [ Show("profiles_screen"), Hide("inventory_screen"), SetVariable('selectedEvidence', None)]
    hbox align (.95,.04) spacing 20:
        textbutton "Close Evidence" action [ Hide("inventory_screen"), Show("inventory_button"), Show("profiles_button"), SetVariable('selectedEvidence', None)]
    $ x = 54 # coordinates of the top left item position
    $ y = -38
    $ i = 0
    for item in evidence:
        if i+1 <= (evidence_page+1)*10 and i+1>evidence_page*10:
            $ x += 138
            if i%5==0:
                $ y += 138
                $ x = 60
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") 
            imagebutton idle pic hover pic xpos x ypos y action [ Play ("sound", "sfx/click.wav"), description_textbox.Action(item.description), SetVariable('selectedEvidence', item)]
            if item is selectedEvidence:
                add "gui/selectioncursor.png" xpos x ypos y
        $ i += 1
        if len(evidence)>10:
            textbutton _("Next Page") action [SetVariable('evidence_page', evidence_page + 1 if evidence_page + 1 <= int(len(evidence)/10) else 0), Show("inventory_screen")] align(.95, .65)
            textbutton _("Prior Page") action [SetVariable('evidence_page', evidence_page - 1 if evidence_page > 0 else 0), Show("inventory_screen")] align(.95, .65)
    frame:
        xfill True
        yfill True
        ypos 420
        text description_textbox.value color "#000000"
    if selectedEvidence is not None and selectedEvidence.clickthruimage is not None:
        textbutton "Examine" action [Show("display_fullscreen_evidence", imagepath = selectedEvidence.clickthruimage), Hide("inventory_screen")] align (.5, .65)
    if crossExaminationInProgress:
        textbutton "Present" action If(selectedEvidence is not None, [Function(endCrossExamination), Hide("inventory_screen"), Show("inventory_button"), Show("profiles_button"), Jump(currentCrossExaminationTag + "_" + str(currentCrossExaminationStatement) + "_present")]) align (.5,.04)

screen display_fullscreen_evidence(imagepath):
    modal True
    add "gui/evidencebackground.png"
    add imagepath align(.5, .5)
    textbutton "Return" action [Hide("display_fullscreen_evidence"), Show("inventory_screen")] align (.5, .95)

screen profiles_button():
    textbutton "Profiles" action [ Show("profiles_screen"), Hide("profiles_button")] align (.05,.04)

screen profiles_screen():    
    default description_textbox = Tooltip(selectedEvidence.description if selectedEvidence is not None else "")
    add "gui/profiles.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.95,.04) spacing 20:
        textbutton "Evidence" action [ Show("inventory_screen"), Hide("profiles_screen"), SetVariable('selectedEvidence', None)]
    hbox align (.05,.04) spacing 20:
        textbutton "Close Profiles" action [ Hide("profiles_screen"), Show("profiles_button"), Show("inventory_button"), SetVariable('selectedEvidence', None)]
    $ x = 54 # coordinates of the top left item position
    $ y = -38
    $ i = 0
    for item in profiles:
        if i+1 <= (profiles_page+1)*10 and i+1>profiles_page*10:
            $ x += 138
            if i%5==0:
                $ y += 138
                $ x = 60
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "")
            imagebutton idle pic hover pic xpos x ypos y action [ Play ("sound", "sfx/click.wav"), description_textbox.Action(item.description), SetVariable('selectedEvidence', item)]
            if item is selectedEvidence:
                add "gui/selectioncursor.png" xpos x ypos y
        $ i += 1
        if len(profiles)>10:
            textbutton _("Next Page") action [SetVariable('profiles_page', profiles_page + 1 if profiles_page + 1 <= int(len(profiles)/10) else 0), Show("profiles_screen")] align(.95, .65)
            textbutton _("Prior Page") action [SetVariable('profiles_page', profiles_page - 1 if profiles_page > 0 else 0), Show("profiles_screen")] align(.95, .65)
    frame:
        xfill True
        yfill True
        ypos 420
        text description_textbox.value color "#000000"
    if crossExaminationInProgress:
        textbutton "Present" action If(selectedEvidence is not None, [Function(endCrossExamination), Hide("profiles_screen"), Show("inventory_button"), Show("profiles_button"), Jump(currentCrossExaminationTag + "_" + str(currentCrossExaminationStatement) + "_present")]) align (.5,.04)
