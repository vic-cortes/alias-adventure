from sys import exit

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw all our elements
    # update everything
    pygame.display.update()
