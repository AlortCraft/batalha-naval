import pygame as pg
import math
import pandas as pd
from pygame.locals import *
from sys import exit


#Cores
preto = (0,0,0)
branco = (255,255,255)
vermelho = (255,0,0)
verde = (0,255,0)
azul = (0,0,165)
cinza = (150,150,150)

#Tela
largura =  1110
altura = 1000
tela = pg.display.set_mode((largura, altura))
tela.fill(azul)

#Fonte
pg.font.init()
fonte= pg.font.SysFont("Comic Sans MS",30)

#QUADRO
quadro =  [['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n'],
           ['n','n','n','n','n','n','n','n','n','n']]

#Valores
ultimoStatus = 0
CliqueFora= 0

click_position_x = -1
click_position_y = -1

X_or_O_turn = 'x'

end_game = 0
#Desenhando coluna e linhas
def gradeTabuleiro(tela):
    pg.draw.line(tela,preto,(100,0), (100,1000), 3)
    pg.draw.line(tela,preto,(200,0), (200,1000), 3)
    pg.draw.line(tela,preto,(300,0), (300,1000), 3)
    pg.draw.line(tela,preto,(400,0), (400,1000), 3)
    pg.draw.line(tela,preto,(500,0), (500,1000), 3)
    pg.draw.line(tela,preto,(600,0), (600,1000), 3)
    pg.draw.line(tela,preto,(700,0), (700,1000), 3)
    pg.draw.line(tela,preto,(800,0), (800,1000), 3)
    pg.draw.line(tela,preto,(900,0), (900,1000), 3)
    pg.draw.line(tela,preto,(1000,0), (1000,1000), 3)
    pg.draw.line(tela,preto,(0,100), (1000,100), 3)
    pg.draw.line(tela,preto,(0,200), (1000,200), 3)
    pg.draw.line(tela,preto,(0,300), (1000,300), 3)
    pg.draw.line(tela,preto,(0,400), (1000,400), 3)
    pg.draw.line(tela,preto,(0,500), (1000,500), 3)
    pg.draw.line(tela,preto,(0,600), (1000,600), 3)
    pg.draw.line(tela,preto,(0,700), (1000,700), 3)
    pg.draw.line(tela,preto,(0,800), (1000,800), 3)
    pg.draw.line(tela,preto,(0,900), (1000,900), 3)
    pg.draw.line(tela,preto,(0,1000), (1000,1000), 3)
#Jogo
while True:
    for event in pg.event.get():
        if event.type == QUIT:
            p = 0
            pg.quit()
            exit()
#Declarando variavel da posicao mouse        
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]
    print(mouse)
#Declarando variavel do click
    click = pg.mouse.get_pressed()
#JOGO
    gradeTabuleiro(tela)
#ULTIMA JOGADA
    if click[0]==1:
        click_last_status = 1
    else:
        click_last_status = 0

    pg.display.update()