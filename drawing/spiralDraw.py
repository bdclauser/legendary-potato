#! python3
# coding = utf-8

import pyautogui
import time

time.sleep(5)

pyautogui.click()  # click to put drawing program in focus

# pyautogui.moveTo(800, 350)

distance = 200
change = 20
while distance > 0:
    # move right
    pyautogui.drag(distance, 0, duration=0.2)
    # move down
    distance = distance - change
    pyautogui.drag(0, distance, duration=0.2)
    # move left
    pyautogui.drag(-distance, 0, duration=0.2)
    # move up
    distance = distance - change
    pyautogui.dragRel(0, -distance, duration=0.2)
