from time import sleep
import math

import player
import surroundings

def main():
    sleep(1)
    
    player.rotateCamX(90)
    print(surroundings.checkLava())

if __name__ == "__main__":
    main()