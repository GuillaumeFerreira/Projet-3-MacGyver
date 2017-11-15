#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Autor: Ferreira Guillaume
#Projet 3: parcours python openclassroom
#Date : 15/11/2017

"""Element for building the labyrinth

    File ElementLabyrinthe.py is the base of the
    attribute and instance for any element of the labyrinth

"""
import re
from tkinter import Canvas, NW


class ElementLabyrinthe:
    positionX = 0
    positionY = 0
    id_element = 0

    def __init__(self, shift_x, shift_y, frame_labyrinthe, photo, positionX, positionY):
        borderwidth = -4
        borderheight = -5
        ElementLabyrinthe.id_element = +1
        self.positionX = positionX
        self.positionY = positionY
        self.canvas = Canvas(frame_labyrinthe, width=45, height=45, borderwidth=0, highlightthickness=0)
        self.canvas.create_image(borderwidth + (shift_x), borderheight + (shift_y), anchor=NW, image=photo)
        self.canvas.place(x=self.positionX, y=self.positionY)

    @classmethod
    def mur(cls, shift_x, shift_y, frame_labyrinthe, photo, id_mur):
        return cls(shift_x, shift_y, frame_labyrinthe, photo, ((id_mur % 15) * 45), ((int(id_mur / 15)) * 45))

    #retourne la valeur entier arrondi au superier ou non
    def __int_more_one(self, valeurCoord):
        if int(valeurCoord / 45) < valeurCoord / 45:
            integer_round = int(valeurCoord / 45) + 1
        else:
            integer_round = int(valeurCoord / 45)
        return integer_round

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
    def __move_or_not(self, condition1, condition2, condition3, condition4):

        if condition1 == "True" and condition2 == "True" and condition3 == "True" and condition4 == "True":
            bouger = True
        else:
            bouger = False

        return bouger

    def situation(self):

        num_img_bd = self.__numImgSousBasDroite()
        num_img_hd = self.__numImgSousHautDroite()
        num_img_bg = self.__numImgSousBasGauche()
        num_img_hg = self.__numImgSousHautGauche()

        if num_img_bd != num_img_hd and num_img_bd != num_img_bg:
            if self.__move_or_not(self.__regarderDroitLabyrinthe(num_img_bd, "HautGauche"), self.__regarderDroitLabyrinthe(num_img_hd, "BasGauche"), self.__regarderDroitLabyrinthe(num_img_bg, "HautDroit"), self.__regarderDroitLabyrinthe(num_img_hg, "BasDroit")):
                #on peut se positionner
                move = True
            else:
                #On ne peut pas se positionner
                move = False

        elif num_img_bd != num_img_hd and num_img_bd == num_img_bg:
            if self.__move_or_not(self.__regarderDroitLabyrinthe(num_img_bd, "HautDroit"), self.__regarderDroitLabyrinthe(num_img_bg, "HautGauche"), self.__regarderDroitLabyrinthe(num_img_hd, "BasDroit"), self.__regarderDroitLabyrinthe(num_img_hg, "BasGauche")):
                #on peut bouger
                move = True
            else:
                #On ne peut pas se positionner
                move = False

        elif num_img_bd == num_img_hd and num_img_bd != num_img_bg:
            if self.__move_or_not(self.__regarderDroitLabyrinthe(num_img_bd, "BasGauche"), self.__regarderDroitLabyrinthe(num_img_hd, "HautGauche"), self.__regarderDroitLabyrinthe(num_img_bg, "BasDroit"), self.__regarderDroitLabyrinthe(num_img_hg, "HautDroit")):
                #on peut se positionner
                move = True
            else:
                #On ne peut pas se positionner
                move = False

        elif num_img_bd == num_img_hd and num_img_bd == num_img_bg:
            if self.__move_or_not(self.__regarderDroitLabyrinthe(num_img_bg, "BasGauche"), self.__regarderDroitLabyrinthe(num_img_hg, "HautGauche"), self.__regarderDroitLabyrinthe(num_img_bd, "BasDroit"), self.__regarderDroitLabyrinthe(num_img_hd, "HautDroit")):
                #on peut se positionner
                move = True
            else:
                #On ne peut pas se positionner
                move = False
        else:
            pass

        return move

    def __regarderDroitLabyrinthe(self, num_img, position_to_watch):
        file = open("Mac.txt", "r")

        for line in file:
            global num_img_rule
            try:
                search_num_img_rule = re.search(r'^'+str(num_img)+'-->(.+)', line)

                num_img_rule = search_num_img_rule.group(1)

            except:
                #rien a faire pas la bonne ligne
                pass
            else:
                #rien a faire pas la bonne ligne
                pass

        file_lab = open("DroitLab.txt", "r")

        for line_d in file_lab:

            try:
                search_item = re.search(r'^'+num_img_rule+'-->.+HG=(.+),HD=(.+),BG=(.+),BD=(.+)/', line_d)

                if position_to_watch == "HautGauche":
                    droit = search_item.group(1)
                elif position_to_watch == "HautDroit":
                    droit = search_item.group(2)
                elif position_to_watch == "BasGauche":
                    droit = search_item.group(3)
                elif position_to_watch == "BasDroit":
                    droit = search_item.group(4)
                else:
                    pass
                return droit
            except:
                #rien a faire pas la bonne ligne
                pass
            else:
                #rien a faire pas la bonne ligne
                pass
