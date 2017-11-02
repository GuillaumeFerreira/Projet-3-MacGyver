#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from multiprocessing import Process
from tkinter import *
import os
import re
from math import *
from PIL import Image, ImageTk
import datetime
import random

def main():
    sys.setrecursionlimit(1500)
    global fenetre
    global MacX
    global MacY
    global listeCoordX
    global listeCoordy
    global ListeObjet
    global ListeObjetCanvas
    global nbObjRamasser
    global nbPresentation
    global nbobj
    nbobj=0
    nbPresentation=0
    RevenuSortiZone=True
    nbObjRamasser=[]
    ListeObjetCanvas=[]
    listeCoordX=[]
    listeCoordy=[]
    nb=23
    while nb <570:
        listeCoordX.append(nb)
        listeCoordy.append(nb)
        nb=nb+22.5
        
    fenetre = Tk()
    fenetre.title('Labyrinthe P3')
    fenetre.geometry("{0}x{1}+0+0".format(fenetre.winfo_screenwidth()-15, fenetre.winfo_screenheight()-15))
    photo = PhotoImage(file="images/wall.gif")
    f = open("Mac.txt", "r")
   
    
    menubar = Menu(fenetre)

    menu1 = Menu(menubar, tearoff=0)
    menu1.add_command(label="Rejouer", command=rejouerDebut)
    menu1.add_command(label="Quitter", command=quit)
    
    menubar.add_cascade(label="Fichier", menu=menu1)

    menu2 = Menu(menubar, tearoff=0)
    menu2.add_command(label="A propos")
    menubar.add_cascade(label="Aide", menu=menu2)

    fenetre.config(menu=menubar)
    
    global Frame1
    Frame1 = Frame(fenetre, borderwidth=2, relief=GROOVE)
    Frame1.config(width=680, height=680)
    Frame1.place(x=400, y=10)
    global FenObjet
    global stringVar
    stringVar=StringVar()
    
    FenObjet = LabelFrame(fenetre, text="Objets récupérés", padx=20, pady=20)
    FenObjet.place(x=50, y=200)
    Label(FenObjet, textvariable=stringVar).pack()
    stringVar.set("-")
    
    stringVarConseil=StringVar()
    FenConseil = LabelFrame(fenetre, text="Conseil", padx=20, pady=20)
    FenConseil.place(x=50, y=50)
    Label(FenConseil, textvariable=stringVarConseil).pack()
    stringVarConseil.set("Ramasser tous les objets avant de se présenter \n au gardien. Il tient beaucoup à ses objets.")

    
    global stringVarGardien
    stringVarGardien=StringVar()
    FenGardien = LabelFrame(fenetre, text="Gardien", padx=20, pady=20)
    FenGardien.place(x=50, y=400)
    Label(FenGardien, textvariable=stringVarGardien).pack()
    stringVarGardien.set("Personne ne sortira tant que je ne serai pas satisfait!")
    
    i=0
    for line in f:
        
        e = re.search(r'-->(.+)', line)
        extension = e.group(1)
        
        fLab = open("DroitLab.txt", "r")
        #contenu = fLab.read()
        for lineD in fLab:
            
            try:
               
                x = re.search(r'^'+extension+'-->.+Pos:(.+),', lineD)
               
                x = x.group(1)
                
                yy = re.search(r'^'+extension+'-->.+,(.+)', lineD)
                y = yy.group(1)
                #print("Image num : "+extension+" x: "+x+ " y: "+y)
                canvas(float(x),float(y),photo,i)
                
            except:
                #rien a faire pas la bonne ligne
                pass
            else:
                #rien a faire pas la bonne ligne
                pass
        fLab.close()
        
        i=i+1
    f.close()




    class Objet:
        numero_objet=0
        
        def __init__(self):
            
            Objet.numero_objet += 1
            
            coord=self.coordValide()
            self.x=float(coord.split(",")[0])
            self.y=float(coord.split(",")[1])
            
            self.photo=""

        def coordValide(self):
            
            x=random.choice(listeCoordX)
            y=random.choice(listeCoordy)
            coord= str(x) + "," + str(y)
            return coord
        def listeImgDec(self):
            listeImgDecObj=[]
            listeImgDecObj.append(-197)
            listeImgDecObj.append(-158)
            listeImgDecObj.append(-4)
            listeImgDecObj.append(-120)
            listeImgDecObj.append(-81)
            listeImgDecObj.append(-42)
            return listeImgDecObj

        
    MacX=51
    MacY=46
    i=1
    #################################################
    #Creation de la liste d objets
    ListeObjet=[]

    for i in range(6):
        
        newObjet=Objet()
        ListeObjet.append(newObjet)
        print("ajout " + str(newObjet)+" "+ str(newObjet.numero_objet)+" "+ str(newObjet.x)+ " "+ str(newObjet.y))
       
    #################################################

        
    #################################################
    #Creation du gardien   
    photo3 = PhotoImage(file="images/gardien.gif")

    canvas14 = Canvas(Frame1,width=32, height=36, borderwidth=0,highlightthickness=0)
    canvas14.create_image(0, 0, anchor=NW, image=photo3)
    canvas14.place(x=592, y=570)
    ##################################################

    
    photo4=Image.open('images/tc-image007.png')
    canvas15 = Canvas(Frame1,width=32, height=36, borderwidth=0,highlightthickness=0)

    resolution = (100,263)
    img = ImageTk.PhotoImage(photo4.resize(resolution))
    canvas15.create_image(-2, -200, anchor=NW, image=img)
    canvas15.place(x=592, y=610)


    ######################################
    #evite la superposition d objet
    #fonction recursive
    def changeX(xprec,valx,i):
        
        for j in range(0,i):
            if (valx<(xprec[j]+43)) and (valx>(xprec[j]-43)):
                valx=random.uniform(22.5, 570.0)
               
                changeX(xprec,valx,i)
            
                
        return float(valx)
    ####################################################
    #Ajout des objets
    listeImgDecObj=[]
    listeImgDecObj.append(-197)
    listeImgDecObj.append(-158)
    listeImgDecObj.append(-4)
    listeImgDecObj.append(-120)
    listeImgDecObj.append(-81)
    listeImgDecObj.append(-42)
    i=0
    xprec=[]
    global listeCoordObjValideX
    global listeCoordObjValideY
    listeCoordObjValideX=[]
    listeCoordObjValideY=[]
    photo6=PhotoImage(file="images/tc-image005.gif")
    for objet in ListeObjet:

        #photo6=PhotoImage(file=objet.photo)
        valx2=objet.x
        valy=objet.y
        coordValide= False
        while coordValide == False:
            if int(valx2/45)<valx2/45:
                Pos=int(valx2/45)+1
            else:
                Pos=int(valx2/45)
                
            if int((valx2+39)/45)<(valx2+39)/45:
                PosD=int((valx2+39)/45)+1
            else:
                PosD=int((valx2+39)/45)
                
            if int(valy/45)<valy/45:
                PosH=int((valy)/45)+1
            else:
                PosH=int((valy)/45)
                
            if int((valy+43)/45)<(valy+43)/45:
                PosB=int((valy+43)/45)+1
            else:
                PosB=int((valy+43)/45)

            condition1="False"
            condition2="False"
            condition3="False"
            condition4="False"
            NumImgBD=(PosB*15)+PosD-15
            NumImgBG=(PosB*15)+Pos-15
            NumImgHD=(PosH*15)+PosD-15
            NumImgHG=(PosH*15)+Pos-15


            if NumImgBD!=NumImgHD and NumImgBD!=NumImgBG:
                
                condition1=regarderDroit(NumImgBD,"HautGauche")
                condition2=regarderDroit(NumImgHD,"BasGauche")
                condition3=regarderDroit(NumImgBG,"HautDroit")
                condition4=regarderDroit(NumImgHG,"BasDroit")

                if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":

                    canvasObj(float(valx2),float(valy),photo6,listeImgDecObj[i])

                    listeCoordObjValideX.append(int(valx2))
                    listeCoordObjValideY.append(int(valy))
                    coordValide=True
                    i=i+1
                else:
                   
                    valx2=random.choice(listeCoordX)
                    valy=random.choice(listeCoordy)
                    
            elif NumImgBD!=NumImgHD and NumImgBD==NumImgBG:
                condition1=regarderDroit(NumImgBD,"HautDroit")
                condition2=regarderDroit(NumImgBG,"HautGauche")
                condition3=regarderDroit(NumImgHD,"BasDroit")
                condition4=regarderDroit(NumImgHG,"BasGauche")
 
                if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
