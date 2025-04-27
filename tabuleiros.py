import pygame as pg
from settings import *

COR = (255,255,255)

TAM_CELULA = 40
LINS_TAB, COLS_TAB = 10, 10
DIST_TABS = 80
GROSSURA_TABS = 2

POS_TAB_01 = (115, 80)
POS_TAB_02 = (595, 80)


def desenhando_tabuleiros(tela):
    rect_pos_tab01 = []
    rect_pos_tab02 = []
    for linha in range(LINS_TAB):
        x = (linha * TAM_CELULA) + (LARGURA//2) - (TAM_CELULA * LINS_TAB/2)
        coluna_temp_01 = []
        coluna_temp_02 = []
        for coluna in range(COLS_TAB):
            y = (coluna * TAM_CELULA) + DIST_TABS
            
            pg.draw.rect(tela, COR, (x - (TAM_CELULA * LINS_TAB / 2) - DIST_TABS / 2, y, TAM_CELULA, TAM_CELULA), GROSSURA_TABS)
            pg.draw.rect(tela, COR, (x + (TAM_CELULA * LINS_TAB / 2) + DIST_TABS / 2, y, TAM_CELULA, TAM_CELULA), GROSSURA_TABS)
            
            coluna_temp_01.append((x - (TAM_CELULA * LINS_TAB / 2) - DIST_TABS/2, y))
            coluna_temp_02.append((x + (TAM_CELULA * LINS_TAB / 2) + DIST_TABS/2, y))
            
        rect_pos_tab01.append(coluna_temp_01)
        rect_pos_tab02.append(coluna_temp_02)
        
            
    return rect_pos_tab01, rect_pos_tab02
