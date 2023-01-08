import Coucou
import Danse
import Tektonik
import Youpi
import os
import time

def setMouvement(aff, fenetre, mouvement):
    if mouvement == "coucou":
        aff.reset(fenetre, 1920, 1080)
        aff.coucouSimple(fenetre, 1920, 1080)
        fenetre.update()
        fenetre.update_idletasks()
        Coucou.Coucou()
    if mouvement == "danse":
        aff.reset(fenetre, 1920, 1080)
        aff.danseSimple(fenetre, 1920, 1080)
        fenetre.update()
        fenetre.update_idletasks()
        Danse.Danse()
    if mouvement == "tektonik":
        aff.reset(fenetre, 1920, 1080)
        aff.tektonikSimple(fenetre, 1920, 1080)
        fenetre.update()
        fenetre.update_idletasks()
        Tektonik.Tektonik()
    if mouvement == "youpi":
        aff.reset(fenetre, 1920, 1080)
        aff.youpiSimple(fenetre, 1920, 1080)
        fenetre.update()
        fenetre.update_idletasks()
        Youpi.Youpi()