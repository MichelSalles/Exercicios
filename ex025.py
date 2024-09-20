"""Crie um programa que leia o nome de uma pessoa e diga se ela tem
'Silva' no nome."""
nome = str(input('Digite seu nome: ')).strip().title()
print('Analisando seu nome... ')
print(f'Seu nome tem Silva? {"Silva" in nome }')# usando o operador in estou verificando se tem "Silva" no nome digitado pelo usuário