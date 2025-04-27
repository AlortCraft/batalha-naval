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
    

    #tabuleiro oculto
    tabuleiro_oculto_1 =  [["" for i in range(tab.LINS_TAB)] for i in range(tab.COLS_TAB)]
    tabuleiro_oculto_2 =  [["" for i in range(tab.LINS_TAB)] for i in range(tab.COLS_TAB)]
    
    #Marcando tabuleiro
    marcacoes_tab01 = []
    marcacoes_tab02 = []
    
    #criando sprites dos navios
    navios = spr.navios_spr()
    
    #Navios
    navio_atual_ = pg.sprite.Group()
    
    navios_tab01 = pg.sprite.Group()
    navios_tab02 = pg.sprite.Group()
   
    quant_navios_j1 = [4,3,2,1]
    quant_navios_j2 = [4,3,2,1]
    
    navio_atual = None
    index_navio_atual = 0
    posicao_livre = True
    #navio_com_mouse.add(navio_atual["nav"])
    r, g, b = 100, 200, 300
    ultimo_update = 0
    
    #Jogo
    cena_atual = "jogo" #Cenas: menu / jogo / troca
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
                    if event.type == pg.KEYDOWN:
                        if event.key == pg.K_1:
                            navio_atual_.empty()
                            
                            if player_atual == "1" and quant_navios_j1[0] > 0:
                                navio_atual = spr.Navios(navios["tm_1"], 1, [tab.POS_TAB_01[0], tab.POS_TAB_01[1]])
                                index_navio_atual = 0
                                navio_atual_.add(navio_atual)
                            elif player_atual == "2" and quant_navios_j2[0] > 0:
                                navio_atual = spr.Navios(navios["tm_1"], 1, [tab.POS_TAB_02[0], tab.POS_TAB_02[1]])
                                index_navio_atual = 0
                                navio_atual_.add(navio_atual)
                                
                                
                            
                            
                        if event.key == pg.K_2:
                            navio_atual_.empty()
                            
                            if player_atual == "1" and quant_navios_j1[1] > 0:
                                navio_atual = spr.Navios(navios["tm_2"], 2, [tab.POS_TAB_01[0], tab.POS_TAB_01[1]])
                                index_navio_atual = 1
                                navio_atual_.add(navio_atual)
                            elif player_atual == "2" and quant_navios_j2[1] > 0:
                                navio_atual = spr.Navios(navios["tm_2"], 2, [tab.POS_TAB_02[0], tab.POS_TAB_02[1]])
                                index_navio_atual = 1
                                navio_atual_.add(navio_atual)
                            
                            
                                    
                        if event.key == pg.K_3:
                            navio_atual_.empty()
                            
                            if player_atual == "1" and quant_navios_j1[2] > 0:
                                navio_atual = spr.Navios(navios["tm_3"], 3, [tab.POS_TAB_01[0], tab.POS_TAB_01[1]])
                                index_navio_atual = 2
                                navio_atual_.add(navio_atual)
                            elif player_atual == "2" and quant_navios_j2[2] > 0:
                                navio_atual = spr.Navios(navios["tm_3"], 3, [tab.POS_TAB_02[0], tab.POS_TAB_02[1]])
                                index_navio_atual = 2
                                navio_atual_.add(navio_atual)
                                    
                        if event.key == pg.K_4:
                            navio_atual_.empty()
                            
                            if player_atual == "1" and quant_navios_j1[3] > 0:
                                navio_atual = spr.Navios(navios["tm_4"], 4, [tab.POS_TAB_01[0], tab.POS_TAB_01[1]])
                                index_navio_atual = 3
                                navio_atual_.add(navio_atual)
                            elif player_atual == "2" and quant_navios_j2[3] > 0:
                                navio_atual = spr.Navios(navios["tm_4"], 4, [tab.POS_TAB_02[0], tab.POS_TAB_02[1]])
                                index_navio_atual = 3
                                navio_atual_.add(navio_atual)
                            
                    
                        if navio_atual != None:
                            navio_atual, navio_colocado = player.posicionar_navios(event, player_atual, navio_atual)
                            navio_atual_.update()
                            if navio_colocado:
                                if player_atual == "1":
                                    pos_tab_tempX = (navio_atual.pos[0] - tab.POS_TAB_01[0])//tab.TAM_CELULA
                                    pos_tab_tempY = (navio_atual.pos[1] - tab.POS_TAB_01[1])//tab.TAM_CELULA
                                    if navio_atual.rotacao == 0:
                                        for y in range(pos_tab_tempX, pos_tab_tempX + navio_atual.num_cel):
                                            tabuleiro_oculto_1[pos_tab_tempX-1][y-1] = "n"
                                        
                                    elif navio_atual.rotacao == 90:
                                        for x in range(pos_tab_tempY, pos_tab_tempY + navio_atual.num_cel):
                                            tabuleiro_oculto_1[x-1][pos_tab_tempY-1] = "n"
                                            
                                    navios_tab01.add(navio_atual)
                                    
                                    quant_navios_j1[index_navio_atual] -= 1
                                    
                                    if quant_navios_j1[index_navio_atual] >= 0:
                                        navio_atual = None
                                    if sum(quant_navios_j1) == 0:
                                        navio_atual = None
                                        player_atual = "2"
                                        cena_atual = "troca"
                                        
                                    
                                elif player_atual == "2":
                                    pos_tab_tempX = (navio_atual.pos[0] - tab.POS_TAB_02[0]) // tab.TAM_CELULA
                                    pos_tab_tempY = (navio_atual.pos[1] - tab.POS_TAB_02[1]) // tab.TAM_CELULA
                                    if navio_atual.rotacao == 0:
                                        for x in range(pos_tab_tempX, pos_tab_tempX + navio_atual.num_cel):
                                            tabuleiro_oculto_2[x-1][pos_tab_tempY] = "n"
                                        navios_tab02.add(navio_atual)
                                        quant_navios_j2[index_navio_atual] -= 1
                                        
                                    elif navio_atual.rotacao == 90:
                                        for y in range(pos_tab_tempY, pos_tab_tempY + navio_atual.num_cel):
                                            tabuleiro_oculto_2[pos_tab_tempX][y-1] = "n"
                                        navios_tab02.add(navio_atual)
                                        quant_navios_j2[index_navio_atual] -= 1
                                            
                                    
                                    
                                    if quant_navios_j2[index_navio_atual] >= 0:
                                        navio_atual = None
                                    elif sum(quant_navios_j2) == 0:
                                        navio_atual = None
                                        
                                        player_atual = "1"
                                        status_jogo = "atacar"
                                        cena_atual = "troca"
                            
                        
                if status_jogo == "atacar":
                    if event.type == pg.MOUSEBUTTONDOWN:
                        #atacando        
                        if player_atual == "1":
                            if (0 <= mouse_pos_tab02_x < tab.LINS_TAB) and (0 <= mouse_pos_tab02_y < tab.COLS_TAB):
                                if (tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][0], tab01[mouse_pos_tab02_x][mouse_pos_tab02_y][1], tab.TAM_CELULA, tab.TAM_CELULA) not in marcacoes_tab02:
                                    marcacoes_tab01.append((tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][0], tab02[mouse_pos_tab02_x][mouse_pos_tab02_y][1], tab.TAM_CELULA, tab.TAM_CELULA))
                                        
                        elif player_atual == "2":
                            if (0 <= mouse_pos_tab01_x < tab.LINS_TAB) and (0 <= mouse_pos_tab01_y < tab.COLS_TAB):
                                if (tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][0], tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][1], tab.TAM_CELULA, tab.TAM_CELULA) not in marcacoes_tab01:
                                    marcacoes_tab01.append((tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][0], tab01[mouse_pos_tab01_x][mouse_pos_tab01_y][1], tab.TAM_CELULA, tab.TAM_CELULA)) 
                                    
                    
            elif cena_atual == "troca":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        cena_atual = "jogo"        
                
        tile_agua.draw(tela)
        tile_agua.update()
        
        
        if cena_atual == "menu":
            cena_atual = cn.menu_inicial(tela, mouse_pos_x, mouse_pos_y)
        elif cena_atual == "jogo":
            tab.desenhando_tabuleiros(tela)
            
            if status_jogo == "posicionar":
                navio_atual_.draw(tela)
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
            
        elif cena_atual == "fim":
            agora = pg.time.get_ticks()
            if (agora - ultimo_update) >= agora:
                ultimo_update = agora
                r += r % 255
                g += g % 255
                b += b % 255
                cor = (r,g,b)
                cn.tela_fim_de_jogo(tela, player_atual, cor)
            
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