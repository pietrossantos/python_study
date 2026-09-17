# Crie um programa que veja quanto uma pessoa tem na carteira e mostre quantos dolares ela pode comprar: 
# Considere: US$1.00 = R$5,16

carteira = float(input('Diga-me quanto você tem em reais na sua carteira:'))
conversão = carteira/5.16
print(f'Convertendo com o que você tem em reais agora, você pode comprar US${conversão:.2f} dólar/es.')

# Desafio concluido com sucesso!