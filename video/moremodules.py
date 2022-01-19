# Extra modules
import pyttsx3
import time
import random
import pyautogui
import nonsentence


engine = pyttsx3.init()

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


while True:

    engine.say(nonsentence.new_sentence(10, 3, 10))
    engine.runAndWait()
