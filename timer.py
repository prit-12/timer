"""
This program is modified for MGTC28 to include a "Nerve of Steel" game.
Upon game start, players stand and wait for a random time between 5 to 25 seconds before sitting. The last to sit down wins.
The 'times-up.jpeg' image is displayed at the end of the game.
"""

import time
import random
from PIL import Image

def main():
    im = Image.open("times-up.jpeg")

    print("Players, stand up!")
    time.sleep(random.randint(5, 25))
    print("Time's up! Last to sit down wins.")
    
    im.show()

if __name__ == "__main__":
    main()
