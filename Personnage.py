#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Canvas

from ElementLabyrinthe import *

class Personnage(ElementLabyrinthe):

    def __init__(self, FrameLabyrinthe, photo, Height, se_deplacer, position_x, position_y):
                
        #Initialisation de l'image de MacGayver dans le labyrinthe  
        #Position initiale de MacGayver.
        #Position en abscisse par rapport au coin en haut à gauche.
        self.position_x = position_x
        #Position en ordonnée par rapport au coin en haut à gauche.
        self.position_y = position_y
        self.se_deplacer = se_deplacer
        self.canvasMacGayver = Canvas(FrameLabyrinthe, width=32, height=Height, borderwidth=0, highlightthickness=0)
        self.canvasMacGayver.create_image(0, 0, anchor=NW, image=photo)
        self.canvasMacGayver.place(x=self.position_x, y=self.position_y)
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
        if self.position_x > 555 and self.position_y > 500:
            macInZone = True
        else:
            macInZone = False
        return macInZone
    
    #Déplace MacGayver vers la Droite dans le labyrinthe
    def deplacementVersDroite(self):
        if self.se_deplacer:
            self.position_x = self.position_x + 22.5
            if self.situation(): 
                self.canvasMacGayver.place(x=self.position_x, y=self.position_y)
            else:
                self.position_x = self.position_x - 22.5

    #Déplace MacGayver vers la Gauche dans le labyrinthe
    def deplacementVersGauche(self):
        if self.se_deplacer:
            self.position_x = self.position_x - 22.5
            if self.situation():    
                self.canvasMacGayver.place(x=self.position_x, y=self.position_y)
            else:
                self.position_x = self.position_x + 22.5
        
    #Déplace MacGayver vers la Bas dans le labyrinthe
    def deplacementVersBas(self):
        if self.se_deplacer:
            self.position_y = self.position_y + 22.5
            if self.situation():
                self.canvasMacGayver.place(x=self.position_x, y=self.position_y)
            else:
                self.position_y = self.position_y - 22.5
        
    #Déplace MacGayver vers la Haut dans le labyrinthe
    def deplacementVersHaut(self):
        if self.se_deplacer:
            self.position_y = self.position_y - 22.5
            if self.situation():
                self.canvasMacGayver.place(x=self.position_x, y=self.position_y)
            else:
                self.position_y = self.position_y + 22.5
            
    def ramasseObjet(self, xDeObjet, yDeObjet):
        possibilite_objet_ramasser = False
        if (int(self.position_x) >= int(xDeObjet) and int(self.position_x) < int(xDeObjet + 39)) or (int(self.position_x + 32) >= int(xDeObjet) and int(self.position_x + 32) < int(xDeObjet + 39)):
            if (int(self.position_y) >= int(yDeObjet - 10) and int(self.position_y) < int(yDeObjet + 43)) or (int(self.position_y + 43) > int(yDeObjet) and int(self.position_y + 43) < int(yDeObjet + 40)):
                self.objetRamasser = self.objetRamasser + 1
                possibilite_objet_ramasser = True
            
        return possibilite_objet_ramasser
            

