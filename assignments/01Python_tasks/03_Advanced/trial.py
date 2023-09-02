import pyautogui
import time

def get_cursor_position():
    while True:
        x, y = pyautogui.position()
        print(f"Cursor position: x={x}, y={y}", end="\r")
        time.sleep(0.1)

# Call the function to continuously display the cursor position
get_cursor_position()