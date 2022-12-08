#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

dolar = 5.25

print('Quantos $ dolar vocẽ deseja comprar?', end='')
number = float(input(': '))

print(f'Para comprar ${number:.2f} dolar, precisa desenbolsar R${number*dolar:.2f}')

