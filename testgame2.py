import pygame
from random import randint

branco = (255, 255, 255)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
verde = (46, 139, 87)
azul = (0, 0, 255)

try:
    pygame.init()
except:
    print('O modulo pygame não foi iniciado com sucesso!')

largura = 640
altura = 480
tamanho = 10
pos_x = randint(0, (largura - tamanho) / 10) * 10
pos_y = randint(0, (altura - tamanho) / 10) * 10
velocidade_x = 0
velocidade_y = 0

fundo = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Simurgh')

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                velocidade_y = 0
                velocidade_x = - 0.1
            if event.key == pygame.K_RIGHT:
                velocidade_y = 0
                velocidade_x = + 0.1
            if event.key == pygame.K_UP:
                velocidade_x = 0
                velocidade_y = - 0.1
            if event.key == pygame.K_DOWN:
                velocidade_x = 0
                velocidade_y = + 0.1

    fundo.fill(preto)
    pygame.draw.rect(fundo, verde, [pos_x, pos_y, tamanho, tamanho])
    pos_x += velocidade_x
    pos_y += velocidade_y
    pygame.display.update()

pygame.quit()