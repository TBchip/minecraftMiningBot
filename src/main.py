from time import sleep
import math

import player
import surroundings

def main():
    sleep(1)

    player.rotateCamX(-90)
    while not surroundings.checkLava():
        player.walkForward(1)

        if(surroundings.checkWallTop()):
            player.mine()
        
        if(surroundings.checkWallBottom()):
            player.mine()
    
    # player.rotateCamX(-90)
    # while not surroundings.checkLava():
    #     player.walkForward(1)

if __name__ == "__main__":
    main()