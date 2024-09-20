""" Crie um Programa que leia o nome completo de uma pessoa e mostre:
 1-O nome com todas as letras maiúsculas.
 2-O nome com todas minúsculas .
 3-Quantas letras ao todo (sem considerar espaços).
 4-Quantas letras tem o primeiro nome. """
nome = str(input('Digite seu nome completo: ')).strip()#função strip elimina os espaços no começo e fim
print(f'Seu nome completo com todas as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome completo com todas as letras minúsculas é: {nome.lower()}')
print(f'Seu nome tem {(len(nome) - nome.count(" "))} letras.') # Função 'count' nessa situação esta retirando os "espaços do nome inteiro "
#print(f'Seu primeiro nome tem {nome.find(" ")} letras')# Função find nesse caso vai encontrar em qual carctere o espaço apareçe
separa = nome.split()# Nessa função o nome foi incluso como lista
print(f'Seu primeiro nome tem {len(separa[0])} letras') #Nessa função está mostrasndo a quantidade de letras que tem no item 0 da lista
print(f'Seu segundo nome tem {len(separa[1])} letras')# nessa função mostra o item 2 da lista
print(f'Seu terceiro nome tem {len(separa[2])} letras')# Nessa função mostra o item 3 da lista
print(f'Seu quarto nome tem {len(separa[3])} letras.')# nessa funçao mostra o item 4 da lista
