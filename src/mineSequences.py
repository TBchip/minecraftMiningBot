import player
import surroundings

def digForward():
    wallLevel = surroundings.checkWall()
    while wallLevel > 0:
        player.mine()
        wallLevel = surroundings.checkWall()
    
    if surroundings.checkLava():
        return False
    else:
        player.walkForward(1)
        return True
        
def digTunnel(length):
    i = 0
    for i in range(length):
        if not digForward():
            break

    return i