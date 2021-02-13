import pyperclip
import math
import time
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
    blockType = blockType.split("[")[0]

    dataList = [float(x) for x in dataList]

    dataList.append(blockType)

    timeStamp = int(time.time()*1000)
    dataList.append(timeStamp)

    return dataList
    

def checkLava():
    #point at block in front of feet
    player.rotateCamY(65)

    locData = player.getLocationData()
    playerY = math.floor(locData[1])

    blockData = getBlockData()
    blockY = blockData[1]

    return blockY+2 == playerY