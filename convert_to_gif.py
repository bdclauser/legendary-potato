import os
import sys
import glob
from PIL import Image

fp_in = "/Users/brianclauser/Downloads/toBorder/withBorder/frame*.png"
fp_out = "/Users/brianclauser/Downloads/toBorder/withBorder/NEW.gif"

img, *imgs = [Image.open(f) for f in sorted(glob.glob(fp_in))]
img.save(fp=fp_out, format='GIF', append_images=imgs,
         save_all=True, duration=200, loop=0)
