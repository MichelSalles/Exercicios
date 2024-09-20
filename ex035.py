"""Desenvolva um programa que leia o comprimento de três retas
 e diga ao usuário se elas podem ou não formar um triangulo.
 r1
 r2
 r3
 """
print(('-=-')*20)
print('Analizador de Triângulos')
print(('-=-')*20)
r1 = int(input('Primeiro segmento: '))
r2 = int(input('Segundo segmento: '))
r3 = int(input("Terceiro segmento: "))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Os três segmentos formam um triangulo!')
else:
    print('Os seguimentos NÃO formam um triângulo!')