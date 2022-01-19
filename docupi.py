import mpmath
import pyautogui
import time


mpmath.mp.dps = 10000 # Set the digits to 100
pi = mpmath.mp.pi # Store the digits in a constant variable called PI
print("Throwing pi in 5 seconds...")
time.sleep(5)
pyautogui.PAUSE = 0
pyautogui.write(str(pi))
