#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random

from ClassObject import *


    
	

    



def perdu():
        global fenetrePerdu
        fenetrePerdu = Tk()
        fenetrePerdu.title('Game Over')
        fenetrePerdu.configure(width=400,height=250)
        w = Label(fenetrePerdu, text="Gardien : Je t'avais prévenu ! Bye bye mon ami!\n \n Tu as perdu, mais ne te décourage pas, recommence.")
        w.place(x=50, y=40)
        fenetre.unbind('<Right>') 
        fenetre.unbind('<Left>')
        fenetre.unbind('<Up>')
        fenetre.unbind('<Down>')
        Button(fenetrePerdu,text='Quitter', command=quit).place(x=90, y=180)
        Button(fenetrePerdu,text='Rejouer' , command=rejouerLoose).place(x=230, y=180)

def gagner():
        
        fenetreGagner = Tk()
        fenetreGagner.title('Victoire')
        fenetreGagner.configure(width=400,height=150)
        w = Label(fenetreGagner, text="Bravo, le gardien t'a finalement laissé passer, tu es libre!")
        w.place(x=50, y=40)
        fenetre.unbind('<Right>') 
        fenetre.unbind('<Left>')
        fenetre.unbind('<Up>')
        fenetre.unbind('<Down>')
        Button(fenetreGagner,text='Quitter', command=quit).place(x=120, y=80)
        Button(fenetreGagner,text='Rejouer' , command=rejouer).place(x=250, y=80)
        


