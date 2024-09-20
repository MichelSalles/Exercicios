"""Escreva um programa que leia a velocidade de um carro.
-Se ele ultrapassar 80kmn/h mostre uma menssagem dizendo que ele foi multado.
-A multa vai custar R$7.00 por cada KM acima do limite."""

v = float(input('Digite a velocidade do carro: '))
m = (v - 80)*7
if v >= 81:
    print(f'Velocidade exedida! voce sera multado em R${m:.2f}')
else:
    print('Você não exedeu o limite de veocidade.')
