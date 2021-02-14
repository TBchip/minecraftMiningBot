from time import sleep
from pynput import keyboard

import player
import surroundings

stopBotLoop = False

def startBotLoop():
    listener = keyboard.Listener(on_release=keyboardListenerOnRelease)
    listener.start()

    stopBotLoop = False
    botLoop()


def keyboardListenerOnRelease(key):
    global stopBotLoop

    if hasattr(key, "char"):
        if key.char == "r":
            stopBotLoop = True
            return False

def botLoop():
    sleep(1)

    player.rotateCamX(-90)
    while not surroundings.checkLava() and not stopBotLoop:
        player.walkForward(1)

        if(surroundings.checkWallTop()):
            player.mine()

        if(surroundings.checkWallBottom()):
            player.mine()