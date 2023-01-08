#!/usr/bin/env python3
#-- coding: utf-8 --#
import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

import time
import sys
from multiprocessing import Process,Queue
import os
import Affichage
sys.path.append('../ecran')
import Gif
sys.path.append('../Mouvements')
import Coucou
sys.path.append('../')
import Coeur

import random
fenetre = tk.Tk()
fenetre.title("LearnoBot") #Titre
fenetre.attributes("-fullscreen",True) #Plein Ecran
fenetre["bg"] = "#FFFFFF"
fenetre.resizable(width=False, height=False)#redimensionnement de la fenetre interdit
screenwidth = fenetre.winfo_screenwidth() #Largeur écran
screenheight = fenetre.winfo_screenheight()#hauteur écran
fenetre.geometry("1920x1080")

i= 500
aff = Affichage.Affichagefen()
time.sleep(2)
aff.accueil(fenetre, 1920, 1080)
while i != 0:
    fenetre.update()
    fenetre.update_idletasks()
    i = i - 1
    print(i)
i = 300
time.sleep(2)
aff.reset(fenetre, 1920, 1080)


for i in range(2):
    Gif.gif("./GIFHumeurs320240/Demarrage.gif")
    
    
aff.coucouSimple(fenetre, 1920, 1080)
while i != 0:
    fenetre.update()
    fenetre.update_idletasks()
    i = i - 1
time.sleep(2)
aff.reset(fenetre, 1920, 1080)
Coucou.Coucou()
Coeur.Coeur(aff,fenetre)

