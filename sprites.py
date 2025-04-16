import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, sprites, index, tempo_animacao):
        super().__init__()
        
        # Variaveis criadas
        self.sprites = sprites
        self.index = index
        self.tempo_animacao = tempo_animacao
        self.ultimo_update = pygame.time.get_ticks()
        
        # variaveis do pygame.sprite.Sprite
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect(topleft=(x, y))
            
    def update(self):
        # pegar tempo atual em milissegundos
        tempo_atual = pygame.time.get_ticks()
        # se ja passou +500 milissegundos, atualize imagem
        if (tempo_atual - self.ultimo_update) >= self.tempo_animacao:
            self.ultimo_update = tempo_atual
            # Atualizando index da sprite entre 0 e 2.
            self.index = (self.index + 1) % len(self.sprites)
            self.image = self.sprites[self.index]
            
def agua_sprite(altura_tela, largura_tela):
    
    agua_size = (32, 32)
    
    agua_spr = [
        pygame.transform.scale(pygame.image.load("sprites/water1.png"), (agua_size[0], agua_size[1])),
        pygame.transform.scale(pygame.image.load("sprites/water2.png"), (agua_size[0], agua_size[1])),
        pygame.transform.scale(pygame.image.load("sprites/water3.png"), (agua_size[0], agua_size[1]))
    ]
    
    # Criando agrupamento entre as sprites
    agua_group = pygame.sprite.Group()
    for x in range(0, largura_tela, agua_size[1]):
        for y in range(0, altura_tela, agua_size[1]):
            tile = Sprite(x, y, agua_spr, x % len(agua_spr), 500)
            agua_group.add(tile)
            
            
    return agua_group
