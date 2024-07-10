import pygame
import sys
from random import randint, uniform

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption("Asteroid Shooter")

back_ground = pygame.image.load("./graphics/background.png").convert_alpha()

total_score = 0


class Ship(pygame.sprite.Sprite):
    def __init__(self, group):
        super().__init__(group)

        self.image = pygame.image.load("./graphics/ship.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        self.can_shoot = True
        self.shoot_time = None
        self.laser_sound = pygame.mixer.Sound("./sounds/laser.ogg")
        self.font = pygame.font.Font('./graphics/subatomic.ttf', 20)
        self.life_left = 5
        self.total_score = 0
        self.has_fuel = False
        self.rapid_duration = 0

        self.mask = pygame.mask.from_surface(self.image)

    def congratulations(self):
        if self.total_score == 50:
            text_wow = self.font.render("WOW!", True, (200, 200, 200))
            text_wow_rect = text_wow.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
            display_surface.blit(text_wow, text_wow_rect)
            pygame.draw.rect(display_surface, "green", text_wow_rect.inflate(50, 30), width=7, border_radius=5)

        if self.total_score == 100:
            text_wow = self.font.render("AWESOME!!", True, (200, 200, 200))
            text_wow_rect = text_wow.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
            display_surface.blit(text_wow, text_wow_rect)
            pygame.draw.rect(display_surface, "green", text_wow_rect.inflate(50, 30), width=7, border_radius=5)

        if self.total_score == 150:
            text_wow = self.font.render("UNSTOPPABLE!!", True, (200, 200, 200))
            text_wow_rect = text_wow.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
            display_surface.blit(text_wow, text_wow_rect)
            pygame.draw.rect(display_surface, "green", text_wow_rect.inflate(50, 30), width=7, border_radius=5)

    def score_display(self):
        text = f"SCORE: {self.total_score}"
        text_surf = self.font.render(text, True, (200, 200, 200))
        text_rect = text_surf.get_rect(center=((WINDOW_WIDTH - (WINDOW_WIDTH - 80)), 35))
        pygame.draw.rect(display_surface, (200, 200, 200), text_rect.inflate(30, 30), width=5, border_radius=10)
        display_surface.blit(text_surf, text_rect)

    def life_display(self):
        text = f"LIFE: {self.life_left}"
        text_surf = self.font.render(text, True, (200, 200, 200))
        text_rect = text_surf.get_rect(center=((WINDOW_WIDTH - 80), 35))
        pygame.draw.rect(display_surface, (200, 200, 200), text_rect.inflate(30, 30), width=5, border_radius=10)
        display_surface.blit(text_surf, text_rect)

    def high_score_display(self):
        high_score = open('graphics/highscore.txt', 'r').read()
        if int(high_score) > self.total_score:
            text = f"High Score: {high_score}"
        else:
            text = f'New High Score: {self.total_score}'
        text_surf = self.font.render(text, True, (200, 200, 200))
        text_rect = text_surf.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) - 100))
        pygame.draw.rect(display_surface, (200, 200, 200), text_rect.inflate(30, 30), width=5, border_radius=10)
        display_surface.blit(text_surf, text_rect)

    def score_update(self):
        high_score = open('graphics/highscore.txt', 'r').read()
        if int(high_score) > self.total_score:
            pass
        else:
            new_score = open('graphics/highscore.txt', 'w')
            new_score.write(str(self.total_score))
            new_score.close()

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
            self.laser_sound.set_volume(0.1)
            self.laser_sound.play()
            self.can_shoot = False

    def collision(self):
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
            self.life_left -= 1
        if pygame.sprite.spritecollide(self, bomb_group, True, pygame.sprite.collide_mask):
            self.life_left -= 2
        if pygame.sprite.spritecollide(self, heart_group, True, pygame.sprite.collide_mask):
            self.life_left += 1
        if pygame.sprite.spritecollide(self, fuel_group, True, pygame.sprite.collide_mask):
            self.has_fuel = True
            self.rapid_duration = pygame.time.get_ticks() + 10000

    def update(self):
        self.get_input()
        self.mouse_click()
        self.laser_timer()
        self.collision()
        self.score_display()
        self.life_display()
        self.congratulations()
        if self.life_left < 0:
            self.high_score_display()
            self.score_update()


class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
        self.rect = self.image.get_rect(midbottom=pos)
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(0, -1)
        self.speed = 800
        self.collision_sound = pygame.mixer.Sound('./sounds/explosion.wav')

        self.mask = pygame.mask.from_surface(self.image)

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
            self.collision_sound.set_volume(0.15)
            self.collision_sound.play()
            ship.total_score += 1
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
            ship.life_left -= 1
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
        self.speed = 1500
        self.collision_sound = pygame.mixer.Sound('./sounds/explosion.wav')

        self.mask = pygame.mask.from_surface(self.image)

    def meteor_collision(self):
        if pygame.sprite.spritecollide(self, meteor_group, True, pygame.sprite.collide_mask):
            self.collision_sound.set_volume(0.2)
            self.collision_sound.play()
            self.kill()
            ship.total_score += 1

    def update(self):
        self.pos += self.speed * dt * self.direction
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.meteor_collision()
        if self.rect.top < 0:
            self.kill()


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
pygame.time.set_timer(fuel_timer, randint(29000, 31000))
fuel_group = pygame.sprite.Group()

laser_timer = pygame.event.custom_type()
pygame.time.set_timer(laser_timer, randint(170, 200))
rapid_laser_group = pygame.sprite.Group()

back_ground_sound = pygame.mixer.Sound('./sounds/music.wav')
back_ground_sound.set_volume(0.1)
back_ground_sound.play(-1)

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
            Fuel((fuel_x_pos, fuel_y_pos), fuel_group)

        if event.type == laser_timer and ship.has_fuel and pygame.time.get_ticks() < ship.rapid_duration:
            laser_x_pos = randint(10, WINDOW_WIDTH-10)
            laser_y_pos = randint(WINDOW_HEIGHT+50, WINDOW_HEIGHT+100)
            Rapid((laser_x_pos, laser_y_pos), rapid_laser_group)

    if pygame.time.get_ticks() >= ship.rapid_duration and ship.life_left >= 0:
        ship.has_fuel = False

    if ship.life_left >= 0:
        display_surface.blit(back_ground, (0, 0))

        ship_group.update()
        laser_group.update()
        meteor_group.update()
        bomb_group.update()
        heart_group.update()
        fuel_group.update()
        rapid_laser_group.update()

        rapid_laser_group.draw(display_surface)
        ship_group.draw(display_surface)
        laser_group.draw(display_surface)
        meteor_group.draw(display_surface)
        bomb_group.draw(display_surface)
        heart_group.draw(display_surface)
        fuel_group.draw(display_surface)

    if ship.life_left < 0:
        font = pygame.font.Font('./graphics/subatomic.ttf', 20)
        text_fail = font.render("Game Over Press P to play again or Q to quit the game", True, (200, 200, 200))
        text_fail_rect = text_fail.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
        display_surface.blit(text_fail, text_fail_rect)
        pygame.draw.rect(display_surface, "red", text_fail_rect.inflate(50, 30), width=7, border_radius=5)
        keys = pygame.key.get_pressed()

        if keys[pygame.K_p]:
            ship.life_left = 5
            ship.total_score = 0
            ship.has_fuel = False

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

        elif keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    pygame.display.update()
