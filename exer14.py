#Exercício Python 014: Escreva um programa que converta uma temperatura digitando em graus Celsius
#  e converta para graus Fahrenheit.

# Formula
# (0 °C × 9/5) + 32 = 32 °F

graus = float(input('Informe a temperatura em °C: '))

fah = (graus * (9/5) + 32)

print('{}°C são igual a {} fahrenheit'.format(graus, fah))
