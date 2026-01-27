"""
Exercício 14 – Conversão de temperatura

Programa que lê uma temperatura em graus Celsius
e converte para Fahrenheit.
"""

temperatura = float (input ('Informe a temperatura em °C: '))
conversor = temperatura * 9 / 5 + 32

print (f'A temperatura de {temperatura}°C, corresponde a {conversor}°F')
