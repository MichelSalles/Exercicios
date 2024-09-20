"""Escreva um programa que faça o computador pensar em um numero inteiro entre 0 e 5
e peça para o usuario tentar descobrir qual foi o número escolhido pelo computador
o programa devrá escrever na tela se o usuário venceu ou perdeu."""
import random
print('-=-'*20)
print('Jogo "Adivinha" ')
print('-=-'*20)
print('Escreva um numero entre 0 e 5:')
n = random.randint(0,5)
us = int(input("Digite um numero: "))
print('PROCESSANDO...')
from time import sleep
sleep(3)
if us == n :
    print('Você acertou!')
else:
    print(f'Game Over! O numero escolhido foi {n}')