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
    tabuleiro_oculto_1 =  [["" for i in range(tabuleiros.LINS_TAB)] for i in range(tabuleiros.COLS_TAB)]
    tabuleiro_oculto_2 =  [["" for i in range(tabuleiros.LINS_TAB)] for i in range(tabuleiros.COLS_TAB)]
    
    #variaveis com as posicoes dos tabuleiros
    tab01, tab02 = tabuleiros.desenhando_tabuleiros(tela)

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
    quant_navios = {
        'tm_4': 1,
        'tm_3': 2,
        'tm_2': 3,
        'tm_1': 4,
    }
    
    #Marcando tabuleiro
    marcacoes_tab01 = []
    marcacoes_tab02 = []
    
    

    #Jogo
    cena_atual = "jogo" #Cenas: menu / jogo / troca
    status_jogo = "atacar" #Status: posicionar / atacar
    player_atual = "1"
    
    
    rodando = True
    while rodando:
        #Definindo FPS
        relogio.tick(FPS)
        
        #Declarando variavel da posicao mouse        
        mouse = pg.mouse.get_pos()
        mouse_pos_x, mouse_pos_y = mouse
        #print(mouse)
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if cena_atual == "jogo":
                    mouse_pos_tab01_x = (mouse_pos_x - tabuleiros.POS_TAB_01[0]) // tabuleiros.TAM_CELULA
                    mouse_pos_tab01_y = (mouse_pos_y - tabuleiros.POS_TAB_01[1]) // tabuleiros.TAM_CELULA
                    
                    mouse_pos_tab02_x = (mouse_pos_x - tabuleiros.POS_TAB_02[0]) // tabuleiros.TAM_CELULA
                    mouse_pos_tab02_y = (mouse_pos_y - tabuleiros.POS_TAB_02[1]) // tabuleiros.TAM_CELULA
                    
                    
                    #posicionando pecas
                    if status_jogo == "posicionar":
                        pass
                    #atacando
                    elif status_jogo == "atacar":
                        if player_atual == "1":
                            if (0 <= mouse_pos_tab02_x < tabuleiros.LINS_TAB) and (0 <= mouse_pos_tab02_y < tabuleiros.COLS_TAB):
                                if pg.mouse.get_pressed()[0] == 1 and (tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][0], tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][1], tabuleiros.TAM_CELULA, tabuleiros.TAM_CELULA) not in marcacoes_tab02:
                                    print("MARCADO 2!")
                                    marcacoes_tab02.append((tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][0], tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][1], tabuleiros.TAM_CELULA, tabuleiros.TAM_CELULA))
                        if player_atual == "2":
                            if (0 <= mouse_pos_tab01_x < tabuleiros.LINS_TAB) and (0 <= mouse_pos_tab01_y < tabuleiros.COLS_TAB):
                                if pg.mouse.get_pressed()[0] == 1 and (tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][0], tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][1], tabuleiros.TAM_CELULA, tabuleiros.TAM_CELULA) not in marcacoes_tab01:
                                    print("MARCADO 1!")
                                    marcacoes_tab01.append((tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][0], tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][1], tabuleiros.TAM_CELULA, tabuleiros.TAM_CELULA))
                
                
        

        
        sprites.anim_constante(tela, agua_spr, agua_tile)
        
        if cena_atual == "menu":
            cena_atual = cenas.menu_inicial(tela, mouse_pos_x, mouse_pos_y)
        elif cena_atual == "jogo":
            tabuleiros.desenhando_tabuleiros(tela)
            
            if status_jogo == "posicionar":
                pass
            
            elif status_jogo == "atacar":
                #desenhando marcacoes
                for marcacao in marcacoes_tab01:
                    x, y, w, h = marcacao
                    pg.draw.line(tela, (0, 0, 255), (x, y), (x + w, y + h), 3) # Linha \
                    pg.draw.line(tela, (0, 0, 255), (x + w, y), (x, y + h), 3) # Linha /

                for marcacao in marcacoes_tab02:
                    x, y, w, h = marcacao
                    pg.draw.line(tela, (0, 0, 255), (x, y), (x + w, y + h), 3)
                    pg.draw.line(tela, (0, 0, 255), (x + w, y), (x, y + h), 3)
                
            cenas.jogo(tela, mouse_pos_x, mouse_pos_y, navios)
            
        elif cena_atual == "troca":
            cenas.tela_troca_player(tela)
            
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