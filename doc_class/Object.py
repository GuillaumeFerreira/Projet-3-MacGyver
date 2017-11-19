#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Autor: Ferreira Guillaume
#Projet 3: parcours python openclassroom

'''Element for building object

    allows to create an object and to place objects in the maze

'''
import random
from tkinter import Canvas, NW
from doc_class.ElementLabyrinthe import ElementLabyrinthe

class Objet(ElementLabyrinthe):
    '''

        Create an object and can destroy it

    '''
    liste_img_dec_obj = []
    liste_img_dec_obj.append(-197)
    liste_img_dec_obj.append(-158)
    liste_img_dec_obj.append(-4)
    liste_img_dec_obj.append(-120)
    liste_img_dec_obj.append(-81)
    liste_img_dec_obj.append(-42)

    def __init__(self, FrameLabyrinthe, photo, id_obj):
        self.id_obj = id_obj
        self.__valid_coordinates_objet()
        self.canvas_objet = Canvas(FrameLabyrinthe, width=39, height=43, borderwidth=0, highlightthickness=0)
        self.canvas_objet.create_image(Objet.liste_img_dec_obj[id_obj], -1, anchor=NW, image=photo)
        self.canvas_objet.place(x=self.position_x, y=self.position_y)

    def __valid_coordinates_objet(self):
        '''

            Construction of the coordinate list to optimize the chances
            of valid coordinates for the position of objects.

        '''
        liste_coord = []
        valid_coordinates = 23
        while valid_coordinates < 570:
            liste_coord.append(valid_coordinates)
            valid_coordinates = valid_coordinates + 22.5

        while self.situation() != True:
            self.position_x = random.choice(liste_coord)
            self.position_y = random.choice(liste_coord)

    def object_is_picked_up(self):
        '''

            Destroy object.

        '''
        self.canvas_objet.destroy()
