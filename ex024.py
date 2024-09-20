
"""Crie um programa que leia o nome de uma cidade e diga se ela COMEÇA ou não com "Santo"."""
cidade = str(input('Digite o nome de uma cidade: ')).title().strip()
print(cidade[:5] == 'Santo') #maneira como eu fiz o programa

# Alá guanabara

cid = str(input('Digite uma cidade: ')).strip()
print(cid[:5].upper() == 'SANTO')




