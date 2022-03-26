screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tetrasidle.png"
        action ShowMenu("TetrasUI")
    imagebutton:
        xalign 1.0
        yalign 0.1
        xoffset -30
        yoffset 30
        idle im.Scale("kaliruun.png", 70, 91)
        action ShowMenu("CharacterProfiles")

screen TetrasUI:
    frame:
        background "tetras"
        xalign 0.5
        yalign 0.5
        xpadding 80
        ypadding 10

        hbox:
            spacing 30

            vbox:
                spacing 15
                text "Glass" size 40
                text "Cobalt" size 40
                text "Yttrium" size 40
                text "Wood" size 40

            vbox:
                spacing 15
                text "[glass]" size 40
                text "[cobalt]" size 40
                text "[yttrium]" size 40
                text "[wood]" size 40
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "back.png"
        action Return()

screen CharacterProfiles:
    frame:
        background im.Scale("gui/frame.png", 600, 500)
        xalign 1.0
        yalign 1.0
        left_margin 400
        top_margin 50

        grid 4 3:
            xalign 0.5
            yalign 0.5
            spacing 40
            left_margin -280
            top_margin -150
            imagebutton:
                idle im.Scale("kaliruun.png", 70, 91)
                action ShowMenu("KaliruunStats")
            imagebutton:
                idle im.Scale("TorrSylos.png", 70, 91)
                action ShowMenu("TorrStats")
            text "Locked"
            text "Locked"

            text "Locked"
            text "Locked"
            text "Locked"
            text "Locked"

            text "Locked"
            text "Locked"
            text "Locked"
            text "Locked"

        imagebutton:
            xalign 1.0
            yalign 0.0
            xoffset -30
            yoffset 60
            idle "back.png"
            action Return()

screen KaliruunStats:
    frame:
        background "gui/frame.png"
        xalign 1.0
        yalign 1.0
        left_margin 400
        top_margin 50

        image "Stats/Kalistats.png"

        grid 12 5:
            spacing -6.2
            yspacing 6.9
            left_margin 386
            top_margin 77

            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

            image "Stats/Stat60.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

            image "Stats/Stat20.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

            image "Stats/Stat40.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

            image "Stats/Stat20.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

screen TorrStats:
    frame:
        background "gui/frame.png"
        xalign 1.0
        yalign 1.0
        left_margin 400
        top_margin 50

        image "Stats/Torrstats.png"

        grid 12 5:
            spacing -6.2
            yspacing 6.9
            left_margin 386
            top_margin 77

            image "Stats/Stat40.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

            image "Stats/Stat80.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

            image "Stats/Stat20.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

            image "Stats/Stat40.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"

            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"
            image "Stats/Stat0.png"