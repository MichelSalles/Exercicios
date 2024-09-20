 #Escreva um programa que pergunte a quantidade de km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 po dia e R$0,15 por Km rodados.#

km = float(input('Digite e a quantidade de Quilometros rodados: '))
dias = int(input('Digite a quantidade de dias alugado: '))
print('Sabendo que cobramos R$0,15 por km rodados e que o aluguel diario é R$60,00')
print(f'Voce rodou {km}Km e alugou o veículo foi alugado por {dias} dias totalizando R${(km*0.15)+(dias*60.0):.2f}')