#!/usr/bin/env python3
#-- coding: utf-8 --
import RPi.GPIO as GPIO
import time
import random
import os

#  MAX moteur  p.ChangeDutyCycle(12.5)
#    time.sleep(0.5)
#  MIN moteur p.ChangeDutyCycle(2.5)
#    time.sleep(0.5)

GPIO.setwarnings(False) #Désactive les warnings dans le terminal

pid = os.fork()
try:
    if pid > 0 :
        pid2 = os.fork()
        try:
            if pid2 > 0 :
                print("Initialisation du moteur du bras gauche")
                servoPINGauche = 18
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(servoPINGauche, GPIO.OUT)
                gauche = GPIO.PWM(servoPINGauche, 50) # GPIO 18 for PWM with 50Hz
                gauche.start(2.5) # Initialization
                while True:
                    gauche.ChangeDutyCycle(round(random.uniform(2.5, 12.5),2))
                    time.sleep(random.randint(1,4))
            else :
                print("Initialisation du moteur du bras droit")
                servoPINDroite = 23
                GPIO.setmode(GPIO.BCM)
                GPIO.setup(servoPINDroite, GPIO.OUT)
                droite = GPIO.PWM(servoPINDroite, 50) # GPIO 23 for PWM with 50Hz
                droite.start(2.5) # Initialization
                while True:
                    droite.ChangeDutyCycle(round(random.uniform(2.5, 12.5),2))
                    time.sleep(random.randint(1,4))
 
        except KeyboardInterrupt:
            print("Arrêt par contrôle clavier")
    else:
        print("Initialisation du moteur bassin")
        servoPINBassin = 24
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPINBassin, GPIO.OUT)
        bassin = GPIO.PWM(servoPINBassin, 50) # GPIO 24 for PWM with 50Hz
        bassin.start(2.5) # Initialization
        while True :
            bassin.ChangeDutyCycle(round(random.uniform(2.5, 12.5),2))
            time.sleep(random.randint(1,4))

except KeyboardInterrupt:
    GPIO.cleanup()
            

