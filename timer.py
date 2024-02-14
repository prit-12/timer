"""
This program is used as an example for MGTC28.
timer.py is a simple Python script that will allow user to set timer duration.
Upon timer expiry, user will see the time up meme and sound notification.
timer.py uses the time library to help keep track of time
"""

import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random
from PIL import Image # the pillow library makes it easy to display images 

def nerve_of_steel_game():
    # Display the initial game instruction
    print("Players stand")

# Wait for a random time between 5 and 25 seconds
random_sleep_time = random.randint(5, 25)
print(f"Random waiting time is {random_sleep_time} seconds. Prepare to sit!")
time.sleep(random_sleep_time)

print("Time Up. Last to sit down wins.")

# Display the "times up" meme
im.show()
