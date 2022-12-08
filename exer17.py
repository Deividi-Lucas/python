#Exercício Python 017: Faça um programa que leia o comprimento do cateto oposto e
#do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
import math

catops = float(input('Comprimento do cateto oposto: '))
catadj = float(input('Comprimento do cateto adjacente: '))

hip = (catadj**2) + (catops**2)

print(f'A hipotenusa é igual a {math.sqrt(hip):.2f}')