#!/usr/bin/env python3
#-- coding: utf-8 --#
import Gif
import random

def setHumeur(Humeur):
    if Humeur == "amoureux":
        tmp = random.randint(1, 3)
        if tmp == 1:
            Gif.gif("./GIFHumeurs/Amoureux/Amoureux1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs/Amoureux/Amoureux2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs/Amoureux/Amoureux3.gif")
    if Humeur == "base":
        tmp = random.randint(1, 6)
        if tmp == 1:
            Gif.gif("./GIFHumeurs/Base/Base1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs/Base/Base2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs/Base/Base3.gif")
        if tmp == 4:
            Gif.gif("./GIFHumeurs/Base/Base4.gif")
        if tmp == 5:
            Gif.gif("./GIFHumeurs/Base/Base5.gif")
        if tmp == 6:
            Gif.gif("./GIFHumeurs/Base/Base6.gif")
    if Humeur == "masque":
        Gif.gif("./GIFHumeurs/Masque.gif")
    if Humeur == "clin d'œil":
        tmp = random.randint(1, 3)
        if tmp == 1:
            Gif.gif("./GIFHumeurs/Clindoeuil/Clindoeuil1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs/Clindoeuil/Clindoeuil2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs/Clindoeuil/Clindoeuil3.gif")
    if Humeur == "colère":
        tmp = random.randint(1, 2)
        if tmp == 1:
            Gif.gif("./GIFHumeurs/Colère/Colère1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs/Colère/Colère2.gif")
    if Humeur == "fatigué":
        tmp = random.randint(1, 2)
        if tmp == 1:
            Gif.gif("./GIFHumeurs/Fatigué/Fatigué1.gif")
        if tmp == 2:
           Gif.gif("./GIFHumeurs/Fatigué/Fatigué2.gif")
    if Humeur == "riz":
        tmp = random.randint(1, 2)
        if tmp == 1:
            Gif.gif("./GIFHumeurs/Rit/Rit1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs/Rit/Rit2.gif")
    if Humeur == "surpris":
        tmp = random.randint(1, 2)
        if tmp == 1:
            Gif.gif("./GIFHumeurs/Surpris/Surpris1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs/Surpris/Surpris2.gif")
    if Humeur == "triste":
        tmp = random.randint(1, 3)
        if tmp == 1:
            Gif.gif("./GIFHumeurs/Triste/Triste1.gif")
        if tmp == 2:
            Gif.gif("./GIFHumeurs/Triste/Triste2.gif")
        if tmp == 3:
            Gif.gif("./GIFHumeurs/Triste/Triste3.gif")