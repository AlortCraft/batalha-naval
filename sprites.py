import pygame
          
def agua_spr_tile(tela, largura_tela, altura_tela):
    
    agua_size = (32, 32)
    
    agua_spr = [
        pygame.transform.scale(pygame.image.load("sprites/water/water1.png"), (agua_size[0], agua_size[1])),
        pygame.transform.scale(pygame.image.load("sprites/water/water2.png"), (agua_size[0], agua_size[1])),
        pygame.transform.scale(pygame.image.load("sprites/water/water3.png"), (agua_size[0], agua_size[1]))
    ]
    #crianco tiles
    tiles = []
    for x in range(0, largura_tela, agua_size[0]):
        for y in range(0, altura_tela, agua_size[1]):
            tiles.append({
                "posicao" : (x,y),
                "index" : (x//agua_size[0]) % len(agua_spr),
                "ultimo_update" : pygame.time.get_ticks()
            })

    #desenhando tiles iniciais
    for tile in tiles:
        index = tile["index"]
        tela.blit(agua_spr[index], tile["posicao"])
            
    return agua_spr, tiles

def anim_constante(tela, sprites, tiles, temp_anim=500):
        #tempo (em milissegundo) de agora
        agora = pygame.time.get_ticks()

        #atualizar sprites
        for tile in tiles:
            if (agora - tile["ultimo_update"]) >= temp_anim:
                tile["ultimo_update"] = agora
                tile["index"] = (tile["index"] + 1) % len(sprites)
                
                #desenhar sprites
                index = tile["index"]
                tela.blit(sprites[index], tile["posicao"])
            

def main():
    pygame.init()
    
    largura, altura = 1110, 1000
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Modulo de Sprites")
    
    relogio = pygame.time.Clock()
    
    sprs_agua, tiles_agua = agua_spr_tile(tela, largura, altura)
    
    #Loop
    run = True
    while run:
        relogio.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        anim_constante(tela, sprs_agua, tiles_agua)
            
        pygame.display.update()
    
    pygame.quit()

if __name__ == "__main__":
    main()