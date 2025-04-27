import pygame as pg
import cores, sprites, tabuleiros
from settings import *

#menu inicial
def menu_inicial(tela_, mouse_x, mouse_y):
    titulo = FONTES["titulo menu_inicial"].render("BATALHA NAVAL", 1, (0,0,0))
    titulo_rect = titulo.get_rect()
    titulo_rect.center = (LARGURA/2, 250)
    
    
    botao_jogar = FONTES["botoes menu_inicial"].render("JOGAR", 1, (0,0,0))
    botao_jogar_rect = botao_jogar.get_rect()
    botao_jogar_rect.center = (LARGURA/2, 400)
    
    
    botao_instrucoes = FONTES["botoes menu_inicial"].render("INSTRUÇÕES", 1, (0,0,0))
    botao_instrucoes_rect = botao_instrucoes.get_rect()
    botao_instrucoes_rect.center = (LARGURA/2, 500)
    
    
    botao_sair = FONTES["botoes menu_inicial"].render("SAIR", 1, (0,0,0))
    botao_sair_rect = botao_sair.get_rect()
    botao_sair_rect.center = (LARGURA/2, 600)
    
    colid_jogar = botao_jogar_rect.collidepoint(mouse_x, mouse_y)
    colid_config = botao_instrucoes_rect.collidepoint(mouse_x, mouse_y)
    colid_sair = botao_sair_rect.collidepoint(mouse_x, mouse_y)
        
    if colid_jogar:
        botao_jogar = FONTES["botoes menu_inicial"].render("JOGAR", 1, (100,100,100))
        if pg.mouse.get_pressed()[0] == 1:
            return "jogo"
    if colid_config:
        botao_instrucoes = FONTES["botoes menu_inicial"].render("INSTRUÇÕES", 1, (100,100,100))
        if pg.mouse.get_pressed()[0] == 1:
            return "config"
    if colid_sair:
        botao_sair = FONTES["botoes menu_inicial"].render("SAIR", 1, (100,100,100))
        if pg.mouse.get_pressed()[0] == 1:
            return "sair"
        
        
    tela_.blit(titulo, titulo_rect)
    tela_.blit(botao_jogar, botao_jogar_rect)
    tela_.blit(botao_instrucoes, botao_instrucoes_rect)
    tela_.blit(botao_sair, botao_sair_rect)
                
    return "menu"
    
    
    
    
#jogo
def jogo(tela_, mouse_x, mouse_y, navios_spr):
    
    #players
    player1 = FONTES["titulo menu_jogo"].render("PLAYER 1", 1, (0, 0, 0))
    player2 = FONTES["titulo menu_jogo"].render("PLAYER 2", 1, (0, 0, 0))
    
    tela_.blit(player1, (tabuleiros.POS_TAB_01[0] + (tabuleiros.COLS_TAB * tabuleiros.TAM_CELULA)/2 - player1.get_rect().center[0], 20))
    tela_.blit(player2, (tabuleiros.POS_TAB_02[0] + (tabuleiros.COLS_TAB * tabuleiros.TAM_CELULA)/2 - player1.get_rect().center[0], 20))
            
    #Desenhando menu do jogo:
    pg.draw.rect(tela_, (100,100,100), (0, ALTURA - 300, LARGURA,300))
    pg.draw.line(tela_, (255,255,255), (LARGURA/2, ALTURA-300), (LARGURA/2, ALTURA), 10)
    pg.draw.line(tela_, (255,255,255), (0, ALTURA-300), (LARGURA, ALTURA-300), 10)
    
        
    quatd_tm_4 = FONTES["texto menu_jogo"].render("1x", 1, (0,0,0))
    quatd_tm_3 = FONTES["texto menu_jogo"].render("2x", 1, (0,0,0))
    quatd_tm_2 = FONTES["texto menu_jogo"].render("3x", 1, (0,0,0))
    quatd_tm_1 = FONTES["texto menu_jogo"].render("4x", 1, (0,0,0))
    
    tela_.blit(navios_spr["tm_4"], (LARGURA/2 + 400, ALTURA-200))
    tela_.blit(navios_spr["tm_3"], (LARGURA/2 + 300, ALTURA-200))
    tela_.blit(navios_spr["tm_2"], (LARGURA/2 + 200, ALTURA-200))
    tela_.blit(navios_spr["tm_1"], (LARGURA/2 + 100, ALTURA-200))
    tela_.blit(quatd_tm_4, (LARGURA/2 + 410, ALTURA - 250))
    tela_.blit(quatd_tm_3, (LARGURA/2 + 300, ALTURA - 250))
    tela_.blit(quatd_tm_2, (LARGURA/2 + 200, ALTURA - 250))
    tela_.blit(quatd_tm_1, (LARGURA/2 + 110, ALTURA - 250))
    
    
    
    titulo_menu_jogo = FONTES["titulo menu_jogo"].render("GAME INSTRUCTIONS", 1, (0,0,0))
    texto1 = FONTES["texto menu_jogo"].render("Aperte 'Z' para colocar rotacionar navio", 1, (0,0,0))
    texto2 = FONTES["texto menu_jogo"].render("Aperte 'C' para colocar colocar navio", 1, (0,0,0))
    
    
    tela_.blit(titulo_menu_jogo, (LARGURA/4 - (20*11.5), ALTURA - 270))
    tela_.blit(texto1, (30, ALTURA - 210))
    tela_.blit(texto2, (30, ALTURA - 140))
    

