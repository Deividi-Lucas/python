#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e 
# mostre seu novo salário, com 15% de aumento.

sal = float(input('Salário do Funcionário: R$'))

print(f'Esse funcionário deve ter um reajuste para R${sal+(sal*0.15):.2f}')

