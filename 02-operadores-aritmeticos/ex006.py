"""
Exercício 06 – Dobro, triplo e raiz quadrada

Programa que lê um número e exibe
seu dobro, triplo e raiz quadrada.
"""

n = int (input ('Digite um número: '))
dobro = n * 2
triplo = n * 3
'''raiz = n ** (1/2)'''
raiz = pow(n, (1/2))

print (f'O dobro de {n}, é igual a {dobro}')
print (f'O triplo de {n}, é igual a {triplo} \nE a raiz quadrada de {n}, é igual a {raiz:.2f}')
