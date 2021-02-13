import pyperclip
import math
import pydirectinput

import player


def getBlockData():
    pyperclip.copy("None")

    pydirectinput.keyDown("f3")
    pydirectinput.keyDown("i")
    pydirectinput.keyUp("f3")
    pydirectinput.keyUp("i")

    dataString = pyperclip.paste()
    if(dataString == "None"):
        return None
    else:
        dataList = dataString.split(" ")
        dataList = dataList[1:]

        blockType = dataList.pop(-1)
        blockType = blockType.split("[")[0]

        dataList = [float(x) for x in dataList]

        dataList.append(blockType)

        return dataList


def checkLava():
    locData = player.getLocationData()
    locData = [math.floor(i) for i in locData[:3]]

    #point at block in front of feet
    player.rotateCamY(65)
    blockData = getBlockData()
    if(blockData == None):
        return True

    dist = abs(locData[0]-blockData[0])+abs(locData[1]-blockData[1])+abs(locData[2]-blockData[2])
    print(dist)
    return dist == 3

def checkWallTop():
    locData = player.getLocationData()
    playerY = math.floor(locData[1])

    player.rotateCamY(35)
    blockData = getBlockData()
    if(blockData == None):
        return False
    blockY = blockData[1]

    return blockY-1 == playerY
def checkWallBottom():
    locData = player.getLocationData()
    playerY = math.floor(locData[1])

    player.rotateCamY(65)
    blockData = getBlockData()
    if(blockData == None):
        return False
    blockY = blockData[1]

    return blockY == playerY