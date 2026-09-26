# Primeira maneira de importar, importando tudo

import math

aluno = float(input('Diga qual é o número e eu darei a sua raiz quadrada:'))
raiz = math.sqrt(aluno)
print(f'A raiz de {aluno} é {raiz} ')

# Segunda maneira de importar, especificando 

from math import sqrt

aluno2 = float(input('Insira um valor:'))
raiz2 = sqrt(aluno2)  # como estou importando especificando, não preciso usar o "math." 
print(f'A raiz de {aluno2} é {raiz2}')
