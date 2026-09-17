n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))

som = n1 + n2 # soma
sub = n1 - n2 # subtração
mult = n1 * n2 # multiplicação
exp = n1 ** n2 # exponenciação
div = n1 / n2 # divisão
divI = n1 // n2 # divisão inteira
res = n1 % n2 # resto
                                                                                              # ":.3f" refere-se a ter 3 pontos flutuantes como limite.
print('a soma é: {}, a subtração é: {}, a multiplicação é: {}, a exponenciação é: {}, a divisão é: {:.3f}'.format(som, sub, mult, exp, div), end=" >>> ") # o end="" serve para juntar um print na mesma linha, podendo adicionar qualquer string entre eles.
print('A divisão inteira é: {}, \no resto é: {}'.format(divI, res)) # o "\n" serve para pular uma linha.

# OPERADORES ARITMETICOS / STRINGS

nome = input('Qual é o seu nome?')
print('Seu nome é: ^{:_^20}^\nPrazer em te conhecer!'.format(nome))      


# Usando o "{:}" posso fazer muitas coisas, como por exemplo: "{:<20}" "{:>20}" vai deixar um espaço limitado a 20, se o nome tiver 5 letras, vai dar um espaço de 15 caracteres; "{:^20}" deixa a string centralizada no meio; "{:_^20}" vai deixar a string no meio e nos espaços restantes vai colocar o "_", e entre outras utilizações interessantes...


# A sintaxe do comando .format() no comando print está comumente sendo escrita com a letra f antes das aspas, simples ou duplas, exemplo:
# print(f'Olá, {name}!) - Ficou bem mais simples, mas como eu estava testando os comandos que o Guanabara       explicou senti dificuldades com esse formato. Consegui os seguintes resultados usando uma sintaxe parecida:

# name = str(input('Seu nome: '))

# print(f'Olá, {name}')

# print(f'Olá, {name:=^20}'.upper())

# Seu nome: Wilson

# Olá, Wilson

# OLÁ, =======WILSON=======

name = input('what´s your name?')
print(f'Your name is: ^{name:_^20}^\nNice to meet you!')

# Funciona de igual forma! 