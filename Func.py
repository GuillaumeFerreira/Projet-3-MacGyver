#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import *
import os
import re
from PIL import Image, ImageTk
import random

from ElementLabyrinthe import *
from Personnage import *

def creationDuLabyrinthe(photo,frameLabyrinthe):
    ###############################################################################
    #Initialisation et construction de labyrinthe  
    #ouverture du fichier qui decrit 
    f = open("Mac.txt", "r")
    i=0
    for line in f:
        
        e = re.search(r'-->(.+)', line)
        extension = e.group(1)
        
        fLab = open("DroitLab.txt", "r")

        for lineD in fLab:
            
            try:
               
                x = re.search(r'^'+extension+'-->.+Pos:(.+),', lineD)
               
                x = x.group(1)
                
                yy = re.search(r'^'+extension+'-->.+,(.+)', lineD)
                y = yy.group(1)

                #canvas(float(x),float(y),photo,i)
                ElementLabyrinthe.mur(float(x),float(y),frameLabyrinthe,photo,i)
            except:
                #rien a faire pas la bonne ligne
                pass
            else:
                #rien a faire pas la bonne ligne
                pass
        fLab.close()
        
        i=i+1
    f.close()
    ################################################################################
    


   
def ramasserObjetEtVictoire(ListeObjet,Mac,ongletObjet,ongletGardien,GardienLab):
   ramasserLesObjets(ListeObjet,Mac)
   nombreobjet_to_pick_up(Mac,ongletObjet)
   
   situation=0
   if Mac.mac_dans_zone_gardien() and Mac.come_out_of_the_area:
        Mac.come_out_of_the_area=False
        Mac.number_of_times_in_the_area=Mac.number_of_times_in_the_area+1
        if Mac.objet_to_pick_up==6:
            
            situation=2
            #gagner(fenetre)
			
        else:
            if Mac.number_of_times_in_the_area>=3:
                #perdu(fenetre)
                
                situation=1
            elif GardienLab.memory_objet==Mac.objet_to_pick_up and Mac.number_of_times_in_the_area<3:
                    #gardien en tres en colere
                    ongletGardien.change_text("Tu te crois malin!\n Tu n'as rien récupéré de plus, va t'en d'ici tout de suite!!!")
            elif Mac.number_of_times_in_the_area==2 and GardienLab.memory_objet!=Mac.objet_to_pick_up:
                ongletGardien.change_text("C'est la deuxième fois que tu viens me voir!\n Tu n'as que " + str(Mac.objet_to_pick_up) +" objets!\n Je te déconseille de revenir me voir une troisième fois \n sans tous les objets!")
            else:
                    #gardien en colere
                if Mac.objet_to_pick_up==1:
                    ongletGardien.change_text("Quoi ? Seulement " + str(Mac.objet_to_pick_up) +" objet ramassé!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
                else:
                    ongletGardien.change_text("Quoi ? Seulement " + str(Mac.objet_to_pick_up) +" objets ramassés!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
                
        GardienLab.memory_objet=Mac.objet_to_pick_up
   else:
        if Mac.mac_dans_zone_gardien()!=True:
            Mac.come_out_of_the_area=True
   return situation
        
def ramasserLesObjets(ListeObjet,Mac):
        #On regarde si MacGayver se trouve sur un objet si oui , on le supprime
        for objet in ListeObjet:
            if Mac.pick_up_objet(objet.position_x,objet.position_y):
                objet.object_is_picked_up()
                ListeObjet.remove(objet)

def nombreobjet_to_pick_up(Mac,ongletObjet):
    if Mac.objet_to_pick_up==0:
        ongletObjet.change_text(" - ")
    elif Mac.objet_to_pick_up==1:
        ongletObjet.change_text(str(Mac.objet_to_pick_up) +" objet ramassé.")
    else:
        ongletObjet.change_text(str(Mac.objet_to_pick_up) +" objets ramassés.")
        




