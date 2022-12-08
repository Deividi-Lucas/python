#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

from math import sqrt

number = int(input('Digite um valor:'))

dobro = number * 2

triplo = number *3

raiz = sqrt(number)


print('O dobro é ',dobro)
print('O triplo é ',triplo)
print('A Raiz é ', raiz)
