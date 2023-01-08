#!/usr/bin/env python3
#-- coding: utf-8 --#
import sys
sys.path.append('../ecran')
import Gif
import random

def setBaseHumeur():
    Gif.gif("./GIFHumeurs320240/Base/Base2.gif")

def setHumeur(aff, fenetre, Humeur):
    print("Humeur à Affichier :"+Humeur)
    if Humeur == "amoureux":
        tmp = random.randint(1, 3)
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 0)
        fenetre.update()
        fenetre.update_idletasks()
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Amoureux/Amoureux1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Amoureux/Amoureux2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs320240/Amoureux/Amoureux3.gif")
    if Humeur == "base":
        tmp = random.randint(1, 6)
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 1)
        fenetre.update()
        fenetre.update_idletasks()
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Base/Base1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Base/Base2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs320240/Base/Base3.gif")
        if tmp == 4:
            Gif.gif("./GIFHumeurs320240/Base/Base4.gif")
        if tmp == 5:
            Gif.gif("./GIFHumeurs320240/Base/Base5.gif")
        if tmp == 6:
            Gif.gif("./GIFHumeurs320240/Base/Base6.gif")
    if Humeur == "masque":
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 2)
        fenetre.update()
        fenetre.update_idletasks()
        Gif.gif("./GIFHumeurs320240/Masque.gif")
    if Humeur == "clin d'œil":
        tmp = random.randint(1, 3)
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 3)
        fenetre.update()
        fenetre.update_idletasks()
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Clindoeuil/Clindoeuil1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Clindoeuil/Clindoeuil2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs320240/Clindoeuil/Clindoeuil3.gif")
    if Humeur == "colère":
        tmp = random.randint(1, 2)
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 4)
        fenetre.update()
        fenetre.update_idletasks()
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Colère/Colère1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Colère/Colère2.gif")
    if Humeur == "fatigué":
        tmp = random.randint(1, 2)
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 5)
        fenetre.update()
        fenetre.update_idletasks()
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Fatigué/Fatigué1.gif")
        if tmp == 2:
           Gif.gif("./GIFHumeurs320240/Fatigué/Fatigué2.gif")
    if Humeur == "riz":
        tmp = random.randint(1, 2)
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 6)
        fenetre.update()
        fenetre.update_idletasks()
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Rit/Rit1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Rit/Rit2.gif")
    if Humeur == "surpris":
        tmp = random.randint(1, 2)
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 7)
        fenetre.update()
        fenetre.update_idletasks()
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Surpris/Surpris1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Surpris/Surpris2.gif")
    if Humeur == "triste":
        tmp = random.randint(1, 3)
        aff.reset(fenetre, 1920, 1080)
        aff.humeurSimple(fenetre, 1920, 1080, 8)
        fenetre.update()
        fenetre.update_idletasks()
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Triste/Triste1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Triste/Triste2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs320240/Triste/Triste3.gif")
