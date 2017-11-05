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
    
    global fenetre
    global ListeObjet

    fenetre=Fenetre('Labyrinthe P3',1400, 1000)
    fenetre.construction()
                             



    ##################################################################################################
    #Construction de la liste de coordonnées permetant d'optimiser les chances du coordonnées valides
    #Pour la position des Objets
    listeCoord=[]
    nb=23
    while nb <570:
        listeCoord.append(nb)    
        nb=nb+22.5
    ##################################################################################################
        


    

   
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
    global Mac
    Mac=MacGayver(frameLabyrinthe.frame,photoMacGayver)
    #################################################
    #################################################
    #Creation de la liste d objets
    photoObjet=PhotoImage(file="images/tc-image005.gif")
    ListeObjet=[]
    for i in range(6):
        newObjet=Objet(listeCoord,frameLabyrinthe.frame,photoObjet,i)
        ListeObjet.append(newObjet)
    #################################################  
    #################################################
    #Creation du gardien   
    photoGardien = PhotoImage(file="images/gardien.gif")
    global GardienLab
    GardienLab=Gardien(frameLabyrinthe.frame,photoGardien)
    ##################################################
    ##################################################
    #petit escalier
    photo4=Image.open('images/tc-image007.png')
    canvas15 = Canvas(frameLabyrinthe.frame,width=32, height=36, borderwidth=0,highlightthickness=0)

    resolution = (100,263)
    img = ImageTk.PhotoImage(photo4.resize(resolution))
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
    
def versDroite(evt):
   Mac.deplacementVersDroite()
   if ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre)=="gagner":
       gagner()
   elif ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre)=="perdu":
       perdu()
   else:
        pass

def versGauche(evt):
   Mac.deplacementVersGauche()
   print(ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre))
   if ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre)=="gagner":
       gagner()
   elif ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre)=="perdu":
       perdu()
   else:
        pass
   
def versHaut(evt):
   Mac.deplacementVersHaut()
   if ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre)=="gagner":
       gagner()
   elif ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre)=="perdu":
       perdu()
   else:
        pass
   
def versBas(evt):
   Mac.deplacementVersBas()
   if ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre)=="gagner":
       gagner()
   elif ramasserObjetEtVictoire(ListeObjet,Mac,stringVar,stringVarGardien,GardienLab,fenetre)=="perdu":
       perdu()
   else:
        pass              

   
def perdu():
        fenetrePerdu=Fenetre('Game Over',400,250)
        fenetrePerdu.construction()


        w = Label(fenetrePerdu, text="Gardien : Je t'avais prévenu ! Bye bye mon ami!\n \n Tu as perdu, mais ne te décourage pas, recommence.")
        w.place(x=50, y=40)
        fenetre.nePlusBouger()
        Button(fenetrePerdu,text='Quitter', command=quit).place(x=90, y=180)
        Button(fenetrePerdu,text='Rejouer' , command=rejouerLoose).place(x=230, y=180)

def gagner():
        fenetreGagner=Fenetre('Victoire',400,150)
        fenetreGagner.construction
        w = Label(fenetreGagner, text="Bravo, le gardien t'a finalement laissé passer, tu es libre!")
        w.place(x=50, y=40)
        fenetre.nePlusBouger()
        Button(fenetreGagner,text='Quitter', command=quit).place(x=120, y=80)
        Button(fenetreGagner,text='Rejouer' , command=rejouer).place(x=250, y=80)
        


def rejouer():
    fenetreGagner.destroy()
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
