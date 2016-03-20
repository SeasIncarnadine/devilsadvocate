init -1 python:
    #import renpy.store as store
    #import renpy.exports as renpy 
    from operator import attrgetter 

    class Evidence():
        def __init__(self, name, description, image, useFn=None):
            self.name = name
            self.description = description
            self.image = image
            self.useFn = useFn
        def use(self):
            if self.useFn is not None:
                self.useFn

    #should this be "evidence", just placed in a different list?
    class Profile():
        def __init__(self, name, description, image=""):
            self.name = name
            self.description = description
            self.image = image

    evidence = []
    profiles = []
    evidence_page = 0
    profiles_page = 0


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


screen inventory_button:
    textbutton "Evidence" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.04)
            
screen inventory_screen:    
    default description_textbox = Tooltip("")
    add "gui/inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.05,.04) spacing 20:
        textbutton "Profiles" action [ Show("profiles_screen"), Hide("inventory_screen")]
    hbox align (.95,.04) spacing 20:
        textbutton "Close Evidence" action [ Hide("inventory_screen"), Show("inventory_button"), Show("profiles_button")]
    $ x = 54 # coordinates of the top left item position
    $ y = -32
    $ i = 0
    $ next_evidence_page = evidence_page + 1            
    if next_evidence_page > int(len(evidence)/10):
        $ next_evidence_page = 0
    for item in evidence:
        if i+1 <= (evidence_page+1)*10 and i+1>evidence_page*10:
            $ x += 138
            if i%5==0:
                $ y += 138
                $ x = 60
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            # sort out this line:
            #imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item.use] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at highlight_evidence
            imagebutton idle pic hover pic xpos x ypos y action [ Play ("sound", "sfx/click.wav"), description_textbox.Action(item.description)]# unhovered [description_textbox.Action("")]# hovered [ Play ("sound", "sfx/click.wav"), description_textbox.Action(item.description)] unhovered [description_textbox.Action("")]# at highlight_evidence
        #should be: set item active. active item sets description
        $ i += 1
        if len(evidence)>10:
            textbutton _("Next Page") action [SetVariable('evidence_page', next_evidence_page), Show("inventory_screen")] xpos .75 ypos .635
    frame:
        xfill True
        yfill True
        ypos 420
        text description_textbox.value color "#000000"

screen profiles_button:
    textbutton "Profiles" action [ Show("profiles_screen"), Hide("profiles_button")] align (.05,.04)

screen profiles_screen:    
    default description_textbox = Tooltip("")
    add "gui/profiles.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.95,.04) spacing 20:
        textbutton "Evidence" action [ Show("inventory_screen"), Hide("profiles_screen")]
    hbox align (.05,.04) spacing 20:
        textbutton "Close Profiles" action [ Hide("profiles_screen"), Show("profiles_button"), Show("inventory_button")]
    $ x = 54 # coordinates of the top left item position
    $ y = -32
    $ i = 0
    $ next_profiles_page = profiles_page + 1            
    if next_profiles_page > int(len(profiles)/10):
        $ next_profiles_page = 0
    for item in profiles:
        if i+1 <= (profiles_page+1)*10 and i+1>profiles_page*10:
            $ x += 138
            if i%5==0:
                $ y += 138
                $ x = 60
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            # sort out this line:
            #imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item.use] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at highlight_evidence
            imagebutton idle pic hover pic xpos x ypos y action [ Play ("sound", "sfx/click.wav"), description_textbox.Action(item.description)]# unhovered [description_textbox.Action("")]# hovered [ Play ("sound", "sfx/click.wav"), description_textbox.Action(item.description)] unhovered [description_textbox.Action("")]# at highlight_evidence
        $ i += 1
        if len(profiles)>10:
            textbutton _("Next Page") action [SetVariable('profiles_page', next_profiles_page), Show("profiles_screen")] xpos .75 ypos .635
    frame:
        xfill True
        yfill True
        ypos 420
        text description_textbox.value color "#000000"


init -1:
    transform highlight_evidence: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5
