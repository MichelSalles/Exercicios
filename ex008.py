#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
n1 = float(input('Digite um valor em metros: '))

cm = n1 * 100  # Converte o valor para centímetros
mm = n1 * 1000  # Converte o valor para milímetros

print(f'Convertendo para centímetros: {cm} cm')
print(f'Convertendo para milímetros: {mm} mm')
