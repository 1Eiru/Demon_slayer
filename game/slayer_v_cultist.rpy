label slayer_v_cultist:
    $renpy.music.stop(channel="tower_music", fadeout=.5)
    $renpy.music.play("images/sounds/fight.mp3","fight_music", loop=True)
    hide screen floor_info
    $ cultist.level = enemy_level
    $ slayer.hp = slayer.max_hp
    $ cultist.hp = cultist.max_hp
    python:
        enemydamage = cultist.attack_dmg
        playerdamage = slayer.attack_dmg
        textvar = ""
    show screen hp_bars_cultist
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
    
    show cultist idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)

    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
    "{color=#27ff00}Player Hp: [slayer.hp]{/color}\n{color=#27ff00}Damage: [slayer.attack_dmg]{/color}\n{color=#FF0000}Enemy Hp: [cultist.hp]\nEnemy Damage: [cultist.attack_dmg]{/color}"
    while slayer.hp > 0 and cultist.hp > 0:
        menu:
            "Slash":
                call camera_slayer_attack from _call_camera_slayer_attack_3
                play sound2("images/sounds/sword.mp3") volume 0.2
                $ cultist.hp -=  slayer.attack_dmg
                call cultist_hit from _call_cultist_hit

            "Stab":
                call camera_slayer_stab from _call_camera_slayer_stab_3
                call cultist_hit from _call_cultist_hit_2
                call random_select from _call_random_select_20
                if (randomstab <= 30):
                    $ cultist.hp -= slayer.attack_dmg * 2
                    play sound2("images/sounds/critical.wav")
                    show screen showenemyDamageTaken(slayer.attack_dmg * 2)
                else:
                    $ cultist.hp -=  slayer.attack_dmg - slayer.attack_dmg * 0.5
                    show screen showenemyDamageTaken(slayer.attack_dmg - slayer.attack_dmg * 0.5) 

            "Inventory":
                call screen inventory_screenx()
        if(inventoryattack):
            call cultist_hit from _call_cultist_hit_1
            $inventoryattack = False
############## CHECK ###########
        if ( cultist.hp <= 0):
            $gold += 150
            $temp = 2500 * (cultist.level/slayer.level)
            $exp += temp
            show cultist death:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
            hide screen showenemyDamageTaken
            "You slayed a {color=#FF0000}Cultist!{/color}"
            "You gained: {color=#FFFF00} [temp:.02f]EXP!{/color}{p}You gained{color=#FFFF00} 150 gold!{/color}"
            if (exp >= 10000):
                $slayer.level += 1
                call levelup from _call_levelup_3
                $exp = 0
            if(boolevel3 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel3 = False
                    hide screen hp_bars_cultist
                    jump level3
                    return
            elif (boolevel2 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel2 = False
                    hide screen hp_bars_cultist
                    jump level2
                    return
            elif (boolevel1 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel1 = False
                    hide screen hp_bars_cultist
                    jump level1
                    return
###################################

        
       
        show slayer idle with dissolve: 
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(18.0, 666.0, 99.0)*RotateMatrix(0.0, 0.0, 0.0)
        $renpy.pause(.1, hard=True)
        hide screen showplayerDamageTaken
        hide screen showenemyDamageTaken
        
        call random_select from _call_random_select_11
        if (randomn <=20):
            show cultist attack:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
            $ renpy.pause(1.5, hard=True)
            show spark:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(306.0, 756.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
            hide screen showenemyDamageTaken
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3")
            $textvar = "CRITICAL"
            $enemydamage = cultist.attack_dmg *2
            $ slayer.hp -= cultist.attack_dmg * 2
            play sound3("images/sounds/critical.wav")
        else:
            show cultist attack:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
            $ renpy.pause(1.5, hard=True)
            play sound1("images/sounds/fireball.mp3") volume 0.5
            show cultist_projectile:
                subpixel True 
                parallel:
                    matrixtransform ScaleMatrix(1.31, 1.17, 1.0)*OffsetMatrix(1044.0, 648.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0) 
                    linear 1.01 matrixtransform ScaleMatrix(1.31, 1.17, 1.0)*OffsetMatrix(153.0, 648.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0) 
                parallel:
                    alpha 0.0 
                    linear 0.14 alpha 1.0 
            $ renpy.pause(1.10, hard=True)
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3")
            $textvar = ""
            $enemydamage = cultist.attack_dmg
            $ slayer.hp -= cultist.attack_dmg

        show screen showplayerDamageTaken(enemydamage,textvar)
        
    "{color=#FF0000}You died.{/color}"
    if(boolevel3):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel3 = False
        hide screen hp_bars_cultist
        jump level3
        return
    elif (boolevel2):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel2 = False
        hide screen hp_bars_cultist
        jump level2
        return
    elif (boolevel1):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel1 = False
        hide screen hp_bars_cultist
        jump level1
        return
    return