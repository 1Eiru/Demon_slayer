define g = Character("Guide")
define s = Character("Slayer")
label story1:
    camera:
        perspective True
    scene happy

    show guide idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(855.0, 540.0, 1116.0)*RotateMatrix(0.0, 0.0, 0.0)
    show slayer idle with fade:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(657.0, 612.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)


    play audio "images/sounds/tts/guide/peace.mp3"
    g "We’ve been living peacefully.Happy town. Lively people. Know what i'm saying?"
    with Pause(.05)
    play audio "images/sounds/tts/yeah.mp3"
    s "Yeah, i hear you..."
    with Pause(.01)
    play audio "images/sounds/tts/guide/suddenly.mp3"
    g "Then, suddenly, a tower erupted from the ground!"
    with Pause(.03)
    play audio "images/sounds/tts/guide/save.mp3"
    g "Please, slayer... save our town and the people."
    with Pause(.02)
    play audio "images/sounds/tts/aye.mp3"
    s "Aye, for sure, that is my job anyway..."
    with Pause(.01)
    play audio "images/sounds/tts/start.mp3"
    s "Let's get started."
    with Pause(.01)

    hide guide idle with dissolve
    hide slayer idle with dissolve
    $renpy.music.play("images/sounds/map.mp3","map_music", loop=True)
    call screen mapUI




                 