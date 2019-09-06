#!/usr/local/bin/python3.7

try:
   f = open("/etc/hosts1")
   # go ahead and read the file
except FileNotFoundError:
   print("no hosts file")
