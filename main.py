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

RGB_COLOR = (64, 64, 64)
score_surface = test_font.render("Alia's Adventure", False, RGB_COLOR)
score_rect = score_surface.get_rect(center=(GAME_WIDTH / 2, 50))

snail_surface = pygame.image.load(GraphicsAssets.SNAIL_PATH).convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright=(600, 300))
snail_x_position = GAME_WIDTH

player_surface = pygame.image.load(GraphicsAssets.PLAYER_PATH).convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 300))

player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.MOUSEMOTION:
        #     if player_rectangle.collidepoint(event.pos):
        #         print("Player rectangle collides with mouse position")
        is_touching_ground = player_rectangle.bottom >= 300

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rectangle.collidepoint(event.pos) and is_touching_ground:
                player_gravity = -20  # Jump effect

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE and is_touching_ground:
                player_gravity = -20  # Jump effect

        if event.type == pygame.KEYUP:
            pass

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, "#c0e8ec", score_rect)
    pygame.draw.rect(screen, "#c0e8ec", score_rect, width=10)
    # pygame.draw.line(screen, "Gold", (0, 300), (GAME_WIDTH, 300), width=2)
    screen.blit(score_surface, score_rect)

    snail_rectangle.x -= 4

    if snail_rectangle.right < 0:
        snail_rectangle.left = GAME_WIDTH

    screen.blit(snail_surface, snail_rectangle)

    # Player
    player_gravity += 1
    player_rectangle.y += player_gravity

    if player_rectangle.bottom >= 300:
        player_rectangle.bottom = 300

    screen.blit(player_surface, player_rectangle)

    # keys = pygame.key.get_pressed()

    # if keys.get(pygame.K_SPACE):
    #     pass

    # if player_rectangle.colliderect(snail_rectangle):
    #     pass

    # mouse_position = pygame.mouse.get_pos()

    # if player_rectangle.collidepoint(mouse_position):
    #     print("Player rectangle collides with mouse position")

    # Draw all our elements
    # update everything
    pygame.display.update()
    clock.tick(LIMIT_FPS)
