#Crie um progra que leia quanto dinheiro umapessoa tem na carteira e quantos Dólares ela pode comprar
# Considere US$1,00 = R$3,27

r = float(input('Quantos Reais você tem : '))
conv = r / 3.27

print(f'Você pode comprar {conv:.2f} Dólares')