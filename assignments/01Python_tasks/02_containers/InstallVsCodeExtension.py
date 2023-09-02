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

subprocess.run(['C:\\Users\\win 10\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'])
time.sleep(4)
pyautogui.shortcut('ctrl','shift','x')
pyautogui.shortcut('ctrl','a')
pyautogui.hotkey('backspace')

