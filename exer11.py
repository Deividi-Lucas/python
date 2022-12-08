#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, 
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada 
# litro de tinta pinta uma área de 2 metros quadrados.

print('Pintando parede')
largura = float(input('Largura da parede? '))
altura = float(input('Altura da parede? '))

quadrado = largura *altura

print(f'A sua parede tem {largura} de largura e {altura} de altura, logo ela tem {quadrado} Metros Quadrados')

litros = quadrado /2

print(f'Precisará de {litros} litro de tinta para pinta-la.')