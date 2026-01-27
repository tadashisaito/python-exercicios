"""
Exercício 10 – Conversão de moeda

Programa que lê a quantidade de dinheiro em reais
e calcula quantos dólares podem ser comprados,
considerando a cotação fixa. (US$ 1,00 = R$ 3,27)
"""


real = float (input ('Quanto dinheiro você tem na Carteira?R$ '))
dolar = real / 3.27

print (f'Com R$ {real:.2f}, você pode comprar US$ {dolar:.2f} ')
