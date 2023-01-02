import Coucou
import Danse
import Tektonik
import Youpi
import os
import time

def setMouvement(mouvement):
    if mouvement == "coucou":
        Coucou.Coucou()
        Tektonik.Tektonik()
    if mouvement == "danse":
        Danse.Danse()
    if mouvement == "tecktonik":
        Tektonik.Tektonik()
    
    if mouvement == "youpi":
        Youpi.Youpi()