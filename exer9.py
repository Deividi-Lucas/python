#Exercício Python 009: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

number = int(input('Digite um valor: '))

print(f'A tabuada do {number} é:\n----------------------')

for i in range(0,11):
    print(f'{number} * {i} = {number*i}')
