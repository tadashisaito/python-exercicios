from datetime import date
nascimento = int (input('Digite o ano que você nasceu: '))
idade = date.today().year - nascimento
anos_atraso = idade - 18
anos_faltam = 18 - idade

print (f'Você tem {idade} anos')

if anos_faltam == 1 or anos_atraso == 1:
    palavra = 'ano'
else:
    palavra = 'anos'


if idade < 18:
    print (f'E ainda vai se alistar ao serviço militar, falta exatamente {anos_faltam} {palavra}')
elif idade == 18:
    print ('E precisa se alistar JÁ')
else:
    print(f'E já passou do tempo de alistamento, você esta {anos_atraso} {palavra} atrasado em relação ao prazo')
