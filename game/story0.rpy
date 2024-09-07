label story0:
    camera:
        perspective True
    scene sad

    show guide idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(855.0, 540.0, 1116.0)*RotateMatrix(0.0, 0.0, 0.0)
    show slayer idle with dissolve:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(657.0, 612.0, 0.0)*RotateMatrix(0.0, 180.0, 0.0)

    play audio "images/sounds/tts/guide/thank.mp3"
    g "Thank God! Demon slayer, you've come!"
    with Pause(.03)
    play audio "images/sounds/tts/guide/those.mp3"
    g "Those monsters killed our people!"
    with Pause(.02)
    play audio "images/sounds/tts/guide/first.mp3"
    g "First, they spawned their tower, and the rest is history."
    with Pause(.02)
    play audio "images/sounds/tts/isee.mp3"
    s "I see... Tell me more..."
    hide guide idle with dissolve
    hide slayer idle with dissolve
    jump story1

                 