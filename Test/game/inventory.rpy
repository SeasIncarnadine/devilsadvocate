init -1 python:
    #import renpy.store as store
    #import renpy.exports as renpy 
    from operator import attrgetter 

    class Evidence():
        def __init__(self, name, description, image, useFn):
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
    textbutton "Show Inventory" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.04)
            
screen inventory_screen:    
    default description_textbox = Tooltip("")
    add "gui/inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.95,.04) spacing 20:
        textbutton "Close Inventory" action [ Hide("inventory_screen"), Show("inventory_button")]
    $ x = 60 # coordinates of the top left item position
    $ y = -32
    $ i = 0
    $ inv_page = 0
    $ next_inv_page = inv_page + 1            
    if next_inv_page > int(len(evidence)/8):
        $ next_inv_page = 0
    for item in evidence:
        if i+1 <= (inv_page+1)*8 and i+1>inv_page*8:
            $ x += 132
            if i%4==0:
                $ y += 132
                $ x = 60
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            # sort out this line:
            #imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item.use] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at highlight_evidence
            imagebutton idle pic hover pic xpos x ypos y action [item.use] hovered [ Play ("sound", "sfx/click.wav"), description_textbox.Action(item.description)] unhovered [description_textbox.Action("")]# at highlight_evidence
        $ i += 1
        if len(evidence)>8:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83
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
