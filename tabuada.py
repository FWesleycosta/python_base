#!/usr/bin/env python3 
""" Print the multiplication table from 1 to 10

---Multiplication table of 1---

    1 x 1 = 1
    1 x 2 = 2
    1 x 3 = 3
...
###############
---Multiplication table of 2---

    2 x 1 = 2 
    2 x 2 = 4
    2 x 3 = 6
...
#############
"""
__version__ = "0.1.0"
__author__ = "Francisco Wesley"
__license__= "Unlicense"

numeros = list(range (1,21))

# Para cada numero em numeros:
for n1 in numeros:
    print("{:-^18}".format(f"Tabuada do {n1}"))
    print()
    for n2 in numeros:
        resultado = n1 * n2
        print("{:^18}".format(f"{n1} x {n2} = {resultado}"))
    print("#" * 18)