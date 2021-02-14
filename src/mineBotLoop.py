from time import sleep
import pynput.keyboard as keyboard

import player
import surroundings

def startBotLoop():
    key

def keyboardListenerOnRelease(key):
    print(key)

def botLoop():
    sleep(1)

    player.rotateCamX(-90)
    while not surroundings.checkLava():
        player.walkForward(1)

        if(surroundings.checkWallTop()):
            player.mine()

        if(surroundings.checkWallBottom()):
            player.mine()