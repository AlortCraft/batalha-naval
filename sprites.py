import pygame


class Agua(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites, index, tempo_animacao=500):
        super().__init__()
            
        self.sprites = sprites
        self.index = index
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_delay = tempo_animacao
        self.last_update = pygame.time.get_ticks()
            
    def update(self):
        now = pygame.time.get_ticks()
        if (now - self.last_update) >= self.animation_delay:
            self.last_update = now
            self.index = (self.index + 1) % len(self.sprites)
            self.image = self.sprites[self.index]
            
def agua_sprite(altura_tela, largura_tela):
    agua_size = (32, 32)
    
    agua_spr = [
        pygame.transform.scale(pygame.image.load("sprites/water1.png").convert_alpha(), (agua_size[0], agua_size[1])),
        pygame.transform.scale(pygame.image.load("sprites/water2.png").convert_alpha(), (agua_size[0], agua_size[1])),
        pygame.transform.scale(pygame.image.load("sprites/water3.png").convert_alpha(), (agua_size[0], agua_size[1]))
    ]
    
    agua_group = pygame.sprite.Group()
    
    for x in range(0, largura_tela, agua_size[1]):
        for y in range(0, altura_tela, agua_size[1]):
            tile = Agua(x, y, agua_spr, x % len(agua_spr), 500)
            agua_group.add(tile)
            
            
    return agua_group
    
