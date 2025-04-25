import pygame

LARGURA, ALTURA = 1110, 800

FPS = 60

pygame.font.init()
FONTES = {
    "titulo menu_inicial": pygame.font.Font("text_fonts/gunplay.otf", 100),
    "botoes menu_inicial": pygame.font.Font("text_fonts/gunplay.otf", 50),
    "titulo menu_jogo": pygame.font.Font("text_fonts/Minecraft.ttf", 40),
    "texto menu_jogo": pygame.font.Font("text_fonts/Minecraft.ttf", 25)
}