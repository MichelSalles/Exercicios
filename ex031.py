"""Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200 Km
e R$0,45 para viagens mais logas."""
dis = float(input('Digite a distancia em Km: '))
passagem = 0.50
if dis > 200 :
    passagem = 0.45
    print(f'Sua viagem tera uma distâcia de {dis} Km. O valor da passagem será R${passagem*dis:.2f}')
else:
    print(f'Sua viagem tera uma distância de {dis} km. O valor da passagem será R${passagem*dis:.2f}')

