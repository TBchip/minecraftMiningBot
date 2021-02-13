from time import sleep
import pyperclip
import pydirectinput
import pyautogui

import surroundings


pixelsPerDegreeX = 2000/302.60
pixelsPerDegreeY = 1100/166.40
secondsPerBlock = 30/129.94


def getLocationData():
    pydirectinput.keyDown("f3")
    pydirectinput.keyDown("c")
    pydirectinput.keyUp("f3")
    pydirectinput.keyUp("c")

    dataString = pyperclip.paste()
    dataList = dataString.split(" ")
    dataList = dataList[6:]

    dataList = [float(x) for x in dataList]
    return dataList
    

def rotateCamX(targetAngle):
    currentAngle = getLocationData()[3]
    deltaAngle = targetAngle-currentAngle

    mouseMovement = int(pixelsPerDegreeX*deltaAngle)
    pydirectinput.moveRel(mouseMovement, 0, relative=True)
    sleep(0.1) # wait for rotation in game

def rotateCamY(targetAngle):
    currentAngle = getLocationData()[4]
    deltaAngle = targetAngle-currentAngle

    mouseMovement = int(pixelsPerDegreeY*deltaAngle)
    pydirectinput.moveRel(0, mouseMovement, relative=True)
    sleep(0.1) # wait for rotation in game

def walkForward(blocks):
    locData = getLocationData()
    
    currentAngle = locData[3]
    currentAngle /= 90
    currentAngle = int(currentAngle)

    # walk towards center of a block
    if(currentAngle == -1): #pos x
        xPos = locData[0]
        xPosDecimals = xPos % 1
        blocks += (0.5-xPosDecimals)
    elif(currentAngle == 0): #pos z
        zPos = locData[2]
        zPosDecimals = zPos % 1
        blocks += (0.5-zPosDecimals)
    elif(currentAngle == 1): #neg x
        xPos = locData[0]
        xPosDecimals = xPos % 1
        blocks -= (0.5-xPosDecimals)
    elif(currentAngle == 2): #neg z
        zPos = locData[2]
        zPosDecimals = zPos % 1
        blocks -= (0.5-zPosDecimals)

    blocks -= 0.5 #fixes movement offset

    pydirectinput.keyDown("w")
    sleep(secondsPerBlock*blocks)
    pydirectinput.keyUp("w")

miningTimeDict = {}
def mine():
    blockToMine = surroundings.getBlockData()
    targetedBlock = surroundings.getBlockData()

    #check for existing mining time
    miningTime = 0
    if blockToMine[3] in miningTimeDict:
        miningTime = miningTimeDict[blockToMine[3]]

    #mine block
    #sometimes, after breaking a block, the player is pointing at void and targetedblock will not be updated.
    #this will compare the timestamp on the targetedblock data to ensure it is newly taken data.
    previousTargetedBlockTimestamp = 0 
    while blockToMine[:4] == targetedBlock[:4] and previousTargetedBlockTimestamp != targetedBlock[4]:
        pydirectinput.mouseDown(button="left")
        sleep(miningTime/1000)
        pydirectinput.mouseUp(button="left")

        miningTime += 50

        previousTargetedBlockTimestamp = targetedBlock[4]
        targetedBlock = surroundings.getBlockData()
    miningTime -= 50 #negate last increase

    #update miningTimeDict
    if blockToMine[3] in miningTimeDict:
        miningTimeDict[blockToMine[3]] = max([miningTime, miningTimeDict[blockToMine[3]]])
    else:
        miningTimeDict[blockToMine[3]] = miningTime
    
    print(miningTimeDict)