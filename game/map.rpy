screen inventory_screen():
    text "{size=15}Inventory: {p}[inlist!s]{p} Inventory2: [inlist2!s]{/size}":
        outlines [ (absolute(2), "#1D090D", absolute(2), absolute(1)) ]
        pos(0, 150)
    vbox:
        text "{color=#621E2C}{size=15}Player exp: [exp:.02f]/10,000{p}Gold:[gold]{p}Level: [slayer.level]{p}Health: [slayer.max_hp]{p}Damage: [slayer.attack_dmg]{/size}{/color}":
            outlines [ (absolute(2), "#1D090D", absolute(2), absolute(1)) ]
            pos (0,50)

screen mapUI():     
    tag mapg
    add "images/bg/bg map.png"
                                                                        #TEXT
    text "{color=#621E2C}{size=20}Shop{/size}{/color}":
        outlines [ (absolute(2), "#1D090D", absolute(2), absolute(1)) ]
        xpos 1050
        ypos 552
    text "{color=#621E2C}Lair{/color}":
        outlines [ (absolute(2), "#1D090D", absolute(2), absolute(1)) ]
        xpos 331
        ypos 519
    text "{color=#621E2C}{size=20}Guide's tower{/size}{/color}":
        outlines [ (absolute(2), "#1D090D", absolute(2), absolute(1)) ]
        xpos 1072
        ypos 248
    textbutton "{size=20}Player Info{/sizes}":
            align (0, 0)
            action ToggleScreen("inventory_screen")
        
    #IMAGEBUTTONS
    imagebutton:
        xpos  964
        ypos  430
        idle "images/bs-idle.png"
        hover "images/bs-hover.png"
        action [Hide("inventory_screen"),Hide("mapUI"),Jump("shop")]
    imagebutton:
        xpos  60
        ypos  373
        idle "images/lair idle.png"
        hover "images/lair-hover.png"
        action [Hide("inventory_screen"),Hide("shop_screen"),Hide("mapUI"),Stop("map_music"),SetMixer("music", 0.5),Play("tower_music","images/sounds/tower.wav"),Jump("level_random")]
    imagebutton:
        xpos  1000
        ypos  200
        idle "images/house idle.png"
        hover "images/house-hover.png"
        action [Hide("inventory_screen"),Hide("shop_screen"),Hide("mapUI"),Jump("guide")]

screen inventory_screenx(): 
    frame pos(175,148):
        hbox:
            for item in inventory2 and inventory64:
                if inventory2[item][0] > 0:
                    $ imagee = inventory64[item]
                    imagebutton:
                        xpos  0
                        ypos  0
                        idle imagee 
                        hover imagee
                        action Call(item+"_label")
    textbutton "Cancel" pos(170,250) action Rollback()
                    


