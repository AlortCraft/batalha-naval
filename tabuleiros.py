import pygame


def gerando_tabuleiros(tela, largura_tela, altura_tela):
    cor = (50,50,50)
    tam_celula = 48
    lins_tab, cols_tab = 10, 10
    dist_tabuleiros = 80
    
    for linha in range(lins_tab):
        x = (linha * tam_celula) + (largura_tela//2) - (tam_celula * lins_tab/2)
        for coluna in range(cols_tab):
            y = (coluna * tam_celula) + 80
            pygame.draw.rect(tela, cor, (x - (tam_celula*lins_tab/2) - dist_tabuleiros/2, y, tam_celula, tam_celula),3)
            pygame.draw.rect(tela, cor, (x + (tam_celula*lins_tab/2) + dist_tabuleiros/2, y, tam_celula, tam_celula),3)
            
def pos_tabuleiro(tela, largura_tela, altura_tela, status):
    if status == 1:
        pass
    else:
        pass


def main():
    pygame.init()
    
    largura, altura = 1110, 1000
    tela = pygame.display.set_mode((largura, altura))
    
    canva = pygame.Surface((largura, altura), pygame.SRCALPHA).convert_alpha()
    canva.fill((255,255,255, 50))
    
    gerando_tabuleiros(tela, largura, altura)
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        gerando_tabuleiros(tela, largura, altura)
        
        pygame.display.update()
    
    pygame.quit()


if __name__ == "__main__":
    main()