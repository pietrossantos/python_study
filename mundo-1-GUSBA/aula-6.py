number1 = input('digite um número:')
print(type(number1)) # o número nesse caso é do tipo str, precisa declarar o valor primitivo int para executar como número inteiro, ou float para número flutuante.

number2 = int(input('digite outro número:'))
print(type(number2)) #nesse caso retornou um inteiro porque declarei um valor primitivo int.

number1 = int(number1)
print(type(number1)) #agora o número 1 também é do tipo inteiro.

#print('A soma dos dois valores é: ', number1 + number2) #agora a soma irá retornar um valor totalmente inteiro.
soma = number1 + number2
#print('A soma entre o valor ', number1, 'e o valor ', number2, 'é:', soma)     jeito menos prático...

print('A soma de {} + {} é: {}'.format(number1, number2, soma)) #usando o método format() para formatar a string, é mais prático e elegante.

n0 = input('digite algo:')
print(n0.isnumeric()) # verifica se n0 é um número, se for retorna True, se não retorna False.
n0 = input('digite algo:')
print(n0.isalpha()) # verifica se n0 é uma alfabético, se for retorna True, se não retorna False.
n0 = input('digite algo:')
print(n0.isalnum()) # verifica se n0 é alfanumérico, se for retorna True, se não retorna False.



# metódos usados nessa aula:
#type() - retorna o tipo do valor declarado.
#format() - formata a string de forma mais prática e elegante.
#isnumeric() - verifica se o valor declarado é um número, se for retorna True, se não retorna False.
#isalpha() - verifica se o valor declarado é uma alfabético, se for retorna True, se não retorna False.
#isalnum() - verifica se o valor declarado é alfanumérico, se for retorna True, se não retorna False.
