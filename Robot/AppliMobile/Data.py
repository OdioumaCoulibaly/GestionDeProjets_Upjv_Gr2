#!/usr/bin/env python3
#-- coding: utf-8 --#

import time
import serial

def getData():
    btSerial = 0
    try:
        btSerial = serial.Serial("/dev/rfcomm0", baudrate=9600, timeout=0.5)
        while btSerial:
            rcv = btSerial.read(512)
            if rcv:
                message = rcv.decode()
                if message == "base":
                   return "base"
                if message == "masque":
                    return "masque"
                if message == "amoureux":
                    return "amoureux"
                if message == "clin d'œil":
                    return "clin d'œil"
                if message == "colère":
                    return "colère"
                if message == "fatigué":
                    return "fatigué"
                if message == "riz":
                    return "riz"
                if message == "surpris":
                    return "surpris"
                if message == "triste":
                    return "triste"
                if message == "coucou":
                    return "coucou"
                if message == "danse":
                    return "danse"
                if message == "tecktonik":
                    return "tektonik"
                if message == "youpi":
                    return "youpi"
    except:
        time.sleep(2)
        print("Connexion BL impossible")