##                    if i!=0:
##                        #evite la superposition d objet
##                        valx2=changeX(xprec,objet.x,len(xprec))
##
                    canvasObj(float(valx2),float(valy),photo6,listeImgDecObj[i])
##                    xprec.append(float(valx2))
                    listeCoordObjValideX.append(int(valx2))
                    listeCoordObjValideY.append(int(valy))
                    coordValide=True
                    i=i+1
                else:
                   
                    valx2=random.choice(listeCoordX)
                    valy=random.choice(listeCoordy)
            elif NumImgBD==NumImgHD and NumImgBD!=NumImgBG:
                condition1=regarderDroit(NumImgBD,"BasGauche")
                condition2=regarderDroit(NumImgHD,"HautGauche")
                condition3=regarderDroit(NumImgBG,"BasDroit")
                condition4=regarderDroit(NumImgHG,"HautDroit")


                
                if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
                    #if i!=0:
##                        #evite la superposition d objet
##                        valx2=changeX(xprec,objet.x,len(xprec))
##
                    canvasObj(float(valx2),float(valy),photo6,listeImgDecObj[i])
##                    xprec.append(float(valx2))
                    listeCoordObjValideX.append(int(valx2))
                    listeCoordObjValideY.append(int(valy))
                    coordValide=True
                    i=i+1
                else:

                    valx2=random.choice(listeCoordX)
                    valy=random.choice(listeCoordy)
                    
            elif NumImgBD==NumImgHD and NumImgBG==NumImgBD:
                condition1=regarderDroit(NumImgBG,"BasGauche")
                condition2=regarderDroit(NumImgHG,"HautGauche")
                condition3=regarderDroit(NumImgBD,"BasDroit")
                condition4=regarderDroit(NumImgHD,"HautDroit")

                if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
