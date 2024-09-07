label random_select:
    $randomn = renpy.random.randint(0,100)
    $randomstab = renpy.random.randint(0,100)
    $randomsec = renpy.random.randint(1,10)
    $randomdmg = renpy.random.randint(15,20)
    return
label enemy_level:
    if (counter is 0):
        $enemy_level = 1
        return
    elif (counter <= 5):
        $enemy_level = renpy.random.randint(1,5)
        return
    elif(counter <=10):
        $enemy_level = renpy.random.randint(6,10)
        return
    elif(counter <=15):
        $enemy_level = renpy.random.randint(11,15)
        return
    elif(counter <=20):
        $enemy_level = renpy.random.randint(16,20)
        return
    elif(counter <=25):
        $enemy_level = renpy.random.randint(21,25)
        return
    elif(counter <=30):
        $enemy_level = renpy.random.randint(26,30)
        return
    elif(counter <=35):
        $enemy_level = renpy.random.randint(31,35)
        return
    elif(counter <=40):
        $enemy_level = renpy.random.randint(36,40)
        return
    elif(counter <=45):
        $enemy_level = renpy.random.randint(41,45)
        return
    elif(counter > 45):
        $enemy_level = renpy.random.randint(46,50)
        return
    return

label monsteren:
    call random_select from _call_random_select
    if (randomn <= 33):
        jump slayer_v_demon
    elif(randomn<= 66):
        jump slayer_v_cultist
    else:
        jump slayer_v_skeleton
    return

label bossen:
    if (counter is 10):
        call random_select from _call_random_select_1
        if(randomn <= 50):
            jump slayer_v_aamon
            return
        else:
            call monsteren from _call_monsteren
            return
    elif (counter is 20):
        call random_select from _call_random_select_2
        if(randomn <= 50):
            jump slayer_v_beelzebub
            return
        else:
            call monsteren from _call_monsteren_1
            return
    elif (counter is 30):
        call random_select from _call_random_select_3
        if(randomn <= 50):
            jump slayer_v_belial
            return
        else:
            call monsteren from _call_monsteren_2
            return
    elif (counter is 40):
        call random_select from _call_random_select_4
        if(randomn <= 50):
            jump slayer_v_kokabiel
            return
        else:
            call monsteren from _call_monsteren_3
            return
    elif (counter is 50):
        call random_select from _call_random_select_5
        if(randomn <= 50):
            jump slayer_v_satan
            return
        else:
            call monsteren from _call_monsteren_4
            return
    call monsteren from _call_monsteren_5
    return



screen floor_info():        
    text "{color=#510303}current floor: {/color}{color=#7b0a0a}[counter] {/color}":
        outlines [ (absolute(2), "#894040", absolute(2), absolute(1)) ]
        xalign 0
        yalign 0
        
screen exp_info():        
    text "{color=#510303}Exp: [exp:.02f]/10,000{/color}":
        outlines [ (absolute(2), "#894040", absolute(2), absolute(1)) ]
        xalign 0
        yalign .05


