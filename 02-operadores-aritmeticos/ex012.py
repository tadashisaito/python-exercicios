"""
Exercício 12 – Desconto de produto

Programa que lê o preço de um produto e calcula
seu novo valor com desconto.
"""

preço: float = float (input ('Digite o preço do produto? R$  '))
novo = preço - (preço * 5/100)

print (f'O produto que custava R$ {preço:.2f}, na promoção com 5% de desconto, sai por R$ {novo:.2f}')
