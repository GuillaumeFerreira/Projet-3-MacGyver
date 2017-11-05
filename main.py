#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random
from ClassObject import *
from Func import *


     
def main():
    ################################
    #Pour passer la fonction .bind()
    global ListeObjet
    global Mac
    global ongletObjet
    global ongletGardien
    global GardienLab
    ################################
    #Pour passer command
    global fenetre
    ###############################
    
    fenetre=Fenetre('Labyrinthe P3',1400, 1000)
    fenetre.construction()
                             

    frameLabyrinthe=FrameLab(fenetre.fenetre,680,680,400,10)
    frameLabyrinthe.construction()

    ongletObjet=Onglet(fenetre.fenetre,"Objets récupérés",20,20,50,200)
    ongletObjet.construction()

    ongletConseil=Onglet(fenetre.fenetre,"Conseil",20,20,50,50)
    ongletConseil.construction()
    ongletConseil.changerTxt("Ramasser tous les objets avant de se présenter \n au gardien. Il tient beaucoup à ses objets.")

    ongletGardien=Onglet(fenetre.fenetre,"Gardien",20,20,50,400)
    ongletGardien.construction()
    ongletGardien.changerTxt("Personne ne sortira tant que je ne serai pas satisfait!")

    #################################################
    #Initialisation et construction de labyrinthe
    photo = PhotoImage(file="images/wall.gif")
    creationDuLabyrinthe(photo,frameLabyrinthe.frame)
    #################################################
    #################################################
    #création de MacGayver
    photoMacGayver=PhotoImage(file="images/macgyver.gif")
    
    Mac=MacGayver(frameLabyrinthe.frame,photoMacGayver)
    #################################################
    #################################################
    #Creation de la liste d objets
    photoObjet=PhotoImage(file="images/tc-image005.gif")
    ListeObjet=[]
    for i in range(6):
        newObjet=Objet(frameLabyrinthe.frame,photoObjet,i)
        ListeObjet.append(newObjet)
    #################################################  
    #################################################
    #Creation du gardien   
    photoGardien = PhotoImage(file="images/gardien.gif")
    GardienLab=Gardien(frameLabyrinthe.frame,photoGardien)
    ##################################################
    ##################################################
    #petit escalier
    photoEscalier=Image.open('images/tc-image007.png')
    canvas15 = Canvas(frameLabyrinthe.frame,width=32, height=36, borderwidth=0,highlightthickness=0)

    resolution = (100,263)
    img = ImageTk.PhotoImage(photoEscalier.resize(resolution))
    canvas15.create_image(-2, -200, anchor=NW, image=img)
    canvas15.place(x=592, y=610)
    ###################################################


 
    #Si pression sur la touche directionnelle fleche droite du clavier déclenche fonction versDroite
    fenetre.fenetre.bind('<Right>',versDroite)
    #Si pression sur la touche directionnelle fleche gauche du clavier déclenche fonction versGauche
    fenetre.fenetre.bind('<Left>', versGauche)
    #Si pression sur la touche directionnelle fleche haut du clavier déclenche fonction versHaut
    fenetre.fenetre.bind('<Up>', versHaut)
    #Si pression sur la touche directionnelle fleche bas du clavier déclenche fonction versBas
    fenetre.fenetre.bind('<Down>', versBas)

    fenetre.fenetre.mainloop()
    
def victoireOrNot(): 
    situation=ramasserObjetEtVictoire(ListeObjet,Mac,ongletObjet,ongletGardien,GardienLab)
    if situation==1:
       perdu()
    elif situation==2:
       gagner()
    else:
        pass
    
def versDroite(evt):
   Mac.deplacementVersDroite()
   victoireOrNot()


def versGauche(evt):
   Mac.deplacementVersGauche()
   victoireOrNot()
   
def versHaut(evt):
   Mac.deplacementVersHaut()
   victoireOrNot()
   
def versBas(evt):
   Mac.deplacementVersBas()
   victoireOrNot()
   
def perdu():
        #declaration global pour passer command
        global fenetrePerdu
        fenetrePerdu=Fenetre('Game Over',400,250)
        fenetrePerdu.construction()


        w = Label(fenetrePerdu.fenetre, text="Gardien : Je t'avais prévenu ! Bye bye mon ami!\n \n Tu as perdu, mais ne te décourage pas, recommence.")
        w.place(x=50, y=40)
        fenetre.nePlusBouger()
        Button(fenetrePerdu.fenetre,text='Quitter', command=quit).place(x=90, y=180)
        Button(fenetrePerdu.fenetre,text='Rejouer' , command=rejouerLoose).place(x=230, y=180)

def gagner():
        #declaration global pour passer command
        global fenetreGagner
        fenetreGagner=Fenetre('Victoire',400,150)
        fenetreGagner.construction()
        w = Label(fenetreGagner.fenetre, text="Bravo, le gardien t'a finalement laissé passer, tu es libre!")
        w.place(x=50, y=40)
        fenetre.nePlusBouger()
        Button(fenetreGagner.fenetre,text='Quitter', command=quit).place(x=120, y=80)
        Button(fenetreGagner.fenetre,text='Rejouer' , command=rejouer).place(x=250, y=80)
        


def rejouer():
    fenetreGagner.fermerLaFenetre()
    fenetre.fermerLaFenetre()
    main()
def rejouerLoose():
    fenetrePerdu.fermerLaFenetre()
    fenetre.fermerLaFenetre()
    main()
def rejouerDebut():
    
    fenetre.fermerLaFenetre()
    main()
   

main()
