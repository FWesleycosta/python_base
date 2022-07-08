#!/usr/bin/env python3 
""" Print the multiplication table from 1 to 10

Multiplication table of 1:

1 x 1 
1 x 2 
1 x 3
------------
Multiplication table of 2:

2 x 1 
2 x 2 
2 x 3
"""
__version__ = "0.1.0"
__author__ = "Francisco Wesley"
__license__= "Unlicense"

#base = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

numeros = list(range (1,11))

# Para cada numero em numeros:
for numero in numeros:
    print("Tabuada do:", numero)
    for outro_numero in numeros:
        print(numero * outro_numero)
    print("------------")