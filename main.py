import pygame as pg
import math
import pandas as pd
import cores, player
import sprites as spr, tabuleiros as tab, cenas as cn
from settings import *
from pygame.locals import *
from sys import exit


def main():
    #Tela / Titulo da Tela / Icone da Tela
    tela = pg.display.set_mode((LARGURA, ALTURA))
    pg.display.set_caption("Batalha Naval")
    pg.display.set_icon(pg.image.load("sprites/naval_icon.png"))
    
    camada1 = pg.Surface((LARGURA, ALTURA))

    #Definindo relogio
    relogio = pg.time.Clock()
    
    #variaveis com as posicoes dos tabuleiros
    tab01, tab02 = tab.desenhando_tabuleiros(tela)

    #Valores
    ultimoStatus = 0
    CliqueFora= 0

    click_position_x = -1
    click_position_y = -1

    X_or_O_turn = 'x'

    end_game = 0
    
    #Background do jogo
    agua_spr, agua_tam = spr.agua_spr()
    tile_agua = pg.sprite.Group()
    for x in range(0, LARGURA, agua_tam[0]):
        index = x // agua_tam[0] % len(agua_spr)
        for y in range(0, ALTURA, agua_tam[1]):
            agua_atual = spr.Agua(agua_spr, index, (x, y), 500)
            tile_agua.add(agua_atual)
            
            
    #criando sprites dos navios
    navios = spr.navios_spr()
    quant_navios = {
        'tm_4': 1,
        'tm_3': 2,
        'tm_2': 3,
        'tm_1': 4,
    }
    

    #tabuleiro oculto
    tabuleiro_oculto_1 =  [["" for i in range(tab.LINS_TAB)] for i in range(tab.COLS_TAB)]
    tabuleiro_oculto_2 =  [["" for i in range(tab.LINS_TAB)] for i in range(tab.COLS_TAB)]
    
    #Marcando tabuleiro
    marcacoes_tab01 = []
    marcacoes_tab02 = []
    
    #Navios
    navio_com_mouse = pg.sprite.Group()
    
    navios_tab01 = pg.sprite.Group()
    navios_tab02 = pg.sprite.Group()
        
    navios_obj = [
        {
        "nav" : spr.Navios(navios["tm_4"]),
        "tam" : 4,
        "qtd" : 1
        },
        {
        "nav" : spr.Navios(navios["tm_3"]),
        "tam" : 3,
        "qtd" : 2
        },
        {
        "nav" : spr.Navios(navios["tm_2"]),
        "tam" : 2,
        "qtd" : 3
        },
        {
        "nav" : spr.Navios(navios["tm_1"]),
        "tam" : 1,
        "qtd" : 4
        }
    ]
    
    navio_atual = navios_obj[0]
    index_nav = 0
    navio_com_mouse.add(navio_atual["nav"])
    
    
    
    
    #Jogo
    cena_atual = "menu" #Cenas: menu / jogo / troca
    status_jogo = "posicionar" #Status: posicionar / atacar
    player_atual = "1"
    rodando = True
    while rodando:
        #Definindo FPS
        relogio.tick(FPS)
        
        #Declarando variavel da posicao mouse        
        mouse = pg.mouse.get_pos()
        mouse_pos_x, mouse_pos_y = mouse
        #print(mouse)
        
        mouse_pos_tab01_x = (mouse_pos_x - tab.POS_TAB_01[0]) // tab.TAM_CELULA
        mouse_pos_tab01_y = (mouse_pos_y - tab.POS_TAB_01[1]) // tab.TAM_CELULA
            
        mouse_pos_tab02_x = (mouse_pos_x - tab.POS_TAB_02[0]) // tab.TAM_CELULA
        mouse_pos_tab02_y = (mouse_pos_y - tab.POS_TAB_02[1]) // tab.TAM_CELULA
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
                break
            if cena_atual == "jogo":
                if status_jogo == "posicionar":
                    navio_atual, navio_colodado = player.posicionar_navios(event, player_atual, navio_atual, (mouse_pos_tab01_x, mouse_pos_tab01_y), (mouse_pos_tab02_x, mouse_pos_tab02_y))
                    if navio_colodado:
                        
                        if player_atual == "1":
                            navios_tab01.add(navio_atual["nav"])
                        elif player_atual == "2":
                            navios_tab02.add(navio_atual["nav"])
                            
                            
                        if navio_atual["qtd"] == 0:
                            index_nav += 1
                            navio_com_mouse.empty()
                            
                            if index_nav == 4:
                                if player_atual == "1":
                                    player_atual = "2"
                                    index_nav = 0
                                    
                                    navios_obj = [
                                        {
                                        "nav" : spr.Navios(navios["tm_4"]),
                                        "tam" : 4,
                                        "qtd" : 1
                                        },
                                        {
                                        "nav" : spr.Navios(navios["tm_3"]),
                                        "tam" : 3,
                                        "qtd" : 2
                                        },
                                        {
                                        "nav" : spr.Navios(navios["tm_2"]),
                                        "tam" : 2,
                                        "qtd" : 3
                                        },
                                        {
                                        "nav" : spr.Navios(navios["tm_1"]),
                                        "tam" : 1,
                                        "qtd" : 4
                                        }
                                    ]
                                    
                                    navio_atual = navios_obj[index_nav]
                                    navio_com_mouse.add(navio_atual["nav"])
                                else:
                                    status_jogo = "atacar"
            
                            else:
                                navio_atual = navios_obj[index_nav]
                                navio_com_mouse.add(navio_atual["nav"])
                            
                            
                            
                
                                    
                elif status_jogo == "atacar":
                    pass
                '''     
                #atacando        
                elif status_jogo == "atacar":
                    if player_atual == "1":
                        if (0 <= mouse_pos_tab02_x < tab.LINS_TAB) and (0 <= mouse_pos_tab02_y < tab.COLS_TAB):
                            if (tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][0], tab01[mouse_pos_tab02_x][mouse_pos_tab02_y][1], tab.TAM_CELULA, tab.TAM_CELULA) not in marcacoes_tab02:
                                marcacoes_tab01.append((tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][0], tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][1], tab.TAM_CELULA, tab.TAM_CELULA))
                                    
                    elif player_atual == "2":
                        if (0 <= mouse_pos_tab01_x < tab.LINS_TAB) and (0 <= mouse_pos_tab01_y < tab.COLS_TAB):
                            if (tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][0], tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][1], tab.TAM_CELULA, tab.TAM_CELULA) not in marcacoes_tab01:
                                    marcacoes_tab01.append((tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][0], tab01[mouse_pos_tab02_x][mouse_pos_tab01_y][1], tab.TAM_CELULA, tab.TAM_CELULA))

                    '''            
                
        tile_agua.draw(tela)
        tile_agua.update()
        
        
        if cena_atual == "menu":
            cena_atual = cn.menu_inicial(tela, mouse_pos_x, mouse_pos_y)
        elif cena_atual == "jogo":
            tab.desenhando_tabuleiros(tela)
            
            if status_jogo == "posicionar":
                navio_com_mouse.draw(tela)
                navios_tab01.draw(tela)
                navios_tab02.draw(tela)
                
            
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
                
            cn.jogo(tela, mouse_pos_x, mouse_pos_y, navios)
            
        elif cena_atual == "troca":
            cn.tela_troca_player(tela)
            
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