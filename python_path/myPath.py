#! python3
# myPath.py - Displays list of my current path information

import sys
import os

for p in sys.path:
    print(p)

os.environ['PYTHONPATH'].split(os.pathsep)
