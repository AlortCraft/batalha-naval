import pygame as pg
from settings import LARGURA, ALTURA
          
def agua_spr_tile(tela):
    
    agua_size = (32, 32)
    
    #carregando sprites
    agua_spr = [
        pg.transform.scale(pg.image.load("sprites/water/water1.png"), (agua_size[0], agua_size[1])),
        pg.transform.scale(pg.image.load("sprites/water/water2.png"), (agua_size[0], agua_size[1])),
        pg.transform.scale(pg.image.load("sprites/water/water3.png"), (agua_size[0], agua_size[1]))
    ]
    #crianco tiles
    tiles = []
    for x in range(0, LARGURA, agua_size[0]):
        for y in range(0, ALTURA, agua_size[1]):
            tiles.append({
                "posicao" : (x,y),
                "index" : (x//agua_size[0]) % len(agua_spr), #o index fica entre 0 e 2
                "ultimo_update" : pg.time.get_ticks()
            })

    #desenhando tiles iniciais
    for tile in tiles:
        index = tile["index"]
        tela.blit(agua_spr[index], tile["posicao"])
        
        
    return agua_spr, tiles

def navios_spr():
    navios = {
        "tm_4" : pg.transform.scale(pg.image.load("sprites/ships/ShipCarrierHull.png"), (48, 48*4)),
        "tm_3" : pg.transform.scale(pg.image.load("sprites/ships/ShipCruiserHull.png"), (36, 48*3)),
        "tm_2" : pg.transform.scale(pg.image.load("sprites/ships/ShipDestroyerHull.png"), (24, 48*2)),
        "tm_1" : pg.transform.scale(pg.image.load("sprites/ships/Plane.png"), (48, 48*1))
    }
    
    return navios


def anim_constante(tela, sprites, tiles, temp_anim=500):
        #tempo (em milissegundo) de agora
        agora = pg.time.get_ticks()

        #atualizar sprites
        for tile in tiles:
            if (agora - tile["ultimo_update"]) >= temp_anim:
                tile["ultimo_update"] = agora
                tile["index"] = (tile["index"] + 1) % len(sprites) #Alterar index
                
                #desenhar sprites
                index = tile["index"]
                tela.blit(sprites[index], tile["posicao"])
            

def main():
    pg.init()
    
    largura, altura = 1110, 1000
    tela = pg.display.set_mode((largura, altura))
    pg.display.set_caption("Modulo de Sprites")
    
    relogio = pg.time.Clock()
    
    sprs_agua, tiles_agua = agua_spr_tile(tela, largura, altura)
    
    #Loop
    run = True
    while run:
        relogio.tick(60)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                break
        
        anim_constante(tela, sprs_agua, tiles_agua)
            
        pg.display.update()
    
    pg.quit()

if __name__ == "__main__":
    main()