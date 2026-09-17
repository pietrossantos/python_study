# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

cliente = input('O que você comprou?')
consultandoPreco = float(input('o preço desse produto é:'))

desconto = consultandoPreco*0.05
novopreco = consultandoPreco-desconto
print(f'O valor do seu produto com o desconto ficou: R${novopreco:.2f}\nAproveite o seu desconto!')

# Desafio concluido com sucesso!