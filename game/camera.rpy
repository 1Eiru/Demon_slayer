label camera_slayer_attack:

    show slayer run zorder 1: 
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(18.0, 666.0, 99.0)*RotateMatrix(0.0, 0.0, 0.0) 
        linear 0.97 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1161.0, 666.0, 99.0)*RotateMatrix(0.0, 0.0, 0.0) 
    $renpy.pause(1.07, hard=True)

    show screen showenemyDamageTaken(playerdamage)
    return

label camera_slayer_stab:
    play sound1("images/sounds/swordthrust.mp3")
    show slayer stab zorder 1 with dissolve: 
        subpixel True 
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1161.0, 666.0, 99.0)*RotateMatrix(0.0, 0.0, 0.0) 
    $renpy.pause(.50, hard=True)
    return




label camera_level3:
    camera:
        perspective True
        subpixel True
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
        linear 1.41 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -225.0, 702.0)*RotateMatrix(0.0, 0.0, 0.0) 
        linear 1.51 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-270.0, -225.0, 702.0)*RotateMatrix(0.0, -18.0, 0.0) 
        linear 2.66 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
    return

label camera_level2:
    camera:
        perspective True
        subpixel True
        pos (0, 0)
        zpos 0.0
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
        linear 1.60 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-54.0, -144.0, 585.0)*RotateMatrix(0.0, 0.0, 0.0) 
        linear 1.49 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-54.0, -117.0, 873.0)*RotateMatrix(0.0, -18.0, 0.0) 
        linear 1.83 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-54.0, -306.0, 873.0)*RotateMatrix(0.0, -18.0, 0.0) 
        linear 0.63 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
    return
label demon_hit:
    show demon idle:
        subpixel True 
        matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
        linear 0.27 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(1.07)*HueMatrix(0.0) 
        linear 0.07 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    with Pause(.20)
    play sound1("images/sounds/demonhurt.mp3")
    with Pause(0.20)
    return

label cultist_hit:
    show cultist hit:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1404.0, 576.0, 189.0)*RotateMatrix(0.0, 0.0, 0.0)
    play sound1("images/sounds/cultisthurt.mp3") 
    $ renpy.pause(1.04, hard=True)
    return

label camera_level1: 
    camera:
        perspective True
        subpixel True
        parallel:
            zpos 0.0 
            linear 2.32 zpos -261.0 
            linear 2.72 zpos -306.0 
            linear 1.57 zpos 0.0 
        parallel:
            matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
            linear 2.32 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 9.0, 0.0) 
            linear 2.72 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, -18.0, 0.0) 
            linear 1.57 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
    return


