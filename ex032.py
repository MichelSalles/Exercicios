"""Faça um programa que leia um ano qualquer e mostre se ela é BISSEXTO."""
from datetime import date
ano = int(input('Que ano quer analizar? Coloque 0 para analizar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano {ano} é um ano Bissexto!")
else:
    print(f'O ano {ano} não é um a no Bissexto!')