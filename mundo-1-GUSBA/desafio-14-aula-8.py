# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
# ex: 6.127 > 6 é a parte inteira
from math import trunc
num = float(input('digite um número:'))
print(f'A parte inteira do seu número é: {trunc(num)}')

# Concluido com sucesso!