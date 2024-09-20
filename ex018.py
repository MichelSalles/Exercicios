""""Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo."""
import math
ang = math.radians(float(input('Digite o valor de um angulo: ')))
seno = math.sin(ang)
cosseno = math.cos(ang)
tangente = math.tan(ang)
print(f'O seno desse angulo é :{seno:.2f}\nO cosseno desse ângulo é {cosseno:.2f}\nE a tangente é {tangente:.2f}')