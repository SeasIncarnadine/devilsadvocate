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
    add "gui/inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    hbox align (.95,.04) spacing 20:
        textbutton "Close Inventory" action [ Hide("inventory_screen"), Show("inventory_button")]
    $ x = 515 # coordinates of the top left item position
    $ y = 25
    $ i = 0
    $ inv_page = 0
    $ next_inv_page = inv_page + 1            
    if next_inv_page > int(len(evidence)/9):
        $ next_inv_page = 0
    for item in evidence:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 190
            if i%3==0:
                $ y += 170
                $ x = 515
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item_use] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at inv_eff
        $ i += 1
        if len(inventory.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83
