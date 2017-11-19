#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Autor: Ferreira Guillaume
#Projet 3: parcours python openclassroom
'''

    Defined all types of characters

'''
from tkinter import Canvas, NW
from ElementLabyrinthe import ElementLabyrinthe

class Personnage(ElementLabyrinthe):
    '''

        class character gives the possibility to create
        macgyver, guardian and any other character

    '''
    def __init__(self, frame_labyrinthe, photo, Height, se_deplacer, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.se_deplacer = se_deplacer
        self.canvas = Canvas(frame_labyrinthe, width=32, height=Height, borderwidth=0, highlightthickness=0)
        self.canvas.create_image(0, 0, anchor=NW, image=photo)
        self.canvas.place(x=self.position_x, y=self.position_y)
        self.memory_objet = 0
        self.objet_to_pick_up = 0
        self.number_of_times_in_the_area = 0
        self.come_out_of_the_area = True

    @classmethod
    def gardien(cls, frame_labyrinthe, photo):
        '''

            Gardien creation.

        '''
        return cls(frame_labyrinthe, photo, 36, False, 592, 570)
    @classmethod
    def mac_gyver(cls, frame_labyrinthe, photo):
        '''

            Macgyver creation.

        '''
        return cls(frame_labyrinthe, photo, 43, True, 51, 46)

    def mac_dans_zone_gardien(self):
        '''

            If character is in zone of gardien return True.

        '''
        return bool(self.position_x > 555 and self.position_y > 500)

    def move_to_the_right(self):
        '''

            Move character to the right.

        '''
        if self.se_deplacer:
            self.position_x = self.position_x + 22.5
            if self.situation():
                self.canvas.place(x=self.position_x, y=self.position_y)
            else:
                self.position_x = self.position_x - 22.5

    def move_to_the_left(self):
        '''

            Move character to the Ledt.

        '''
        if self.se_deplacer:
            self.position_x = self.position_x - 22.5
            if self.situation():
                self.canvas.place(x=self.position_x, y=self.position_y)
            else:
                self.position_x = self.position_x + 22.5

    def move_to_the_down(self):
        '''

            Character move down.

        '''
        if self.se_deplacer:
            self.position_y = self.position_y + 22.5
            if self.situation():
                self.canvas.place(x=self.position_x, y=self.position_y)
            else:
                self.position_y = self.position_y - 22.5

    def move_to_the_up(self):
        '''

            Character move up.

        '''
        if self.se_deplacer:
            self.position_y = self.position_y - 22.5
            if self.situation():
                self.canvas.place(x=self.position_x, y=self.position_y)
            else:
                self.position_y = self.position_y + 22.5

    def pick_up_objet(self, x_of_object, y_of_object):
        '''

            Object is picked up by the character.

        '''
        possibilite_objet_ramasser = False
        if (int(self.position_x) >= int(x_of_object) and int(self.position_x) < int(x_of_object + 39)) or (int(self.position_x + 32) >= int(x_of_object) and int(self.position_x + 32) < int(x_of_object + 39)):
            if (int(self.position_y) >= int(y_of_object - 10) and int(self.position_y) < int(y_of_object + 43)) or (int(self.position_y + 43) > int(y_of_object) and int(self.position_y + 43) < int(y_of_object + 40)):
                self.objet_to_pick_up = self.objet_to_pick_up + 1
                possibilite_objet_ramasser = True
        return possibilite_objet_ramasser