##                    if i!=0:
##                        #evite la superposition d objet
##                        valx2=changeX(xprec,objet.x,len(xprec))
##
                    canvasObj(float(valx2),float(valy),photo6,listeImgDecObj[i])
##                    xprec.append(float(valx2))
                    listeCoordObjValideX.append(int(valx2))
                    listeCoordObjValideY.append(int(valy))
                    coordValide=True
                    i=i+1
                else:
                    
                    valx2=random.choice(listeCoordX)
                    valy=random.choice(listeCoordy)
           
            else:
                #coordValide=True
                print ("pass")


                                
    photo2 = PhotoImage(file="images/macgyver.gif")
    global canvas13
    canvas13 = Canvas(Frame1,width=32, height=43, borderwidth=0,highlightthickness=0)
    canvas13.create_image(0, 0, anchor=NW, image=photo2)
    canvas13.place(x=MacX, y=MacY)
    

    
    fenetre.bind('<Right>', toucheeventR) 
    fenetre.bind('<Left>', toucheeventL)
    fenetre.bind('<Up>', toucheeventU)
    fenetre.bind('<Down>', toucheeventD)


   
    fenetre.mainloop()
  
def canvasObj(x,y,photo,decalage):
    
    
    
    canvas16 = Canvas(Frame1,width=39, height=43, borderwidth=0,highlightthickness=0)
    canvas16.create_image(decalage, -1, anchor=NW, image=photo)
    canvas16.place(x=x, y=y)
    ListeObjetCanvas.append(canvas16)
  
    return canvas16

def canvas(x,y,photo,i):
    borderwidth=-4
    borderheight=-5
    placeX =(i%15)*45
    placeY=(int(i/15))*45
    
  
 
    canvas = Canvas(Frame1,width=45, height=45, borderwidth=0, highlightthickness=0)
    canvas.create_image(borderwidth+(x), borderheight+(y), anchor=NW, image=photo)
    canvas.place(x=placeX, y=placeY)
    return canvas
