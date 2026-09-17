# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-lá, sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('Qual a largura, em metros, da sua parede?'))
altura = float(input('Qual a altura, em metros, da sua parede?'))
tinta = 2
area = largura*altura
tintaNecessaria = area/tinta
print(f'Você tem uma parede com a área de: {area}m², então a tinta necessária para pinta-lá é: {tintaNecessaria}m²')

# Desafio concluido com sucesso!