label slayer_v_skeleton: 
    $renpy.music.stop(channel="tower_music", fadeout=.5)
    $renpy.music.play("images/sounds/fight.mp3","fight_music", loop=True)
    hide screen floor_info
    $ skeleton.level = enemy_level
    $ slayer.hp = slayer.max_hp
    $ skeleton.hp = skeleton.max_hp
    python:
        enemydamage = skeleton.attack_dmg
        playerdamage = slayer.attack_dmg
        textvar = ""
    show screen hp_bars_skeleton
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
    
    show skeleton idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)

    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)
    "{color=#27ff00}Player Hp: [slayer.hp]{/color}\n{color=#27ff00}Damage: [slayer.attack_dmg]{/color}\n{color=#FF0000}Enemy Hp: [skeleton.hp]\nEnemy Damage: [skeleton.attack_dmg]{/color}"
    while slayer.hp > 0 and skeleton.hp > 0:
        menu:
            "Slash":
                call camera_slayer_attack from _call_camera_slayer_attack_7
                play sound1("images/sounds/sword.mp3") volume 0.2
                $ skeleton.hp -=  slayer.attack_dmg
                play sound2("images/sounds/skeletonhurt.mp3")
                show skeleton hurt
            "Stab":
                call camera_slayer_stab from _call_camera_slayer_stab_7
                play sound1("images/sounds/skeletonhurt.mp3")
                show skeleton hurt
                call random_select from _call_random_select_24
                if (randomstab <= 30):
                    $ skeleton.hp -= slayer.attack_dmg * 2
                    play sound2("images/sounds/critical.wav")
                    show screen showenemyDamageTaken(slayer.attack_dmg * 2)
                else:
                    $ skeleton.hp -=  slayer.attack_dmg - slayer.attack_dmg * 0.5
                    show screen showenemyDamageTaken(slayer.attack_dmg - slayer.attack_dmg * 0.5)


            "Inventory":
                call screen inventory_screenx()
        if(inventoryattack):
            show skeleton hurt
            play sound2("images/sounds/skeletonhurt.mp3")
            $inventoryattack = False
############## CHECK ###########
        if ( skeleton.hp <= 0):
            $gold += 150
            $temp = 2500 * (skeleton.level/slayer.level)
            $exp += temp
            show skeleton death:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
            hide screen showenemyDamageTaken
            "You slayed a {color=#FF0000}skeleton!{/color}"
            "You gained: {color=#FFFF00} [temp:.02f]EXP!{/color}{p}You gained{color=#FFFF00} 150 gold!{/color}"
            if (exp >= 10000):
                $slayer.level += 1
                call levelup from _call_levelup_7
                $exp = 0
            if(boolevel3 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel3 = False
                    hide screen hp_bars_skeleton
                    jump level3
                    return
            elif (boolevel2 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel2 = False
                    hide screen hp_bars_skeleton
                    jump level2
                    return
            elif (boolevel1 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel1 = False
                    hide screen hp_bars_skeleton
                    jump level1
                    return
###################################

        $renpy.pause(.80, hard=True)
        show slayer idle with dissolve: 
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(18.0, 666.0, 99.0)*RotateMatrix(0.0, 0.0, 0.0)
        hide screen showplayerDamageTaken
        hide screen showenemyDamageTaken
        
        call random_select from _call_random_select_16
        if (randomn <= 70):
            $enemydamage = skeleton.attack_dmg 
            show skeleton walk:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.25 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(315.0, 513.0, 495.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(1.35)
            play sound1("images/sounds/swordslash.mp3") volume .5
            show skeleton attack2 zorder 2:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(315.0, 387.0, 783.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.50)
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3")
            show screen showplayerDamageTaken(enemydamage, "")
            $slayer.hp -= skeleton.attack_dmg
            with Pause(1.10)
            show skeleton idle zorder 0 with dissolve:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
        else:
            $enemydamage = skeleton.attack_dmg *2
            show skeleton walk:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.25 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(315.0, 513.0, 495.0)*RotateMatrix(0.0, 0.0, 0.0) 
            with Pause(1.35)
            show skeleton attack1 zorder 2:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(315.0, 387.0, 783.0)*RotateMatrix(0.0, 0.0, 0.0)
            with Pause(.20)
            play sound1("images/sounds/swordthrust.mp3")
            with Pause(.10)
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3")
            play sound3("images/sounds/critical.wav")
            show screen showplayerDamageTaken(enemydamage, "CRITICAL!")
            $slayer.hp -= skeleton.attack_dmg * 2 
            with Pause(1.10)
            show skeleton idle zorder 0 with dissolve:
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)






    "{color=#FF0000}You died.{/color}"
    if(boolevel3):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel3 = False
        hide screen hp_bars_skeleton
        jump level3
        return
    elif (boolevel2):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel2 = False
        hide screen hp_bars_skeleton
        jump level2
        return
    elif (boolevel1):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel1 = False
        hide screen hp_bars_skeleton
        jump level1
        return
    return