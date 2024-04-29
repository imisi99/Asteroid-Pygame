import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Asteroid Shooter")

back_ground = pygame.image.load("./graphics/background.png").convert_alpha()


class Ship(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load("./graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

    def get_input(self):
        self.rect.center = pygame.mouse.get_pos()

    def update(self):
        self.get_input()


class Laser(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


ship_group = pygame.sprite.GroupSingle()
ship = Ship(ship_group)

laser_group = pygame.sprite.Group()
laser = Laser(laser_group)

while True:

    clock = pygame.time.Clock()
    dt = (clock.tick()) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    display_surface.blit(back_ground, (0, 0))

    ship_group.draw(display_surface)
    laser_group.draw(display_surface)

    ship_group.update()

    pygame.display.update()
