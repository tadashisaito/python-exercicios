"""
Exercício 11 – Cálculo de área e tinta

Programa que lê a largura e a altura de uma parede,
calcula sua área e a quantidade de tinta necessária
para pintá-la.
"""

largura = float (input ('Largura da parede: '))
altura = float (input ('Altura da parede: '))
area = altura * largura
tinta = area/2

print (f'Sua parede tem a dimensão da sua parede é de {largura}x{altura}, a sua área é de {area}m²')
print (f'Para pintar essa parede, você precisará de {tinta}L de tinta')

