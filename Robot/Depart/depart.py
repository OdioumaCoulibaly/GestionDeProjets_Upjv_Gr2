#!/usr/bin/env python3
#-- coding: utf-8 --#

import time
import sys
from multiprocessing import Process,Queue
import os
sys.path.append('../ecran')
import Gif
sys.path.append('../Mouvements')
import Coucou
sys.path.append('../')
import Coeur
import random


#Lance 2 fois le gif... (temps de lancement & connexion)
for i in range(2):
    Gif.gif("./GIF/Demarrage.gif")
Coucou.Coucou()
Coeur.Coeur()

