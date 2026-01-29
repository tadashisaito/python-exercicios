"""
Exercício 18 – Funções trigonométricas

Programa que lê um ângulo e exibe os valores
de seno, cosseno e tangente.
"""

from math import radians, sin, cos, tan
ang = float (input ('Digite o angulo que você deseja: '))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))

print (f'O angulo de {ang} tem o SENO de {seno:.2f}')
print (f'O angulo de {ang} tem o COSSENO de {cosseno:.2f}')
print (f'O angulo de {ang} tem o TANGENTE de {tangente:.2f}')
