#!/usr/bin/env python3.7

import os
dirpath = input("Enter the name of the directory: ")
#print(dirpath)
os.chdir(dirpath)
for file in os.listdir("."):
    info = os.stat(file)
    print("%-20s : size %d" % (file, info.st_size))