def tela_troca_player(tela_):
    tela_.fill((255,255,255))
    texto_titulo = FONTES["titulo menu_jogo"].render("Hora da Troca!", 1, (0,0,0))
    texto1 = FONTES["texto menu_jogo"].render("Aperte 'ESPACE' para continuar", 1, (0,0,0))
    tela_.blit(texto_titulo, (LARGURA/2 - (texto_titulo.get_rect().center[0]), ALTURA/2 - (texto_titulo.get_rect().center[1]) - 100))
    tela_.blit(texto1, (LARGURA/2 - (texto1.get_rect().center[0]), ALTURA/2 - (texto1.get_rect().center[1])))
    
    
def tela_fim_de_jogo(tela_, player_ganhador, cor):
    tela_.fill(cor)
    
    if player_ganhador == "1":
        texto_titulo = FONTES["titulo menu_jogo"].render("Player 1 Venceu!", 1, (0,0,0))
    if player_ganhador == "2":
        texto_titulo = FONTES["titulo menu_jogo"].render("Player 2 Venceu!", 1, (0,0,0))
    texto1 = FONTES["texto menu_jogo"].render("Aperte 'ESPACE' para continuar", 1, (0,0,0))
    tela_.blit(texto_titulo, (LARGURA/2 - (texto_titulo.get_rect().center[0]), ALTURA/2 - (texto_titulo.get_rect().center[1]) - 100))
    tela_.blit(texto1, (LARGURA/2 - (texto1.get_rect().center[0]), ALTURA/2 - (texto1.get_rect().center[1])))
    
    
    

def main():
    pg.init()
    #Tela do jogo e FPS
    tela = pg.display.set_mode((LARGURA, ALTURA))
    relogio = pg.time.Clock()
    
    #Background do jogo
    agua_spr, agua_tile = sprites.agua_spr_tile(tela)
    
    #criando sprites dos navios
    navios = sprites.navios_spr()
    
    
    cena_atual = "menu"
    run = True
    while run:
        relogio.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
            
        #Declarando variavel da posicao mouse        
        mouse = pg.mouse.get_pos()
        mouse_pos_x, mouse_pos_y = mouse
            
        sprites.anim_constante(tela, agua_spr, agua_tile)
        
        if cena_atual == "menu":
            cena_atual = menu_inicial(tela, mouse_pos_x, mouse_pos_y)
        elif cena_atual == "jogo":
            jogo(tela, mouse_pos_x, mouse_pos_y, navios)
        elif cena_atual == "sair":
            run = False
            break
        
        
        
        pg.display.update()
        
        
    pg.quit()
            
    
    



if __name__ == "__main__":
    main()