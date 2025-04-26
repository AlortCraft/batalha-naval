import pygame as pg
from settings import LARGURA, ALTURA
import tabuleiros as tab


class Agua(pg.sprite.Sprite): # herdando atributos/metodos de outra classe da biblioteca pygame
    def __init__(self, sprites, index, pos, temp_anim = 500):
        super().__init__() # inicializando classe
        
        self.sprites = sprites
        self.index = index
        
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (pos[0], pos[1])
        
        self.temp_anim = temp_anim
        self.ultimo_update = pg.time.get_ticks()
        
    def update(self):
        agora = pg.time.get_ticks()
        if (agora - self.ultimo_update) >= self.temp_anim:
            self.ultimo_update = agora
            self.index = (self.index + 1) % len(self.sprites)
            self.image = self.sprites[self.index]
            
            
class Navios(pg.sprite.Sprite):
    def __init__(self, sprite):
        super().__init__()
        self.pos = (0,0)
        
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rotacao = 0
        
    def rotacionar(self):
        self.rotacao = (self.rotacao + 90) % 180
        self.image = pg.transform.rotate(self.image, 90)
        
    def update(self, pos_atual):
        self.pos = pos_atual
        
        if self.rotacao == 0:
            self.rect.topleft = (self.pos[0], self.pos[1] + (tab.TAM_CELULA/2))
        else:
            self.rect.topleft = (self.pos[0] + (tab.TAM_CELULA/2), self.pos[1])
            
        
            
         
def agua_spr():
    
    agua_size = (32, 32)
    
    #carregando sprites
    agua_spr = [
        pg.transform.scale(pg.image.load("sprites/water/water1.png"), (agua_size[0], agua_size[1])),
        pg.transform.scale(pg.image.load("sprites/water/water2.png"), (agua_size[0], agua_size[1])),
        pg.transform.scale(pg.image.load("sprites/water/water3.png"), (agua_size[0], agua_size[1]))
    ]   
        
    return agua_spr, agua_size


def navios_spr():
    navios = {
        "tm_4" : pg.transform.scale(pg.image.load("sprites/ships/ShipCarrierHull.png"), (tab.TAM_CELULA, tab.TAM_CELULA*4)),
        "tm_3" : pg.transform.scale(pg.image.load("sprites/ships/ShipCruiserHull.png"), (tab.TAM_CELULA * .6, tab.TAM_CELULA*3)),
        "tm_2" : pg.transform.scale(pg.image.load("sprites/ships/ShipDestroyerHull.png"), (tab.TAM_CELULA * .5, tab.TAM_CELULA*2)),
        "tm_1" : pg.transform.scale(pg.image.load("sprites/ships/Plane.png"), (tab.TAM_CELULA * .9, tab.TAM_CELULA*1))
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
    
    sprs_agua, tiles_agua = agua_spr(tela, largura, altura)
    
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