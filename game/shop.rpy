default dagonboo = False
default salveboo = False
default fingerboo = False
screen shop_screen(): 
    frame pos(0,0):
            hbox:  
                imagebutton:
                    xpos  0
                    ypos  0
                    idle "images/inventory/dagon_icon.png"
                    hover "images/inventory/dagon_icon.png"
                    action [SetVariable("dagonboo", True),Call("add")]
                imagebutton:
                    xpos  0
                    ypos  0
                    idle "images/inventory/salve_icon.png"
                    hover "images/inventory/salve_icon.png"
                    action [SetVariable("salveboo", True),Call("add")]
                imagebutton:
                    xpos  0
                    ypos  0
                    idle "images/inventory/finger_icon.png"
                    hover "images/inventory/finger_icon.png"
                    action [SetVariable("fingerboo", True),Call("add")]
                textbutton "Back" action [Hide("shop_screen"),Show("mapUI")]
                    
label add():
    call reload from _call_reload_11
    if(dagonboo):
        if (gold < 250):
            "Not enough gold!"
            jump shop
        else:
            $gold -=250
            $inventory2["Dagon"][0] +=1
            $dagonboo = False
            $temp = inventory2["Dagon"][0]
            "You bought a dagon! Dagon: [temp]"
            call reload from _call_reload_5
            jump shop
    elif(salveboo):
        if (gold < 100):
            "Not enough gold!"
            jump shop
        else:
            $gold -=100
            $inventory2["Salve"][0] +=1
            $salveboo = False
            $temp = inventory2["Salve"][0]
            "You bought a salve! Salve: [temp]"
            call reload from _call_reload_6
            jump shop
    elif(fingerboo):
        if (gold < 350):
            "Not enough gold!"
            jump shop
        else:
            $gold -=200
            $inventory2["Finger"][0] +=1
            $fingerboo = False
            $temp = inventory2["Finger"][0]
            "You bought a finger spell! Finger Spell: [temp]"
            call reload from _call_reload_7
            jump shop



label shop:
    camera:
        pos (0, 0)
        zpos 0
        perspective True
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(549.0, 387.0, 981.0)*RotateMatrix(0.0, 0.0, 0.0)

    scene bg_shop:
    show screen shop_screen
    $renpy.pause(hard=True)
      
