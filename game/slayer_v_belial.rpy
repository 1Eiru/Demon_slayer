
label slayer_v_belial:
    $renpy.music.stop(channel="tower_music", fadeout=.5)
    $renpy.music.play("images/sounds/fight.mp3","fight_music", loop=True)
    hide screen level_info
    $powerup = True
    $ slayer.hp = slayer.max_hp
    $ belial.hp = belial.max_hp
    $playerdamage = slayer.attack_dmg
    $enemydamage = belial.attack_dmg
    show screen hp_bars_belial
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
    
    show belial idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)

    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
    "{color=#27ff00}Player Hp: [slayer.hp]{/color}\n{color=#27ff00}Damage: [slayer.attack_dmg]{/color}\n{color=#FF0000}Enemy Hp:[belial.hp]\nEnemy Damage:[belial.attack_dmg]{/color}"

    while slayer.hp > 0 and belial.hp > 0:
        #PLAYER ATTACK
        menu:
            
            "Slash":
                call camera_slayer_attack from _call_camera_slayer_attack_2
                play sound1("images/sounds/sword.mp3") volume 0.5
                $ belial.hp -=  slayer.attack_dmg 
                play sound2("images/sounds/belialhurt.mp3") volume 0.5
                show belial hit:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
            "Stab":
                call camera_slayer_stab from _call_camera_slayer_stab_2
                play sound1("images/sounds/belialhurt.mp3") 
                show belial hit:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
                call random_select from _call_random_select_19
                if (randomstab <= 30):
                    $ belial.hp -= slayer.attack_dmg * 2
                    play sound2("images/sounds/critical.wav")
                    show screen showenemyDamageTaken(slayer.attack_dmg * 2)
                else:
                    $ belial.hp -=  slayer.attack_dmg - slayer.attack_dmg * 0.5
                    show screen showenemyDamageTaken(slayer.attack_dmg - slayer.attack_dmg * 0.5)  
                    
            "Inventory":
                call screen inventory_screenx()

        if(inventoryattack):
            play sound2("images/sounds/belialhurt.mp3") volume .2
            show belial hit:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
            $inventoryattack = False


        ############## CHECK ###########
        if ( belial.hp <= 0):
            $gold += 450
            $temp = 3500 * (belial.level/slayer.level)
            $exp += temp
            "You slayed {color=#FF0000}Belial!{/color}"
            "You gained: {color=#FFFF00} [temp:.02f]EXP!{/color}{p}You gained{color=#FFFF00} 450 gold!{/color}"
            if (exp >= 10000):
                $slayer.level += 1
                call levelup from _call_levelup_2
                $exp = 0
            if (belial_orb is False):
                "You obtained 1 demon soul."
                $belial_orb = True
                $inventory["Belial's Soul"] =1
                call reload from _call_reload_2
            if(boolevel3 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel3 = False
                    hide screen hp_bars_belial
                    jump level3
                    return
            elif (boolevel2 == True):   
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel2 = False
                    hide screen hp_bars_belial
                    jump level2
                    return
            elif (boolevel1 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel1 = False
                    hide screen hp_bars_belial
                    jump level1
                    return

        $renpy.pause(.80, hard=True)
        show slayer idle with dissolve:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
        hide screen showenemyDamageTaken
        hide screen showplayerDamageTaken

        if (belial.hp <= 25):
            if (powerup):
                with Pause(.5)
                show slayer idle with dissolve:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
                play sound3("images/sounds/transform.mp3") 
                show belial powerup:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1233.0, -45.0, 558.0)*RotateMatrix(0.0, 0.0, 0.0)
                with Pause(2.0)
                $powerup = False

            

            call random_select from _call_random_select_10

            if (randomn <=20 ): 
                ##Attack 2
                $textvar = "CRITICAL"
                $enemydamage = belial.attack_dmg *2
                show belial powerattack:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
                with Pause(.70)
                play sound1("images/sounds/fireballbreath.mp3") volume 0.3
                show belial_fireball zorder 2:
                    subpixel True 
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2034.0, 1125.0, -2088.0)*RotateMatrix(0.0, 0.0, 0.0) 
                    linear 0.73 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1161.0, 1611.0, -2088.0)*RotateMatrix(0.0, 0.0, 0.0) 
                with Pause(0.83)
                show belial_explosion2 zorder 2:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(351.0, 459.0, 873.0)*RotateMatrix(0.0, 0.0, 0.0)
                show slayer hit
                play sound3("images/sounds/playerhurt.mp3") volume 0.5
                with Pause(1.50)
                play sound2("images/sounds/critical.wav")
                show screen showplayerDamageTaken(enemydamage,textvar)
                $ slayer.hp -= belial.attack_dmg * 2

                show slayer hit
            elif(randomn <=41 ):
                #Attack 3
                $textvar = "CRITICAL"
                $enemydamage = belial.attack_dmg + belial.attack_dmg * 1.5 
                show belial powerattack:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
                with Pause(.70)
                play sound1("images/sounds/fireballbreath.mp3") volume 0.3
                show belial_fireball zorder 2:
                    subpixel True 
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2034.0, 1125.0, -2088.0)*RotateMatrix(0.0, 0.0, 0.0) 
                    linear 0.62 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1197.0, 1125.0, -2088.0)*RotateMatrix(0.0, 0.0, 0.0) 
                with Pause(0.72)
                show belial_explosion1 zorder 2:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(585.0, 549.0, 1107.0)*RotateMatrix(0.0, 0.0, 0.0)
                play sound2("images/sounds/critical.wav")
                show screen showplayerDamageTaken(enemydamage,textvar)
                $ slayer.hp -= belial.attack_dmg + belial.attack_dmg * 1.5

                show slayer hit
                play sound3("images/sounds/playerhurt.mp3") volume 0.5
            else:
                #Attack4
                $textvar = ""
                $enemydamage = belial.attack_dmg + belial.attack_dmg * .5
                show belial powerattack:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
                with Pause(.70)
                show belial_projectile zorder 2:
                    subpixel True 
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1458.0, 846.0, -324.0)*RotateMatrix(0.0, 0.0, 0.0) 
                    linear 0.63 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-63.0, 846.0, -324.0)*RotateMatrix(0.0, 0.0, 0.0) 
                play sound1("images/sounds/fireball.mp3") volume 0.3
                with Pause(0.73)
                show belial_projectile_hit zorder 2:
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(297.0, 684.0, 477.0)*RotateMatrix(0.0, 0.0, 0.0)

                show screen showplayerDamageTaken(enemydamage,textvar)
                $ slayer.hp -= belial.attack_dmg + belial.attack_dmg * .5

                show slayer hit
                play sound3("images/sounds/playerhurt.mp3") volume 0.5
        else:
            #Opponent ATTACK
            #ATTACK1
            $textvar = ""
            $enemydamage = belial.attack_dmg
            show belial attack:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1251.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.70)
            show belial_projectile zorder 2:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1458.0, 846.0, -324.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 0.63 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-63.0, 846.0, -324.0)*RotateMatrix(0.0, 0.0, 0.0) 
            play sound1("images/sounds/fireball.mp3") volume 0.3
            with Pause(0.73)
            show belial_projectile_hit zorder 2:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(297.0, 684.0, 477.0)*RotateMatrix(0.0, 0.0, 0.0)

            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= belial.attack_dmg 

            show slayer hit
            play sound3("images/sounds/playerhurt.mp3") volume 0.5
            



     

    "{color=#FF0000}You died.{/color}"
    if(boolevel3):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $renpy.music.stop(channel="fight_music", fadeout=.5)
        $ boolevel3 = False
        hide screen hp_bars_belial
        jump level3
        return
    elif (boolevel2):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $renpy.music.stop(channel="fight_music", fadeout=.5)
        $ boolevel2 = False
        hide screen hp_bars_belial
        jump level2
        return
    elif (boolevel1):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $renpy.music.stop(channel="fight_music", fadeout=.5)
        $ boolevel1 = False
        hide screen hp_bars_belial
        jump level1
        return
    return