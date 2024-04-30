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

        self.mask = pygame.mask.from_surface(self.image)

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

    def collision(self):
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
            pass
        if pygame.sprite.spritecollide(self, bomb_group, True, pygame.sprite.collide_mask):
            pass
        if pygame.sprite.spritecollide(self, heart_group, True, pygame.sprite.collide_mask):
            pass
        if pygame.sprite.spritecollide(self, fuel_group, True, pygame.sprite.collide_mask):
            pass

    def update(self):
        self.get_input()
        self.mouse_click()
        self.laser_timer()
        self.collision()


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 800

        self.mask = pygame.mask.from_surface(self.image)

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
            self.kill()

    def update(self):
        self.pos += self.speed * dt * self.direction
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.meteor_collision()
        if self.rect.top < 0:
            self.kill()


class Meteor(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        meteor = pygame.image.load('./graphics/meteor.png').convert_alpha()
        meteor_scale = pygame.math.Vector2(meteor.get_size()) * uniform(1.0, 1.1)
        meteor_image = pygame.transform.scale(meteor, meteor_scale)
        self.image = meteor_image
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.3, 0.3), 1)
        self.speed = randint(400, 500)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.pos += self.speed * self.direction * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.bottom > WINDOW_HEIGHT:
            self.kill()
        if self.rect.left < 0:
            self.kill()
        if self.rect.right > WINDOW_WIDTH:
            self.kill()


class Bomb(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        bomb = pygame.image.load('./graphics/bomb.png').convert_alpha()
        self.image = bomb
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.15, 0.1), 1)
        self.speed = randint(400, 500)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.pos += self.speed * self.direction * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()


class Heart(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        heart = pygame.image.load('./graphics/heart.png').convert_alpha()
        self.image = heart
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.15, 0.1), 1)
        self.speed = randint(400, 500)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.pos += self.speed * self.direction * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()


class Fuel(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        fuel = pygame.image.load('./graphics/fuel.png').convert_alpha()
        self.image = fuel
        self.rect = self.image.get_rect(center=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(uniform(-0.15, 0.1), 1)
        self.speed = randint(400, 500)

        self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.pos += self.speed * self.direction * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        if self.rect.top > WINDOW_HEIGHT:
            self.kill()


class Rapid(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 1000

        self.mask = pygame.mask.from_surface(self.image)

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
            self.kill()

    def update(self):
        self.pos += self.speed * dt * self.direction
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.meteor_collision()
        if self.rect.top < 0:
            self.kill()


class Score:
    def __init__(self):
        self.font = pygame.font.Font('./graphics/subatomic.ttf', 20)
        self.total_score = 0

    def display(self):
        text = f"SCORE: {self.total_score}"
        text_surf = self.font.render(text, True, (200, 200, 200))
        text_rect = text_surf.get_rect(center=((WINDOW_WIDTH - (WINDOW_WIDTH - 80)), 35))
        pygame.draw.rect(display_surface, (200, 200, 200), text_rect.inflate(30, 30), width=5, border_radius=10)
        display_surface.blit(text_surf, text_rect)


class Life:
    def __init__(self):
        self.font = pygame.font.Font('./graphics/subatomic.ttf', 20)
        self.life_left = 5

    def display(self):
        text = f"LIFE: {self.life_left}"
        text_surf = self.font.render(text, True, (200, 200, 200))
        text_rect = text_surf.get_rect(center=((WINDOW_WIDTH-80), 35))
        pygame.draw.rect(display_surface, (200, 200, 200), text_rect.inflate(30, 30), width=5, border_radius=10)
        display_surface.blit(text_surf, text_rect)


ship_group = pygame.sprite.GroupSingle()
ship = Ship(ship_group)

laser_group = pygame.sprite.Group()

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, randint(500, 600))
meteor_group = pygame.sprite.Group()

bomb_timer = pygame.event.custom_type()
pygame.time.set_timer(bomb_timer, randint(4500, 5500))
bomb_group = pygame.sprite.Group()

heart_timer = pygame.event.custom_type()
pygame.time.set_timer(heart_timer, randint(17000, 20000))
heart_group = pygame.sprite.Group()

fuel_timer = pygame.event.custom_type()
pygame.time.set_timer(fuel_timer, randint(28000, 32000))
fuel_group = pygame.sprite.Group()

laser_timer = pygame.event.custom_type()
pygame.time.set_timer(laser_timer, randint(170, 200))
rapid_laser_group = pygame.sprite.Group()

score = Score()
life = Life()

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

        if event.type == bomb_timer:
            bomb_x_pos = randint(100, WINDOW_WIDTH-100)
            bomb_y_pos = randint(-150, -100)
            Bomb((bomb_x_pos, bomb_y_pos), bomb_group)

        if event.type == heart_timer:
            heart_x_pos = randint(100, WINDOW_WIDTH-100)
            heart_y_pos = randint(-150, -100)
            Heart((heart_x_pos, heart_y_pos), heart_group)

        if event.type == fuel_timer:
            fuel_x_pos = randint(100, WINDOW_WIDTH-100)
            fuel_y_pos = randint(-150, -100)
            Fuel((fuel_x_pos, fuel_y_pos), heart_group)

        if event.type == laser_timer:
            laser_x_pos = randint(10, WINDOW_WIDTH-10)
            laser_y_pos = randint(WINDOW_HEIGHT+50, WINDOW_HEIGHT+100)
            Rapid((laser_x_pos, laser_y_pos), rapid_laser_group)

    display_surface.blit(back_ground, (0, 0))

    ship_group.update()
    laser_group.update()
    meteor_group.update()
    bomb_group.update()
    heart_group.update()
    fuel_group.update()
    rapid_laser_group.update()

    score.display()
    life.display()

    ship_group.draw(display_surface)
    laser_group.draw(display_surface)
    meteor_group.draw(display_surface)
    bomb_group.draw(display_surface)
    heart_group.draw(display_surface)
    fuel_group.draw(display_surface)
    rapid_laser_group.draw(display_surface)

    pygame.display.update()
