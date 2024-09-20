"""Faça um programa que leia um número de 0 a 9999 e mostre na tela
cada um dos dígitos separados.

Ex:
Digite um número: 1834

unidade:4
dezena:3
centena:8
milhar:1
"""
"""n = str(input('Digite um numero entre 0 à 9999: '))

print(f'Unidade: {n[3]}')
print(f'Desena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')
#Usando o fatiamento de uma string, tive que transformar o texto em str pois como numerico não consegui fatiar ele"""
# essa foi a maneira como eu fiz
# agora vou deixar como o guanaba ensinou( o cara e brabo pra fazer contas ):
num = int(input("Informe um numero: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade {u}')
print(f'Desena {d}')
print(f"Centena {c}")
print(f'Milhar {m}')