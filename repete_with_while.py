#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Francisco Wesley"

# While - Enquanto

n = 0
while n < 101:
    if n % 2 !=0:
        n += 1
        continue
    print(n)
    n +=1