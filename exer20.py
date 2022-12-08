#Exercício Python 020: O mesmo professor do desafio 019 quer sortear 
#a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random as rd 

n1 = input('aluno 01: ')
n2 = input('aluno 02: ')
n3 = input('aluno 03: ')
n4 = input('aluno 04: ')

lista = [n1, n2, n3, n4]
rd.shuffle(lista)

print('A lista ficou assim:')
print(f'{lista}')