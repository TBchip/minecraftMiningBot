from time import sleep
from os import system
from pynput import keyboard
import threading

import player
import surroundings
import mineSequences


stopBotLoop = False

def startBotLoop():
    global stopBotLoop
    stopBotLoop = False

    listener = keyboard.Listener(on_release=keyboardListenerOnRelease)
    listener.start()

    infoDelay(5)

    botLoop()

def infoDelay(openMinecraftDelay):
    print("setup:")
    print("-"*25)
    print("slot 1: pickaxe")
    print("slot 2: water bucket")
    print("-"*25)
    print("walk to the position you want to start in")
    print("-"*25)
    print()
    print()
    print("press R to stop the bot loop")
    print(f"after pressing enter you will have {openMinecraftDelay} seconds to open the minecraft window")
    print("-"*25)
    input("press enter to continue...")

    for i in range(int(openMinecraftDelay*10)):
        if stopBotLoop:
            return

        system("cls")
        print()
        print("press R to stop the bot loop")
        print(f"bot starting in {round((openMinecraftDelay-(i/10)), 1)} seconds, please open minecraft")
        sleep(0.1)

    print("press R to stop the bot loop")
    system("cls")


def keyboardListenerOnRelease(key):
    global stopBotLoop

    if hasattr(key, "char"):
        if key.char == "r":
            stopBotLoop = True
            return False

    if stopBotLoop:
        return False

def botLoop():
    global stopBotLoop
    
    #get initial location data
    player.updateLocationData()

    #rotate to closest cardinal direction
    angle = player.locationData[3]
    angle /= 90
    angle = int(round(angle, 0))*90
    angle %= 360
    player.rotateCamX(angle)
    
    while not stopBotLoop:
        mineSequences.stripMinePart(10)

    stopBotLoop = True