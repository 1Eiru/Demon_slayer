default inventory = {}
default inventory2 = {"Dagon":[1, "images/inventory/dagon_icon.png"], "Salve":[1, "images/inventory/salve_icon.png"] , "Finger":[1, "images/inventory/finger_icon.png"]}
default inventory64 = {"Dagon":"images/inventory/dagon64.png", "Salve":"images/inventory/salve64.png", "Finger":"images/inventory/finger64.png"}
default boolevel3 = False
default boolevel2 = False
default boolevel1 = False
default max_floor = [None] * 51
default counter = 0
default enemy_level = 1
default beelzebub_orb = False
default belial_orb = False
default kokabiel_orb = False
default aamon_orb = False
default satan_orb = False
default inventoryattack = False
default exp = 0
default gold = 1000
define red = Solid("#1D090D")
define music.tower = "images/sounds/tower.wav"
init python: 
    renpy.music.register_channel("map_music",mixer="music",loop =True)
    renpy.music.register_channel("fight_music",mixer="music",loop =True)
    renpy.music.register_channel("tower_music",mixer="music",loop =True)
    renpy.music.register_channel("sound1", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.set_volume(0.5, delay=0, channel="map_music")
    class base:
        def __init__(self, name, max_hp, hp, attack_dmg,level):
            self.name = name
            self.max_hp = max_hp
            self.hp = hp
            self.attack_dmg = attack_dmg
            self.level = level

        def addHP(amount):
            self.hp += amount



transform MyTransform:
        parallel:
            ypos 658
            linear 1.51 ypos -100
        parallel:
            zpos 0.0 
            linear 1.51 zpos 0
        parallel:
            alpha 1.0 
            linear 1.51 alpha 0.0 


label levelup():
    $slayer.max_hp = 11 + (.4 * slayer.level)
    $slayer.attack_dmg = 2 + (.4 * slayer.level)
    return


screen showplayerDamageTaken(enemydamage,textvar):
    $damagetext = "-" +  str(enemydamage)
    text "{color=#ff0000}[damagetext] [textvar]{/color}" at MyTransform: 
        outlines [ (absolute(2), "#660707", absolute(2), absolute(1)) ]
        xpos 368
        ypos 658


screen showenemyDamageTaken(playerdamage):
    $damagetext = "-" +  str(playerdamage)
    text "{color=#ff0000}[damagetext]{/color}" at MyTransform: 
        outlines [ (absolute(2), "#660707", absolute(2), absolute(1)) ]
        xpos 1485
        ypos 761

label reload:
    $inlist = [k for k,v in inventory.items() if v is not 0]
    $inlist2 = [[k,v[0]] for k,v in inventory2.items() if v is not 0]
    return

label Dagon_label:
    $inventoryattack = True
    if (inventory2["Dagon"][0] <= 0):
        "No charges."
        return
    else:
        $inventory2["Dagon"][0]-=1
        show dagon_weapon:
            subpixel True 
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(378.0, 648.0, 0.0)*RotateMatrix(0.0, 180.0, -54.0) 
            linear 0.73 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(378.0, 648.0, 0.0)*RotateMatrix(0.0, 180.0, 27.0) 
        with Pause(0.23)
        show thunder_splash:
            subpixel True 
            matrixtransform ScaleMatrix(3.46, 1.76, 1.0)*OffsetMatrix(288.0, 144.0, 0.0)*RotateMatrix(0.0, 180.0, -288.0) 
            linear 0.13 matrixtransform ScaleMatrix(3.46, 1.76, 1.0)*OffsetMatrix(252.0, 297.0, 0.0)*RotateMatrix(0.0, 180.0, -189.0) 
            linear 0.05 matrixtransform ScaleMatrix(3.46, 1.76, 1.0)*OffsetMatrix(198.0, 261.0, 0.0)*RotateMatrix(0.0, 180.0, -126.0) 
        play sound1("images/sounds/dagon.mp3") volume 0.5
        with Pause(0.60)

        $temp = slayer.attack_dmg *2
        show screen showenemyDamageTaken(temp)
        python:
            demon.hp -=slayer.attack_dmg *2
            cultist.hp -=slayer.attack_dmg * 2
            skeleton.hp -=slayer.attack_dmg * 2
            aamon.hp -= slayer.attack_dmg * 2
            beelzebub.hp -= slayer.attack_dmg * 2
            belial.hp -= slayer.attack_dmg * 2
            kokabiel.hp -= slayer.attack_dmg * 2
            satan.hp -= slayer.attack_dmg * 2
            

        hide dagon_weapon with dissolve
        hide thunder_splash       
    return

label Salve_label:
    if (inventory2["Salve"][0] <= 0):
        "No charges."
        return
    else:
        play sound1("images/sounds/salve.mp3") volume 0.5
        show heal_effect zorder 2 with dissolve:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-81.0, 648.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
        $inventory2["Salve"][0]-=1
        $slayer.hp += 5
        if (slayer.hp > slayer.max_hp):
            $slayer.hp = slayer.max_hp
        return
    return

label Finger_label:
    $inventoryattack = True
    if (inventory2["Finger"][0] <= 0):
        "No charges."
        return
    else:
        show finger:
            subpixel True 
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(252.0, 927.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
            linear 0.42 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(252.0, 522.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
        with Pause(0.52)






        show finger_fx zorder 2:
            matrixtransform ScaleMatrix(4.79, 2.09, 1.0)*OffsetMatrix(234.0, 270.0, 0.0)*RotateMatrix(0.0, 0.0, -54.0)
        play sound3("images/sounds/finger.mp3") volume 0.3
        $temp = slayer.level *2
        python:
            demon.hp -=slayer.level *2
            cultist.hp -=slayer.level  * 2
            skeleton.hp -=slayer.level  * 2
            aamon.hp -= slayer.level  * 2
            beelzebub.hp -= slayer.level  * 2
            belial.hp -= slayer.level  * 2
            kokabiel.hp -= slayer.level  * 2
            satan.hp -= slayer.level * 2
            slayer.hp -= 0.8*slayer.level
        show screen showenemyDamageTaken(temp)
    with Pause(0.52)
    hide finger
    return


label start:
    $ _skipping = False
    hide black
    $inlist = [k for k,v in inventory.items() if v is not 0]
    $inlist2 = [[k,v[0]] for k,v in inventory2.items() if v is not 0]
    $ slayer = base("Slayer",11,11,2,1)
    $ demon = base("Demon",8,8,1,enemy_level)
    $ cultist = base("Cultist",9,9,1.3,enemy_level)
    $ skeleton = base("Skeleton",9,9,1.2,enemy_level)
    $ aamon = base("Aamon: {color=#DE193E}Grand Marquis{/color}",25,25,4,10)
    $ beelzebub = base("Beelzebub: {color=#DE193E}Gluttony{/color}",30,30,6,20)
    $ belial = base("Belial: {color=#DE193E}Wicked{/color}",45,45,8,30)
    $ kokabiel = base("Kokabiel: {color=#DE193E}The fallen{/color}",55,55,9,40)
    $ satan = base("Satan: {color=#DE193E}Wrath{/color}",60,60,10,50)
    jump story0
    # jump story3
    # jump level1
    # jump level2
    # jump slayer_v_demon
    # jump slayer_v_satan
    # jump slayer_v_skeleton
    # jump slayer_v_cultist
    # jump slayer_v_beelzebub
    #jump level3
    # jump slayer_v_aamon
    # jump slayer_v_kokabiel
    # jump slayer_v_belial
    #$renpy.music.play("images/sounds/map.mp3","map_music", loop=True)
    # call screen mapUI
    #jump guide
    return
   


    



                
