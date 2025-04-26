import pygame as pg
import tabuleiros as tab
from settings import *


def posicionar_navios(evento, player, navio, mouse_pos_tab01, mouse_pos_tab02):
    colocado = False
    
    if evento.type == pg.MOUSEMOTION:
        if player == "1":
            if (0 <= mouse_pos_tab01[0] < tab.LINS_TAB) and (0 <= mouse_pos_tab01[1] < tab.COLS_TAB):
                if navio["nav"].rotacao == 90 and mouse_pos_tab01[0] >= tab.LINS_TAB - navio["tam"]:
                    print(mouse_pos_tab01)
                    navio["nav"].update((tab.POS_TAB_01[0] + (tab.TAM_CELULA * (tab.LINS_TAB-(navio["tam"]+1))), tab.POS_TAB_01[1] + (tab.TAM_CELULA * mouse_pos_tab01[1])))
                elif navio["nav"].rotacao == 0 and mouse_pos_tab01[1] >= tab.COLS_TAB - (navio["tam"]+1):
                    navio["nav"].update((tab.POS_TAB_01[0] + (tab.TAM_CELULA * mouse_pos_tab01[0]), tab.POS_TAB_01[1] + (tab.TAM_CELULA * (tab.COLS_TAB-(navio["tam"]+1)))))
                else:
                    navio["nav"].update((tab.POS_TAB_01[0] + (tab.TAM_CELULA * mouse_pos_tab01[0]), tab.POS_TAB_01[1] + (tab.TAM_CELULA * mouse_pos_tab01[1])))
        
        elif player == "2":
            if (0 <= mouse_pos_tab02[0] < tab.LINS_TAB) and (0 <= mouse_pos_tab02[1] < tab.COLS_TAB):
                if navio["nav"].rotacao == 90 and mouse_pos_tab02[0] >= tab.LINS_TAB - navio["tam"]:
                    print(mouse_pos_tab02)
                    navio["nav"].update((tab.POS_TAB_02[0] + (tab.TAM_CELULA * (tab.LINS_TAB-(navio["tam"]+1))), tab.POS_TAB_02[1] + (tab.TAM_CELULA * mouse_pos_tab02[1])))
                elif navio["nav"].rotacao == 0 and mouse_pos_tab02[1] >= tab.COLS_TAB - (navio["tam"]+1):
                    navio["nav"].update((tab.POS_TAB_02[0] + (tab.TAM_CELULA * mouse_pos_tab02[0]), tab.POS_TAB_02[1] + (tab.TAM_CELULA * (tab.COLS_TAB-(navio["tam"]+1)))))
                else:
                    navio["nav"].update((tab.POS_TAB_02[0] + (tab.TAM_CELULA * mouse_pos_tab02[0]), tab.POS_TAB_02[1] + (tab.TAM_CELULA * mouse_pos_tab02[1])))
                    
    if evento.type == pg.KEYDOWN:
        if evento.key == pg.K_z:
            navio["nav"].rotacionar()
        
        if evento.key == pg.K_c:
            navio["qtd"] -= 1
            colocado = True
                
    return navio, colocado
            


def atacar(evento, player, mouse_pos):
    pass


def trocar(evento, player, mouse_pos):
    pass