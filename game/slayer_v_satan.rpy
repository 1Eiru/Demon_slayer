label slayer_v_satan:
    $renpy.music.stop(channel="tower_music", fadeout=.5)
    $renpy.music.play("images/sounds/fight.mp3","fight_music", loop=True)
    hide screen level_info
    $powerup = True
    $ slayer.hp = slayer.max_hp
    $ satan.hp = satan.max_hp
    $playerdamage = slayer.attack_dmg
    show screen hp_bars_satan
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
    
    show satan1 idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(990.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)

    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
    "{color=#27ff00}Player Hp: [slayer.hp]{/color}\n{color=#27ff00}Damage: [slayer.attack_dmg]{/color}\n{color=#FF0000}Enemy Hp:[satan.hp]\nEnemy Damage:[satan.attack_dmg]{/color}"

    while slayer.hp > 0 and satan.hp > 0:
        #PLAYER ATTACK
        menu:
            
            "Slash":
                call camera_slayer_attack from _call_camera_slayer_attack_6
                play sound2("images/sounds/sword.mp3") volume 0.2
                $ satan.hp -=  slayer.attack_dmg 
                if(powerup):
                    show satan1 hurt
                    play sound1("images/sounds/belialhurt.mp3") volume 0.5
                else:
                    show satan1 truehurt
                    play sound1("images/sounds/belialhurt.mp3") volume 0.5

            "Stab":
                call camera_slayer_stab from _call_camera_slayer_stab_6
                if(powerup):
                    show satan1 hurt
                    play sound1("images/sounds/belialhurt.mp3") volume 0.5
                else:
                    show satan1 truehurt
                    play sound1("images/sounds/belialhurt.mp3") volume 0.5
                call random_select from _call_random_select_23
                if (randomstab <= 30):
                    $ satan.hp -= slayer.attack_dmg * 2
                    play sound2("images/sounds/critical.wav")
                    show screen showenemyDamageTaken(slayer.attack_dmg * 2)
                else:
                    $ satan.hp -=  slayer.attack_dmg - slayer.attack_dmg * 0.5
                    show screen showenemyDamageTaken(slayer.attack_dmg - slayer.attack_dmg * 0.5) 

            "Inventory":
                call screen inventory_screenx()

        if(inventoryattack):
            if(powerup):
                show satan1 hurt
                play sound1("images/sounds/belialhurt.mp3") volume 0.5
            else:
                show satan1 truehurt
                play sound1("images/sounds/belialhurt.mp3") volume 0.5
            $inventoryattack = False
        ############## CHECK ###########
        if ( satan.hp <= 0):
            $gold += 450
            $temp = 5000 * (satan.level/slayer.level)
            $exp += temp
            "You slayed {color=#FF0000}Satan!{/color}"
            "You gained: {color=#FFFF00} [temp:.02f]EXP!{/color}{p}You gained{color=#FFFF00} 450 gold!{/color}"
            if (exp >= 10000):
                $slayer.level += 1
                call levelup from _call_levelup_6
                $exp = 0
            if (satan_orb is False):
                "You obtained 1 demon soul."
                $satan_orb = True
                $inventory["Satan's Soul"] =1
                call reload from _call_reload_4
            if(boolevel3 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel3 = False
                    hide screen hp_bars_satan
                    jump level3
                    return
            elif (boolevel2 == True):   
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel2 = False
                    hide screen hp_bars_satan
                    jump level2
                    return
            elif (boolevel1 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel1 = False
                    hide screen hp_bars_satan
                    jump level1
                    return
       
        #reset position
        $renpy.pause(.80, hard=True)
        show slayer idle with dissolve:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
        hide screen showenemyDamageTaken
        hide screen showplayerDamageTaken

        if (satan.hp <= 20 and powerup is True):
            show satan1 death
            $renpy.pause(1.20, hard=True)
            play sound3("images/sounds/transform.mp3") 
            show satan1 reborn
            $renpy.pause(2.10, hard=True)
            $satan.hp += 25
            $powerup = False

        if(powerup is False):
            call random_select from _call_random_select_14
            $enemydamage = randomdmg
            show satan1 truewalk zorder 2:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(990.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.26 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(171.0, 504.0, 603.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(2.00)
            play sound1("images/sounds/satan2attack.mp3")
            with Pause(0.30)
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3")
            show screen showplayerDamageTaken(enemydamage, "!!!")
            $ slayer.hp -= randomdmg
            show satan1 trueidle zorder 0 with dissolve:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(990.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)


        if(powerup):
            call random_select from _call_random_select_15
            if (randomn <= 51):
                $textvar = ""
                $enemydamage = satan.attack_dmg 
                show satan1 walk zorder 2:
                    subpixel True
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1098.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0) 
                    linear 0.88 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0) 
                with Pause(1.0)
                play sound1("images/sounds/satan1attack.mp3") volume 0.2
                with Pause(.50)
                show slayer hit
                play sound2("images/sounds/playerhurt.mp3")
                show screen showplayerDamageTaken(enemydamage,textvar)
                $ slayer.hp -= satan.attack_dmg

                show satan1 idle zorder 0 with dissolve: 
                    matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(990.0, 504.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0)
            else:
                $textvar = "CRITICAL"
                $enemydamage = satan.attack_dmg  * 2
                show satan1 cast
                play sound1("images/sounds/raze.mp3") volume 1.0
                show satan1_projectile zorder 2:
                    matrixtransform ScaleMatrix(3.43, 3.43, 1.0)*OffsetMatrix(-18.0, 108.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
                with Pause(.50)
                show slayer hit
                play sound2("images/sounds/playerhurt.mp3") volume 0.5
                play sound3("images/sounds/critical.wav") 
                show screen showplayerDamageTaken(enemydamage,textvar)
                $ slayer.hp -= satan.attack_dmg * 2

    


 





     

    "{color=#FF0000}You died.{/color}"
    if(boolevel3):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $renpy.music.stop(channel="fight_music", fadeout=.5)
        $ boolevel3 = False
        hide screen hp_bars_satan
        jump level3
        return
    elif (boolevel2):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $renpy.music.stop(channel="fight_music", fadeout=.5)
        $ boolevel2 = False
        hide screen hp_bars_satan
        jump level2
        return
    elif (boolevel1):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $renpy.music.stop(channel="fight_music", fadeout=.5)
        $ boolevel1 = False
        hide screen hp_bars_satan
        jump level1
        return
    return