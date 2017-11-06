#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random


class Fenetre:
    
    def __init__(self,title,width,height):
        self.fenetre=Tk()
        self.title=title
        self.height=height
        self.width=width

    def construction(self):
        self.fenetre.title(self.title)
        self.fenetre.geometry("{0}x{1}+0+0".format(self.width,self.height))
    def fermerLaFenetre(self):
        self.fenetre.destroy()
    def nePlusBouger(self):
        self.fenetre.unbind('<Right>') 
        self.fenetre.unbind('<Left>')
        self.fenetre.unbind('<Up>')
        self.fenetre.unbind('<Down>')

      

class FrameLab:
    def __init__(self,racine,width,height,x,y):
        self.frame=Frame(racine, borderwidth=2, relief=GROOVE)
        self.width=width
        self.height=height
        self.x=x
        self.y=y
    def construction(self):
        self.frame.config(width=self.width, height=self.height)
        self.frame.place(x=self.x, y=self.y)
class Onglet:
    def __init__(self,racine,titre,Padx,Pady,x,y):
        self.labelframe=LabelFrame(racine, text=titre, padx=Padx, pady=Pady)
        self.x=x
        self.y=y
        self.stringVar=StringVar()
    def construction(self):
        self.labelframe.place(x=self.x, y=self.y)
        Label(self.labelframe, textvariable=self.stringVar).pack()
        self.stringVar.set("-")
    def changerTxt(self,nouvellePhrase):
        self.stringVar.set(nouvellePhrase)
