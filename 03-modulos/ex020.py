"""
Exercício 20 – Ordem de apresentação

Programa que lê o nome de alunos e sorteia
a ordem de apresentação dos trabalhos.
"""

from random import shuffle
a1 = str (input ('Primeiro aluno: '))
a2 = str (input ('Segundo aluno: '))
a3 = str (input ('Terceiro aluno: '))
a4 = str (input ('Quarto aluno: '))

lista = [a1, a2, a3, a4]
shuffle (lista)

print (f'A ordem de apresentação será:')
print (lista)

