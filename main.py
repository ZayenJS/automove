#! /usr/bin/python3
'''
    Script to automove the mouse cursor to prevent
    the computer from going to sleep
'''

import time
import sys

from random import randint
from datetime import datetime

import tkinter as tk
import pyautogui

pyautogui.FAILSAFE = False
root = tk.Tk()
# gets the screen size the then move the mouse cursor within the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

try:
    while True:
        # time to sleep between movements
        sleep_time = randint(3, 60 * 3)
        # time to move the mouse cursor -
        # it will be divided by 10 to not take too long
        movement_time = randint(2, 8)
        # gets a random position on the screen
        x = randint(1, screen_width)
        y = randint(1, screen_height)

        pyautogui.moveTo(x, y, movement_time / 10)

        print(f"Movement made at {datetime.now().time()}")
        # convert seconds to minutes

        minutes = sleep_time // 60
        seconds = sleep_time % 60

        minutes = f"{minutes} {'minutes' if minutes > 1 else 'minute'}"
        seconds = f"{seconds} {'seconds' if seconds > 1 else 'second'}"

        print(f"Next movement in {minutes} {seconds}")

        time.sleep(sleep_time)

        print("=" * 36)
except KeyboardInterrupt:
    print("\n\nProgram terminated")
    sys.exit()
