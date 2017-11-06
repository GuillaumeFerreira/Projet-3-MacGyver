#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random
from ElementLabyrinthe import *

class Objet(ElementLabyrinthe):
        listeImgDecObj=[]
        listeImgDecObj.append(-197)
        listeImgDecObj.append(-158)
        listeImgDecObj.append(-4)
        listeImgDecObj.append(-120)
        listeImgDecObj.append(-81)
        listeImgDecObj.append(-42)
        ##################################################################################################
        #Construction de la liste de coordonnées permetant d'optimiser les chances du coordonnées valides
        #Pour la position des Objets
        listeCoord=[]
        nb=23
        while nb <570:
            listeCoord.append(nb)    
            nb=nb+22.5
        ##################################################################################################        

        def __init__(self,FrameLabyrinthe,photo,id_obj):
            self.id_obj=id_obj
            self.__valideCoordonneesObjet()
            self.canvasObjet=Canvas(FrameLabyrinthe,width=39, height=43, borderwidth=0,highlightthickness=0)
            self.canvasObjet.create_image(Objet.listeImgDecObj[id_obj], -1, anchor=NW, image=photo)
            self.canvasObjet.place(x=self.positionX, y=self.positionY)
            
            
        def __valideCoordonneesObjet(self):
                while self.situation()!=True:
                        self.positionX=random.choice(Objet.listeCoord)
                        self.positionY=random.choice(Objet.listeCoord)
                        
        def objetEstRamasser(self):
                self.canvasObjet.destroy()
