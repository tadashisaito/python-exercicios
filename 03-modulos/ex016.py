"""
Exercício 16 – Parte inteira

Programa que lê um número real e exibe
sua parte inteira.
"""

from math import trunc
n = float (input ('Digite um valor: '))
print (f'O valor digitado foi {n}, a sua porção inteira é {trunc(n)}')
