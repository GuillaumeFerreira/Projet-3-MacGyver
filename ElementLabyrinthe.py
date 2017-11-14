#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
from tkinter import Canvas, NW


class ElementLabyrinthe:
    positionX = 0
    positionY = 0
    id_element = 0

    def __init__(self, decalageImgX, decalageImgY, frame_labyrinthe, photo, positionX, positionY):
        borderwidth = -4
        borderheight = -5
        ElementLabyrinthe.id_element = +1
        self.positionX = positionX
        self.positionY = positionY
        self.canvas = Canvas(frame_labyrinthe, width=45, height=45, borderwidth=0, highlightthickness=0)
        self.canvas.create_image(borderwidth + (decalageImgX), borderheight + (decalageImgY), anchor=NW, image=photo)
        self.canvas.place(x=self.positionX, y=self.positionY)

    @classmethod
    def mur(cls, decalageImgX, decalageImgY, frame_labyrinthe, photo, id_mur):
        return cls(decalageImgX, decalageImgY, frame_labyrinthe, photo, ((id_mur % 15) * 45), ((int(id_mur / 15)) * 45))

    #retourne la valeur entier arrondi au superier ou non 
    def __int_more_one(self, valeurCoord):
        if int(valeurCoord / 45) < valeurCoord / 45:
            entierArrondi = int(valeurCoord / 45) + 1
        else:
            entierArrondi = int(valeurCoord / 45)
        return entierArrondi

    #Renvoie le numéro de l'image de la partie Haut Gauche de l'élement
    def __numImgSousHautGauche(self):
        return ((self.__int_more_one(self.positionY) * 15) + self.__int_more_one(self.positionX) - 15)

    #Renvoie le numéro de l'image de la partie Haut Droite de l'élement
    def __numImgSousHautDroite(self):
        return ((self.__int_more_one(self.positionY) * 15) + self.__int_more_one(self.positionX + 32) - 15)

    #Renvoie le numéro de l'image de la partie Bas Gauche de l'élement
    def __numImgSousBasGauche(self):
        return ((self.__int_more_one(self.positionY + 43) * 15) + self.__int_more_one(self.positionX) - 15)

    #Renvoie le numéro de l'image de la partie Bas Droite de l'élement
    def __numImgSousBasDroite(self):
        return ((self.__int_more_one(self.positionY + 43) * 15) + self.__int_more_one(self.positionX + 32) - 15)

    #renvoie le droit de se positionner ou non
    def __droitDeBougerOuPas(self, condition1, condition2, condition3, condition4):

        if condition1 == "True" and condition2 == "True" and condition3 == "True" and condition4 == "True":
            bouger = True
        else:
            bouger = False

        return bouger

    def situation(self):

        NumImgBD = self.__numImgSousBasDroite()
        NumImgHD = self.__numImgSousHautDroite()
        NumImgBG = self.__numImgSousBasGauche()
        NumImgHG = self.__numImgSousHautGauche()

        if NumImgBD != NumImgHD and NumImgBD != NumImgBG:
            if self.__droitDeBougerOuPas(self.__regarderDroitLabyrinthe(NumImgBD, "HautGauche"), self.__regarderDroitLabyrinthe(NumImgHD, "BasGauche"), self.__regarderDroitLabyrinthe(NumImgBG, "HautDroit"), self.__regarderDroitLabyrinthe(NumImgHG, "BasDroit")):
                #on peut se positionner
                bougerPossible = True
            else:
                #On ne peut pas se positionner
                bougerPossible = False

        elif NumImgBD != NumImgHD and NumImgBD == NumImgBG:
            if self.__droitDeBougerOuPas(self.__regarderDroitLabyrinthe(NumImgBD, "HautDroit"), self.__regarderDroitLabyrinthe(NumImgBG, "HautGauche"), self.__regarderDroitLabyrinthe(NumImgHD, "BasDroit"), self.__regarderDroitLabyrinthe(NumImgHG, "BasGauche")):
                #on peut bouger
                bougerPossible = True
            else:
                #On ne peut pas se positionner
                bougerPossible = False

        elif NumImgBD == NumImgHD and NumImgBD != NumImgBG:
            if self.__droitDeBougerOuPas(self.__regarderDroitLabyrinthe(NumImgBD, "BasGauche"), self.__regarderDroitLabyrinthe(NumImgHD, "HautGauche"), self.__regarderDroitLabyrinthe(NumImgBG, "BasDroit"), self.__regarderDroitLabyrinthe(NumImgHG, "HautDroit")):
                #on peut se positionner
                bougerPossible = True
            else:
                #On ne peut pas se positionner
                bougerPossible = False

        elif NumImgBD == NumImgHD and NumImgBD == NumImgBG:
            if self.__droitDeBougerOuPas(self.__regarderDroitLabyrinthe(NumImgBG, "BasGauche"), self.__regarderDroitLabyrinthe(NumImgHG, "HautGauche"), self.__regarderDroitLabyrinthe(NumImgBD, "BasDroit"), self.__regarderDroitLabyrinthe(NumImgHD, "HautDroit")):
                #on peut se positionner
                bougerPossible = True
            else:
                #On ne peut pas se positionner
                bougerPossible = False                    
        else:
            pass

        return bougerPossible
        
    def __regarderDroitLabyrinthe(self, NumImg, positionAregarder):            
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

            try:
                x = re.search(r'^'+extension+'-->.+HG=(.+),HD=(.+),BG=(.+),BD=(.+)/', lineD)

                if positionAregarder == "HautGauche":
                    droit = x.group(1)
                elif positionAregarder == "HautDroit":
                    droit = x.group(2)
                elif positionAregarder == "BasGauche":
                    droit = x.group(3)
                elif positionAregarder == "BasDroit":
                    droit = x.group(4)
                else:
                    pass
                return droit
            except:
                #rien a faire pas la bonne ligne
                pass
            else:
                #rien a faire pas la bonne ligne
                pass

