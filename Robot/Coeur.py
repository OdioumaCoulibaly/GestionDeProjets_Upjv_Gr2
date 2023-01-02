#!/usr/bin/env python3
# -- coding: utf-8 --
import RPi.GPIO as GPIO
import time
import random
import os
import sys
import select
sys.path.append('../ReconnaissanceVocale')
import Ecoute
sys.path.append('../Humeurs')
import Humeur
sys.path.append('../Mouvement')
import Mouvement
#  MAX moteur  p.ChangeDutyCycle(12.5)
#    time.sleep(0.5)
#  MIN moteur p.ChangeDutyCycle(2.5)
#    time.sleep(0.5)


def check_variable():
    pipe_read = os.open("C:\\temp\\pipe", os.O_RDONLY)
    binary_data = os.read(pipe_read, 1024)  # Lire jusqu'à 1024 octets
    message = binary_data.decode()
    print("Read :"+message)
    if not message:
        # Obtenez le temps actuel en secondes
        current_time = time.time()
        # Définissez le temps de départ en secondes
        tmp = random.randint(120, 360)
        start_time = current_time - tmp
        # Boucle jusqu'à ce que la variable soit vraie ou que les secondes se soient écoulées
        while not message and current_time - start_time < tmp:
            time.sleep(1)  # Attendez 1 seconde avant de vérifier à nouveau
            current_time = time.time()
            pipe_read = os.open("C:\\temp\\pipe", os.O_RDONLY)
            binary_data = os.read(pipe_read, 1024)  # Lire jusqu'à 1024 octets
            message = binary_data.decode()
            print("Read :"+message)
        # Si la variable est toujours fausse après 5 minutes, imprimez HelloWorld
        if not message:
            pipe_write = os.open("C:\\temp\\pipe", os.O_WRONLY)
            binary_data = Ecoute.setRandomHumeur().encode()
            os.write(pipe_write, binary_data)


def Coeur():
    #os.mkfifo("C:\\temp\\pipe")
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
                            message = "base"
                            binary_data = message.encode()
                            os.write(pipe_write, binary_data)
                            while True:
                                binary_data = Ecoute.Ecoute()
                                if binary_data:
                                    binary_data = binary_data.encode()
                                    os.write(pipe_write, binary_data)
                            os.close(pipe_write)

                        else:
                            while True:
#                               print("Complément : Si rien n'est détecté, l'humeur change seule")
                                if readable:
                                    binary_data = os.read(pipe_read, 1024)  # Lire jusqu'à 1024 octets
                                    message = binary_data.decode()
                                    print("Read WhileHumeurs:"+message)
                                    if message:
                                        print(message + "SPOTTED")
                                    else:
                                        print("Quedal")   
                    except KeyboardInterrupt:
                        print("Arrêt par contrôle clavier")
                    # Si Ecoute.Ecoute() ne donne rien depuis rand(1minute, 6minute) l'humeur change seule aléatoirement :) (Emmet des sons ?)

                else:

                    print("CAPTEUR 2 APPLI")

            except KeyboardInterrupt:
               print("Arrêt par contrôle clavier")
        else:
            pid3 = os.fork()
            try:
                if pid3 > 0:

                    print("Réactions 1 HUMEURS")
                    Humeur.setBaseHumeur()
                    while True:
                        pipe_read = os.open("C:\\temp\\pipe", os.O_RDONLY)
                        fd = [pipe_read]
                        readable, _, _ = select.select(fd,[],[], 1)
                        if readable:
                            binary_data = os.read(pipe_read, 1024)
                            print(binary_data)# Lire jusqu'à 1024 octets
                            message = binary_data.decode()
                            print(message)
                            if message:
                                print(Humeur)
                                Humeur.setHumeur(message)
                                Mouvement.setMouvement(message)
                        else:
                            Humeur.setBaseHumeur()
                    os.close(pipe_read)
    
            except KeyboardInterrupt:
                print("Arrêt par contrôle clavier")

    except KeyboardInterrupt:
        GPIO.cleanup()
            





