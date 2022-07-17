"""
Faça um programa que imprime os números pares de 1 a 200

ex
`python3 numeros_pares.py´
2
4
6
8
....
"""

number = 0

while number < 201:
    if number % 2 !=0:
        number += 1
        continue
    print(number)
    number +=1




