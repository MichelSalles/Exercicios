#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

p = float(input("Digite o valor do produto: R$"))
des = p * (5/100)

print(f'Na liquidação o valor sai : {p - des:.2f}')