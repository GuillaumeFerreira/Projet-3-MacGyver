#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random
from ElementLabyrinthe import *

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
            
class Gardien(ElementLabyrinthe):

        def __init__(self,FrameLabyrinthe,photo):
            self.positionX=592
            self.positionY=570
            self.memoireNbObjet=0
            self.canvasGardien= Canvas(FrameLabyrinthe,width=32, height=36, borderwidth=0,highlightthickness=0)
            self.canvasGardien.create_image(0, 0, anchor=NW, image=photo)
            self.canvasGardien.place(x=self.positionX, y=self.positionY)
