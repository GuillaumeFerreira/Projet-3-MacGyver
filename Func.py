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
   nombreObjetRamasser(Mac,ongletObjet)
   
   situation=0
   if Mac.mac_dans_zone_gardien() and Mac.etreResortiDeLaZone:
        Mac.etreResortiDeLaZone=False
        Mac.nombreDeFoisDansZone=Mac.nombreDeFoisDansZone+1
        if Mac.objetRamasser==6:
            
            situation=2
            #gagner(fenetre)
			
        else:
            if Mac.nombreDeFoisDansZone>=3:
                #perdu(fenetre)
                
                situation=1
            elif GardienLab.memoireNbObjet==Mac.objetRamasser and Mac.nombreDeFoisDansZone<3:
                    #gardien en tres en colere
                    ongletGardien.change_text("Tu te crois malin!\n Tu n'as rien récupéré de plus, va t'en d'ici tout de suite!!!")
            elif Mac.nombreDeFoisDansZone==2 and GardienLab.memoireNbObjet!=Mac.objetRamasser:
                ongletGardien.change_text("C'est la deuxième fois que tu viens me voir!\n Tu n'as que " + str(Mac.objetRamasser) +" objets!\n Je te déconseille de revenir me voir une troisième fois \n sans tous les objets!")
            else:
                    #gardien en colere
                if Mac.objetRamasser==1:
                    ongletGardien.change_text("Quoi ? Seulement " + str(Mac.objetRamasser) +" objet ramassé!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
                else:
                    ongletGardien.change_text("Quoi ? Seulement " + str(Mac.objetRamasser) +" objets ramassés!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
                
        GardienLab.memoireNbObjet=Mac.objetRamasser
   else:
        if Mac.mac_dans_zone_gardien()!=True:
            Mac.etreResortiDeLaZone=True
   return situation
        
def ramasserLesObjets(ListeObjet,Mac):
        #On regarde si MacGayver se trouve sur un objet si oui , on le supprime
        for objet in ListeObjet:
            if Mac.ramasseObjet(objet.position_x,objet.position_y):
                objet.object_is_picked_up()
                ListeObjet.remove(objet)

def nombreObjetRamasser(Mac,ongletObjet):
    if Mac.objetRamasser==0:
        ongletObjet.change_text(" - ")
    elif Mac.objetRamasser==1:
        ongletObjet.change_text(str(Mac.objetRamasser) +" objet ramassé.")
    else:
        ongletObjet.change_text(str(Mac.objetRamasser) +" objets ramassés.")
        




