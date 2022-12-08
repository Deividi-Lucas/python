#Exercício Python 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

#Ex: Digite um número: 6.127
#O número 6.127 tem a parte Inteira 6.
from math import trunc

number = float(input('Digite um valor quebrado: '))

print('A parte inteira deste valor é {}'.format(trunc(number)))