"""Escreva um preograma que pergunte o salário de um funcionario e calcule o valor do seu aumento.
-Para salários superiores a R$1.250,00, calcule um aumento de 10%.
-Para os inferiores ou iguais, o aumento é de 15%"""
salario = float(input('Digite o valor do seu salário: '))
if salario <= 1250.00:
    aumento = 15
else:
    aumento = 10
print(
    f'Seu salário tera um aumento de {aumento}% e passará a ser de R${(salario + (salario * aumento / 100)):.2f}')