label level1:
    $renpy.music.stop(channel="fight_music", fadeout=.5)
    $demon.attack_dmg = 1
    $demon.max_hp = 8
    $cultist.attack_dmg = 1.3
    $cultist.max_hp = 9
    $skeleton.attack_dmg = 1.2
    $skeleton.max_hp = 9
    $ max_floor[counter] = "level1"
    show screen floor_info
    show screen exp_info
    camera:
        perspective True
        ypos 0
        zpos 0.0
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    scene bg_tower_1:
        matrixtransform ScaleMatrix(1.05, 1.2, 1.0)*OffsetMatrix(378.0, 0.0, -189.0)*RotateMatrix(0.0, 0.0, 0.0)
    show tower_ground:
        matrixtransform ScaleMatrix(1.0, 1.29, 1.0)*OffsetMatrix(630.0, 720.0, -72.0)*RotateMatrix(45.0, 0.0, 0.0)
    show tower_sides
    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(891.0, 558.0, -108.0)*RotateMatrix(0.0, 18.0, 0.0)

    menu menu1:
        "Back to map":
            call reload from _call_reload_8
            $renpy.music.stop(channel="tower_music", fadeout=.5)
            $renpy.music.play("images/sounds/map.mp3","map_music", loop=True)
            $counter = 0
            $max_floor = [None] * 51
            hide screen floor_info
            hide screen exp_info 
            call screen mapUI
            

        "Go up (+1 floor)":
            if(counter is 50 ):
                "You are at the highest floor!"
                jump menu1
            else:
                if (max_floor[counter+1]is not None):
                    
                    $ counter+=1
                    jump expression max_floor[counter]
                    return
                else:
                    $ counter += 1
                    jump level_random
                    return
               
        "Go down (-1 floor)":
            if(counter <=0):
                
                "You are at floor 0!"
                jump menu1
                return
            else:

                $ counter -=1
                jump expression max_floor[counter]
                return

        "search for enemy":
            call search_for_enemy from _call_search_for_enemy
            call camera_level1 from _call_camera_level1
            $renpy.pause(random_time, hard=True)
            "Enemy found!"
            call enemy_level from _call_enemy_level
            $demon.max_hp = demon.max_hp + (enemy_level * .8)
            $demon.attack_dmg =  demon.attack_dmg  +  (enemy_level * .8)
            $cultist.max_hp = cultist.max_hp + (enemy_level * .8)
            $cultist.attack_dmg =  cultist.attack_dmg  +  (enemy_level * .8)
            $skeleton.max_hp = skeleton.max_hp + (enemy_level * .8)
            $skeleton.attack_dmg =  skeleton.attack_dmg  +  (enemy_level * .8)
            hide screen floor_info
            $ boolevel1 = True
            hide screen exp_info
            call bossen from _call_bossen
            return
    return

label level2:
    $renpy.music.stop(channel="fight_music", fadeout=.5)
    $cultist.attack_dmg = 1.3
    $cultist.max_hp = 9
    $demon.attack_dmg = 1
    $demon.max_hp = 8
    $skeleton.attack_dmg = 1.2
    $skeleton.max_hp = 9
    $ max_floor[counter] = "level2"
    show screen floor_info 
    show screen exp_info
    camera:
        perspective True
        ypos 0
        zpos 0.0
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)

    scene bg_tower_2:
        matrixtransform ScaleMatrix(1.21, 1.2, 1.0)*OffsetMatrix(378.0, 0.0, -189.0)*RotateMatrix(0.0, 0.0, 0.0)
    show tower_ground:
        matrixtransform ScaleMatrix(1.0, 1.29, 1.0)*OffsetMatrix(630.0, 720.0, -72.0)*RotateMatrix(45.0, 0.0, 0.0)
    show tower_sides
    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(891.0, 558.0, -108.0)*RotateMatrix(0.0, 171.0, 0.0)

    menu menu2:
        "Back to map":
            call reload from _call_reload_9
            $renpy.music.stop(channel="tower_music", fadeout=.5)
            $renpy.music.play("images/sounds/map.mp3","map_music", loop=True)
            $counter = 0
            hide screen floor_info
            hide screen exp_info 
            call screen mapUI

        "Go up (+1 floor)":
            if(counter is 50 ):
                "You are at the highest floor!"
                jump menu1
            else:
                if (max_floor[counter+1]is not None):              
                    $ counter+=1                
                    jump expression max_floor[counter]
                    return
                else:
                    $ counter += 1               
                    jump level_random
                    return

        "Go down (-1 floor)":
            if(counter <=0):
                
                "You are at floor 0!"
                jump menu2
                return
            else:

                $ counter -=1
                jump expression max_floor[counter]
                return
        "search for enemy":
            call search_for_enemy from _call_search_for_enemy_1
            call camera_level2 from _call_camera_level2
            $renpy.pause(random_time, hard=True)
            "Enemy found!"
            call enemy_level from _call_enemy_level_1
            $demon.max_hp = demon.max_hp + (enemy_level * .8)
            $demon.attack_dmg =  demon.attack_dmg  +  (enemy_level * .8)
            $cultist.max_hp = cultist.max_hp + (enemy_level * .8)
            $cultist.attack_dmg =  cultist.attack_dmg  +  (enemy_level * .8)
            $skeleton.max_hp = skeleton.max_hp + (enemy_level * .8)
            $skeleton.attack_dmg =  skeleton.attack_dmg  +  (enemy_level * .8)
            hide screen floor_info
            $ boolevel2 = True
            hide screen exp_info
            call bossen from _call_bossen_1
            return
    return


