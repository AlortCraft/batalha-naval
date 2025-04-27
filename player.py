import pygame as pg
import tabuleiros as tab
from settings import *


def posicionar_navios(evento, player, navio):
    colocado = False
    if evento.key == pg.K_RIGHT:
        if player == "1":
            if navio.rotacao == 90 and (navio.pos[0] - tab.POS_TAB_01[0]) // tab.TAM_CELULA < (tab.COLS_TAB - (navio.num_cel)):
                navio.pos[0] += tab.TAM_CELULA
                    
            elif navio.rotacao == 0 and (navio.pos[0] - tab.POS_TAB_01[0]) // tab.TAM_CELULA < tab.COLS_TAB-1:
                navio.pos[0] += tab.TAM_CELULA
                
                
        elif player == "2":
            if navio.rotacao == 90 and (navio.pos[0] - tab.POS_TAB_02[0]) // tab.TAM_CELULA < (tab.COLS_TAB - (navio.num_cel)):
                navio.pos[0] += tab.TAM_CELULA
                    
            elif navio.rotacao == 0 and (navio.pos[0] - tab.POS_TAB_02[0]) // tab.TAM_CELULA < tab.COLS_TAB-1:
                navio.pos[0] += tab.TAM_CELULA
                
    elif evento.key == pg.K_LEFT:
        if player == "1":
            if navio.rotacao == 90 and (navio.pos[0] - tab.POS_TAB_01[0]) // tab.TAM_CELULA > 0:
                navio.pos[0] -= tab.TAM_CELULA
                    
            elif navio.rotacao == 0 and (navio.pos[0] - tab.POS_TAB_01[0]) // tab.TAM_CELULA > 0:
                navio.pos[0] -= tab.TAM_CELULA
                
                
        elif player == "2":
            if navio.rotacao == 90 and (navio.pos[0] - tab.POS_TAB_02[0]) // tab.TAM_CELULA > 0:
                navio.pos[0] -= tab.TAM_CELULA
                    
            elif navio.rotacao == 0 and (navio.pos[0] - tab.POS_TAB_02[0]) // tab.TAM_CELULA > 0:
                navio.pos[0] -= tab.TAM_CELULA
    
    if evento.key == pg.K_UP:
        if player == "1":
            if navio.rotacao == 90 and (navio.pos[1] - tab.POS_TAB_01[1]) // tab.TAM_CELULA > 0:
                navio.pos[1] -= tab.TAM_CELULA
                    
            elif navio.rotacao == 0 and (navio.pos[1] - tab.POS_TAB_01[1]) // tab.TAM_CELULA > 0:
                navio.pos[1] -= tab.TAM_CELULA
                
                
        elif player == "2":
            if navio.rotacao == 90 and (navio.pos[1] - tab.POS_TAB_02[1]) // tab.TAM_CELULA > 0:
                navio.pos[1] -= tab.TAM_CELULA
                    
            elif navio.rotacao == 0 and (navio.pos[1] - tab.POS_TAB_02[1]) // tab.TAM_CELULA > 0:
                navio.pos[1] -= tab.TAM_CELULA
    
    elif evento.key == pg.K_DOWN:
        if player == "1":
            if navio.rotacao == 90 and (navio.pos[1] - tab.POS_TAB_01[1]) // tab.TAM_CELULA < tab.LINS_TAB -1:
                navio.pos[1] += tab.TAM_CELULA
                    
            elif navio.rotacao == 0 and (navio.pos[1] - tab.POS_TAB_01[1]) // tab.TAM_CELULA < (tab.LINS_TAB - navio.num_cel):
                navio.pos[1] += tab.TAM_CELULA
                
                
        elif player == "2":
            if navio.rotacao == 90 and (navio.pos[1] - tab.POS_TAB_02[1]) // tab.TAM_CELULA < tab.LINS_TAB -1:
                navio.pos[1] += tab.TAM_CELULA
                    
            elif navio.rotacao == 0 and (navio.pos[1] - tab.POS_TAB_02[1]) // tab.TAM_CELULA < (tab.LINS_TAB - navio.num_cel):
                navio.pos[1] += tab.TAM_CELULA
                    

    if evento.key == pg.K_z:
        navio.rotacionar()
    
    if evento.key == pg.K_c:
        colocado = True
            
    return navio, colocado
            


def atacar(evento, player, mouse_pos):
    pass


def trocar(evento, player, mouse_pos):
    pass