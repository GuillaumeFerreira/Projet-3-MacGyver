#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

    Game, make evolve MacGyver in the labyrinth and help him to escape.

'''
from tkinter import PhotoImage, Canvas, NW, Button, Label
from PIL import Image, ImageTk
from doc_class.Personnage import Personnage
from doc_class.Object import Objet
from doc_class.ElementTK import Fenetre, FrameLab, Onglet
from utils.Func import creation_of_the_labyrinth, pick_up_objects_and_win


def main():
    '''

        function to create, manage events in real time

    '''
    ################################
    #Pour passer la fonction .bind()
    global LISTE_OBJET
    global MAC
    global ONGLET_OBJET
    global ONGLET_GARDIEN
    global GARDIEN_LAB
    ################################
    #Pour passer command
    global FENETRE
    ###############################

    FENETRE = Fenetre('Labyrinthe P3', 1400, 1000)
    FENETRE.build()

    frame_fabyrinthe = FrameLab(FENETRE.fenetre, 680, 680, 400, 10)
    frame_fabyrinthe.build()

    ONGLET_OBJET = Onglet(FENETRE.fenetre, "Objets récupérés", 20, 20, 50, 200)
    ONGLET_OBJET.build()

    onglet_conseil = Onglet(FENETRE.fenetre, "Conseil", 20, 20, 50, 50)
    onglet_conseil.build()
    onglet_conseil.change_text("Ramasser tous les objets avant de se présenter \n au gardien. Il tient beaucoup à ses objets.")

    ONGLET_GARDIEN = Onglet(FENETRE.fenetre, "Gardien", 20, 20, 50, 400)
    ONGLET_GARDIEN.build()
    ONGLET_GARDIEN.change_text("Personne ne sortira tant que je ne serai pas satisfait!")

    #################################################
    #Initialisation et construction de labyrinthe
    photo = PhotoImage(file="images/wall.gif")
    creation_of_the_labyrinth(photo, frame_fabyrinthe.frame)
    #################################################
    #################################################
    #création de MacGayver
    photo_mac_gyver = PhotoImage(file="images/macgyver.gif")

    MAC = Personnage.mac_gyver(frame_fabyrinthe.frame, photo_mac_gyver)
    #################################################
    #################################################
    #Creation de la liste d objets
    photo_objet = PhotoImage(file="images/tc-image005.gif")
    LISTE_OBJET = []
    for i in range(6):
        new_objet = Objet(frame_fabyrinthe.frame, photo_objet, i)
        LISTE_OBJET.append(new_objet)
    #################################################
    #Creation du gardien
    photo_gardien = PhotoImage(file="images/gardien.gif")
    GARDIEN_LAB = Personnage.gardien(frame_fabyrinthe.frame, photo_gardien)
    ##################################################
    ##################################################
    #petit escalier
    photo_escalier = Image.open('images/tc-image007.png')
    canvas15 = Canvas(frame_fabyrinthe.frame, width=32, height=36, borderwidth=0, highlightthickness=0)

    resolution = (100, 263)
    img = ImageTk.PhotoImage(photo_escalier.resize(resolution))
    canvas15.create_image(-2, -200, anchor=NW, image=img)
    canvas15.place(x=592, y=610)

    #Si pression sur la touche directionnelle fleche droite du clavier déclenche fonction versDroite
    FENETRE.fenetre.bind('<Right>', right)
    #Si pression sur la touche directionnelle fleche gauche du clavier déclenche fonction versGauche
    FENETRE.fenetre.bind('<Left>', left)
    #Si pression sur la touche directionnelle fleche haut du clavier déclenche fonction versHaut
    FENETRE.fenetre.bind('<Up>', move_up)
    #Si pression sur la touche directionnelle fleche bas du clavier déclenche fonction versBas
    FENETRE.fenetre.bind('<Down>', down)

    FENETRE.fenetre.mainloop()

def victoire_or_not():
    '''

        Watch if the player has met the objectives.

    '''
    situation = pick_up_objects_and_win(LISTE_OBJET, MAC, ONGLET_OBJET, ONGLET_GARDIEN, GARDIEN_LAB)
    if situation == 1:
        perdu()
    elif situation == 2:
        gagner()
    else:
        pass

def right(evt):
    '''

       If pressing the arrow key right arrow key triggers function right.

    '''
    MAC.move_to_the_right()
    victoire_or_not()

def left(evt):
    '''

       If pressing the arrow key right arrow key triggers function left.

    '''
    MAC.move_to_the_left()
    victoire_or_not()

def move_up(evt):
    '''

       If pressing the arrow key right arrow key triggers function move_up.

    '''
    MAC.move_to_the_up()
    victoire_or_not()

def down(evt):
    '''

       If pressing the arrow key right arrow key triggers function down.

    '''
    MAC.move_to_the_down()
    victoire_or_not()

def perdu():
    '''

       Show the window when the game loses.

    '''
    #declaration global pour passer command
    global FENETRE_PERDU
    FENETRE_PERDU = Fenetre('Game Over', 400, 250)
    FENETRE_PERDU.build()
    label = Label(FENETRE_PERDU.fenetre, text="Gardien : Je t'avais prévenu ! Bye bye mon ami!\n \n Tu as perdu, mais ne te décourage pas, recommence.")
    label.place(x=50, y=40)
    FENETRE.dont_move()
    Button(FENETRE_PERDU.fenetre, text='Quitter', command=quit).place(x=90, y=180)
    Button(FENETRE_PERDU.fenetre, text='Rejouer', command=rejouer_loose).place(x=230, y=180)

def gagner():
    '''

       Show the window when the game win.

    '''
    #declaration global pour passer command
    global FENETRE_GAGNER
    FENETRE_GAGNER = Fenetre('Victoire', 400, 150)
    FENETRE_GAGNER.build()
    label = Label(FENETRE_GAGNER.fenetre, text="Bravo, le gardien t'a finalement laissé passer, tu es libre!")
    label.place(x=50, y=40)
    FENETRE.dont_move()
    Button(FENETRE_GAGNER.fenetre, text='Quitter', command=quit).place(x=120, y=80)
    Button(FENETRE_GAGNER.fenetre, text='Rejouer', command=rejouer).place(x=250, y=80)

def rejouer():
    '''

        close the window and start the game again

    '''
    FENETRE_GAGNER.close_the_window()
    FENETRE.close_the_window()
    main()
def rejouer_loose():
    '''

        close the window and start the game again

    '''
    FENETRE_PERDU.close_the_window()
    FENETRE.close_the_window()
    main()

main()
