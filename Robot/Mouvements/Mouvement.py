import Coucou
import Danse
import Tektonik
import YoupiDroit
import YoupiGauche
import os

def setMouvement(mouvement):
    if mouvement == "coucou":
        Coucou.Coucou()
    if mouvement == "danse":
        Danse.Danse()
    if mouvement == "tektonik":
        Tektonik.Tektonik()
    
    if mouvement == "youpi":
        pid = os.fork()
        try:
            if pid > 0:
                YoupiDroit.YoupiDroit()
            else:
                YoupiGauche.YoupiGauche()
        except KeyboardInterrupt:
        print("Arrêt par contrôle clavier")