#!/usr/bin/env python3

from PIL import Image, ImageOps
import os
import sys

path = '/Users/brianclauser/automate_everything/resized'
MAX_SIZE = (800, 600)


def newsize():

    os.makedirs('resized', exist_ok=True)
    for filename in os.listdir('.'):
        if not (filename.endswith('.png') or filename.endswith('jpeg') or filename.endswith('jpg')):
            continue  # skip non-image files
        im = Image.open(filename)
        print('Resizing %s...' % (filename))

        imResize = im.resize((MAX_SIZE), Image.ANTIALIAS)
        # im.thumbnail(MAX_SIZE)  # Only works when original is larger
        # im.save(os.path.join(path, filename))
        imResize.save(os.path.join(path, filename.replace("jpeg", "jpg")))


newsize()
