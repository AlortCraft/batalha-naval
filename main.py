import pygame as pg
from settings import *
import player
import sprites as spr
import tabuleiros as tab
import cenas as cn



def main():
    pg.init()
    tela = pg.display.set_mode((LARGURA, ALTURA))
    
    pg.display.set_caption("Batalha Naval")
    pg.display.set_icon(pg.image.load("sprites/naval_icon.png"))
    
    relogio = pg.time.Clock()
    
    
    pg.mixer.music.load("sound_effects/menu.wav")
    pg.mixer.music.play(-1)
    
    bomb_water = pg.mixer.Sound("sound_effects/bomb_water.wav")
    bomb_explosion = pg.mixer.Sound("sound_effects/explosion.wav")
    ship_colocado = pg.mixer.Sound("sound_effects/ship_placed.wav")
    
    
    tab01, tab02 = tab.desenhando_tabuleiros(tela)
    

    agua_spr, agua_tile = spr.agua_spr_tile(tela)


    tabuleiro_oculto_1 =  [["" for i in range(tab.LINS_TAB)] for i in range(tab.COLS_TAB)]
    tabuleiro_oculto_2 =  [["" for i in range(tab.LINS_TAB)] for i in range(tab.COLS_TAB)]
    

    marcacoes_tab01 = []
    marcacoes_tab02 = []
    marcacoes_tab01_oc = []
    marcacoes_tab02_oc = []
    
  
    navios_tab01 = []
    navios_tab02 = []
    
    navios = spr.navios_info()
    navio_atual = None
    index_navio_atual = 0
   
    quant_navios_j1 = [4,3,2,1]
    quant_navios_j2 = [4,3,2,1]
    
    
    cena_atual = "menu"
    status_jogo = "posicionar"
    player_atual = "1"
    rodando = True
    while rodando:
        relogio.tick(FPS)
         
        mouse = pg.mouse.get_pos()
        mouse_pos_x, mouse_pos_y = mouse
        
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
                        
                        navio_atual, colocado, index_navio_atual = player.movimentar_navios(event, player_atual, navios, navio_atual, index_navio_atual, quant_navios_j1, quant_navios_j2)
                        
                        if navio_atual != None:
                            if colocado:
                                posicao_livre = True
                                if player_atual == "1":
                                    pos_tab_tempX = (navio_atual["pos"][0] - tab.POS_TAB_01[0]) // tab.TAM_CELULA
                                    pos_tab_tempY = (navio_atual["pos"][1] - tab.POS_TAB_01[1]) // tab.TAM_CELULA
                                    
                                    if navio_atual["rotacao"] == 90:
                                        for x in range(pos_tab_tempX, pos_tab_tempX + navio_atual["num_cel"]):
                                            if tabuleiro_oculto_1[x][pos_tab_tempY] == "n":
                                                posicao_livre = False
                                                
                                        if posicao_livre:
                                            for x in range(pos_tab_tempX, pos_tab_tempX + navio_atual["num_cel"]):
                                                tabuleiro_oculto_1[x][pos_tab_tempY] = "n"
                                                
                                                navio_atual["celulas"].append((x, pos_tab_tempY))
                                        
                                    else:
                                        for y in range(pos_tab_tempY, pos_tab_tempY + navio_atual["num_cel"]):
                                            if tabuleiro_oculto_1[pos_tab_tempX][y] == "n":
                                                posicao_livre = False
                                                
                                        if posicao_livre:    
                                            for y in range(pos_tab_tempY, pos_tab_tempY + navio_atual["num_cel"]):
                                                tabuleiro_oculto_1[pos_tab_tempX][y] = "n"
                                                
                                                navio_atual["celulas"].append((pos_tab_tempX, y))
                                    
                                    if posicao_livre:
                                        ship_colocado.play(0)
                                        navios_tab01.append(navio_atual)
                                        navio_atual = None
                                        navios = spr.navios_info()
                                        quant_navios_j1[index_navio_atual] -= 1
                            
                                        
                                    if sum(quant_navios_j1) == 0:
                                        navio_atual = None
                                        player_atual = "2"
                                        cena_atual = "troca"
                                    
                                    
                                elif player_atual == "2":
                                    pos_tab_tempX = (navio_atual["pos"][0] - tab.POS_TAB_02[0]) // tab.TAM_CELULA
                                    pos_tab_tempY = (navio_atual["pos"][1] - tab.POS_TAB_02[1]) // tab.TAM_CELULA
                                
                                    if navio_atual["rotacao"] == 90:
                                        for x in range(pos_tab_tempX, pos_tab_tempX + navio_atual["num_cel"]):
                                            if tabuleiro_oculto_2[x][pos_tab_tempY] == "n":
                                                posicao_livre = False
                                                
                                        if posicao_livre:
                                            for x in range(pos_tab_tempX, pos_tab_tempX + navio_atual["num_cel"]):
                                                tabuleiro_oculto_2[x][pos_tab_tempY] = "n"
                                                
                                                navio_atual["celulas"].append((x, pos_tab_tempY))
                                        
                                    else:
                                        for y in range(pos_tab_tempY, pos_tab_tempY + navio_atual["num_cel"]):
                                            if tabuleiro_oculto_2[pos_tab_tempX][y] == "n":
                                                posicao_livre = False
                                                
                                        if posicao_livre:    
                                            for y in range(pos_tab_tempY, pos_tab_tempY + navio_atual["num_cel"]):
                                                tabuleiro_oculto_2[pos_tab_tempX][y] = "n"
                                                
                                                navio_atual["celulas"].append((pos_tab_tempX, y))
                                    
                                    if posicao_livre:
                                        ship_colocado.play(0)
                                        navios_tab02.append(navio_atual)
                                        navio_atual = None
                                        navios = spr.navios_info()
                                        quant_navios_j2[index_navio_atual] -= 1
                            
                                        
                                    if sum(quant_navios_j2) == 0:
                                        navio_atual = None
                                        player_atual = "1"
                                        cena_atual = "troca"
                                        status_jogo = "atacar"
                            
                          
                elif status_jogo == "atacar":
                    if event.type == pg.MOUSEBUTTONDOWN:       
                        if player_atual == "1":
                            
                            marcacao = player.atacar(player_atual, tab01, tab02, (mouse_pos_tab01_x, mouse_pos_tab01_y), (mouse_pos_tab02_x, mouse_pos_tab02_y), marcacoes_tab01, marcacoes_tab02)
                            
                            if marcacao != None:
                                x = int(marcacao[0] - tab.POS_TAB_02[0]) // tab.TAM_CELULA
                                y = int(marcacao[1] - tab.POS_TAB_02[1]) // tab.TAM_CELULA
                                
                                
                                if tabuleiro_oculto_2[x][y] != "n":    
                                    bomb_water.play(0)
                                    
                                    marcacoes_tab02.append(marcacao)
                                    marcacoes_tab02_oc.append("x")
                                    
                                    player_atual = "2"
                                    cena_atual = "troca"
                                else:
                                    bomb_explosion.play(0)
                                    
                                    for navio in navios_tab02:
                                        if (x,y) in navio["celulas"] and navio["destruido"] == False:
                                            navio["destruido"] = True
                                            marcacoes_tab02_oc.append("o")
                            
                            
                        elif player_atual == "2":
                            marcacao = player.atacar(player_atual, tab01, tab02, (mouse_pos_tab01_x, mouse_pos_tab01_y), (mouse_pos_tab02_x, mouse_pos_tab02_y), marcacoes_tab01, marcacoes_tab02)
                            
                            if marcacao != None:
                                x = int((marcacao[0] - tab.POS_TAB_01[0]) // tab.TAM_CELULA)
                                y = int((marcacao[1] - tab.POS_TAB_01[1]) // tab.TAM_CELULA)
                                
                                
                                if tabuleiro_oculto_1[x][y] != "n":
                                    bomb_water.play(0)
                                    marcacoes_tab01.append(marcacao)
                                    marcacoes_tab01_oc.append("x")
                                    player_atual = "1"
                                    cena_atual = "troca"
                                else:
                                    bomb_explosion.play(0)
                                    
                                    for navio in navios_tab01:
                                        if (x,y) in navio["celulas"] and navio["destruido"] == False:
                                            navio["destruido"] = True
                                            marcacoes_tab01_oc.append("o")
                                    
                    
            elif cena_atual == "troca":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        cena_atual = "jogo"
            
            elif cena_atual == "fim":
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_SPACE:
                        status_jogo = "posicionar"
                        player_atual = "1"
                        cena_atual = "menu"
                        
                        tabuleiro_oculto_1 =  [["" for i in range(tab.LINS_TAB)] for i in range(tab.COLS_TAB)]
                        tabuleiro_oculto_2 =  [["" for i in range(tab.LINS_TAB)] for i in range(tab.COLS_TAB)]
                        

                        marcacoes_tab01 = []
                        marcacoes_tab02 = []
                        marcacoes_tab01_oc = []
                        marcacoes_tab02_oc = []
                    
                        navios_tab01 = []
                        navios_tab02 = [] 
                        
                        quant_navios_j1 = [4,3,2,1]
                        quant_navios_j2 = [4,3,2,1]
                        
                        pg.mixer.music.stop()
                        pg.mixer.music.load("sound_effects/menu.wav")
                        pg.mixer.music.play(-1)
                
        
        
        
        if cena_atual == "menu":
            spr.anim_constante(tela, agua_spr, agua_tile)
            cena_atual = cn.menu_inicial(tela, mouse_pos_x, mouse_pos_y)
            
            if cena_atual == "jogo":
                pg.mixer.music.stop()
            
        elif cena_atual == "jogo":
            spr.anim_constante(tela, agua_spr, agua_tile)
            tab.desenhando_tabuleiros(tela)
            
            
            if player_atual == "1":
                for navio in navios_tab01:
                    tela.blit(navio["sprite"], navio["pos"])
                    
            if player_atual == "2":
                for navio in navios_tab02:
                    tela.blit(navio["sprite"], navio["pos"])
                    
                    
            for navio in navios_tab01:
                    if navio["destruido"] == True:
                        tela.blit(navio["sprite"], navio["pos"])
                        
            for navio in navios_tab02:
                    if navio["destruido"] == True:
                        tela.blit(navio["sprite"], navio["pos"])
                        
                    
            
            if status_jogo == "posicionar":
                if navio_atual:
                    tela.blit(navio_atual["sprite"], navio_atual["pos"])
            
            elif status_jogo == "atacar":
                for marcacao in marcacoes_tab01:
                    x, y, w, h = marcacao
   
                    pg.draw.line(tela, (255,0,0), (x, y), (x + w, y + h), 3)
                    pg.draw.line(tela, (255,0,0), (x + w, y), (x, y + h), 3)
                    
                
                    
                for marcacao in marcacoes_tab02:
                    x, y, w, h = marcacao
                    
                    pg.draw.line(tela, (255,0,0), (x, y), (x + w, y + h), 3)
                    pg.draw.line(tela, (255,0,0), (x + w, y), (x, y + h), 3)
                    
                    
                    
                if marcacoes_tab01_oc.count("o") == 10:
                    player_atual = "2"
                    cena_atual = "fim"
                    pg.mixer.music.load("sound_effects/victory.wav")
                    pg.mixer.music.play(-1)
                    
                elif marcacoes_tab02_oc.count("o") == 10:
                    player_atual = "1"
                    cena_atual = "fim"
                    pg.mixer.music.load("sound_effects/victory.wav")
                    pg.mixer.music.play(-1)
            
            cn.jogo(tela, player_atual, status_jogo)
            
        elif cena_atual == "troca":
            cn.tela_troca_player(tela)
            
        elif cena_atual == "fim":
            cn.tela_fim_de_jogo(tela, player_atual)
            
        elif cena_atual == "sair":
            rodando = False

        pg.display.update()
        
    pg.quit()
    


if __name__ == "__main__":
    main()