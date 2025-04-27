import pygame as pg
import sprites as spr
import tabuleiros as tab
from settings import *


def menu_inicial(tela_, mouse_x, mouse_y):
    titulo = FONTES["titulo menu_inicial"].render("BATALHA NAVAL", 1, (0,0,0))
    titulo_rect = titulo.get_rect()
    titulo_rect.center = (LARGURA/2, 250)
    
    
    botao_jogar = FONTES["botoes menu_inicial"].render("JOGAR", 1, (0,0,0))
    botao_jogar_rect = botao_jogar.get_rect()
    botao_jogar_rect.center = (LARGURA/2, 400)

    botao_sair = FONTES["botoes menu_inicial"].render("SAIR", 1, (0,0,0))
    botao_sair_rect = botao_sair.get_rect()
    botao_sair_rect.center = (LARGURA/2, 500)
    
    colid_jogar = botao_jogar_rect.collidepoint(mouse_x, mouse_y)
    colid_sair = botao_sair_rect.collidepoint(mouse_x, mouse_y)
        
    if colid_jogar:
        botao_jogar = FONTES["botoes menu_inicial"].render("JOGAR", 1, (100,100,100))
        if pg.mouse.get_pressed()[0] == 1:
            return "jogo"
 
    if colid_sair:
        botao_sair = FONTES["botoes menu_inicial"].render("SAIR", 1, (100,100,100))
        if pg.mouse.get_pressed()[0] == 1:
            return "sair"
        
        
    tela_.blit(titulo, titulo_rect)
    tela_.blit(botao_jogar, botao_jogar_rect)
    tela_.blit(botao_sair, botao_sair_rect)
                
    return "menu"
    
    
    
    

def jogo(tela_, player, status):
    

    player1 = FONTES["titulo menu_jogo"].render("PLAYER 1", 1, (0, 0, 0))
    player2 = FONTES["titulo menu_jogo"].render("PLAYER 2", 1, (0, 0, 0))
    
    tela_.blit(player1, (tab.POS_TAB_01[0] + (tab.COLS_TAB * tab.TAM_CELULA)/2 - player1.get_rect().center[0], 20))
    tela_.blit(player2, (tab.POS_TAB_02[0] + (tab.COLS_TAB * tab.TAM_CELULA)/2 - player1.get_rect().center[0], 20))
            

    pg.draw.rect(tela_, (100,100,100), (0, ALTURA - 300, LARGURA,300))
    pg.draw.line(tela_, (255,255,255), (LARGURA/2, ALTURA-300), (LARGURA/2, ALTURA), 10)
    pg.draw.line(tela_, (255,255,255), (0, ALTURA-300), (LARGURA, ALTURA-300), 10)
    
        
    quatd_tm_4 = FONTES["texto menu_jogo"].render("1x", 1, (0,0,0))
    quatd_tm_3 = FONTES["texto menu_jogo"].render("2x", 1, (0,0,0))
    quatd_tm_2 = FONTES["texto menu_jogo"].render("3x", 1, (0,0,0))
    quatd_tm_1 = FONTES["texto menu_jogo"].render("4x", 1, (0,0,0))
    
    
    
    texto_vez_player = FONTES["titulo menu_jogo"].render(f"Vez do Player {player}", 1, (0, 0, 0))
    texto_vez_player_rect = texto_vez_player.get_rect()
    texto_vez_player_rect.center = (LARGURA/2 + LARGURA/4 ,ALTURA - 150)
    
    tela_.blit(texto_vez_player, texto_vez_player_rect)
    
    titulo_menu_jogo = FONTES["titulo menu_jogo"].render("GAME INSTRUCTIONS", 1, (0,0,0))
    tela_.blit(titulo_menu_jogo, (LARGURA/4 - (20*11.5), ALTURA - 270))
     
    if status == "posicionar":
        texto1 = FONTES["texto menu_jogo"].render("Aperte '1234' para escolher navios", 1, (0,0,0))
        texto2 = FONTES["texto menu_jogo"].render("Aperte 'z' para rotacionar navio", 1, (0,0,0))
        texto3 = FONTES["texto menu_jogo"].render("Aperte 'C' para colocar navio", 1, (0,0,0))
        texto4 = FONTES["texto menu_jogo"].render("Utilize as setas para mover o navio", 1, (0,0,0))
    
        tela_.blit(texto1, (30, ALTURA - 210))
        tela_.blit(texto2, (30, ALTURA - 160))
        tela_.blit(texto3, (30, ALTURA - 110))
        tela_.blit(texto4, (30, ALTURA - 60))
    elif status == "atacar":
        texto1 = FONTES["texto menu_jogo"].render("Aperte o botao esquerdo do", 1, (0,0,0))
        texto2 = FONTES["texto menu_jogo"].render("mouse para atacar adversario", 1, (0,0,0))

    
        tela_.blit(texto1, (30, ALTURA - 210))
        tela_.blit(texto2, (30, ALTURA - 190))
    

def tela_troca_player(tela_):
    tela_.fill((255,255,255))
    
    texto_titulo = FONTES["titulo menu_jogo"].render("Hora da Troca!", 1, (0,0,0))
    texto1 = FONTES["texto menu_jogo"].render("Aperte 'ESPACE' para continuar", 1, (0,0,0))
    
    tela_.blit(texto_titulo, (LARGURA/2 - (texto_titulo.get_rect().center[0]), ALTURA/2 - (texto_titulo.get_rect().center[1]) - 100))
    tela_.blit(texto1, (LARGURA/2 - (texto1.get_rect().center[0]), ALTURA/2 - (texto1.get_rect().center[1])))
    
    
def tela_fim_de_jogo(tela_, player_ganhador):
    tela_.fill((0,255,0))
    
    texto_titulo = FONTES["titulo menu_jogo"].render(f"Player {player_ganhador} Venceu!", 1, (0,0,0))
    
    texto1 = FONTES["texto menu_jogo"].render("Aperte 'ESPACE' para voltar ao menu inicial", 1, (0,0,0))
    
    tela_.blit(texto_titulo, (LARGURA/2 - (texto_titulo.get_rect().center[0]), ALTURA/2 - (texto_titulo.get_rect().center[1]) - 100))
    tela_.blit(texto1, (LARGURA/2 - (texto1.get_rect().center[0]), ALTURA/2 - (texto1.get_rect().center[1])))
    