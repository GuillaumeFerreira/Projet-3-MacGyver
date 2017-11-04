#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random


#################################################################################################
###############################  Définition des Class  ##########################################
class ElementLabyrinthe:
        positionX=0
        positionY=0
        id_element=0
        
        def __init__(self):
            ElementLabyrinthe.id_element =+1
        #Renvoie la position Gauche dans la FrameLabyrinthe
        def PosGauche(self):
            return self.entierOrPlusUn(self.positionX)
        
            #Renvoie la position Droite dans la FrameLabyrinthe
        def PosDroite(self):
            return self.entierOrPlusUn(self.positionX+32)
        
            #Renvoie la position Haut dans la FrameLabyrinthe
        def PosHaut(self):
            return self.entierOrPlusUn(self.positionY)
        
             #Renvoie la position Bas dans la FrameLabyrinthe
        def PosBas(self):
            return self.entierOrPlusUn(self.positionY+43)
        
            #retourne la valeur entier arrondi au superier ou non 
        def entierOrPlusUn(self,valeurCoord):
            if int(valeurCoord/45)<valeurCoord/45:
                entierArrondi=int(valeurCoord/45)+1
            else:
                entierArrondi=int(valeurCoord/45)
            return entierArrondi

            #Renvoie le numéro de l'image de la partie Haut Gauche de l'élement
        def numImgSousHautGauche(self):
            return ((self.PosHaut()*15)+ self.PosGauche()-15)
        
            #Renvoie le numéro de l'image de la partie Haut Droite de l'élement
        def numImgSousHautDroite(self):
            return ((self.PosHaut()*15)+ self.PosDroite()-15)
        
            #Renvoie le numéro de l'image de la partie Bas Gauche de l'élement
        def numImgSousBasGauche(self):
            return ((self.PosBas()*15)+ self.PosGauche()-15)
        
            #Renvoie le numéro de l'image de la partie Bas Droite de l'élement
        def numImgSousBasDroite(self):
            return ((self.PosBas()*15)+ self.PosDroite()-15)
        #renvoie le droit de se positionner ou non
        def droitDeBougerOuPas(self,condition1,condition2,condition3,condition4):

            if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
                bouger=True
            else:
                bouger=False
            
            return bouger
        
        def situation(self):
        
            NumImgBD=self.numImgSousBasDroite()
            NumImgHD=self.numImgSousHautDroite()
            NumImgBG=self.numImgSousBasGauche()
            NumImgHG=self.numImgSousHautGauche()
            
            if NumImgBD!=NumImgHD and NumImgBD!=NumImgBG:
                if self.droitDeBougerOuPas(self.regarderDroitLabyrinthe(NumImgBD,"HautGauche"),self.regarderDroitLabyrinthe(NumImgHD,"BasGauche"),self.regarderDroitLabyrinthe(NumImgBG,"HautDroit"),self.regarderDroitLabyrinthe(NumImgHG,"BasDroit")):
                    #on peut se positionner
                    bougerPossible=True
                else:
                    #On ne peut pas se positionner
                    bougerPossible=False

            elif NumImgBD!=NumImgHD and NumImgBD==NumImgBG:
                if self.droitDeBougerOuPas(self.regarderDroitLabyrinthe(NumImgBD,"HautDroit"),self.regarderDroitLabyrinthe(NumImgBG,"HautGauche"),self.regarderDroitLabyrinthe(NumImgHD,"BasDroit"),self.regarderDroitLabyrinthe(NumImgHG,"BasGauche")):
                    #on peut bouger
                    bougerPossible=True
                else:
                    #On ne peut pas se positionner
                    bougerPossible=False

            elif NumImgBD==NumImgHD and NumImgBD!=NumImgBG:
                if self.droitDeBougerOuPas(self.regarderDroitLabyrinthe(NumImgBD,"BasGauche"),self.regarderDroitLabyrinthe(NumImgHD,"HautGauche"),self.regarderDroitLabyrinthe(NumImgBG,"BasDroit"),self.regarderDroitLabyrinthe(NumImgHG,"HautDroit")):
                    #on peut se positionner
                    bougerPossible=True
                else:
                    #On ne peut pas se positionner
                    bougerPossible=False

            
            elif NumImgBD==NumImgHD and NumImgBD==NumImgBG:
                if self.droitDeBougerOuPas(self.regarderDroitLabyrinthe(NumImgBG,"BasGauche"),self.regarderDroitLabyrinthe(NumImgHG,"HautGauche"),self.regarderDroitLabyrinthe(NumImgBD,"BasDroit"),self.regarderDroitLabyrinthe(NumImgHD,"HautDroit")):
                    #on peut se positionner
                    bougerPossible=True
                else:
                    #On ne peut pas se positionner
                    bougerPossible=False                    
            else:
                pass

            return bougerPossible
        
        def regarderDroitLabyrinthe(self,NumImg,positionAregarder):            
            f = open("Mac.txt", "r")
            
            
            for line in f:
                global extension
                try:
                    e = re.search(r'^'+str(NumImg)+'-->(.+)', line)
                    
                    extension = e.group(1)
                    
                except:
                    #rien a faire pas la bonne ligne
                    pass
                else:
                    #rien a faire pas la bonne ligne
                    pass
             
            fLab = open("DroitLab.txt", "r")
                
            for lineD in fLab:
                global droit
                try:
                    x = re.search(r'^'+extension+'-->.+HG=(.+),HD=(.+),BG=(.+),BD=(.+)/', lineD)
                      
                    
                    if positionAregarder=="HautGauche":
                        droit=x.group(1)
                    elif positionAregarder=="HautDroit":
                        droit=x.group(2)
                    elif positionAregarder=="BasGauche":
                        droit=x.group(3)
                    elif positionAregarder=="BasDroit":
                        droit=x.group(4)
                    else:
                        pass
                    
                except:
                    #rien a faire pas la bonne ligne
                    pass
                else:
                    #rien a faire pas la bonne ligne
                    pass

            return droit
        
