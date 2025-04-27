import pygame as pg
import tabuleiros as tab
from settings import *


def movimentar_navios(evento, player, navio_spr, navio_atual, index_navio, qt_nav_j1, qt_nav_j2):
    colocado = False
    tab_pos = None
    qt_nav = None
    
    if player == "1":
        tab_pos = tab.POS_TAB_01
        qt_nav = qt_nav_j1
    elif player == "2":
        tab_pos = tab.POS_TAB_02
        qt_nav = qt_nav_j2
    
    if evento.key == pg.K_1 and qt_nav[0] > 0:
        navio_atual = navio_spr["tm_1"]
        navio_atual["pos"] = [tab_pos[0], tab_pos[1]]
        index_navio = 0
    
    elif evento.key == pg.K_2 and qt_nav[1] > 0:
        navio_atual = navio_spr["tm_2"]
        navio_atual["pos"] = [tab_pos[0], tab_pos[1]]
        index_navio = 1
    
    elif evento.key == pg.K_3 and qt_nav[2] > 0:
        navio_atual = navio_spr["tm_3"]
        navio_atual["pos"] = [tab_pos[0], tab_pos[1]]
        index_navio = 2
    
    elif evento.key == pg.K_4 and qt_nav[3] > 0:
        navio_atual = navio_spr["tm_4"]
        navio_atual["pos"] = [tab_pos[0], tab_pos[1]]
        index_navio = 3
        
    if navio_atual != None:
        ship_andando = pg.mixer.Sound("sound_effects/ship_walk.wav")
        
        if evento.key == pg.K_RIGHT:
            if ( (navio_atual["pos"][0] - tab_pos[0]) // tab.TAM_CELULA ) + 1 <  tab.COLS_TAB - ((navio_atual["num_cel"] - 1) * (navio_atual["rotacao"] == 90)):
                navio_atual["pos"][0] += tab.TAM_CELULA
                ship_andando.play(0)
        
        elif evento.key == pg.K_LEFT:
            if (navio_atual["pos"][0] - tab_pos[0]) // tab.TAM_CELULA > 0:
                navio_atual["pos"][0] -= tab.TAM_CELULA
                ship_andando.play(0)
        
        elif evento.key == pg.K_UP:
            if (navio_atual["pos"][1] - tab_pos[1]) // tab.TAM_CELULA > 0:
                navio_atual["pos"][1] -= tab.TAM_CELULA
                ship_andando.play(0)
        
        elif evento.key == pg.K_DOWN:
            if ( (navio_atual["pos"][1] - tab_pos[1]) // tab.TAM_CELULA ) + 1 < tab.LINS_TAB - ((navio_atual["num_cel"] - 1) * (navio_atual["rotacao"] == 0)):
                navio_atual["pos"][1] += tab.TAM_CELULA
                ship_andando.play(0)
                
                
        if evento.key == pg.K_z:
            if (navio_atual["rotacao"] == 0 and ((navio_atual["pos"][0] - tab_pos[0]) // tab.TAM_CELULA) < (tab.COLS_TAB - (navio_atual["num_cel"] - 1))):
                navio_atual["rotacao"] = (navio_atual["rotacao"] + 90) % 180
                navio_atual["sprite"] = pg.transform.rotate(navio_atual["sprite"], 90)
                ship_andando.play(0)
                
            elif (navio_atual["rotacao"] == 90 and ((navio_atual["pos"][1] - tab_pos[1]) // tab.TAM_CELULA) < (tab.LINS_TAB - (navio_atual["num_cel"] - 1))):
                navio_atual["rotacao"] = (navio_atual["rotacao"] + 90) % 180
                navio_atual["sprite"] = pg.transform.rotate(navio_atual["sprite"], 90)
                ship_andando.play(0)
                
            
        if evento.key == pg.K_c:
            colocado = True
        
    
    return navio_atual, colocado, index_navio
    
    
def atacar(player, tab01, tab02, mouse_pos_tab01, mouse_pos_tab02, marcacoes_tab01, marcacoes_tab02):
    marcacao = None
    if player == "1":
        if (0 <= mouse_pos_tab02[0] < tab.LINS_TAB) and (0 <= mouse_pos_tab02[1] < tab.COLS_TAB):
            if (tab02[mouse_pos_tab02[0]][mouse_pos_tab02[1]][0], tab01[mouse_pos_tab02[0]][mouse_pos_tab02[1]][1], tab.TAM_CELULA, tab.TAM_CELULA) not in marcacoes_tab02:
                marcacao = (tab02[mouse_pos_tab02[0]][mouse_pos_tab02[1]][0], tab02[mouse_pos_tab02[0]][mouse_pos_tab02[1]][1], tab.TAM_CELULA, tab.TAM_CELULA)
                    
    elif player == "2":
        if (0 <= mouse_pos_tab01[0] < tab.LINS_TAB) and (0 <= mouse_pos_tab01[1] < tab.COLS_TAB):
            if (tab01[mouse_pos_tab01[0]][mouse_pos_tab01[1]][0], tab01[mouse_pos_tab01[0]][mouse_pos_tab01[1]][1], tab.TAM_CELULA, tab.TAM_CELULA) not in marcacoes_tab01:
                marcacao = (tab01[mouse_pos_tab01[0]][mouse_pos_tab01[1]][0], tab01[mouse_pos_tab01[0]][mouse_pos_tab01[1]][1], tab.TAM_CELULA, tab.TAM_CELULA)
                
                
    return marcacao
            