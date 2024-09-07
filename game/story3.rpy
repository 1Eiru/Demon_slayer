define g = Character("Guide")
define s = Character("Slayer")
define n = Character("Narrator")
label story3:
    $renpy.music.stop(channel="map_music", fadeout=.5)
    camera:
        perspective True
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)


    scene sad

    
    show guide idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(936.0, 540.0, 1116.0)*RotateMatrix(0.0, 0.0, 0.0)


    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1530.0, 612.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)

    play sound "images/sounds/explosion.mp3"
    show bomb:
        matrixtransform ScaleMatrix(4.43, 3.06, 1.0)*OffsetMatrix(36.0, 135.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)
    $renpy.pause(2.50, hard=True)

    scene happy with fade

    show guide idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(936.0, 540.0, 1116.0)*RotateMatrix(0.0, 0.0, 0.0)


    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1530.0, 612.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)
    
    play audio "images/sounds/tts/guide/endtts.mp3"
    g "You saved us! Slayer!"
    with Pause(.03)
    s "<3"
    play audio "images/sounds/tts/guide/end.mp3"
    n "The people of the town. The Guide and Slayer lived happily ever after."
    with Pause(.03)
    $renpy.music.play("images/sounds/map.mp3","map_music", loop=True)
    "Thank you for playing!"
    $renpy.pause(5.50, hard=True)
    return
    



                 