#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random
from ClassObject import *

###################################################################################################
#################################  Définition des Class  ##########################################
##class ElementLabyrinthe:
##        positionX=0
##        positionY=0
##        id_element=0
##        
##        def __init__(self):
##            ElementLabyrinthe.id_element =+1
##        #Renvoie la position Gauche dans la FrameLabyrinthe
##        def PosGauche(self):
##            return self.entierOrPlusUn(self.positionX)
##        
##            #Renvoie la position Droite dans la FrameLabyrinthe
##        def PosDroite(self):
##            return self.entierOrPlusUn(self.positionX+32)
##        
##            #Renvoie la position Haut dans la FrameLabyrinthe
##        def PosHaut(self):
##            return self.entierOrPlusUn(self.positionY)
##        
##             #Renvoie la position Bas dans la FrameLabyrinthe
##        def PosBas(self):
##            return self.entierOrPlusUn(self.positionY+43)
##        
##            #retourne la valeur entier arrondi au superier ou non 
##        def entierOrPlusUn(self,valeurCoord):
##            if int(valeurCoord/45)<valeurCoord/45:
##                entierArrondi=int(valeurCoord/45)+1
##            else:
##                entierArrondi=int(valeurCoord/45)
##            return entierArrondi
##
##            #Renvoie le numéro de l'image de la partie Haut Gauche de l'élement
##        def numImgSousHautGauche(self):
##            return ((self.PosHaut()*15)+ self.PosGauche()-15)
##        
##            #Renvoie le numéro de l'image de la partie Haut Droite de l'élement
##        def numImgSousHautDroite(self):
##            return ((self.PosHaut()*15)+ self.PosDroite()-15)
##        
##            #Renvoie le numéro de l'image de la partie Bas Gauche de l'élement
##        def numImgSousBasGauche(self):
##            return ((self.PosBas()*15)+ self.PosGauche()-15)
##        
##            #Renvoie le numéro de l'image de la partie Bas Droite de l'élement
##        def numImgSousBasDroite(self):
##            return ((self.PosBas()*15)+ self.PosDroite()-15)
##        #renvoie le droit de se positionner ou non
##        def droitDeBougerOuPas(self,condition1,condition2,condition3,condition4):
##
##            if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
##                bouger=True
##            else:
##                bouger=False
##            
##            return bouger
##        
##        def situation(self):
##        
##            NumImgBD=self.numImgSousBasDroite()
##            NumImgHD=self.numImgSousHautDroite()
##            NumImgBG=self.numImgSousBasGauche()
##            NumImgHG=self.numImgSousHautGauche()
##            
##            if NumImgBD!=NumImgHD and NumImgBD!=NumImgBG:
##                if self.droitDeBougerOuPas(self.regarderDroitLabyrinthe(NumImgBD,"HautGauche"),self.regarderDroitLabyrinthe(NumImgHD,"BasGauche"),self.regarderDroitLabyrinthe(NumImgBG,"HautDroit"),self.regarderDroitLabyrinthe(NumImgHG,"BasDroit")):
##                    #on peut se positionner
##                    bougerPossible=True
##                else:
##                    #On ne peut pas se positionner
##                    bougerPossible=False
##
##            elif NumImgBD!=NumImgHD and NumImgBD==NumImgBG:
##                if self.droitDeBougerOuPas(self.regarderDroitLabyrinthe(NumImgBD,"HautDroit"),self.regarderDroitLabyrinthe(NumImgBG,"HautGauche"),self.regarderDroitLabyrinthe(NumImgHD,"BasDroit"),self.regarderDroitLabyrinthe(NumImgHG,"BasGauche")):
##                    #on peut bouger
##                    bougerPossible=True
##                else:
##                    #On ne peut pas se positionner
##                    bougerPossible=False
##
##            elif NumImgBD==NumImgHD and NumImgBD!=NumImgBG:
##                if self.droitDeBougerOuPas(self.regarderDroitLabyrinthe(NumImgBD,"BasGauche"),self.regarderDroitLabyrinthe(NumImgHD,"HautGauche"),self.regarderDroitLabyrinthe(NumImgBG,"BasDroit"),self.regarderDroitLabyrinthe(NumImgHG,"HautDroit")):
##                    #on peut se positionner
##                    bougerPossible=True
##                else:
##                    #On ne peut pas se positionner
##                    bougerPossible=False
##
##            
##            elif NumImgBD==NumImgHD and NumImgBD==NumImgBG:
##                if self.droitDeBougerOuPas(self.regarderDroitLabyrinthe(NumImgBG,"BasGauche"),self.regarderDroitLabyrinthe(NumImgHG,"HautGauche"),self.regarderDroitLabyrinthe(NumImgBD,"BasDroit"),self.regarderDroitLabyrinthe(NumImgHD,"HautDroit")):
##                    #on peut se positionner
##                    bougerPossible=True
##                else:
##                    #On ne peut pas se positionner
##                    bougerPossible=False                    
##            else:
##                pass
##
##            return bougerPossible
##        
##        def regarderDroitLabyrinthe(self,NumImg,positionAregarder):            
##            f = open("Mac.txt", "r")
##            
##            
##            for line in f:
##                global extension
##                try:
##                    e = re.search(r'^'+str(NumImg)+'-->(.+)', line)
##                    
##                    extension = e.group(1)
##                    
##                except:
##                    #rien a faire pas la bonne ligne
##                    pass
##                else:
##                    #rien a faire pas la bonne ligne
##                    pass
##             
##            fLab = open("DroitLab.txt", "r")
##                
##            for lineD in fLab:
##                global droit
##                try:
##                    x = re.search(r'^'+extension+'-->.+HG=(.+),HD=(.+),BG=(.+),BD=(.+)/', lineD)
##                      
##                    
##                    if positionAregarder=="HautGauche":
##                        droit=x.group(1)
##                    elif positionAregarder=="HautDroit":
##                        droit=x.group(2)
##                    elif positionAregarder=="BasGauche":
##                        droit=x.group(3)
##                    elif positionAregarder=="BasDroit":
##                        droit=x.group(4)
##                    else:
##                        pass
##                    
##                except:
##                    #rien a faire pas la bonne ligne
##                    pass
##                else:
##                    #rien a faire pas la bonne ligne
##                    pass
##
##            return droit
##        
##class MacGayver(ElementLabyrinthe):
##       
##        def __init__(self,FrameLabyrinthe,photo):    
##            #Initialisation de l'image de MacGayver dans le labyrinthe  
##            #Position initiale de MacGayver.
##            #Position en abscisse par rapport au coin en haut à gauche.
##            self.positionX=51
##            #Position en ordonnée par rapport au coin en haut à gauche.
##            self.positionY=46
##            self.canvasMacGayver=Canvas(FrameLabyrinthe,width=32, height=43, borderwidth=0,highlightthickness=0)
##            self.canvasMacGayver.create_image(0, 0, anchor=NW, image=photo)
##            self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
##
##            self.objetRamasser=0
##            self.nombreDeFoisDansZone=0
##            self.etreResortiDeLaZone=True
##            #retourne True ou false pour savoir si MacGayver est dans la zone
##        
##        def macDansZoneGardien(self):
##            if self.positionX>555 and self.positionY>500:
##                    macInZone=True
##            else:
##                    macInZone=False
##            return macInZone
##        
##            #Déplace MacGayver vers la Droite dans le labyrinthe
##        def deplacementVersDroite(self):
##            self.positionX=self.positionX+22.5
##            if self.situation()==True: 
##                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
##            else:
##                self.positionX=self.positionX-22.5
##
##            #Déplace MacGayver vers la Gauche dans le labyrinthe
##        def deplacementVersGauche(self):
##            self.positionX=self.positionX-22.5
##            if self.situation()==True:    
##                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
##            else:
##                self.positionX=self.positionX+22.5
##            
##            #Déplace MacGayver vers la Bas dans le labyrinthe
##        def deplacementVersBas(self):
##            self.positionY=self.positionY+22.5
##            if self.situation()==True:
##                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
##            else:
##                self.positionY=self.positionY-22.5
##            
##            #Déplace MacGayver vers la Haut dans le labyrinthe
##        def deplacementVersHaut(self):
##            self.positionY=self.positionY-22.5
##            if self.situation()==True:
##                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
##            else:
##                self.positionY=self.positionY+22.5
##                
##        def ramasseObjet(self,xDeObjet,yDeObjet):
##            
##            if (int(self.positionX)>= int(xDeObjet) and int(self.positionX) < int(xDeObjet+39)) or (int(self.positionX+32)>= int(xDeObjet) and int(self.positionX+32) < int(xDeObjet+39)):
##                if (int(self.positionY) >= int(yDeObjet-10) and int(self.positionY) < int(yDeObjet+43)) or (int(self.positionY+43) > int(yDeObjet) and int(self.positionY+43) < int(yDeObjet+40)) :
##                    self.objetRamasser=self.objetRamasser+1
##                    return True
##                
##                else:
##                    return False
##            else:
##                return False 
##            
##
##
##
##class Objet(ElementLabyrinthe):
##        listeImgDecObj=[]
##        listeImgDecObj.append(-197)
##        listeImgDecObj.append(-158)
##        listeImgDecObj.append(-4)
##        listeImgDecObj.append(-120)
##        listeImgDecObj.append(-81)
##        listeImgDecObj.append(-42)
##        
##        def __init__(self,listeCoord,FrameLabyrinthe,photo,id_obj):
##            self.id_obj=id_obj
##            self.valideCoordonneesObjet(listeCoord)
##            self.canvasObjet=Canvas(FrameLabyrinthe,width=39, height=43, borderwidth=0,highlightthickness=0)
##            self.canvasObjet.create_image(Objet.listeImgDecObj[id_obj], -1, anchor=NW, image=photo)
##            self.canvasObjet.place(x=self.positionX, y=self.positionY)
##            
##        def valideCoordonneesObjet(self,listeCoord):
##                while self.situation()!=True:
##                        self.positionX=random.choice(listeCoord)
##                        self.positionY=random.choice(listeCoord)
##                        
##        def objetEstRamasser(self):
##                self.canvasObjet.destroy()
##                
##class Mur(ElementLabyrinthe):
##        def __init__(self,decalageImgX,decalageImgY,FrameLabyrinthe,photo,id_mur):
##            borderwidth=-4
##            borderheight=-5
##            self.positionX =(id_mur%15)*45
##            self.positionY=(int(id_mur/15))*45
##            
##            canvas = Canvas(Frame1,width=45, height=45, borderwidth=0, highlightthickness=0)
##            canvas.create_image(borderwidth+(decalageImgX), borderheight+(decalageImgY), anchor=NW, image=photo)
##            canvas.place(x=self.positionX, y=self.positionY)
##                
##class Gardien(ElementLabyrinthe):
##
##        def __init__(self,FrameLabyrinthe,photo):
##            self.positionX=592
##            self.positionY=570
##            self.memoireNbObjet=0
##            canvasGardien= Canvas(FrameLabyrinthe,width=32, height=36, borderwidth=0,highlightthickness=0)
##            canvasGardien.create_image(0, 0, anchor=NW, image=photo)
##            canvasGardien.place(x=self.positionX, y=self.positionY)
#################################################################################################### 
####################################################################################################



        
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
            gagner()
        else:
            if Mac.nombreDeFoisDansZone>=3:
                perdu()
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
