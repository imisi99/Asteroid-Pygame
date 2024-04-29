import pygame
import sys
from random import randint, uniform

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
        self.can_shoot = True
        self.shoot_time = None
        self.laser_sound = pygame.mixer.Sound("./sounds/laser.ogg")

    def get_input(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= 370:
                self.can_shoot = True

    def mouse_click(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            self.shoot_time = pygame.time.get_ticks()
            Laser(self.rect.midtop, laser_group)
            self.laser_sound.set_volume(0.2)
            self.laser_sound.play()
            self.can_shoot = False

    def update(self):
        self.get_input()
        self.mouse_click()
        self.laser_timer()


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 600

    def update(self):
        self.pos += self.speed * dt * self.direction
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))


class Meteor(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.image.load('./graphics/meteor.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.3, 0.3), 1)
        self.speed = randint(400, 500)

    def update(self):
        self.pos += self.speed * self.direction * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))


class Score:
    def __init__(self):
        self.font = pygame.font.Font('./graphics/subatomic.ttf', 20)

    def display(self):
        total_score = 5
        text = f"SCORE: {total_score}"
        text_surf = self.font.render(text, True, (200, 200, 200))
        text_rect = text_surf.get_rect(center=((WINDOW_WIDTH - (WINDOW_WIDTH - 80)), 35))
        pygame.draw.rect(display_surface, (200, 200, 200), text_rect.inflate(30, 30), width=5, border_radius=10)
        display_surface.blit(text_surf, text_rect)


ship_group = pygame.sprite.GroupSingle()
ship = Ship(ship_group)

laser_group = pygame.sprite.Group()

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, randint(500, 600))
meteor_group = pygame.sprite.Group()

score = Score()

while True:

    clock = pygame.time.Clock()
    dt = clock.tick(120) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == meteor_timer:
            meteor_x_pos = randint(100, WINDOW_WIDTH-100)
            meteor_y_pos = randint(-150, -100)
            Meteor((meteor_x_pos, meteor_y_pos), meteor_group)

    display_surface.blit(back_ground, (0, 0))

    score.display()
    ship_group.draw(display_surface)
    laser_group.draw(display_surface)
    meteor_group.draw(display_surface)

    ship_group.update()
    laser_group.update()
    meteor_group.update()

    pygame.display.update()
