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
sys.path.append('../AppliMobile')
import Data
sys.path.append('../Humeurs')
import Humeur
sys.path.append('../Mouvements')
import Mouvement
#  MAX moteur  p.ChangeDutyCycle(12.5)
#    time.sleep(0.5)
#  MIN moteur p.ChangeDutyCycle(2.5)
#    time.sleep(0.5)



def Coeur(aff, fenetre):
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
                            print("CAPTEUR 2 Appli")
                            while True:
                                data = Data.getData()
                                if data:
                                    pipe_write = os.open("C:\\temp\\pipe", os.O_WRONLY)
                                    data = data.encode()
                                    os.write(pipe_write, data)
                                    os.close(pipe_write)
                                    
                    except KeyboardInterrupt:
                        print("Arrêt par contrôle clavier")
                    
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
                                Humeur.setHumeur(aff, fenetre, message)
                                Mouvement.setMouvement(aff, fenetre, message)
                        else:
                            Humeur.setBaseHumeur()
                            os.close(pipe_read)
                            time.sleep(3)
    
            except KeyboardInterrupt:
                print("Arrêt par contrôle clavier")

    except KeyboardInterrupt:
        GPIO.cleanup()
            





