import sys
import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1300, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
surface = pygame.Surface((540, 360))

pygame.display.set_caption(title="Asteroid Shooter")
ship_surf = pygame.image.load("./graphics/ship.png").convert_alpha()
background = pygame.image.load("./graphics/background.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill((200, 200, 200))
    # surface.fill("red")
    # display_surface.blit(surface, (270, surface.get_height()/2))
    display_surface.blit(background, (10, 0))
    display_surface.blit(ship_surf, (500, 620))

    pygame.display.update()
