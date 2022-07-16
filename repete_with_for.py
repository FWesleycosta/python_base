#!/usr/bin/env python3

__version__ = "0.1.0"
__author__ = "Francisco Wesley"

original = [1, 2, 3]

#For loops
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

#List Comprehension
dobrada = [n * 2 for n in original]
print(dobrada)

# Dict Comprehension
dados = {
    line.split(":")[0]: line.split(":").strip()
    for line in open("post.txt")
    if ":" in line
}

dados = {}
for line in open("post.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados[key] = valor.split()
print(dados)