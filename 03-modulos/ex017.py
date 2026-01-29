"""
Exercício 17 – Cálculo da hipotenusa

Programa que lê os valores dos catetos de um
triângulo retângulo e calcula a hipotenusa.
"""

from math import hypot
co = float (input ('Comprimento do cateto oposto: '))
ca =  float (input ('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print (f'A hipotenusa vai medir {hi:.2f}')
