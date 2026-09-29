# O mesmo professor do desafio anterior quer sortear a ordem da apresentação dos alunos. Faça um programa que leia o nome dos 4 alunos e mostre na tela os alunos sorteados em ordem

import random

aluno1 = 'Pedro'
aluno2 = 'Tiago'
aluno3 = 'Mateus'
aluno4 = 'Igor'

listaAlunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(listaAlunos)
print(f'Bom, tivemos um sorteio, e esses foram os sorteados em ordem: {listaAlunos}')

# TIVE QUE RECORRER A AJUDA DESSA VEZ...