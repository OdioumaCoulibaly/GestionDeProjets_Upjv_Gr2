#!/usr/bin/env python3
# -- coding: utf-8 --
import Mouvement
import Humeur
import Ecoute
import RPi.GPIO as GPIO
import time
import random
import os
sys.path.append('./RecVoc')
sys.path.append('../Humeurs')
sys.path.append('../Mouvement')
#  MAX moteur  p.ChangeDutyCycle(12.5)
#    time.sleep(0.5)
#  MIN moteur p.ChangeDutyCycle(2.5)
#    time.sleep(0.5)


def check_variable():
    pipe_read = os.open("C:\\temp\\pipe", os.O_RDONLY)
    if not pipe_read:
        # Obtenez le temps actuel en secondes
        current_time = time.time()
        # Définissez le temps de départ en secondes
        tmp = random.randint(120, 360)
        start_time = current_time - tmp
        # Boucle jusqu'à ce que la variable soit vraie ou que les secondes se soient écoulées
        while not pipe_read and current_time - start_time < tmp:
            time.sleep(1)  # Attendez 1 seconde avant de vérifier à nouveau
            current_time = time.time()
            pipe_read = os.open("C:\\temp\\pipe", os.O_RDONLY)
        # Si la variable est toujours fausse après 5 minutes, imprimez HelloWorld
        if not pipe_read:
            pipe_write = os.open("C:\\temp\\pipe", os.O_WRONLY)
            os.write(pipe_write, Ecoute.setRandomHumeur())


def Coeur():
    os.mkfifo("C:\\temp\\pipe")
    GPIO.setwarnings(False)  # Désactive les warnings dans le terminal

    pid = os.fork()
    try:
        if pid > 0:
            pid2 = os.fork()
            try:
                if pid2 > 0:

                    pid3 = os.fork()
                    try:
                        if pid3 > 0:
                            print("CAPTEUR 1 ECOUTE")
                            pipe_write = os.open("C:\\temp\\pipe", os.O_WRONLY)
                            os.write(pipe_write, "base")
                            while True:
                                os.write(pipe_write, Ecoute.Ecoute())
                            os.close(pipe_write)

                        else:
                            while True:
                                print(
                                    "Complément : Si rien n'est détecté, l'humeur change seule")
                                pipe_read = os.open(
                                    "C:\\temp\\pipe", os.O_RDONLY)
                                check_variable(pipe_read)

                    except KeyboardInterrupt:
                        print("Arrêt par contrôle clavier")
                    # Si Ecoute.Ecoute() ne donne rien depuis rand(1minute, 6minute) l'humeur change seule aléatoirement :) (Emmet des sons ?)

                else:

                    print("CAPTEUR 2 APPLI")
                    pipe_write = os.open("C:\\temp\\pipe", os.O_WRONLY)
                    os.close(pipe_write)

            except KeyboardInterrupt:
               print("Arrêt par contrôle clavier")
        else:
            pid3 = os.fork()
            try:
                if pid3 > 0:

                    print("Réactions 1 HUMEURS")
                    while True:
                        pipe_read = os.open("C:\\temp\\pipe", os.O_RDONLY)
                        Humeur.setHumeur(pipe_read)
                    os.close(pipe_write)

                else:

                    print("Réactions 2 MOUVEMENT")
                    pipe_read = os.open("C:\\temp\\pipe", os.O_RDONLY)
                    os.close(pipe_write)
                    while True:
                        pipe_read = os.open("C:\\temp\\pipe", os.O_RDONLY)
                        Mouvement.setMouvement(pipe_read)
                    os.close(pipe_write)





            except KeyboardInterrupt:
                print("Arrêt par contrôle clavier")

    except KeyboardInterrupt:
        GPIO.cleanup()
            





