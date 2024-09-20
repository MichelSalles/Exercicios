"""Faça um programa que leia três números e mostre na tela qual é o maior e qual é o menor."""
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
#Verifica o número maior:
maior = n1
if n2 > n1 and n2 > n3 :
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
#Verifica o número menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print(f'O MAIOR numero é {maior}')
print(f'O MEENOR número é {menor}')