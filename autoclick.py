import pyautogui # Import the module using this line
import time # To delay the clicking

print("Autoclicker starting in 5 seconds...")
time.sleep(5)
pyautogui.PAUSE = 0.00001
while True:
    pyautogui.click()

