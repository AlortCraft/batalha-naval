import pygame

COR = (50,50,50)

TAM_CELULA = 48
LINS_TAB, COLS_TAB = 10, 10
DIST_TABS = 80
GROSSURA_TABS = 2

POS_TAB_01 = (35, 80)
POS_TAB_02 = (595, 80)

            


def desenhando_tabuleiros(tela, largura_tela):
    for linha in range(LINS_TAB):
        x = (linha * TAM_CELULA) + (largura_tela//2) - (TAM_CELULA * LINS_TAB/2)
        for coluna in range(COLS_TAB):
            y = (coluna * TAM_CELULA) + 80
            pygame.draw.rect(tela, COR, (x - (TAM_CELULA*LINS_TAB/2) - DIST_TABS/2, y, TAM_CELULA, TAM_CELULA), GROSSURA_TABS)
            pygame.draw.rect(tela, COR, (x + (TAM_CELULA*LINS_TAB/2) + DIST_TABS/2, y, TAM_CELULA, TAM_CELULA), GROSSURA_TABS)
            
            
            
            
def pos_tabuleiro(tela, largura_tela, altura_tela, status):
    if status == 1:
        pass
    else:
        pass


def main():
    pygame.init()
    
    largura, altura = 1110, 1000
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Tabuleiros")
    
    canva = pygame.Surface((largura, altura), pygame.SRCALPHA).convert_alpha()
    canva.fill((255,255,255, 50))
    
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        desenhando_tabuleiros(tela, largura)
        
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()