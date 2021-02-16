from time import sleep
import pyperclip
import pydirectinput
import pyautogui

import surroundings


pixelsPerDegreeX = 2000/302.60
pixelsPerDegreeY = 1100/166.40
secondsPerBlock = 0.67


locationData = []
def updateLocationData():
    global locationData

    pydirectinput.keyDown("f3")
    pydirectinput.press("c")
    pydirectinput.keyUp("f3")

    dataString = pyperclip.paste()

    dataList = dataString.split(" ")
    dataList = dataList[6:]

    dataList = [float(x) for x in dataList]

    locationData = dataList


def rotateCamX(targetAngle):
    global locationData

    currentAngle = locationData[3]
    deltaAngle = targetAngle-currentAngle

    mouseMovement = int(pixelsPerDegreeX*deltaAngle)
    pydirectinput.moveRel(mouseMovement, 0, relative=True)

    surroundings.blockDataUpToDate = False
    
    locationData[3] = targetAngle

def rotateCamXRelative(angle):
    global locationData
    
    mouseMovement = int(pixelsPerDegreeX*angle)
    pydirectinput.moveRel(mouseMovement, 0, relative=True)

    surroundings.blockDataUpToDate = False
    
    locationData[3] += angle

def rotateCamY(targetAngle):
    global locationData

    currentAngle = locationData[4]
    deltaAngle = targetAngle-currentAngle

    mouseMovement = int(pixelsPerDegreeY*deltaAngle)
    pydirectinput.moveRel(0, mouseMovement, relative=True)

    surroundings.blockDataUpToDate = False

    locationData[4] = targetAngle

def walkForward(blocks):
    global locationData

    fixSidewaysAlignment()

    updateLocationData()
    
    currentAngle = locationData[3]
    currentAngle /= 90
    currentAngle = int(round(currentAngle, 0))
    currentAngle = ((currentAngle+2)%4)-2

    # walk towards center of a block
    if(currentAngle == -1): #pos x
        xPos = locationData[0]
        xPosDecimals = xPos % 1
        blocks += (0.7-xPosDecimals)

        locationData[0] += blocks
    elif(currentAngle == 0): #pos z
        zPos = locationData[2]
        zPosDecimals = zPos % 1
        blocks += (0.7-zPosDecimals)

        locationData[2] += blocks
    elif(currentAngle == 1): #neg x
        xPos = locationData[0]
        xPosDecimals = xPos % 1
        blocks -= (0.3-xPosDecimals)

        locationData[0] -= blocks
    elif(currentAngle == 2 or currentAngle == -2): #neg z
        zPos = locationData[2]
        zPosDecimals = zPos % 1
        blocks -= (0.3-zPosDecimals)

        locationData[2] -= blocks

    pydirectinput.keyDown("shift")
    pydirectinput.keyDown("w")
    sleep(secondsPerBlock*blocks)
    pydirectinput.keyUp("w")
    sleep(0.1)
    pydirectinput.keyUp("shift")

    surroundings.blockDataUpToDate = False

def fixAlignment():
    walkForward(0.01)

def fixSidewaysAlignment():
    global locationData

    updateLocationData()

    currentAngle = locationData[3]
    currentAngle /= 90
    currentAngle = int(round(currentAngle, 0))
    currentAngle = ((currentAngle+2)%4)-2

    # walk towards center of a block
    if(currentAngle == -1): #pos x
        zPos = locationData[2]
        zPosDecimals = zPos % 1
        sideWaysBlocks = (0.5-zPosDecimals)
        if(sideWaysBlocks >= 0):
            sideWaysKey = "d"
        else:
            sideWaysKey = "a"
        sideWaysBlocks = abs(sideWaysBlocks)
    elif(currentAngle == 0): #pos z
        xPos = locationData[0]
        xPosDecimals = xPos % 1
        sideWaysBlocks = (0.5-xPosDecimals)
        if(sideWaysBlocks >= 0):
            sideWaysKey = "a"
        else:
            sideWaysKey = "d"
        sideWaysBlocks = abs(sideWaysBlocks)
    elif(currentAngle == 1): #neg x
        zPos = locationData[2]
        zPosDecimals = zPos % 1
        sideWaysBlocks = (0.5-zPosDecimals)
        if(sideWaysBlocks >= 0):
            sideWaysKey = "a"
        else:
            sideWaysKey = "d"
        sideWaysBlocks = abs(sideWaysBlocks)
    elif(currentAngle == 2 or currentAngle == -2): #neg z
        xPos = locationData[0]
        xPosDecimals = xPos % 1
        sideWaysBlocks = (0.5-xPosDecimals)
        if(sideWaysBlocks >= 0):
            sideWaysKey = "d"
        else:
            sideWaysKey = "a"
        sideWaysBlocks = abs(sideWaysBlocks)

    if(sideWaysBlocks > 0.19):
        pydirectinput.keyDown("shift")
        pydirectinput.keyDown(sideWaysKey)
        sleep(secondsPerBlock*sideWaysBlocks)
        pydirectinput.keyUp(sideWaysKey)
        sleep(0.1)
        pydirectinput.keyUp("shift")

    surroundings.blockDataUpToDate = False

miningTimeDict = {}
staticMiningTimes = {"minecraft:gravel": 1050}
def mine():
    #select pickaxe
    pydirectinput.press("1")

    blockToMine = surroundings.getBlockData()

    if blockToMine[3] in staticMiningTimes:
        pydirectinput.mouseDown(button="left")
        sleep(staticMiningTimes[blockToMine[3]]/1000)
        pydirectinput.mouseUp(button="left")
        surroundings.blockDataUpToDate = False
    else:
        targetedBlock = surroundings.getBlockData()

        #check for existing mining time
        miningTime = 0
        if blockToMine[3] in miningTimeDict:
            miningTime = miningTimeDict[blockToMine[3]]

        #mine block
        while blockToMine == targetedBlock:
            pydirectinput.mouseDown(button="left")
            sleep(miningTime/1000)
            pydirectinput.mouseUp(button="left")
            surroundings.blockDataUpToDate = False

            miningTime += 50

            targetedBlock = surroundings.getBlockData()
            
        miningTime -= 50 #negate last increase

        #update miningTimeDict
        if blockToMine[3] in miningTimeDict:
            miningTimeDict[blockToMine[3]] = max([miningTime, miningTimeDict[blockToMine[3]]])
        else:
            miningTimeDict[blockToMine[3]] = miningTime

    return True