def toucheeventR(evt):
    global MacX
    global MacY
    MacX=MacX+22.5
    global NumImg
    
    if int(MacX/45)<MacX/45:
        PosG=int(MacX/45)+1
    else:
        PosG=int(MacX/45)
        
    MacXdroite=MacX+32   
    if int(MacXdroite/45)<MacXdroite/45:
        PosD=int(MacXdroite/45)+1
    else:
        PosD=int(MacXdroite/45)
      

        
    if int(MacY/45)<MacY/45:
        PosYhaut=int(MacY/45)+1
    else:
        PosYhaut=int(MacY/45)
    MacYdbas=MacY+43  
    if int(MacYdbas/45)<MacYdbas/45:
        PosYbas=int(MacYdbas/45)+1
    else:
        PosYbas=int(MacYdbas/45)

    condition1="False"
    condition2="False"
    condition3="False"
    condition4="False"
    NumImgBD=(PosYbas*15)+PosD-15
    NumImgBG=(PosYbas*15)+PosG-15
    NumImgHD=(PosYhaut*15)+PosD-15
    NumImgHG=(PosYhaut*15)+PosG-15


    if NumImgBD!=NumImgHD and NumImgBD!=NumImgBG:
        condition1=regarderDroit(NumImgBD,"HautGauche")
        condition2=regarderDroit(NumImgHD,"BasGauche")
        condition3=regarderDroit(NumImgBG,"HautDroit")
        condition4=regarderDroit(NumImgHG,"BasDroit")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacX=MacX-22.5
    elif NumImgBD!=NumImgHD and NumImgBD==NumImgBG:
        condition1=regarderDroit(NumImgBD,"HautDroit")
        condition2=regarderDroit(NumImgBG,"HautGauche")
        condition3=regarderDroit(NumImgHD,"BasDroit")
        condition4=regarderDroit(NumImgHG,"BasGauche")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacX=MacX-22.5
    elif NumImgBD==NumImgHD and NumImgBD!=NumImgBG:
        condition1=regarderDroit(NumImgBD,"BasGauche")
        condition2=regarderDroit(NumImgHD,"HautGauche")
        condition3=regarderDroit(NumImgBG,"BasDroit")
        condition4=regarderDroit(NumImgHG,"HautDroit")


        
        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacX=MacX-22.5
            
    elif NumImgBD==NumImgHD and NumImgBD==NumImgBG:
        condition1=regarderDroit(NumImgBG,"BasGauche")
        condition2=regarderDroit(NumImgHG,"HautGauche")
        condition3=regarderDroit(NumImgBD,"BasDroit")
        condition4=regarderDroit(NumImgHD,"HautDroit")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacX=MacX-22.5
    else:
        pass
    ramasserObj(MacX,MacY)
    gagner(MacX,MacY)
    
    

def regarderDroit(NumImg,positionAregarder):            
    f = open("Mac.txt", "r")
    global droit
    
    for line in f:
        global extension
        try:
            e = re.search(r'^'+str(NumImg)+'-->(.+)', line)
            
            extension = e.group(1)
            
        except:
            #rien a faire pas la bonne ligne
            pass
        else:
            #rien a faire pas la bonne ligne
            pass
     
    fLab = open("DroitLab.txt", "r")
        
    for lineD in fLab:
        
        try:
            x = re.search(r'^'+extension+'-->.+HG=(.+),HD=(.+),BG=(.+),BD=(.+)/', lineD)
              
            
            if positionAregarder=="HautGauche":
                droit=x.group(1)
            elif positionAregarder=="HautDroit":
                droit=x.group(2)
            elif positionAregarder=="BasGauche":
                droit=x.group(3)
            elif positionAregarder=="BasDroit":
                droit=x.group(4)
            else:
                pass
            
        except:
            #rien a faire pas la bonne ligne
            pass
        else:
            #rien a faire pas la bonne ligne
            pass

    return (droit)
                      
