label slayer_v_demon:
    $renpy.music.stop(channel="tower_music", fadeout=.5)
    $renpy.music.play("images/sounds/fight.mp3","fight_music", loop=True)
    hide screen floor_info
    $ demon.level = enemy_level
    $ slayer.hp = slayer.max_hp
    $ demon.hp = demon.max_hp
    python:
        enemydamage = demon.attack_dmg
        playerdamage = slayer.attack_dmg
        textvar = ""
    show screen hp_bars_demon
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
    
    show demon idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)

    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(36.0, 693.0, 90.0)*RotateMatrix(0.0, 0.0, 0.0)

    "{color=#27ff00}Player Hp: [slayer.hp]{/color}\n{color=#27ff00}Damage: [slayer.attack_dmg]{/color}\n{color=#FF0000}Enemy Hp:[demon.hp]\nEnemy Damage:[demon.attack_dmg]{/color}"
    while slayer.hp > 0 and demon.hp > 0:
        menu slayer_v_demonmenu:
            "Slash":
                call camera_slayer_attack from _call_camera_slayer_attack_4
                play sound2("images/sounds/sword.mp3") volume 0.2
                $ demon.hp -=  slayer.attack_dmg
                call demon_hit from _call_demon_hit

            "Stab":
                call camera_slayer_stab from _call_camera_slayer_stab_4
                call demon_hit from _call_demon_hit_2
                call random_select from _call_random_select_21
                if (randomstab <= 30):
                    $ demon.hp -= slayer.attack_dmg * 2
                    play sound2("images/sounds/critical.wav")
                    show screen showenemyDamageTaken(slayer.attack_dmg * 2)
                else:
                    $ demon.hp -=  slayer.attack_dmg - slayer.attack_dmg * 0.5
                    show screen showenemyDamageTaken(slayer.attack_dmg - slayer.attack_dmg * 0.5) 

            "Inventory":
                call screen inventory_screenx()

        if(inventoryattack):
            call demon_hit from _call_demon_hit_1
            $inventoryattack = False
        
############## CHECK ###########
        if ( demon.hp <= 0):
            $gold += 150
            $temp = 2300 * (demon.level/slayer.level)
            $exp += temp
            hide screen showenemyDamageTaken
            show demon death
            "You slayed a {color=#FF0000}Demon!{/color}"
            "You gained: {color=#FFFF00} [temp:.02f]EXP!{/color}{p}You gained{color=#FFFF00} 150 gold!{/color}"
            if (exp >= 10000):
                $slayer.level += 1
                call levelup from _call_levelup_4
                $exp = 0
            if(boolevel3 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel3 = False
                    hide screen hp_bars_demon
                    jump level3
                    return
            elif (boolevel2 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel2 = False
                    hide screen hp_bars_demon
                    jump level2
                    return
            elif (boolevel1 == True):
                    $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
                    $ boolevel1 = False
                    hide screen hp_bars_demon
                    jump level1
                    return
###################################
        hide screen showplayerDamageTaken
        $renpy.pause(.80, hard=True)
        show slayer idle with dissolve: 
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(18.0, 666.0, 99.0)*RotateMatrix(0.0, 0.0, 0.0)

        
  
        show demon idle:
            subpixel True 
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0) 
            linear 1.09 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(468.0, 414.0, 765.0)*RotateMatrix(0.0, 0.0, 0.0) 
        $renpy.pause(1.09, hard=True)


        hide screen showenemyDamageTaken

        call random_select from _call_random_select_12
        if (randomn <=25):
            $textvar = "CRITICAL"
            $enemydamage = demon.attack_dmg *2
            show demon attack2 zorder 2:  
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(414.0, 387.0, 927.0)*RotateMatrix(0.0, 0.0, 0.0)
            $renpy.pause(1.5, hard=True)
            play sound1("images/sounds/normalfire.mp3") volume 0.2
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3") volume 0.5
            show screen showplayerDamageTaken(enemydamage,textvar)
            play sound3("images/sounds/critical.wav")
            $ slayer.hp -= demon.attack_dmg * 2
            $renpy.pause(1.0, hard=True)
            show demon idle zorder 0 with dissolve: 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
        else:
            $textvar = ""
            $enemydamage = demon.attack_dmg
            show demon attack zorder 2:
                subpixel True 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(405.0, 396.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0) 
                linear 1.50 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(369.0, 477.0, 621.0)*RotateMatrix(0.0, 0.0, 0.0) 
            $renpy.pause(1.60, hard=True)
            play sound1("images/sounds/normalfire.mp3") volume 0.3
            show slayer hit
            play sound2("images/sounds/playerhurt.mp3") volume 0.5
            show screen showplayerDamageTaken(enemydamage,textvar)
            $ slayer.hp -= demon.attack_dmg
            $renpy.pause(1.0, hard=True)
            show demon idle zorder 0 with dissolve: 
                matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
            

        
    "{color=#FF0000}You died.{/color}"
    if(boolevel3):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel3 = False
        hide screen hp_bars_demon
        jump level3
        return
    elif (boolevel2):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel2 = False
        hide screen hp_bars_demon
        jump level2
        return
    elif (boolevel1):
        $renpy.music.play("images/sounds/tower.wav","tower_music", loop=True)
        $ boolevel1 = False
        hide screen hp_bars_demon
        jump level1
        return
    return