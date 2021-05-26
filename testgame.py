import pygame


branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)

from time import sleep
from random import randint

pygame.init()
fundo=pygame.display.set_mode((680, 480))
largura=680
altura=480
tamanho=10
pos_x = randint(0, (largura - tamanho) / 10) * 10
pos_y = randint(0, (altura - tamanho) / 10) * 10
pygame.display.set_caption('Simurgh')
sleep(10)

sair=True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair=False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pos_x-=10
            if event.key == pygame.K_RIGHT:
                pos_x+=10
            if event.key == pygame.K_UP:
                pos_y-=10
            if event.key == pygame.K_DOWN:
                pos_y+=10
        print(event)
    fundo.fill(azul)
    pygame.draw.rect(fundo, preto,[pos_x, pos_y, tamanho,tamanho])
    pos_x+=0.1
    pygame.display.update()

pygame.quit()