def toucheeventL(evt):
    global MacY
    global MacX
    MacX=MacX-22.5
    

    if int(MacX/45)<MacX/45:
        PosG=int(MacX/45)+1
    else:
        PosG=int(MacX/45)
        
    MacXdroite=MacX+32   
    if int(MacXdroite/45)<MacXdroite/45:
        PosD=int(MacXdroite/45)+1
    else:
        PosD=int(MacXdroite/45)

        
    if int(MacY/45)<MacY/45:
        PosYhaut=int(MacY/45)+1
    else:
        PosYhaut=int(MacY/45)
    MacYdbas=MacY+43  
    if int(MacYdbas/45)<MacYdbas/45:
        PosYbas=int(MacYdbas/45)+1
    else:
        PosYbas=int(MacYdbas/45)
    condition1="False"
    condition2="False"
    condition3="False"
    condition4="False"
    NumImgBD=(PosYbas*15)+PosD-15
    NumImgBG=(PosYbas*15)+PosG-15
    NumImgHD=(PosYhaut*15)+PosD-15
    NumImgHG=(PosYhaut*15)+PosG-15


    if NumImgBD!=NumImgHD and NumImgBD!=NumImgBG:
        condition1=regarderDroit(NumImgBD,"HautGauche")
        condition2=regarderDroit(NumImgHD,"BasGauche")
        condition3=regarderDroit(NumImgBG,"HautDroit")
        condition4=regarderDroit(NumImgHG,"BasDroit")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacX=MacX+22.5
    elif NumImgBD!=NumImgHD and NumImgBD==NumImgBG:
        condition1=regarderDroit(NumImgBD,"HautDroit")
        condition2=regarderDroit(NumImgBG,"HautGauche")
        condition3=regarderDroit(NumImgHD,"BasDroit")
        condition4=regarderDroit(NumImgHG,"BasGauche")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacX=MacX+22.5
    elif NumImgBD==NumImgHD and NumImgBD!=NumImgBG:
        condition1=regarderDroit(NumImgBD,"BasGauche")
        condition2=regarderDroit(NumImgHD,"HautGauche")
        condition3=regarderDroit(NumImgBG,"BasDroit")
        condition4=regarderDroit(NumImgHG,"HautDroit")


        
        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacX=MacX+22.5
            
    elif NumImgBD==NumImgHD and NumImgBD==NumImgBD:
        condition1=regarderDroit(NumImgBG,"BasGauche")
        condition2=regarderDroit(NumImgHG,"HautGauche")
        condition3=regarderDroit(NumImgBD,"BasDroit")
        condition4=regarderDroit(NumImgHD,"HautDroit")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacX=MacX+22.5
    else:
        pass
    ramasserObj(MacX,MacY)
    gagner(MacX,MacY)
'''    
    if  PosYhaut==PosYbas:
        if PosG==PosD:
            print("regarder droit image numero "+str((PosYbas*15)+PosG-15))
            
        else:
            print("regarder droit image numero "+str((PosYbas*15)+PosG-15))
    else:
        if PosG==PosD:
            print("regarder droit image numero "+str((PosYbas*15)+PosG-15)+" et "+str((PosYhaut*15)+PosG-15))
        else:
            print("regarder droit image numero "+str((PosYbas*15)+PosG-15)+" et "+str((PosYhaut*15)+PosG-15))'''

