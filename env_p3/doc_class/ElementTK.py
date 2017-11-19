#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#Autor: Ferreira Guillaume
#Projet 3: parcours python openclassroom

"""Just Element Tkinter

    File ElementTK.py  allows creation of objects from the library
    tkinter needed for the labyrinth.

"""
import tkinter


class Fenetre:
    """

    class Fenetre allows the creation of window that will contain the game.
        - 4 instances

    """
    def __init__(self, title, width, height):
        self.fenetre = tkinter.Tk()
        self.title = title
        self.height = height
        self.width = width

    def build(self):
        """

        allows you to define the title and size of the window.

        """
        self.fenetre.title(self.title)
        self.fenetre.geometry("{0}x{1}+0+0".format(self.width, self.height))

    def close_the_window(self):
        """

        destroy the window.

        """
        self.fenetre.destroy()

    def dont_move(self):
        """

        prevents the character from moving.

        """
        self.fenetre.unbind('<Right>')
        self.fenetre.unbind('<Left>')
        self.fenetre.unbind('<Up>')
        self.fenetre.unbind('<Down>')


class FrameLab:
    """contains the labyrinth

    allows to create the framework for the labyrinth

    """
    def __init__(self, racine, width, height, position_x, position_y):
        self.frame = tkinter.Frame(racine, borderwidth=2)
        self.width = width
        self.height = height
        self.position_x = position_x
        self.position_y = position_y

    def build(self):
        """

        allows you to define and place the framework

        """
        self.frame.config(width=self.width, height=self.height)
        self.frame.place(x=self.position_x, y=self.position_y)


class Onglet:
    """

    allows you to create a tab with text for more interaction with the player

    """
    def __init__(self, racine, titre, Padx, Pady, position_x, position_y):
        self.labelframe = tkinter.LabelFrame(racine, text=titre, padx=Padx, pady=Pady)
        self.position_x = position_x
        self.position_y = position_y
        self.string_var = tkinter.StringVar()
    def build(self):
        """

        create the tab and initialize the text

        """
        self.labelframe.place(x=self.position_x, y=self.position_y)
        tkinter.Label(self.labelframe, textvariable=self.string_var).pack()
        self.string_var.set("-")
    def change_text(self, new_sentence):
        """

        allows to change the text of the tab

        """
        self.string_var.set(new_sentence)
