#!/usr/bin/env python3
# -- coding: utf-8 --#
import random
sys.path.append('./ReconnaissanceVocale')
import ChatVoc
import sys
import random

def Ecoute():
    parole = ChatVoc.Rec()
    if parole == "base":
       return "base"
    if parole == "masque":
        return "masque"
    if parole == "amoureux":
        return "amoureux"
    if parole == "clin d'œil":
        return "clin d'œil"
    if parole == "colère":
        return "colère"
    if parole == "fatigué":
        return "fatigué"
    if parole == "riz":
        return "riz"
    if parole == "surpris":
        return "surpris"
    if parole == "triste":
        return "triste"
    if parole == "coucou":
        return "coucou"
    if parole == "danse":
        return "danse"
    if parole == "tektonik":
        return "tektonik"
    if parole == "youpi":
        return "youpi"
    
def setRandomHumeur():
    tmp = random.randint(0, 12)
    if tmp == 0:
        return "base"
    if tmp == 1:
        return "masque"
    if tmp == 2:
        return "amoureux"
    if tmp == 3:
        return "clin d'œil"
    if tmp == 4:
        return "colère"
    if tmp == 5:
        return "fatigué"
    if tmp == 6:
        return "riz"
    if tmp == 7:
        return "surpris"
    if tmp == 8:
        return "triste"
    if tmp == 9:
        return "coucou"
    if tmp == 10:
        return "danse"
    if tmp == 11:
        return "tektonik"
    if tmp == 12:
        return "youpi"
