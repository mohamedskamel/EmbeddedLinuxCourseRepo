
import webbrowser
import pyautogui
import time

def move_and_click(x, y, click_delay=0.5):
    pyautogui.moveTo(x, y)
    time.sleep(click_delay)
    pyautogui.click()

webbrowser.get('windows-default').open_new_tab("https://www.gmail.com/")
time.sleep(4)
# Example usage
x_pixels = -1626  # Number of pixels to move horizontally
y_pixels = -254   # Number of pixels to move vertically

xRead_pixels = -1426  # Number of pixels to move horizontally
yRead_pixels = -254   # Number of pixels to move vertically
# Get the current cursor position
current_x, current_y = pyautogui.position()

# Calculate the new position by adding the specified number of pixels
new_x = x_pixels
new_y = y_pixels

# Move the cursor to the new position and perform a click
move_and_click(new_x, new_y)

time.sleep(4)
# Calculate the new position by adding the specified number of pixels
new_x = xRead_pixels
new_y = yRead_pixels

# Move the cursor to the new position and perform a click
move_and_click(new_x, new_y)