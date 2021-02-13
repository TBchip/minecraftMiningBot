from time import sleep
import math

import player
import surroundings

def main():
    sleep(1)

    player.rotateCamX(90)
    while not surroundings.checkLava():
        player.walkForward(1)

        player.rotateCamY(0)
        player.mine()

        player.rotateCamY(40)
        player.mine()

if __name__ == "__main__":
    main()