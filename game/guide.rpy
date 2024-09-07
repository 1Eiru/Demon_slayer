label guide:
    hide screen shop_screen
    camera:
        perspective True
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(18.0, 18.0, 855.0)*RotateMatrix(0.0, 0.0, 0.0)


    scene bg_guide

    show guide idle:
        matrixtransform ScaleMatrix(1.35, 1.29, 1.0)*OffsetMatrix(675.0, 414.0, 207.0)*RotateMatrix(0.0, 0.0, 0.0)

    menu tr:
        "Ask.":
            menu ask:
                "Where do i find a demon boss?":
                    play audio "images/sounds/tts/guide/demonboss.mp3"
                    "Major demons are located on every 10th floor of the tower."
                    with Pause(.03)
                    jump ask
                "Demon souls?":
                    play audio "images/sounds/tts/guide/demonsouls.mp3"
                    "Demon souls are obtained from Demon bosses. 5 demon souls are required to destroy the tower."
                    with Pause(.05)
                    jump ask
                "Back.":
                    call screen mapUI
        "Give 5 demon souls.":
            if ( len(inventory) is 5):
                play audio "images/sounds/tts/guide/youdidit.mp3"
                "You did it, slayer!"
                with Pause(0.1)
                jump story3

            else:
                play audio "images/sounds/tts/guide/notenough.mp3"
                "Not enough souls."
                with Pause(0.1)
                jump tr
        "Back.":
                call screen mapUI