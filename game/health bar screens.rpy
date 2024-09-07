
screen hp_bars_demon():
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "[slayer.name] - Level:[slayer.level]"
        bar value slayer.hp range slayer.max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[demon.name] - Level:[demon.level]"
        bar value demon.hp range demon.max_hp

screen hp_bars_cultist():
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "[slayer.name] - Level:[slayer.level]"
        bar value slayer.hp range slayer.max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[cultist.name] - Level:[cultist.level]"
        bar value cultist.hp range cultist.max_hp

screen hp_bars_skeleton():
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "[slayer.name] - Level:[slayer.level]"
        bar value slayer.hp range slayer.max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[skeleton.name] - Level:[skeleton.level]"
        bar value skeleton.hp range skeleton.max_hp

screen hp_bars_beelzebub():
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "[slayer.name] - Level:[slayer.level]"
        bar value slayer.hp range slayer.max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[beelzebub.name]"
        bar value beelzebub.hp range beelzebub.max_hp

screen hp_bars_belial():
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "[slayer.name] - Level:[slayer.level]"
        bar value slayer.hp range slayer.max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[belial.name]"
        bar value belial.hp range belial.max_hp

screen hp_bars_kokabiel():
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "[slayer.name] - Level:[slayer.level]"
        bar value slayer.hp range slayer.max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[kokabiel.name]"
        bar value kokabiel.hp range kokabiel.max_hp

screen hp_bars_aamon():
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "[slayer.name] - Level:[slayer.level]"
        bar value slayer.hp range slayer.max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[aamon.name]"
        bar value aamon.hp range aamon.max_hp

screen hp_bars_satan():
    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "[slayer.name] - Level:[slayer.level]"
        bar value slayer.hp range slayer.max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "[satan.name]"
        bar value satan.hp range satan.max_hp