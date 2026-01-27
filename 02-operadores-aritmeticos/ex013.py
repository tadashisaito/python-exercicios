"""
Exercício 13 – Aumento de salário

Programa que lê o salário de um funcionário
e calcula o novo valor com aumento.
"""

salario = float (input('Qual é o salário do funcionário?R$ '))
novo = salario + (salario * 15/100)

print (f'Um funcionário que ganhava R$ {salario:.2f}, com o aumento de 15%, passa a receber R$ {novo:.2f}')
