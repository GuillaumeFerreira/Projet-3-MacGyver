#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

    The func.py file gathers the functions necessary
    for the management of the game

'''
import re
from doc_class.ElementLabyrinthe import ElementLabyrinthe


def creation_of_the_labyrinth(photo, frame_fabyrinthe):
    '''

        Initialization and construction of labyrinth

    '''
    file = open("config\Mac.txt", "r")
    i = 0
    for line in file:

        search_num_img_rule = re.search(r'-->(.+)', line)
        num_img_rule = search_num_img_rule.group(1)

        f_lab = open("config\DroitLab.txt", "r")

        for line_d in f_lab:

            try:
                search_item = re.search(r'^'+num_img_rule+'-->.+Pos:(.+),', line_d)

                search_item_x = search_item.group(1)

                search_item = re.search(r'^'+num_img_rule+'-->.+,(.+)', line_d)
                search_item_y = search_item.group(1)
                ElementLabyrinthe.mur(float(search_item_x), float(search_item_y), frame_fabyrinthe, photo, i)
            except:
                #rien a faire pas la bonne ligne
                pass
            else:
                #rien a faire pas la bonne ligne
                pass
        f_lab.close()

        i = i + 1
    file.close()

def pick_up_objects_and_win(liste_objet, mac, onglet_objet, onglet_gardien, gardien_lab):
    '''

        Check if the player and get to the end of the labyrinth
        and to fulfill his mission.

    '''
    pick_up_the_object(liste_objet, mac)
    nombre_objet_to_pick_up(mac, onglet_objet)
    situation = 0
    if mac.mac_dans_zone_gardien() and mac.come_out_of_the_area:
        mac.come_out_of_the_area = False
        mac.number_of_times_in_the_area = mac.number_of_times_in_the_area+1
        if mac.objet_to_pick_up == 6:
            situation = 2
        else:
            if mac.number_of_times_in_the_area >= 3:
                situation = 1
            elif gardien_lab.memory_objet == mac.objet_to_pick_up and mac.number_of_times_in_the_area < 3:
                #gardien en tres en colere
                onglet_gardien.change_text("Tu te crois malin!\n Tu n'as rien récupéré de plus, va t'en d'ici tout de suite!!!")
            elif mac.number_of_times_in_the_area == 2 and gardien_lab.memory_objet != mac.objet_to_pick_up:
                onglet_gardien.change_text("C'est la deuxième fois que tu viens me voir!\n Tu n'as que " + str(mac.objet_to_pick_up) +" objets!\n Je te déconseille de revenir me voir une troisième fois \n sans tous les objets!")
            else:
                #gardien en colere
                if mac.objet_to_pick_up == 1:
                    onglet_gardien.change_text("Quoi ? Seulement " + str(mac.objet_to_pick_up) +" objet ramassé!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
                else:
                    onglet_gardien.change_text("Quoi ? Seulement " + str(mac.objet_to_pick_up) +" objets ramassés!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")

        gardien_lab.memory_objet = mac.objet_to_pick_up
    else:
        if mac.mac_dans_zone_gardien() != True:
            mac.come_out_of_the_area = True
    return situation

def pick_up_the_object(liste_objet, mac):
    '''

        We look if macGyver is on an object if so, we delete it.

    '''
    for objet in liste_objet:
        if mac.pick_up_objet(objet.position_x, objet.position_y):
            objet.object_is_picked_up()
            liste_objet.remove(objet)

def nombre_objet_to_pick_up(mac, onglet_objet):
    '''

        Change the text of the tab.

    '''
    if mac.objet_to_pick_up == 0:
        onglet_objet.change_text(" - ")
    elif mac.objet_to_pick_up == 1:
        onglet_objet.change_text(str(mac.objet_to_pick_up) + " objet ramassé.")
    else:
        onglet_objet.change_text(str(mac.objet_to_pick_up) + " objets ramassés.")
