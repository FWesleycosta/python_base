#!/usr/bin/env python3

import os
import sys

# Easy to ASK Forgiveness than permission


try:
    names = open("names.txt").readlines() #FileNotFoundError
    1/1 #ZeroDivisionError
    print(names.append)
except FileNotFoundError as error:
    print(f"{str(error)}.")
    sys.exit(1)
except ZeroDivisionError:
    print("[Error] You cant divide by zero!!")
    sys.exit(1)
else: #Execute in cause error
    print("Sucesso!!!")
finally: # Forever execution
    print("Execute isso sempre!")

try:
    print(names[2])
except:
    print("[Error] Missing name in the list")
    sys.exit(1)