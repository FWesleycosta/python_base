#!/usr/bin/env python3 

""" Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
"""
__version__ = "0.2.0"
__author__ = "Francisco Wesley"
__license__= "Unlicense"

# Creare dict

from pprint import pprint

aula_english = {
    "sala1": ["Erik", "Maia"],
    "sala2": ["Joana", "Antonio", "Carlos"]
}

aula_music = {
   "sala1": ["Erik"],
   "sala2": ["Carlos", "Maria"]
}

aula_dance = {
    "sala1": ["Gustavo", "Sofia", "Joana"],
    "sala2": ["Antonio"]
}

print(
    f"Alunos da Sala 1 {aula_english['sala1']} e alunos da Sala 2 {aula_english['sala2']} que estão cursando as aulas de Inglês. \n"
    f"Alunos da Sala 1 {aula_music['sala1']} e alunos da Sala 2 {aula_music['sala2']} que estão cursando as aulas de Música.\n"
    f"Alunos da Sala 1 {aula_dance['sala1']} e alunos da Sala 2 {aula_dance['sala2']} que estão cursando as aulas de Dança.\n"
)



