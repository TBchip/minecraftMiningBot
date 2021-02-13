import pyperclip
import math

import pydirectinput

import player


def getBlockData():
    pydirectinput.keyDown("f3")
    pydirectinput.keyDown("i")
    pydirectinput.keyUp("f3")
    pydirectinput.keyUp("i")

    dataString = pyperclip.paste()
    dataList = dataString.split(" ")
    dataList = dataList[1:]

    blockType = dataList.pop(-1)
    dataList = [float(x) for x in dataList]
    dataList.append(blockType)

    return dataList
    

def checkLava():
    #point at block in front of feet
    player.rotateCamY(65)

    locData = player.getLocationData()
    playerY = math.floor(locData[1])

    blockData = getBlockData()
    blockY = blockData[1]

    return blockY+1 != playerY