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
def YoupiDroit():
    GPIO.setwarnings(False) #Désactive les warnings dans le terminal
    print("Initialisation du moteur du bras droit")
    servoPINDroite = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINDroite, GPIO.OUT)
    droite = GPIO.PWM(servoPINDroite, 50) # GPIO 18 for PWM with 50Hz
    droite.start(2.5) # Initialization
    print("Je vais faire Youpi du bras droit")
    droite.ChangeDutyCycle(5)
    time.sleep(0.15)
    droite.ChangeDutyCycle(4)
    time.sleep(0.15)
    droite.ChangeDutyCycle(5)
    time.sleep(0.15)
    droite.ChangeDutyCycle(4)
    time.sleep(0.15)
    droite.ChangeDutyCycle(5)
    time.sleep(0.15)
    droite.ChangeDutyCycle(4)
    time.sleep(0.15)
    droite.ChangeDutyCycle(15)
    time.sleep(random.randint(1,4))
    GPIO.cleanup()
    print("Fin du YoupiDroite")
                




