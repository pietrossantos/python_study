# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo 
from math import sin, cos, tan, pi

angulo = float(input('digite um ângulo até 360°:'))
convertendoAngulo = angulo * pi/180
rAngulo = convertendoAngulo
print(rAngulo)
print(f'O seu ângulo é de {angulo}°, os valores dele são:\nseno: {sin(rAngulo)}\ncosseno: {cos(rAngulo)}\ntangente: {tan(rAngulo)}')

# Concluido com sucesso!



