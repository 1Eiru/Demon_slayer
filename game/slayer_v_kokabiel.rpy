label slayer_v_kokabiel:
    $renpy.music.stop(channel="tower_music", fadeout=.5)
    $renpy.music.play("images/sounds/fight.mp3","fight_music", loop=True)
    hide screen level_info
    $ slayer.hp = slayer.max_hp
    $ kokabiel.hp = kokabiel.max_hp
    $playerdamage = slayer.attack_dmg
    $enemydamage = kokabiel.attack_dmg
    show screen hp_bars_kokabiel
    camera:
        perspective True
        zpos 400.0
        xzoom 1.0
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    scene cave_bg:
            ypos -108
            matrixtransform ScaleMatrix(1.32, 1.12, 1.0)*OffsetMatrix(0.0, 0.0, -180.0)*RotateMatrix(0.0, 0.0, 0.0)
    show fore:
        ypos -108
        matrixtransform ScaleMatrix(1.32, 1.13, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    show floor:
        pos (0, -531)
        matrixtransform ScaleMatrix(1.36, 1.55, 1.0)*OffsetMatrix(0.0, 936.0, 117.0)*RotateMatrix(81.0, 0.0, 0.0)
    
    show kokabiel idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1098.0, 342.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)

    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
    "{color=#27ff00}Player Hp: [slayer.hp]{/color}\n{color=#27ff00}Damage: [slayer.attack_dmg]{/color}\n{color=#FF0000}Enemy Hp:[kokabiel.hp]\nEnemy Damage:[kokabiel.attack_dmg]{/color}"

    while slayer.hp > 0 and kokabiel.hp > 0:
        #PLAYER ATTACK
        menu:
            
            "Slash":
                call camera_slayer_attack from _call_camera_slayer_attack_5
                play sound2("images/sounds/sword.mp3") volume 0.2
                $ kokabiel.hp -=  slayer.attack_dmg
                show kokabiel hit
                play sound1("images/sounds/femalehurt.mp3")

            "Stab":
                call camera_slayer_stab from _call_camera_slayer_stab_5
                show kokabiel hit
                play sound1("images/sounds/femalehurt.mp3")
                call random_select from _call_random_select_22
                if (randomstab <= 30):
                    $ kokabiel.hp -= slayer.attack_dmg * 2
                    play sound2("images/sounds/critical.wav")
                    show screen showenemyDamageTaken(slayer.attack_dmg * 2)
                else:
                    $ kokabiel.hp -=  slayer.attack_dmg - slayer.attack_dmg * 0.5
                    show screen showenemyDamageTaken(slayer.attack_dmg - slayer.attack_dmg * 0.5) 

            "Inventory":
                call screen inventory_screenx()
        if(inventoryattack):
            show kokabiel hit
            play sound1("images/sounds/femalehurt.mp3")
            $inventoryattack = False

    ############## CHECK ###########
        if ( kokabiel.hp <= 0):
            $gold += 450
            $temp = 4500 * (kokabiel.level/slayer.level)
            $exp += temp
            "You slayed {color=#FF0000}Kokabiel!{/color}"
            "You gained: {color=#FFFF00} [temp:.02f]EXP!{/color}{p}You gained{color=#FFFF00} 450 gold!{/color}"
            if (exp >= 10000):
                $slayer.level += 1
                call levelup from _call_levelup_5
                $exp = 0
            if (kokabiel_orb is False):
                "You obtained 1 demon soul."
                $kokabiel_orb = True
                $inventory["Fallen Soul"]=1
                call reload from _call_reload_3
            if(boolevel3 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel3 = False
                    hide screen hp_bars_kokabiel
                    jump level3
                    return
            elif (boolevel2 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel2 = False
                    hide screen hp_bars_kokabiel
                    jump level2
                    return
            elif (boolevel1 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel1 = False
                    hide screen hp_bars_kokabiel
                    jump level1
                    return


        #Opponent ATTACK
        with Pause(.80)
        show slayer idle with dissolve:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
        hide screen showenemyDamageTaken
        hide screen showplayerDamageTaken

        call random_select from _call_random_select_13
        if(randomn <=69 ):
            #Attack1
            $textvar = ""
            $enemydamage = kokabiel.attack_dmg
            show kokabiel attack with dissolve: 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1098.0, 342.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)
            play sound1("images/sounds/lightbeam.mp3") 
            show kokabiel_projectile1 zorder 2:
                subpixel True 
                rotate -9.0
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1305.0, 477.0, -54.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.04 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-54.0, 657.0, -54.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(1.14)

            ##SCREEN##
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= kokabiel.attack_dmg
            show slayer hit
            play sound1("images/sounds/playerhurt.mp3") 
        elif(randomn <= 85):
            #Attack2
            $textvar = "CRITICAL!"
            $enemydamage = kokabiel.attack_dmg + kokabiel.attack_dmg * 1.5
            show kokabiel attack with dissolve: 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1098.0, 342.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)
            play sound1("images/sounds/lightbeam2.mp3") 
            show kokabiel_projectile1 zorder 2:
                subpixel True 
                rotate 90.0
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1386.0, 189.0, -54.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 0.37 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1386.0, -1278.0, -54.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(0.47)
            show kokabiel_holy zorder 2:
                rotate 180.0
                matrixtransform ScaleMatrix(1.0, 2.45, 1.0)*OffsetMatrix(117.0, 405.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.20)

            ##SCREEN##
            play sound3("images/sounds/critical.wav") 
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= kokabiel.attack_dmg + kokabiel.attack_dmg * 1.5
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3") volume 0.5
        else:
            #Attack3
            $textvar = "CRITICAL!!!"
            $enemydamage = kokabiel.attack_dmg + kokabiel.attack_dmg * 2
            show kokabiel attack with dissolve: 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1098.0, 342.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)
            play sound1("images/sounds/lightbeam2.mp3") 
            show kokabiel_projectile1 zorder 2:
                subpixel True 
                rotate 90.0
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1386.0, 189.0, -54.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 0.37 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1386.0, -1278.0, -54.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(0.47)   
            show kokabiel_thunder zorder 2:
                matrixtransform ScaleMatrix(1.78, 2.46, 1.0)*OffsetMatrix(162.0, 153.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.30)

            ##SCREEN##
            play sound3("images/sounds/critical.wav") 
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= kokabiel.attack_dmg + kokabiel.attack_dmg * 2
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3") volume 0.5



       




       
        
        




     

    "{color=#FF0000}You died.{/color}"
    if(boolevel3):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel3 = False
        hide screen hp_bars_kokabiel
        jump level3
        return
    elif (boolevel2):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel2 = False
        hide screen hp_bars_kokabiel
        jump level2
        return
    elif (boolevel1):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel1 = False
        hide screen hp_bars_kokabiel
        jump level1
        return
    return