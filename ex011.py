#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintá-la.
# Considere que cada litro de tinta pinta uma area de 2m².#

l = float(input('Digite a LARGURA em Metros: '))
a = float(input('Digite a ALTURA em Metros: '))
area = l * a
print(f'Considerando uma area de {area}m² e que a tinta rende 2m². \nSerá necessario {area/2} litros de tinta.')