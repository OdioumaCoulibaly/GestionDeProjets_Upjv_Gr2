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

def Coucou():
    GPIO.setwarnings(False) #Désactive les warnings dans le terminal
    print("Initialisation du moteur du bras gauche")
    servoPINGauche = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINGauche, GPIO.OUT)
    gauche = GPIO.PWM(servoPINGauche, 50) # GPIO 18 for PWM with 50Hz
    gauche.start(2.5) # Initialization
    print("Je vais dire coucou")
    gauche.ChangeDutyCycle(2)
    time.sleep(1)
    gauche.ChangeDutyCycle(10)
    time.sleep(1)
    gauche.ChangeDutyCycle(8)
    time.sleep(0.25)
    gauche.ChangeDutyCycle(10)
    time.sleep(0.25)
    gauche.ChangeDutyCycle(8)
    time.sleep(0.25)
    gauche.ChangeDutyCycle(10)
    time.sleep(0.25)
    gauche.ChangeDutyCycle(8)
    time.sleep(0.25)
    gauche.ChangeDutyCycle(2)
    time.sleep(random.randint(1,4))
    GPIO.cleanup()
    print("Fin du Coucou")
            



