import pygame as pg
from settings import *
import tabuleiros as tab


def agua_spr_tile(tela):
    
    agua_size = (32, 32)
    
    agua_spr = [
        pg.transform.scale(pg.image.load("sprites/water/water1.png"), (agua_size[0], agua_size[1])),
        pg.transform.scale(pg.image.load("sprites/water/water2.png"), (agua_size[0], agua_size[1])),
        pg.transform.scale(pg.image.load("sprites/water/water3.png"), (agua_size[0], agua_size[1]))
    ] 

    agua_tiles = []
    for x in range(0, LARGURA, agua_size[0]):
        for y in range(0, ALTURA, agua_size[1]):
            agua_tiles.append({
                 "posicao" : (x,y),
                 "index" : (x//agua_size[0]) % len(agua_spr),
                 "ultimo_update" : pg.time.get_ticks()
            })
 

    for tile in agua_tiles:
        index = tile["index"]
        tela.blit(agua_spr[index], tile["posicao"])
        
        
    return agua_spr, agua_tiles

def anim_constante(tela, sprites, tiles, temp_anim=500):
         agora = pg.time.get_ticks()
 
         for tile in tiles:
            if (agora - tile["ultimo_update"]) >= temp_anim:
                tile["ultimo_update"] = agora
                tile["index"] = (tile["index"] + 1) % len(sprites)

                index = tile["index"]
                tela.blit(sprites[index], tile["posicao"])
            else:
                tela.blit(sprites[tile["index"]], tile["posicao"])


def navios_info():
    navios = {
        "tm_4": {
            "sprite": pg.transform.scale(pg.image.load("sprites/ships/ShipCarrierHull.png"), (tab.TAM_CELULA, tab.TAM_CELULA * 4)),
            "num_cel": 4,
            "pos": [0, 0],
            "rotacao": 0,
            "celulas": [],
            "destruido": False
        },
        "tm_3": {
            "sprite": pg.transform.scale(pg.image.load("sprites/ships/ShipCruiserHull.png"), (tab.TAM_CELULA * .6, tab.TAM_CELULA * 3)),
            "num_cel": 3,
            "pos": [0, 0],
            "rotacao": 0,
            "celulas": [],
            "destruido": False
        },
        "tm_2": {
            "sprite": pg.transform.scale(pg.image.load("sprites/ships/ShipDestroyerHull.png"), (tab.TAM_CELULA * .5, tab.TAM_CELULA * 2)),
            "num_cel": 2,
            "pos": [0, 0],
            "rotacao": 0,
            "celulas": [],
            "destruido": False
        },
        "tm_1": {
            "sprite": pg.transform.scale(pg.image.load("sprites/ships/Plane.png"), (tab.TAM_CELULA * .9, tab.TAM_CELULA * 1)),
            "num_cel": 1,
            "pos": [0, 0],
            "rotacao": 0,
            "celulas": [],
            "destruido": False
        }
     }
    return navios

