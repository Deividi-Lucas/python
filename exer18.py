#Exercício Python 018: Faça um programa que leia um ângulo qualquer e
#mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

number = float(input('Digite o angulo em graus: '))

tr = math.radians(number)

print(f'Consseno = {math.cos(tr):.2f}\nSeno = {math.sin(tr):.2f}\nTangente = {math.tan(tr):.2f}')



