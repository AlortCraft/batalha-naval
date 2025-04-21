import pygame

LARGURA, ALTURA = 1110, 1000

FPS = 60

pygame.font.init()
FONTES = {
    "titulo menu_inicial": pygame.font.Font("text_fonts/gunplay.otf", 100),
    "botoes menu_inicial": pygame.font.Font("text_fonts/gunplay.otf", 50),
    "titulo menu_jogo": pygame.font.Font("text_fonts/minecraft.ttf", 40),
    "texto menu_jogo": pygame.font.Font("text_fonts/minecraft.ttf", 25)
}