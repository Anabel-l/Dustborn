screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tetrasidle.png"
        action ShowMenu("TetrasUI")



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