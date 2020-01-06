#!/usr/bin/env python3

import fileinput
import sys
from binascii import a2b_base64

file_path = sys.argv[1]
rewrite_rules = a2b_base64(str.encode(sys.argv[2])).decode("ISO-8859-1")

with fileinput.FileInput(file_path, inplace=True) as file:
    inside_rewrites = False
    # Clear existing rewrites and replace them by new ones
    for line in file:
        if "END_REWRITES" in line:
            print(str(rewrite_rules))
            inside_rewrites = False

        if not inside_rewrites:
           print(line, end='')
        if "START_REWRITES" in line:
            inside_rewrites = True
