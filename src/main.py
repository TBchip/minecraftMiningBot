from time import sleep
import math
from pynput import keyboard
import pickle
from pathlib import Path

import player
import surroundings

stopBot = False
def main():
    global stopBot

    listener = keyboard.Listener(
        on_press=None,
        on_release=on_release)
    listener.start()

    while not stopBot:
        sleep(0.1)

    # pickle.dump(player.miningTimeDict, open("./folder/config.txt", "wb"))
    # d = pickle.load(open("config.txt", "rb"))

def botLoop():
    sleep(1)

    player.rotateCamX(-90)
    while not surroundings.checkLava() and not stopBot:
        player.walkForward(1)

        if(surroundings.checkWallTop()):
            player.mine()
        
        if(surroundings.checkWallBottom()):
            player.mine()

def saveMiningConfig():
    Path("./miningConfigs/").mkdir(parents=True, exist_ok=True)
    pickle.dump(player.miningTimeDict, open("./miningConfigs/config.txt", "wb"))
def loadMiningConfig():
    if Path("./miminingConfigs/config.txt").exists():
        player.miningTimeDict = pickle.load(open("config.txt", "rb"))

def on_release(key):
    global stopBot

    print(key)

    if key == keyboard.Key.esc:
        stopBot = True
        return False
    elif key.char:
        if key.char == "p":
            saveMiningConfig()
        elif key.char == "o":
            loadMiningConfig()


if __name__ == "__main__":
    main()