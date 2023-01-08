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

def Danse():
    print("Lancement Danse")
    GPIO.setwarnings(False) #Désactive les warnings dans le terminal
    servoPINGauche = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINGauche, GPIO.OUT)
    gauche = GPIO.PWM(servoPINGauche, 50) # GPIO 18 for PWM with 50Hz
    gauche.start(2.5) # Initialization
    
    servoPINDroite = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINDroite, GPIO.OUT)
    droite = GPIO.PWM(servoPINDroite, 50) # GPIO 23 for PWM with 50Hz
    droite.start(2.5) # Initialization
    
    servoPINBassin = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINBassin, GPIO.OUT)
    bassin = GPIO.PWM(servoPINBassin, 50) # GPIO 24 for PWM with 50Hz
    bassin.start(2.5) # Initialization

    for i in range(2):
        gauche.ChangeDutyCycle(12)
        time.sleep(1)
        bassin.ChangeDutyCycle(12)
        time.sleep(1)
        droite.ChangeDutyCycle(5)
        time.sleep(1)
        droite.ChangeDutyCycle(12)
        time.sleep(1)
        bassin.ChangeDutyCycle(4)
        time.sleep(1)
        gauche.ChangeDutyCycle(4)
        time.sleep(1)
        
    gauche.ChangeDutyCycle(2.5)
    droite.ChangeDutyCycle(2.5)
    bassin.ChangeDutyCycle(2.5)