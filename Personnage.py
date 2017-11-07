#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Canvas
from ElementLabyrinthe import *

class Personnage(ElementLabyrinthe):

    def __init__(self, FrameLabyrinthe, photo, Height, se_deplacer, positionX, positionY):
                
        #Initialisation de l'image de MacGayver dans le labyrinthe  
        #Position initiale de MacGayver.
        #Position en abscisse par rapport au coin en haut à gauche.
        self.positionX = positionX
        #Position en ordonnée par rapport au coin en haut à gauche.
        self.positionY = positionY
        self.se_deplacer = se_deplacer
        self.canvasMacGayver = Canvas(FrameLabyrinthe, width=32, height=Height, borderwidth=0, highlightthickness=0)
        self.canvasMacGayver.create_image(0, 0, anchor=NW, image=photo)
        self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
        self.memoireNbObjet = 0
        self.objetRamasser = 0
        self.nombreDeFoisDansZone = 0
        self.etreResortiDeLaZone = True
        
    @classmethod
    def gardien(cls, FrameLabyrinthe, photo):
        return cls(FrameLabyrinthe, photo, 36, False, 592, 570)
    @classmethod
    def macGayver(cls, FrameLabyrinthe, photo):    
        return cls(FrameLabyrinthe, photo, 43, True, 51, 46)

    #retourne True ou false pour savoir si MacGayver est dans la zone
    def mac_dans_zone_gardien(self):
        if self.positionX > 555 and self.positionY > 500:
            macInZone = True
        else:
            macInZone = False
        return macInZone
    
    #Déplace MacGayver vers la Droite dans le labyrinthe
    def deplacementVersDroite(self):
        if self.se_deplacer:
            self.positionX = self.positionX + 22.5
            if self.situation(): 
                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
            else:
                self.positionX = self.positionX - 22.5

    #Déplace MacGayver vers la Gauche dans le labyrinthe
    def deplacementVersGauche(self):
        if self.se_deplacer:
            self.positionX = self.positionX - 22.5
            if self.situation():    
                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
            else:
                self.positionX = self.positionX + 22.5
        
    #Déplace MacGayver vers la Bas dans le labyrinthe
    def deplacementVersBas(self):
        if self.se_deplacer:
            self.positionY = self.positionY + 22.5
            if self.situation():
                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
            else:
                self.positionY = self.positionY - 22.5
        
    #Déplace MacGayver vers la Haut dans le labyrinthe
    def deplacementVersHaut(self):
        if self.se_deplacer:
            self.positionY = self.positionY - 22.5
            if self.situation():
                self.canvasMacGayver.place(x=self.positionX, y=self.positionY)
            else:
                self.positionY = self.positionY + 22.5
            
    def ramasseObjet(self, xDeObjet, yDeObjet):
        possibilite_objet_ramasser = False
        if (int(self.positionX) >= int(xDeObjet) and int(self.positionX) < int(xDeObjet + 39)) or (int(self.positionX + 32) >= int(xDeObjet) and int(self.positionX + 32) < int(xDeObjet + 39)):
            if (int(self.positionY) >= int(yDeObjet - 10) and int(self.positionY) < int(yDeObjet + 43)) or (int(self.positionY + 43) > int(yDeObjet) and int(self.positionY + 43) < int(yDeObjet + 40)):
                self.objetRamasser = self.objetRamasser + 1
                possibilite_objet_ramasser = True
            
        return possibilite_objet_ramasser
            

