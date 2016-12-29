#! /usr/env/python3

# Matt King
# 12/27/2016
# A basic text-adventure game centered around functional programming in Python

import time
# import playerClass - Must create player doll
from mainHall import mainHall

def displayIntro():
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Welcome to the realm of Valen! ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(2)

    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Do you dare to seek the crescent stone? ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    time.sleep(3)

displayIntro()
mainHall()

