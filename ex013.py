#Faça um algoritmo que leia o salário de funcionárioe mostre o seu novo salário com 15% de aumento
sal = float(input("Digite osalário do funcionário:"))
aument15porc = sal * (15/100)
sal_novo = sal + aument15porc
print(f'O novo salário é de R${sal_novo:.2f} ')