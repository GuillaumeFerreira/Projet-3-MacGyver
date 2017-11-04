#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random
from ClassObject import *
#from Func import *



def main():
    
    global fenetre
    global ListeObjet

    
    ##################################################################################################
    #Construction de la fenêtre Tkinter
    fenetre = Tk()
    #Titre de la fenêtre Tkinter
    fenetre.title('Labyrinthe P3')
    #Dimensions de la fenêtre
    fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth()-15, fenetre.winfo_screenheight()-15))
    ###################################################################################################
    
    ##################################################################################################
    #Construction du menu en haut à gauche de la fenêtre principale
    menubar = Menu(fenetre)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Rejouer", command=rejouerDebut)
    menu1.add_command(label="Quitter", command=quit)
    
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu2)

    fenetre.config(menu=menubar)
    ##################################################################################################


    ##################################################################################################
    #Construction de la liste de coordonnées permetant d'optimiser les chances du coordonnées valides
    #Pour la position des Objets
    listeCoord=[]
    nb=23
    while nb <570:
        listeCoord.append(nb)    
        nb=nb+22.5
    ##################################################################################################
        


    

   

    global Frame1
    Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Frame1.config(width=680, height=680)
    Frame1.place(x=400, y=10)
    global FenObjet
    global stringVar
    stringVar=StringVar()
    
    FenObjet = LabelFrame(fenetre, text="Objets récupérés", padx=20, pady=20)
    FenObjet.place(x=50, y=200)
    Label(FenObjet, textvariable=stringVar).pack()
    stringVar.set("-")
    
    stringVarConseil=StringVar()
    FenConseil = LabelFrame(fenetre, text="Conseil", padx=20, pady=20)
    FenConseil.place(x=50, y=50)
    Label(FenConseil, textvariable=stringVarConseil).pack()
    stringVarConseil.set("Ramasser tous les objets avant de se présenter \n au gardien. Il tient beaucoup à ses objets.")

    
    global stringVarGardien
    stringVarGardien=StringVar()
    FenGardien = LabelFrame(fenetre, text="Gardien", padx=20, pady=20)
    FenGardien.place(x=50, y=400)
    Label(FenGardien, textvariable=stringVarGardien).pack()
    stringVarGardien.set("Personne ne sortira tant que je ne serai pas satisfait!")
    
    #################################################
    #Initialisation et construction de labyrinthe
    photo = PhotoImage(file="images/wall.gif")
    creationDuLabyrinthe(photo)
    #################################################
    #################################################
    #création de MacGayver
    photoMacGayver=PhotoImage(file="images/macgyver.gif")
    global Mac
    Mac=MacGayver(Frame1,photoMacGayver)
    #################################################
    #################################################
    #Creation de la liste d objets
    photoObjet=PhotoImage(file="images/tc-image005.gif")
    ListeObjet=[]
    for i in range(6):
        newObjet=Objet(listeCoord,Frame1,photoObjet,i)
        ListeObjet.append(newObjet)
    #################################################  
    #################################################
    #Creation du gardien   
    photoGardien = PhotoImage(file="images/gardien.gif")
    global GardienLab
    GardienLab=Gardien(Frame1,photoGardien)
    ##################################################
    ##################################################
    #petit escalier
    photo4=Image.open('images/tc-image007.png')
    canvas15 = Canvas(Frame1,width=32, height=36, borderwidth=0,highlightthickness=0)

    resolution = (100,263)
    img = ImageTk.PhotoImage(photo4.resize(resolution))
    canvas15.create_image(-2, -200, anchor=NW, image=img)
    canvas15.place(x=592, y=610)
    ###################################################



    #Si pression sur la touche directionnelle fleche droite du clavier déclenche fonction versDroite
    fenetre.bind('<Right>',versDroite)
    #Si pression sur la touche directionnelle fleche gauche du clavier déclenche fonction versGauche
    fenetre.bind('<Left>', versGauche)
    #Si pression sur la touche directionnelle fleche haut du clavier déclenche fonction versHaut
    fenetre.bind('<Up>', versHaut)
    #Si pression sur la touche directionnelle fleche bas du clavier déclenche fonction versBas
    fenetre.bind('<Down>', versBas)

    fenetre.mainloop()
              
def creationDuLabyrinthe(photo):
    ###############################################################################
    #Initialisation et construction de labyrinthe  
    #ouverture du fichier qui decrit 
    f = open("Mac.txt", "r")
    i=0
    for line in f:
        
        e = re.search(r'-->(.+)', line)
        extension = e.group(1)
        
        fLab = open("DroitLab.txt", "r")

        for lineD in fLab:
            
            try:
               
                x = re.search(r'^'+extension+'-->.+Pos:(.+),', lineD)
               
                x = x.group(1)
                
                yy = re.search(r'^'+extension+'-->.+,(.+)', lineD)
                y = yy.group(1)

                #canvas(float(x),float(y),photo,i)
                Mur(float(x),float(y),Frame1,photo,i)
            except:
                #rien a faire pas la bonne ligne
                pass
            else:
                #rien a faire pas la bonne ligne
                pass
        fLab.close()
        
        i=i+1
    f.close()
    ################################################################################
    
