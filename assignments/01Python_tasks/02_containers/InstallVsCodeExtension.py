##########################################################################################
#                                                                                        #
# File: installVsCodeExtensions.py                                                       #
# Author: Mohamed Samy Ahmed                                                             #
# Date: August 8, 2023                                                                   #
#                                                                                        #
# Description:                                                                           #
#    Provide a brief description of the purpose and functionality of the Python file.    #
#                                                                                        #
##########################################################################################

import pyautogui
import time
import subprocess

def move_and_click(x, y, click_delay=0.5):
    pyautogui.moveTo(x, y)
    time.sleep(click_delay)
    pyautogui.click()


subprocess.run(['C:\\Users\\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'])
time.sleep(4)

# Example usage
x_pixels = 100  # Number of pixels to move horizontally
y_pixels = 50   # Number of pixels to move vertically

# Get the current cursor position
current_x, current_y = pyautogui.position()

# Calculate the new position by adding the specified number of pixels
new_x = current_x + x_pixels
new_y = current_y + y_pixels

# Move the cursor to the new position and perform a click
move_and_click(new_x, new_y)