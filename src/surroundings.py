from time import sleep
import pyperclip
import math
import pydirectinput

import player


blockData = []
blockDataUpToDate = False
def getBlockData():
    global blockData, blockDataUpToDate
    if(blockDataUpToDate):
        return blockData

    blockDataUpToDate = True

    pyperclip.copy("None")

    pydirectinput.keyDown("f3")
    pydirectinput.press("i")
    pydirectinput.keyUp("f3")

    dataString = pyperclip.paste()

    if dataString.startswith("/summon"):
        return "falling"


    if(dataString == "None"):
        blockData = None
        return None
    else:
        dataList = dataString.split(" ")
        dataList = dataList[1:]

        blockType = dataList.pop(-1)
        blockType = blockType.split("[")[0]

        dataList = [float(x) for x in dataList]

        dataList.append(blockType)

        blockData = dataList
        return dataList


def checkLava():
    locData = [math.floor(i) for i in player.locationData[:3]]

    #if offset is to large then move cam
    if(abs(55-player.locationData[4]) > 4):
        player.rotateCamY(55)

    blockData = getBlockData()
    #if not pointing at block
    if(blockData == None):
        return True
    #wait for falling block to land
    while getBlockData == "falling":
        blockData = getBlockData()
        sleep(0.1)

    #get disance to the block the player is pointing at
    dist = abs(locData[0]-blockData[0])+abs(locData[1]-blockData[1])+abs(locData[2]-blockData[2])

    return dist >= 3

#clear out lava in front of player by placing water
def clearLava():
    #if offset is to large then move cam
    if(abs(90-player.locationData[4]) > 4):
        player.rotateCamY(90)

    pydirectinput.press("2")

    pydirectinput.click(button="right")
    sleep(0.18)
    pydirectinput.click(button="right")


#returns 0 for dont mine 1 for mine bottom 2 for mine top
def checkWall():
    playerY = math.floor(player.locationData[1])

    #if offset is to large then move cam
    if(abs(55-player.locationData[4]) > 4):
        player.rotateCamY(55)

    blockData = getBlockData()
    #if not pointing at block
    if(blockData == None):
        return 0
    #wait for falling block to land
    while getBlockData == "falling":
        blockData = getBlockData()
        sleep(0.1)
    blockY = blockData[1]

    return min(max(0, blockY-playerY+1), 2)