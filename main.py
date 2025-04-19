import pygame as pg
import math
import pandas as pd
import cores, sprites, tabuleiros
from pygame.locals import *
from sys import exit


def main():
    #Tela
    largura =  1110
    altura = 1000
    tela = pg.display.set_mode((largura, altura))
    pg.display.set_caption("Batalha Naval")
    pg.display.set_icon(pg.image.load("sprites/naval_icon.png"))

    #Definindo relogio
    relogio = pg.time.Clock()

    #Fonte
    pg.font.init()
    fonte_titulo = pg.font.Font("text_fonts/gunplay.otf", 100)
    fonte_instr = pg.font.Font("text_fonts/minecraft.ttf", 50)

    texto = fonte_instr.render("Instrucoes de jogo", 1, (0,0,0))

    pg.draw.rect(tela, (100,100,100), (0, altura - 400, largura,400))
    pg.draw.line(tela, (255,255,255), (largura/2, altura-390), (largura/2, altura), 10)
    pg.draw.line(tela, (255,255,255), (0, altura-390), (largura, altura-390), 10)

    tela.blit(texto, (30, altura - 370))


    #tabuleiro oculto
    tabuleiro_oculto =  [["" for i in range(tabuleiros.LINS_TAB)] for i in range(tabuleiros.COLS_TAB)]

    #Valores
    ultimoStatus = 0
    CliqueFora= 0

    click_position_x = -1
    click_position_y = -1

    X_or_O_turn = 'x'

    end_game = 0

    #gerando sprites e tiles da agua
    spr_agua, tiles_agua = sprites.agua_spr_tile(tela,largura, altura)

    #Desenhando coluna e linhas
    '''
    def gradeTabuleiro(tela):
        for i in range(100,1001, 100):
            pg.draw.line(tela,cores.preto,(i,0), (i,1000), 3)
        for j in range(100,1001, 100):
            pg.draw.line(tela,cores.preto,(0,j), (1000,j), 3)
    '''

    #Jogo
    troca_jogador = False
    player_ganhador = 0
    rodando = True
    while rodando:
        #Definindo FPS
        relogio.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                rodando = False
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                print("Clicou")
                    
        #Desenhando a agua e atualizando sprites
        sprites.anim_constante(tela, spr_agua, tiles_agua)
        
        #gerar tabuleiros
        tabuleiros.desenhando_tabuleiros(tela, largura)
        
        
                        
        #Declarando variavel da posicao mouse        
        mouse = pg.mouse.get_pos()
        mouse_pos_x, mouse_pos_y = mouse
        
        if mouse_pos_x <= largura/2:
            print(f"TABULEIRO 1 - X: {(mouse_pos_x - tabuleiros.POS_TAB_01[0])//48} | Y: {(mouse_pos_y - tabuleiros.POS_TAB_01[1])//48}")
        else:
            print(f"TABULEIRO 2 - X: {(mouse_pos_x - tabuleiros.POS_TAB_02[0])//48} | Y: {(mouse_pos_y - tabuleiros.POS_TAB_02[1])//48}")
                
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