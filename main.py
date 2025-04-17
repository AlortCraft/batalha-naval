import pygame as pg
import math
import pandas as pd
import cores, sprites
from pygame.locals import *
from sys import exit

#Tela
largura =  1110
altura = 1000
tela = pg.display.set_mode((largura, altura))

#Definindo relogio
relogio = pg.time.Clock()

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

#Criando sprites da agua e agrupando
agua = sprites.agua_sprite(largura, altura)

#Desenhando coluna e linhas
'''
def gradeTabuleiro(tela):
    for i in range(100,1001, 100):
        pg.draw.line(tela,cores.preto,(i,0), (i,1000), 3)
    for j in range(100,1001, 100):
        pg.draw.line(tela,cores.preto,(0,j), (1000,j), 3)
'''

#Jogo
rodando = True
while rodando:
    #Definindo FPS
    relogio.tick(60)
    for event in pg.event.get():
        if event.type == QUIT:
           rodando = False
           break
                   
#Desenhando a agua e atualizando sprites
agua.draw(tela)
agua.update()
                   
#Declarando variavel da posicao mouse        
    mouse = pg.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]
    print(mouse)
           
#Declarando variavel do click
    click = pg.mouse.get_pressed()
           
#JOGO
#gradeTabuleiro(tela)
           
#ULTIMA JOGADA
    if click[0]==1:
        click_last_status = 1
    else:
        click_last_status = 0

    pg.display.update()
pg.quit()
