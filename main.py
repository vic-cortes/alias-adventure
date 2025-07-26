from sys import exit

import pygame

LIMIT_FPS = 60

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Alia's Adventure")
clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))
test_surface.fill("Red")


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_surface, (200, 100))

    # Draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(LIMIT_FPS)
