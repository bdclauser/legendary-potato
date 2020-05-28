#! /usr/bin/env python3
# gif_border.py - Automatically grabs a gif and indexs each frame in folder

import os
import sys
from PIL import Image, ImageOps, ImageSequence

os.makedirs('withBorder', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.gif')):
        continue  # skip all non-gif files
    with Image.open(filename) as image:
        index = 1
        for frame in ImageSequence.Iterator(image):
            frame.save("frame%d.png" % index)
            index += 1
