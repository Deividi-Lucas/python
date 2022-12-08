#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random as rd 
lista = list()

for i in range(0,4):
    lista.append(input('Nome dos alunos: '))

print(lista)

print(f'O sorteado foi...{rd.choice(lista)}')
