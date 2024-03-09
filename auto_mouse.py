import pyautogui
import time

# Set the interval (in seconds) for moving the mouse
interval = 5

try:
    while True:
        # Move the mouse cursor slightly to prevent the screen from going inactive
        pyautogui.moveRel(1, 1)
        time.sleep(interval)
except KeyboardInterrupt:
    print("Program terminated by user.")