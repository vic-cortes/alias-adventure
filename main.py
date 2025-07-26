from sys import exit

import pygame

from config import FontsAssets, GraphicsAssets

LIMIT_FPS = 60
GAME_WIDTH = 800
GAME_HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Alia's Adventure")
clock = pygame.time.Clock()
test_font = pygame.font.Font(FontsAssets.MAIN_FONT, 50)

sky_surface = pygame.image.load(GraphicsAssets.SKY_PATH).convert()
ground_surface = pygame.image.load(GraphicsAssets.GROUND_PATH).convert()
text_surface = test_font.render("Alia's Adventure", False, "Black")

snail_surface = pygame.image.load(GraphicsAssets.SNAIL_PATH).convert_alpha()
snail_x_position = GAME_WIDTH


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_x_position -= 4

    if snail_x_position < 0:
        snail_x_position = GAME_WIDTH

    screen.blit(snail_surface, (snail_x_position, 250))

    # Draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(LIMIT_FPS)
