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
def Youpi():
    GPIO.setwarnings(False) #Désactive les warnings dans le terminal
    servoPINDroite = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINDroite, GPIO.OUT)
    droite = GPIO.PWM(servoPINDroite, 50) # GPIO 18 for PWM with 50Hz
    droite.start(2.5) # Initialization
    
    servoPINGauche = 18
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPINGauche, GPIO.OUT)
    gauche = GPIO.PWM(servoPINGauche, 50) # GPIO 18 for PWM with 50Hz
    gauche.start(2.5) # Initialization
    
    droite.ChangeDutyCycle(5)
    time.sleep(0.15)
    gauche.ChangeDutyCycle(12)
    time.sleep(0.15)
    droite.ChangeDutyCycle(4)
    time.sleep(0.15)
    gauche.ChangeDutyCycle(11)
    time.sleep(0.15)
    droite.ChangeDutyCycle(5)
    time.sleep(0.15)
    gauche.ChangeDutyCycle(12)
    time.sleep(0.15)
    droite.ChangeDutyCycle(4)
    time.sleep(0.15)
    gauche.ChangeDutyCycle(11)
    time.sleep(0.15)
    droite.ChangeDutyCycle(5)
    time.sleep(0.15)
    gauche.ChangeDutyCycle(12)
    time.sleep(0.15)
    droite.ChangeDutyCycle(4)
    time.sleep(0.15)
    gauche.ChangeDutyCycle(11)
    time.sleep(0.15)
    gauche.ChangeDutyCycle(12)
    time.sleep(0.15)
    droite.ChangeDutyCycle(15)
    time.sleep(0.1)
    gauche.ChangeDutyCycle(2)
    time.sleep(2)
                
                
                




