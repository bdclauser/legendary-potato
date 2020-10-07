#!/usr/bin/env python3

import pyatuogui as pag
import pyperclip
import subprocess
import time

zlink = open('zoom_links.txt', 'w')

subprocess.call(["/usr/bin/open", "Applications/zoom.us.app"])
time.sleep(2)

periods = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']

for periods in periods:
    period = pag.locateCenterOnScreen(period + '.png')
    pag.moveTo(period.x/2, period.y/2)
    pag.click()

    copy_invite = pag.locateCenterOnScreen('copy_invite.png')
    pag.moveTo(copy_invite.x / 2, copy_invite.y / 2)
    pag.click()
    time.sleep(2)
    zlink.write(pyperclip.paste() + '\n')

print('All zoom links have been copeied and pasted into your text file.')
