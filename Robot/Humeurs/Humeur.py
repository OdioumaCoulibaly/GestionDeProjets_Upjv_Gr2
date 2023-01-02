#!/usr/bin/env python3
#-- coding: utf-8 --#
import sys
sys.path.append('../ecran')
import Gif
import random

def setBaseHumeur():
    Gif.gif("./GIFHumeurs320240/Base/Base2.gif")

def setHumeur(Humeur):
    print("Humeur à Affichier :"+Humeur)
    if Humeur == "amoureux":
        tmp = random.randint(1, 3)
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Amoureux/Amoureux1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Amoureux/Amoureux2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs320240/Amoureux/Amoureux3.gif")
    if Humeur == "base":
        tmp = random.randint(1, 6)
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
        Gif.gif("./GIFHumeurs320240/Masque.gif")
    if Humeur == "clin d'œil":
        tmp = random.randint(1, 3)
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Clindoeuil/Clindoeuil1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Clindoeuil/Clindoeuil2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs320240/Clindoeuil/Clindoeuil3.gif")
    if Humeur == "colère":
        tmp = random.randint(1, 2)
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Colère/Colère1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Colère/Colère2.gif")
    if Humeur == "fatigué":
        tmp = random.randint(1, 2)
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Fatigué/Fatigué1.gif")
        if tmp == 2:
           Gif.gif("./GIFHumeurs320240/Fatigué/Fatigué2.gif")
    if Humeur == "riz":
        tmp = random.randint(1, 2)
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Rit/Rit1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Rit/Rit2.gif")
    if Humeur == "surpris":
        tmp = random.randint(1, 2)
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Surpris/Surpris1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Surpris/Surpris2.gif")
    if Humeur == "triste":
        tmp = random.randint(1, 3)
        if tmp == 1:
            Gif.gif("./GIFHumeurs320240/Triste/Triste1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs320240/Triste/Triste2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs320240/Triste/Triste3.gif")