def toucheeventU(evt):
    global MacX
    global MacY
    MacY=MacY-22.5
    
    if int(MacX/45)<MacX/45:
        PosG=int(MacX/45)+1
    else:
        PosG=int(MacX/45)
        
    MacXdroite=MacX+32   
    if int(MacXdroite/45)<MacXdroite/45:
        PosD=int(MacXdroite/45)+1
    else:
        PosD=int(MacXdroite/45)

        
    if int(MacY/45)<MacY/45:
        PosYhaut=int(MacY/45)+1
    else:
        PosYhaut=int(MacY/45)
    MacYdbas=MacY+43  
    if int(MacYdbas/45)<MacYdbas/45:
        PosYbas=int(MacYdbas/45)+1
    else:
        PosYbas=int(MacYdbas/45)
    
    condition1="False"
    condition2="False"
    condition3="False"
    condition4="False"
    NumImgBD=(PosYbas*15)+PosD-15
    NumImgBG=(PosYbas*15)+PosG-15
    NumImgHD=(PosYhaut*15)+PosD-15
    NumImgHG=(PosYhaut*15)+PosG-15


    if NumImgBD!=NumImgHD and NumImgBD!=NumImgBG:
        condition1=regarderDroit(NumImgBD,"HautGauche")
        condition2=regarderDroit(NumImgHD,"BasGauche")
        condition3=regarderDroit(NumImgBG,"HautDroit")
        condition4=regarderDroit(NumImgHG,"BasDroit")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacY=MacY+22.5
    elif NumImgBD!=NumImgHD and NumImgBD==NumImgBG:
        condition1=regarderDroit(NumImgBD,"HautDroit")
        condition2=regarderDroit(NumImgBG,"HautGauche")
        condition3=regarderDroit(NumImgHD,"BasDroit")
        condition4=regarderDroit(NumImgHG,"BasGauche")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacY=MacY+22.5
    elif NumImgBD==NumImgHD and NumImgBD!=NumImgBG:
        condition1=regarderDroit(NumImgBD,"BasGauche")
        condition2=regarderDroit(NumImgHD,"HautGauche")
        condition3=regarderDroit(NumImgBG,"BasDroit")
        condition4=regarderDroit(NumImgHG,"HautDroit")


        
        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacY=MacY+22.5
            
    elif NumImgBD==NumImgHD and NumImgBD==NumImgBD:
        condition1=regarderDroit(NumImgBG,"BasGauche")
        condition2=regarderDroit(NumImgHG,"HautGauche")
        condition3=regarderDroit(NumImgBD,"BasDroit")
        condition4=regarderDroit(NumImgHD,"HautDroit")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacY=MacY+22.5
    else:
        pass
    ramasserObj(MacX,MacY)
    gagner(MacX,MacY)
    
def toucheeventD(evt):
    global MacX
    global MacY
    MacY=MacY+22.5
    
    if int(MacX/45)<MacX/45:
        PosG=int(MacX/45)+1
    else:
        PosG=int(MacX/45)
        
    MacXdroite=MacX+32   
    if int(MacXdroite/45)<MacXdroite/45:
        PosD=int(MacXdroite/45)+1
    else:
        PosD=int(MacXdroite/45)

        
    if int(MacY/45)<MacY/45:
        PosYhaut=int(MacY/45)+1
    else:
        PosYhaut=int(MacY/45)
    MacYdbas=MacY+43  
    if int(MacYdbas/45)<MacYdbas/45:
        PosYbas=int(MacYdbas/45)+1
    else:
        PosYbas=int(MacYdbas/45)
    
    condition1="False"
    condition2="False"
    condition3="False"
    condition4="False"
    NumImgBD=(PosYbas*15)+PosD-15
    NumImgBG=(PosYbas*15)+PosG-15
    NumImgHD=(PosYhaut*15)+PosD-15
    NumImgHG=(PosYhaut*15)+PosG-15


    if NumImgBD!=NumImgHD and NumImgBD!=NumImgBG:
        condition1=regarderDroit(NumImgBD,"HautGauche")
        condition2=regarderDroit(NumImgHD,"BasGauche")
        condition3=regarderDroit(NumImgBG,"HautDroit")
        condition4=regarderDroit(NumImgHG,"BasDroit")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacY=MacY-22.5
    elif NumImgBD!=NumImgHD and NumImgBD==NumImgBG:
        condition1=regarderDroit(NumImgBD,"HautDroit")
        condition2=regarderDroit(NumImgBG,"HautGauche")
        condition3=regarderDroit(NumImgHD,"BasDroit")
        condition4=regarderDroit(NumImgHG,"BasGauche")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacY=MacY-22.5
    elif NumImgBD==NumImgHD and NumImgBD!=NumImgBG:
        condition1=regarderDroit(NumImgBD,"BasGauche")
        condition2=regarderDroit(NumImgHD,"HautGauche")
        condition3=regarderDroit(NumImgBG,"BasDroit")
        condition4=regarderDroit(NumImgHG,"HautDroit")

        
        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacY=MacY-22.5
            
    elif NumImgBD==NumImgHD and NumImgBD==NumImgBD:
        condition1=regarderDroit(NumImgBG,"BasGauche")
        condition2=regarderDroit(NumImgHG,"HautGauche")
        condition3=regarderDroit(NumImgBD,"BasDroit")
        condition4=regarderDroit(NumImgHD,"HautDroit")

        if condition1=="True" and condition2=="True" and condition3=="True" and condition4=="True":
            canvas13.place(x=MacX, y=MacY)
        else:
            print ("impossible de se deplacer")
            MacY=MacY-22.5
    else:
        pass
    
    ramasserObj(MacX,MacY)
    gagner(MacX,MacY)

