from pathlib import Path
from os import system
import pickle

import player
import mineBotLoop

def saveMiningConfig():
    print("--save a minebot config--")
    configFileName = input("name: ")+".mbc"

    Path("./miningConfigs/").mkdir(parents=True, exist_ok=True)
    pickle.dump(player.miningTimeDict, open("./miningConfigs/"+configFileName, "wb"))

    return f"succes: saved current config to {configFileName}"

def loadMiningConfig():
    print("--load a minebot config--")
    configFileName = input("name: ")+".mbc"

    if Path("./miningConfigs/"+configFileName).exists():
        player.miningTimeDict = pickle.load(open("./miningConfigs/"+configFileName, "rb"))
        return f"Succes: loaded {configFileName}"
    else:
        return f"error: failed to load, config {Path('./miminingConfigs/'+configFileName).absolute()} does not exist"

def printMiningConfig():
    for key in player.miningTimeDict:
        print(f"{key} - {player.miningTimeDict[key]}")
    
    if(len(player.miningTimeDict) == 0):
        print("the current mining config is empty")

    print("-"*25)
    print("press enter to continue")
    input()

    return "succes: displayed current miningconfig data"

def startBotLoop():
    mineBotLoop.startBotLoop()