class MacGayver(ElementLabyrinthe):
       
        def __init__(self,FrameLabyrinthe,photo):    
            #Initialisation de l'image de MacGayver dans le labyrinthe  
            #Position initiale de MacGayver.
            #Position en abscisse par rapport au coin en haut à gauche.
            self.positionX=51
            #Position en ordonnée par rapport au coin en haut à gauche.
            self.positionY=46
            self.canvasMacGayver=Canvas(FrameLabyrinthe,width=32, height=43, borderwidth=0,highlightthickness=0)
            self.canvasMacGayver.create_image(0, 0, anchor=NW, image=photo)
            self.canvasMacGayver.place(x=self.positionX, y=self.positionY)

            self.objetRamasser=0
            self.nombreDeFoisDansZone=0
            self.etreResortiDeLaZone=True
            #retourne True ou false pour savoir si MacGayver est dans la zone
        
        def macDansZoneGardien(self):
            if self.positionX>555 and self.positionY>500:
                    macInZone=True
            else:
                    macInZone=False
            return macInZone
        
            #Déplace MacGayver vers la Droite dans le labyrinthe
        def deplacementVersDroite(self):
            self.positionX=self.positionX+22.5
            if self.situation()==True: 
                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
            else:
                self.positionX=self.positionX-22.5

            #Déplace MacGayver vers la Gauche dans le labyrinthe
        def deplacementVersGauche(self):
            self.positionX=self.positionX-22.5
            if self.situation()==True:    
                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
            else:
                self.positionX=self.positionX+22.5
            
            #Déplace MacGayver vers la Bas dans le labyrinthe
        def deplacementVersBas(self):
            self.positionY=self.positionY+22.5
            if self.situation()==True:
                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
            else:
                self.positionY=self.positionY-22.5
            
            #Déplace MacGayver vers la Haut dans le labyrinthe
        def deplacementVersHaut(self):
            self.positionY=self.positionY-22.5
            if self.situation()==True:
                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
            else:
                self.positionY=self.positionY+22.5
                
        def ramasseObjet(self,xDeObjet,yDeObjet):
            
            if (int(self.positionX)>= int(xDeObjet) and int(self.positionX) < int(xDeObjet+39)) or (int(self.positionX+32)>= int(xDeObjet) and int(self.positionX+32) < int(xDeObjet+39)):
                if (int(self.positionY) >= int(yDeObjet-10) and int(self.positionY) < int(yDeObjet+43)) or (int(self.positionY+43) > int(yDeObjet) and int(self.positionY+43) < int(yDeObjet+40)) :
                    self.objetRamasser=self.objetRamasser+1
                    return True
                
                else:
                    return False
            else:
                return False 
            



class Objet(ElementLabyrinthe):
        listeImgDecObj=[]
        listeImgDecObj.append(-197)
        listeImgDecObj.append(-158)
        listeImgDecObj.append(-4)
        listeImgDecObj.append(-120)
        listeImgDecObj.append(-81)
        listeImgDecObj.append(-42)
        
        def __init__(self,listeCoord,FrameLabyrinthe,photo,id_obj):
            self.id_obj=id_obj
            self.valideCoordonneesObjet(listeCoord)
            self.canvasObjet=Canvas(FrameLabyrinthe,width=39, height=43, borderwidth=0,highlightthickness=0)
            self.canvasObjet.create_image(Objet.listeImgDecObj[id_obj], -1, anchor=NW, image=photo)
            self.canvasObjet.place(x=self.positionX, y=self.positionY)
            
        def valideCoordonneesObjet(self,listeCoord):
                while self.situation()!=True:
                        self.positionX=random.choice(listeCoord)
                        self.positionY=random.choice(listeCoord)
                        
        def objetEstRamasser(self):
                self.canvasObjet.destroy()
                
class Mur(ElementLabyrinthe):
        def __init__(self,decalageImgX,decalageImgY,FrameLabyrinthe,photo,id_mur):
            borderwidth=-4
            borderheight=-5
            self.positionX =(id_mur%15)*45
            self.positionY=(int(id_mur/15))*45
            
            canvas = Canvas(FrameLabyrinthe,width=45, height=45, borderwidth=0, highlightthickness=0)
            canvas.create_image(borderwidth+(decalageImgX), borderheight+(decalageImgY), anchor=NW, image=photo)
            canvas.place(x=self.positionX, y=self.positionY)
                
class Gardien(ElementLabyrinthe):

        def __init__(self,FrameLabyrinthe,photo):
            self.positionX=592
            self.positionY=570
            self.memoireNbObjet=0
            canvasGardien= Canvas(FrameLabyrinthe,width=32, height=36, borderwidth=0,highlightthickness=0)
            canvasGardien.create_image(0, 0, anchor=NW, image=photo)
            canvasGardien.place(x=self.positionX, y=self.positionY)
################################################################################################## 
##################################################################################################