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
import random

#Lance 3 fois le gif... (temps de lancement & connexion)
for i in range(3):
    Gif.gif("./Demarrage.gif")
Coucou.Coucou()
Coeur.Coeur()

