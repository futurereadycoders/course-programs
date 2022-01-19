# A Discord spammer using Python
import time
import random
import pyautogui

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]

print("Spamming Discord!")
time.sleep(5)

while True:
    word = ""
    for i in range(random.randint(3,10)):
        word = word + random.choice(vowels)
        word = word + random.choice(consonants)
    pyautogui.write(word)
    pyautogui.press("enter")
    time.sleep(0.5)

