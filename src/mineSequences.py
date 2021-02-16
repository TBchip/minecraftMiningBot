from time import sleep

import player
import surroundings
import mineBotLoop

def digForward():
    wallLevel = surroundings.checkWall()
    while wallLevel > 0 and not mineBotLoop.stopBotLoop:
        player.mine()
        wallLevel = surroundings.checkWall()
    
    if surroundings.checkLava():
        surroundings.clearLava()
    
    player.walkForward(1)
    return True

def digTunnel(length):
    i = 0
    for i in range(length):
        if mineBotLoop.stopBotLoop:
            return i

        digForward()

    return i

def stripMinePart(tunnelLength):
    player.fixAlignment()
    digTunnel(3)

    if mineBotLoop.stopBotLoop:
        return False

    player.rotateCamXRelative(-90)
    player.fixAlignment()
    digTunnel(tunnelLength)

    if mineBotLoop.stopBotLoop:
        return False

    player.rotateCamXRelative(90)
    player.fixAlignment()
    digTunnel(3)

    if mineBotLoop.stopBotLoop:
        return False

    player.rotateCamXRelative(90)
    player.fixAlignment()
    digTunnel(tunnelLength*2)

    if mineBotLoop.stopBotLoop:
        return False

    player.rotateCamXRelative(90)
    player.fixAlignment()
    digTunnel(3)

    if mineBotLoop.stopBotLoop:
        return False

    player.rotateCamXRelative(90)
    player.fixAlignment()
    digTunnel(tunnelLength)

    if mineBotLoop.stopBotLoop:
        return False

    player.rotateCamXRelative(90)
    player.fixAlignment()
    digTunnel(3)
