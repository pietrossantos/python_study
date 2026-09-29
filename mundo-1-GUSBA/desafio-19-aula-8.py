# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3

import pygame
import time

pygame.init()
pygame.mixer.music.load('jazz.mp3')
pygame.mixer.music.play()
#input('Pressione ENTER para parar a música...')
while pygame.mixer.music.get_busy():
    time.sleep(1)

# Necessário recorrer a ajuda!