#!/usr/bin/env python3 

""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""
__version__ = "0.1.0"
__author__ = "Francisco Wesley"
__license__= "Unlicense"

# Dados

alunos_sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
alunos_sala2 = ["Joao", "Antonio", "Carlos", "Maria", "Isolda"]

aula_english = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_music = ["Erik", "Carlos", "Maria"]
aula_dance = ["Gustavo", "Sofia", "Joana", "Antonio"]

atividades = [
    ("English", aula_english), 
    ("Music", aula_music), 
    ("Dance", aula_dance)
]

# Listar alunos em cada atividade por sala

for nome_atividade, atividade in atividades:

    print(f"Alunos da atividade {nome_atividade}\n")
    print()

    aula_sala1 = []
    aula_sala2 = []

    for aluno in atividade:
        if aluno in alunos_sala1:
            aula_sala1.append(aluno)
        elif aluno in alunos_sala2:
            aula_sala2.append(aluno)

    print("Sala 1", aula_sala1)
    print("Sala 2", aula_sala2)
    print()
    print("-" * 30)
