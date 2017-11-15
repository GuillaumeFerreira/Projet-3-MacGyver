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
        ElementLabyrinthe.id_element = +1
        self.positionX = positionX
        self.positionY = positionY
        self.canvas = Canvas(frame_labyrinthe, width=45, height=45, borderwidth=0, highlightthickness=0)
        self.canvas.create_image(-4 + (shift_x), -5 + (shift_y), anchor=NW, image=photo)
        self.canvas.place(x=self.positionX, y=self.positionY)

    @classmethod
    def mur(cls, shift_x, shift_y, frame_labyrinthe, photo, id_mur):
        return cls(shift_x, shift_y, frame_labyrinthe, photo, ((id_mur % 15) * 45), ((int(id_mur / 15)) * 45))

    #retourne la valeur entier arrondi au superier ou non
    def __int_more_one(self, coord):
        if int(coord / 45) < coord / 45:
            integer_round = int(coord / 45) + 1
        else:
            integer_round = int(coord / 45)
        return integer_round

    #renvoie le droit de se positionner ou non
    def __move_or_not(self, condition1, condition2, condition3, condition4):

        return bool(condition1 == "True" and condition2 == "True" and condition3 == "True" and condition4 == "True")

    def situation(self):

        num_img_bd = (self.__int_more_one(self.positionY + 43) * 15) + self.__int_more_one(self.positionX + 32) - 15
        num_img_hd = (self.__int_more_one(self.positionY) * 15) + self.__int_more_one(self.positionX + 32) - 15
        num_img_bg = (self.__int_more_one(self.positionY + 43) * 15) + self.__int_more_one(self.positionX) - 15
        num_img_hg = (self.__int_more_one(self.positionY) * 15) + self.__int_more_one(self.positionX) - 15

        if num_img_bd != num_img_hd and num_img_bd != num_img_bg:
            return bool(self.__move_or_not(self.__regarderDroitLabyrinthe(num_img_bd, "HautGauche"), self.__regarderDroitLabyrinthe(num_img_hd, "BasGauche"), self.__regarderDroitLabyrinthe(num_img_bg, "HautDroit"), self.__regarderDroitLabyrinthe(num_img_hg, "BasDroit")))

        elif num_img_bd != num_img_hd and num_img_bd == num_img_bg:
            return bool(self.__move_or_not(self.__regarderDroitLabyrinthe(num_img_bd, "HautDroit"), self.__regarderDroitLabyrinthe(num_img_bg, "HautGauche"), self.__regarderDroitLabyrinthe(num_img_hd, "BasDroit"), self.__regarderDroitLabyrinthe(num_img_hg, "BasGauche")))

        elif num_img_bd == num_img_hd and num_img_bd != num_img_bg:
            return bool(self.__move_or_not(self.__regarderDroitLabyrinthe(num_img_bd, "BasGauche"), self.__regarderDroitLabyrinthe(num_img_hd, "HautGauche"), self.__regarderDroitLabyrinthe(num_img_bg, "BasDroit"), self.__regarderDroitLabyrinthe(num_img_hg, "HautDroit")))

        elif num_img_bd == num_img_hd and num_img_bd == num_img_bg:
            return bool(self.__move_or_not(self.__regarderDroitLabyrinthe(num_img_bg, "BasGauche"), self.__regarderDroitLabyrinthe(num_img_hg, "HautGauche"), self.__regarderDroitLabyrinthe(num_img_bd, "BasDroit"), self.__regarderDroitLabyrinthe(num_img_hd, "HautDroit")))


        

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
