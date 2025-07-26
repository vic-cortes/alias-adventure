from sys import exit

import pygame

from config import GraphicsAssets

LIMIT_FPS = 60
GAME_WIDTH = 800
GAME_HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((GAME_WIDTH, GAME_HEIGHT))
pygame.display.set_caption("Alia's Adventure")
clock = pygame.time.Clock()

sky_surface = pygame.image.load(GraphicsAssets.SKY_PATH)
ground_surface = pygame.image.load(GraphicsAssets.GROUND_PATH)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    # Draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(LIMIT_FPS)
