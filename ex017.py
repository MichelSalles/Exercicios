#Faça um programa que eia o comprimento do cateto oposto e o cateto adjacente de um triangulo,
# calcule e mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
hypot = math.hypot(co,ca)
print(f'Hipotenusa é igual a : {hypot:.2f}')