label level3:
    $renpy.music.stop(channel="fight_music", fadeout=.5)
    $cultist.attack_dmg = 1.3
    $cultist.max_hp = 9
    $demon.attack_dmg = 1
    $demon.max_hp = 8
    $skeleton.attack_dmg = 1.2
    $skeleton.max_hp = 9
    $ max_floor[counter] = "level3"
    show screen floor_info
    show screen exp_info
    camera:
        perspective True
        ypos 0
        zpos 0.0
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    scene bg_tower_3:
        matrixtransform ScaleMatrix(1.21, 1.2, 1.0)*OffsetMatrix(378.0, 0.0, -189.0)*RotateMatrix(0.0, 0.0, 0.0)
    show tower_ground:
        matrixtransform ScaleMatrix(1.0, 1.29, 1.0)*OffsetMatrix(630.0, 720.0, -72.0)*RotateMatrix(45.0, 0.0, 0.0)
    show tower_sides
    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(891.0, 558.0, -108.0)*RotateMatrix(0.0, 171.0, 0.0)
    
    menu menu3:
        "Back to map":   
            call reload from _call_reload_10
            $renpy.music.stop(channel="tower_music", fadeout=.5)
            $renpy.music.play("images/sounds/map.mp3","map_music", loop=True)
            $counter = 0     
            hide screen floor_info
            hide screen exp_info 
            call screen mapUI

        "Go up (+1 floor)":
            if(counter is 50 ):
                "You are at the highest floor!"
                jump menu1
            else:
                if (max_floor[counter+1]is not None):
                    
                    $ counter+=1
        
                    jump expression max_floor[counter]
                    return
                else:
                    $ counter += 1

                    jump level_random
                    return

        "Go down (-1 floor)":
            if(counter <=0):
                
                "You are at floor 0!"
                jump menu3
                return
            else:
   
                $ counter -= 1
                
                jump expression max_floor[counter]
                return

        "search for enemy":
            call search_for_enemy from _call_search_for_enemy_2
            call camera_level3 from _call_camera_level3
            $renpy.pause(random_time, hard=True)
            "Enemy found!"
            call enemy_level from _call_enemy_level_2
            $demon.max_hp = demon.max_hp + (enemy_level * .8)
            $demon.attack_dmg =  demon.attack_dmg  +  (enemy_level * .8)
            $cultist.max_hp = cultist.max_hp + (enemy_level * .8)
            $cultist.attack_dmg =  cultist.attack_dmg  +  (enemy_level * .8)
            $skeleton.max_hp = skeleton.max_hp + (enemy_level * .8)
            $skeleton.attack_dmg =  skeleton.attack_dmg  +  (enemy_level * .8)
            hide screen floor_info
            $ boolevel3 = True
            hide screen exp_info
            call bossen from _call_bossen_2
            return
    return




label search_for_enemy:
    call random_select from _call_random_select_6
    $ random_time = randomsec * .4
    return

label level_random:
    call random_select from _call_random_select_7

    if (randomn <=34):
        jump level1
    elif(randomn <=67):
        jump level2
    else:
        jump level3
    return
    
    



