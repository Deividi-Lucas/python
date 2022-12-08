#Exercício Python 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

text = input('Digite algo: ')

print('O tipo primitivo desse valor é {}'.format(type(text)))
print('Só tem espaço?',text.isspace())
print('É um número? {}'.format(text.isnumeric()))
print('É Alfabético?  {}'.format(text.isalpha()))
print('É alfanumérico? {}'.format(text.isalnum()))
print('Está em Maiúsculo? {}'.format(text.isupper()))
print('Está em Minúsculo? {}'.format(text.islower()))
print('Está Capitalizada? {}'.format(text.istitle()))
