#!/usr/bin/env python3

import os
import pathlib

path = os.path.realpath('~/Downloads/STJOE')
current_directory = pathlib.Path(path)

# For Adding to file name
for filename in os.listdir('.'):
    if not filename.endswith('.zip'):
        continue
    file, file_ext = os.path.splitext(filename)
    # print(filename)
    dst = "STJOE_" + file + "_001" + file_ext  # change as needed
    src = filename
    dst = dst
    print('Renaming %s...' % (filename))
    os.rename(src, dst)


""" # For Removing from file name
for filename in os.listdir('.'):
    if not filename.endswith('.zip'):
        continue
    file, file_ext = os.path.splitext(filename)
    f = str(filename)
    rf = f.strip('_00.')  # change as needed
    dst = rf
    src = filename
    dst = dst
    print('Renaming %s...' % (filename))
    os.rename(src, dst) """