def gagner(x,y):
    global nbPresentation
    global nbobj
    global RevenuSortiZone
    if x>555 and y>500 and len(nbObjRamasser)==6:
        global fenetreGagner
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
        
    elif x>555 and y>500 and len(nbObjRamasser)<6:
        
        if nbobj!=len(nbObjRamasser):
            nbobj=len(nbObjRamasser)
            nbPresentation=nbPresentation+1
            RevenuSortiZone=False
        elif nbobj==len(nbObjRamasser) and RevenuSortiZone:
            stringVarGardien.set("Tu te crois malin!\n Tu n'as rien récupéré de plus, va t'en d'ici tout de suite!!!")
            nbPresentation=nbPresentation+1
            RevenuSortiZone=False
        print(nbPresentation)                        
        if nbPresentation==1:
            if len(nbObjRamasser)==1:
                stringVarGardien.set("Quoi ? Seulement " + str(len(nbObjRamasser)) +" objet ramassé!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
            else:
                stringVarGardien.set("Quoi ? Seulement " + str(len(nbObjRamasser)) +" objets ramassés!\n Tu oses venir me voir sans avoir fait le job.\n Ne reviens me voir que si tu les as tous retrouvés!")
        elif nbPresentation==2 and nbobj!=len(nbObjRamasser):
            stringVarGardien.set("C'est la deuxième fois que tu viens me voir!\n Tu n'as que " + str(len(nbObjRamasser)) +" objets!\n Je te déconseille de revenir me voir une troisième fois \n sans tous les objets!")
        elif nbPresentation==3:
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
    else:
        
        RevenuSortiZone=True
        print("Pas encore au bout du labyrinthe")
def ramasserObj(x,y):
    i=0
    
    for xDansListe in listeCoordObjValideX:
        
        if (int(x)>= int(xDansListe) and int(x) < int(xDansListe+39)) or (int(x+32)>= int(xDansListe) and int(x+32) < int(xDansListe+39)):
            if (int(y) >= int(listeCoordObjValideY[i]-10) and int(y) < int(listeCoordObjValideY[i]+43)) or (int(y+43) > int(listeCoordObjValideY[i]) and int(y+43) < int(listeCoordObjValideY[i]+40)) :
                print("On ramase l objet")
                j=0
                
                for objCanvas in ListeObjetCanvas:
                    
                    if j == i:
                        
                        try:
                            
                            Itrouver=False
                            for chiffre in nbObjRamasser:
                                if chiffre==i:
                                    Itrouver=True
                                else:
                                    pass
                            if Itrouver==True:
                                pass
                            else:
                                nbObjRamasser.append(i)
                                
                                if len(nbObjRamasser)==1:
                                    stringVar.set(str(len(nbObjRamasser)) +" objet a été ramassé")
                                    #LabelObj=Label(FenObjet, text=str(len(nbObjRamasser)) +" Objet a été ramassé").pack()
                                else:
                                    stringVar.set(str(len(nbObjRamasser)) +" objets ont été ramassés")
                                    #LabelObj.config(text=str(len(nbObjRamasser)) +" Objets ont été ramassés")
                        except:
                            nbObjRamasser.append(i)
                            
                            
                        objCanvas.destroy()
                    j=j+1

                
                
            else:
                print("Pas d objet a ramasser Y")

        else:
            print("Pas d objet a ramasser")
        i=i+1
def rejouer():
    fenetreGagner.destroy()
    fenetre.destroy()
    main()
def rejouerLoose():
    fenetrePerdu.destroy()
    fenetre.destroy()
    main()
def rejouerDebut():
    
    fenetre.destroy()
    main()
    

main()
