screen gameUI:
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "tetras.png"
        action ShowMenu("TetrasUI")

screen TetrasUI:
    #add "tetras"
    frame:
        xalign 0.5
        yalign 0.5
        xpadding 30
        ypadding 30

        hbox:
            spacing 40

            vbox:
                spacing 10
                text "Glass" size 40
                text "Cobalt" size 40
                text "Yttrium" size 40
                text "Wood" size 40

            vbox:
                spacing 10
                text "[glass]" size 40
                text "[cobalt]" size 40
                text "[yttrium]" size 40
                text "[wood]" size 40
    imagebutton:
        xalign 1.0
        yalign 0.0
        xoffset -30
        yoffset 30
        idle "backbutton.png"
        action Return()