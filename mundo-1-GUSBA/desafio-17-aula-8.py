# Um professor quer sortear um dos seus 4 alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e mostrando na tela o nome do escolhido
import random
aluno1 = 'Pedro'
aluno2 = 'Tiago'
aluno3 = 'Mateus'
aluno4 = 'Igor'

alunos = aluno1, aluno2, aluno3, aluno4
alunoApagaQuadro = random.choice(alunos)
print(f'Na sala há 4 alunos a serem sorteados pelo professor para apagar o quadro, o nome deles é: {aluno1}, {aluno2}, {aluno3}, {aluno4}. Acabou que o\n sortudo da vez foi o {alunoApagaQuadro}')

# Concluido com sucesso!