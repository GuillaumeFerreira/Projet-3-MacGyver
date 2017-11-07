#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import tkinter

class Fenetre:

    def __init__(self, title, width, height):
        self.fenetre = tkinter.Tk()
        self.title = title
        self.height = height
        self.width = width

    def build(self):
        self.fenetre.title(self.title)
        self.fenetre.geometry("{0}x{1}+0+0".format(self.width, self.height))

    def close_the_window(self):
        self.fenetre.destroy()

    def nePlusBouger(self):
        self.fenetre.unbind('<Right>')
        self.fenetre.unbind('<Left>')
        self.fenetre.unbind('<Up>')
        self.fenetre.unbind('<Down>')


class FrameLab:

    def __init__(self, racine, width, height, position_x, position_y):
        self.frame = tkinter.Frame(racine, borderwidth=2)
        self.width = width
        self.height = height
        self.x = position_x
        self.y = position_y

    def construction(self):
        self.frame.config(width=self.width, height=self.height)
        self.frame.place(x=self.x, y=self.y)


class Onglet:

    def __init__(self, racine, titre, Padx, Pady, position_x, position_y):
        self.labelframe = tkinter.LabelFrame(racine, text=titre, padx=Padx, pady=Pady)
        self.x = position_x
        self.y = position_y
        self.stringVar = tkinter.StringVar()
    def construction(self):
        self.labelframe.place(x=self.x, y=self.y)
        tkinter.Label(self.labelframe, textvariable=self.stringVar).pack()
        self.stringVar.set("-")
    def change_text(self, new_sentence):
        self.stringVar.set(new_sentence)
