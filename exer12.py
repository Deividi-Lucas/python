#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e 
# mostre seu novo preço, com 5% de desconto.

produto = float(input('Valor do produto?: '))

print(f'O produto com preço de R${produto} deve ser reajustado para R${produto-(produto*0.05)}')

print(f'Fim do programa.')

