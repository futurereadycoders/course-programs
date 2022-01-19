import mpmath
import pyautogui
import time

time.sleep(5)
NUMBER_OF_DIGITS = 1000
mpmath.mp.dps = NUMBER_OF_DIGITS
pyautogui.write(str(mpmath.mp.pi))
