from sys import exit

import pygame

from config import GraphicsAssets

LIMIT_FPS = 60

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alia's Adventure")
clock = pygame.time.Clock()

sky_surface = pygame.image.load(GraphicsAssets.SKY_PATH)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (200, 100))

    # Draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(LIMIT_FPS)
