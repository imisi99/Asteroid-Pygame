import sys
import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1680, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption(title="Asteroid Shooter")
surface = pygame.Surface((1060, 480))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.fill("red")
    surface.fill("yellow")
    display_surface.blit(surface, (20, 20))
    pygame.display.update()