def versDroite(evt):
   Mac.deplacementVersDroite()
   ramasserObjetEtVictoire()

def versGauche(evt):
   Mac.deplacementVersGauche()
   ramasserObjetEtVictoire()
   
def versHaut(evt):
   Mac.deplacementVersHaut()
   ramasserObjetEtVictoire()
   
def versBas(evt):
   Mac.deplacementVersBas()
   ramasserObjetEtVictoire()

   
def ramasserObjetEtVictoire():
   ramasserLesObjets()
   nombreObjetRamasser()
   if Mac.macDansZoneGardien() and Mac.etreResortiDeLaZone:
        Mac.etreResortiDeLaZone=False
        Mac.nombreDeFoisDansZone=Mac.nombreDeFoisDansZone+1
        if Mac.objetRamasser==6:
            gagner(fenetre)
        else:
            if Mac.nombreDeFoisDansZone>=3:
                perdu(fenetre)
            elif GardienLab.memoireNbObjet==Mac.objetRamasser and Mac.nombreDeFoisDansZone<3:
                    #gardien en tres en colere
                    stringVarGardien.set("Tu te crois malin!\n Tu n'as rien récupéré de plus, va t'en d'ici tout de suite!!!")
            elif Mac.nombreDeFoisDansZone==2 and GardienLab.memoireNbObjet!=Mac.objetRamasser:
                stringVarGardien.set("C'est la deuxième fois que tu viens me voir!\n Tu n'as que " + str(Mac.objetRamasser) +" objets!\n Je te déconseille de revenir me voir une troisième fois \n sans tous les objets!")
            else:
                    #gardien en colere
                if Mac.objetRamasser==1:
                    stringVarGardien.set("Quoi ? Seulement " + str(Mac.objetRamasser) +" objet ramassé!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
                else:
                    stringVarGardien.set("Quoi ? Seulement " + str(Mac.objetRamasser) +" objets ramassés!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
                
        GardienLab.memoireNbObjet=Mac.objetRamasser
   else:
        Mac.etreResortiDeLaZone=True
        
def ramasserLesObjets():
        #On regarde si MacGayver se trouve sur un objet si oui , on le supprime
        for objet in ListeObjet:
            if Mac.ramasseObjet(objet.positionX,objet.positionY):
                objet.objetEstRamasser()
                ListeObjet.remove(objet)

def nombreObjetRamasser():
    if Mac.objetRamasser==0:
        stringVar.set(" - ")
    elif Mac.objetRamasser==1:
        stringVar.set(str(Mac.objetRamasser) +" objet ramassé.")
    else:
        stringVar.set(str(Mac.objetRamasser) +" objets ramassés.")
        



def perdu():
        global fenetrePerdu
        fenetrePerdu = Tk()
        fenetrePerdu.title('Game Over')
        fenetrePerdu.configure(width=400,height=250)
        w = Label(fenetrePerdu, text="Gardien : Je t'avais prévenu ! Bye bye mon ami!\n \n Tu as perdu, mais ne te décourage pas, recommence.")
        w.place(x=50, y=40)
        fenetre.unbind('<Right>') 
        fenetre.unbind('<Left>')
        fenetre.unbind('<Up>')
        fenetre.unbind('<Down>')
        Button(fenetrePerdu,text='Quitter', command=quit).place(x=90, y=180)
        Button(fenetrePerdu,text='Rejouer' , command=rejouerLoose).place(x=230, y=180)

def gagner():
        
        fenetreGagner = Tk()
        fenetreGagner.title('Victoire')
        fenetreGagner.configure(width=400,height=150)
        w = Label(fenetreGagner, text="Bravo, le gardien t'a finalement laissé passer, tu es libre!")
        w.place(x=50, y=40)
        fenetre.unbind('<Right>') 
        fenetre.unbind('<Left>')
        fenetre.unbind('<Up>')
        fenetre.unbind('<Down>')
        Button(fenetreGagner,text='Quitter', command=quit).place(x=120, y=80)
        Button(fenetreGagner,text='Rejouer' , command=rejouer).place(x=250, y=80)
        


def rejouer():
    fenetreGagner.destroy()
    fenetre.destroy()
    main()
def rejouerLoose():
    fenetrePerdu.destroy()
    fenetre.destroy()
    main()
def rejouerDebut():
    
    fenetre.destroy()
    main()
   

main()
