label slayer_v_aamon:
    
    $renpy.music.stop(channel="tower_music", fadeout=.5)
    $renpy.music.play("images/sounds/fight.mp3","fight_music", loop=True)
    hide screen level_info
    $ slayer.hp = slayer.max_hp
    $ aamon.hp = aamon.max_hp
    $playerdamage = slayer.attack_dmg
    $enemydamage = aamon.attack_dmg
    show screen hp_bars_aamon
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
    
    show aamon idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(981.0, 540.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)



    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
    "{color=#27ff00}Player Hp: [slayer.hp]{/color}\n{color=#27ff00}Damage: [slayer.attack_dmg]{/color}\n{color=#FF0000}Enemy Hp:[aamon.hp]\nEnemy Damage:[aamon.attack_dmg]{/color}"

    while slayer.hp > 0 and aamon.hp > 0:
        #PLAYER ATTACK
        menu:
            
            "Slash":
                call camera_slayer_attack from _call_camera_slayer_attack
                play sound1("images/sounds/sword.mp3") volume .2
                $ aamon.hp -=  slayer.attack_dmg
                show aamon hit
                play sound2("images/sounds/bosshurt.mp3") volume .5
            "Stab":
                call camera_slayer_stab from _call_camera_slayer_stab
                play sound1("images/sounds/bosshurt.mp3")
                show aamon hit
                call random_select from _call_random_select_17
                if (randomstab <= 30):
                    $ aamon.hp -= slayer.attack_dmg * 2
                    play sound2("images/sounds/critical.wav")
                    show screen showenemyDamageTaken(slayer.attack_dmg * 2)
                else:
                    $ aamon.hp -=  slayer.attack_dmg - slayer.attack_dmg * 0.5
                    show screen showenemyDamageTaken(slayer.attack_dmg - slayer.attack_dmg * 0.5)  

            "Inventory":
                call screen inventory_screenx()
            
        if(inventoryattack):
            show aamon hit
            play sound2("images/sounds/bosshurt.mp3") volume .5
            $inventoryattack = False

    ############## CHECK ###########
        if ( aamon.hp <= 0):
            $gold += 450
            $temp = 3500 * (aamon.level/slayer.level)
            $exp += temp
            "You slayed {color=#FF0000}Aamon!{/color}"
            "You gained: {color=#FFFF00} [temp:.02f]EXP!{/color}{p}You gained{color=#FFFF00} 450 gold!{/color}"
            if (exp >= 10000):
                $slayer.level += 1
                call levelup from _call_levelup
                $exp = 0
            if (aamon_orb is False):
                "You obtained 1 demon soul."
                $aamon_orb = True
                $inventory["Aamon's soul"] =1
                call reload from _call_reload
            if(boolevel3 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel3 = False
                    hide screen hp_bars_aamon
                    jump level3
                    return
            elif (boolevel2 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)   
                    $ boolevel2 = False
                    hide screen hp_bars_aamon
                    jump level2
                    return
            elif (boolevel1 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel1 = False
                    hide screen hp_bars_aamon
                    jump level1
                    return


        #Opponent ATTACK
        with Pause(.70)
        show slayer idle with dissolve:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)

        hide screen showenemyDamageTaken
        hide screen showplayerDamageTaken
        call random_select from _call_random_select_8

        if (randomn <=33):
            #attack1
            $textvar = ""
            $enemydamage = aamon.attack_dmg
            play sound2("images/sounds/fly.mp3") volume 0.5
            show aamon move:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(981.0, 540.0, 738.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.02 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(297.0, 477.0, 738.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(1.12)
            play sound1("images/sounds/flame.mp3")
            show aamon attack zorder 2:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(153.0, 531.0, 513.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.30)
            ##SCREEN##
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= aamon.attack_dmg

            show slayer hit
            play sound3("images/sounds/playerhurt.mp3")
            with Pause(.80)
            show aamon idle zorder 0 with dissolve:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(981.0, 540.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)
        
        elif(randomn <=66):
            #attack2
            $textvar = "CRITICAL"
            $enemydamage = aamon.attack_dmg + aamon.attack_dmg *1.5
            show aamon attack with dissolve
            show belial_fireball:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2178.0, 1206.0, -3195.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 0.47 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1620.0, 1206.0, -3195.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(0.57)
            show bomb zorder 2:
                matrixtransform ScaleMatrix(1.52, 1.6, 1.0)*OffsetMatrix(288.0, 396.0, 774.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.70)
            play sound1("images/sounds/explosion.mp3")
            ##SCREEN##
            play sound3("images/sounds/critical.wav")
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= aamon.attack_dmg * 1.5

            show slayer hit
            play sound2("images/sounds/playerhurt.mp3")
        else:
            #attack3
            $textvar = "CRITICAL!!!"
            $enemydamage = aamon.attack_dmg + aamon.attack_dmg * 2
            play sound2("images/sounds/fly.mp3") volume 0.5
            show aamon move:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(981.0, 540.0, 738.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.02 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(297.0, 477.0, 738.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(1.00)
            show aamon idle
            with Pause(.20)
            show breath zorder 2:
                zpos 0.0
                rotate 27.0
                crop (0.0, 0.0, 1.0, 1.0)
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(63.0, 360.0, 738.0)*RotateMatrix(0.0, 180.0, 0.0)
                xpan 0.0
                ypan 0.0
                xtile 1
            with Pause(.20)
            show breath_hit zorder 2:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(432.0, 549.0, 738.0)*RotateMatrix(0.0, 180.0, -36.0)
            play sound2("images/sounds/firebreath.mp3")
            with Pause(.20)
            ##SCREEN##
            play sound3("images/sounds/critical.wav")
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= aamon.attack_dmg * 2

            show slayer hit
            play sound1("images/sounds/playerhurt.mp3")
            with Pause(1.80)
            show aamon idle zorder 0 with dissolve:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(981.0, 540.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0)



    "{color=#FF0000}You died.{/color}"
    if(boolevel3):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel3 = False
        hide screen hp_bars_aamon
        jump level3
        return
    elif (boolevel2):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel2 = False
        hide screen hp_bars_aamon
        jump level2
        return
    elif (boolevel1):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel1 = False
        hide screen hp_bars_aamon
        jump level1
        return
    return