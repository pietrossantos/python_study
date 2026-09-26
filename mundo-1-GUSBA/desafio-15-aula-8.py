# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

from math import sqrt, pow
cateto1 = int(input('digite o valor do cateto oposto:'))
cateto2 = int(input('digite o valor do cateto adjacente:'))

hipotenusa = pow(cateto1, 2) + pow(cateto2, 2)
rhipotenusa = sqrt(hipotenusa)
print(f'O comprimento da sua hipotenusa é: {rhipotenusa:.2f}')

# Concluido com sucesso!