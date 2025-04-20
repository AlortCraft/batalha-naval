import pygame as pg
import math
import pandas as pd
import cores, sprites, tabuleiros, cenas
from settings import *
from pygame.locals import *
from sys import exit


def main():
    #Tela / Titulo da Tela / Icone da Tela
    tela = pg.display.set_mode((LARGURA, ALTURA))
    pg.display.set_caption("Batalha Naval")
    pg.display.set_icon(pg.image.load("sprites/naval_icon.png"))

    #Definindo relogio
    relogio = pg.time.Clock()

    #tabuleiro oculto
    tabuleiro_oculto =  [["" for i in range(tabuleiros.LINS_TAB)] for i in range(tabuleiros.COLS_TAB)]

    #Valores
    ultimoStatus = 0
    CliqueFora= 0

    click_position_x = -1
    click_position_y = -1

    X_or_O_turn = 'x'

    end_game = 0
    
    #Background do jogo
    agua_spr, agua_tile = sprites.agua_spr_tile(tela)
    
    #criando sprites dos navios
    navios = sprites.navios_spr()

    #Jogo
    cena_atual = "menu"
    troca_jogador = False
    player_ganhador = 0
    rodando = True
    while rodando:
        #Definindo FPS
        relogio.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                print("Clicou")
        
        if cena_atual == "menu":
            pass         
        
        
                        
        #Declarando variavel da posicao mouse        
        mouse = pg.mouse.get_pos()
        mouse_pos_x, mouse_pos_y = mouse
        
        sprites.anim_constante(tela, agua_spr, agua_tile)
        
        if cena_atual == "menu":
            cena_atual = cenas.menu_inicial(tela, mouse_pos_x, mouse_pos_y)
        elif cena_atual == "jogo":
            cenas.jogo(tela, mouse_pos_x, mouse_pos_y, navios)
        elif cena_atual == "sair":
            run = False
            break
                
        #Declarando variavel do click
        click = pg.mouse.get_pressed()
        
        #ULTIMA JOGADA
        if click[0]==1:
            click_last_status = 1
        else:
            click_last_status = 0
        

        pg.display.update()
    pg.quit()
    


if __name__ == "__main__":
    main()