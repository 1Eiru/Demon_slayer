

label slayer_v_beelzebub:
    $renpy.music.stop(channel="tower_music", fadeout=.5)
    $renpy.music.play("images/sounds/fight.mp3","fight_music", loop=True)
    hide screen level_info
    $ slayer.hp = slayer.max_hp
    $ beelzebub.hp = beelzebub.max_hp
    $playerdamage = slayer.attack_dmg
    $enemydamage = beelzebub.attack_dmg
    show screen hp_bars_beelzebub
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
    
    show beelzebub idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1143.0, 414.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)

    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
    "{color=#27ff00}Player Hp: [slayer.hp]{/color}\n{color=#27ff00}Damage: [slayer.attack_dmg]{/color}\n{color=#FF0000}Enemy Hp:[beelzebub.hp]\nEnemy Damage:[beelzebub.attack_dmg]{/color}"

    while slayer.hp > 0 and beelzebub.hp > 0:
        #PLAYER ATTACK
        menu:
            
            "Slash":
                call camera_slayer_attack from _call_camera_slayer_attack_1
                play sound1("images/sounds/sword.mp3") volume .2
                $ beelzebub.hp -=  slayer.attack_dmg
                show beelzebub hit:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
                play sound2("images/sounds/bosshurt.mp3") volume .5
            
            "Stab":
                call camera_slayer_stab from _call_camera_slayer_stab_1
                show beelzebub hit:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
                play sound1("images/sounds/bosshurt.mp3") volume .5
                call random_select from _call_random_select_18
                if (randomstab <= 30):
                    $ beelzebub.hp -= slayer.attack_dmg * 2
                    play sound2("images/sounds/critical.wav")
                    show screen showenemyDamageTaken(slayer.attack_dmg * 2)
                else:
                    $ beelzebub.hp -=  slayer.attack_dmg - slayer.attack_dmg * 0.5
                    show screen showenemyDamageTaken(slayer.attack_dmg - slayer.attack_dmg * 0.5)  

            "Inventory":
                call screen inventory_screenx()
        if(inventoryattack):
            show beelzebub hit:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
            play sound2("images/sounds/bosshurt.mp3") volume .5
            $inventoryattack = False

    ############## CHECK ###########
        if ( beelzebub.hp <= 0):
            $gold += 450
            $temp = 3500 * (beelzebub.level/slayer.level)
            $exp += temp
            "You slayed {color=#FF0000}Beelzebub!{/color}"
            "You gained: {color=#FFFF00} [temp:.02f]EXP!{/color}{p}You gained{color=#FFFF00} 450 gold!{/color}"
            if (exp >= 10000):
                $slayer.level += 1
                call levelup from _call_levelup_1
                $exp = 0
            if (beelzebub_orb is False):
                "You obtained 1 demon soul."
                $beelzebub_orb = True
                $inventory["Gluttony's soul"] =1
                call reload from _call_reload_1
            if(boolevel3 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel3 = False
                    hide screen hp_bars_beelzebub
                    jump level3
                    return
            elif (boolevel2 == True):   
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel2 = False
                    hide screen hp_bars_beelzebub
                    jump level2
                    return
            elif (boolevel1 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel1 = False
                    hide screen hp_bars_beelzebub
                    jump level1
                    return


        #Opponent ATTACK
        
        $renpy.pause(1.07, hard=True)
        hide screen showenemyDamageTaken
        show slayer idle with dissolve:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)

        

       
        call random_select from _call_random_select_9

        if (randomn <=10 ): 
            #ATTACK1
            $textvar = "CRITICAL"
            $enemydamage = beelzebub.attack_dmg *2
            show beelzebub attack:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(882.0, 315.0, 675.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.90)
            show beelzebub_projectile2 zorder 2:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(513.0, 567.0, 927.0)*RotateMatrix(0.0, 0.0, 0.0)
            play sound1("images/sounds/raze.mp3") volume 1.0
            with Pause(.30)
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3") volume 0.2

            ##SCREEN##
            play sound3("images/sounds/critical.wav")
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= beelzebub.attack_dmg * 2

            with Pause(.10)
            show beelzebub idle zorder 0 with dissolve:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1143.0, 414.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)

        elif(randomn <=20):
            #ATTACK2
            $textvar = "Lifesteal/Critical"
            $enemydamage = beelzebub.attack_dmg *2
            show beelzebub attack2:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(882.0, 387.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.90)
            show beelzebub_projectile zorder 2:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1161.0, 531.0, 927.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 0.72 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(540.0, 603.0, 927.0)*RotateMatrix(0.0, 0.0, 0.0) 
            play sound1("images/sounds/raze.mp3") volume 1.0
            with Pause(0.82)
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3") volume 0.2
            ##SCREEN##
            play sound3("images/sounds/critical.wav")
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= beelzebub.attack_dmg * 2
            $ beelzebub.hp += 2

            with Pause(.10)

        elif(randomn <=60):
            #ATTACK3
            $textvar = ""
            $enemydamage = beelzebub.attack_dmg +1
            show beelzebub run zorder 2:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 621.0, 270.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.19 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(252.0, 621.0, 270.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(1.0)
            show beelzebub attack:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(234.0, 306.0, 774.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause (.20)
            play sound1("images/sounds/beelattack1.mp3")
            with Pause (.30)
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3")

            #SCREEN
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= beelzebub.attack_dmg +1

            with Pause(1.0)
        else:
            #ATTACK4
            $textvar = ""
            $enemydamage = beelzebub.attack_dmg
            show beelzebub run zorder 2:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 621.0, 270.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.19 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(252.0, 621.0, 270.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(1.0)
            show beelzebub attack2:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(234.0, 360.0, 747.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause (.40)
            play sound1("images/sounds/beelattack1.mp3")
            with Pause (.40)
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3")

            ##SCREEN
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= beelzebub.attack_dmg

            with Pause(1.0)
        hide screen showplayerDamageTaken
        show beelzebub idle zorder 0 with dissolve:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1143.0, 414.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)



    
 
        




     

    "{color=#FF0000}You died.{/color}"
    if(boolevel3):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel3 = False
        hide screen hp_bars_beelzebub
        jump level3
        return
    elif (boolevel2):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel2 = False
        hide screen hp_bars_beelzebub
        jump level2
        return
    elif (boolevel1):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel1 = False
        hide screen hp_bars_beelzebub
        jump level1
        return
    return