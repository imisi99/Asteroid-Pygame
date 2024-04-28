import sys
from random import randint, uniform
import pygame


# Laser Movement
def laser_update(laser_list_1, speed=500):
    for rect_1 in laser_list_1:
        rect_1.y -= round(speed * dt)
        if rect_1.bottom < 0:
            laser_list_1.remove(rect_1)


# Rapid Laser Movement
def rapid_laser_update(laser_list_2, speed=500):
    item_to_remove = []
    for rect_1 in laser_list_2:
        rect_1.y -= round(speed * dt)
        if rect_1.top < 0:
            item_to_remove.append(rect_1)
    for item in item_to_remove:
        laser_list_2.remove(item)


# Meteor Movement
def meteor_update(meteor_list_1, speed=400):
    for meteor_tuple_1 in meteor_list_1:
        direction_1 = meteor_tuple_1[1]
        meteor_rect_1 = meteor_tuple_1[0]
        meteor_rect_1.center += direction_1 * speed * dt
        if meteor_rect_1.top > WINDOW_HEIGHT:
            meteor_list_1.remove(meteor_tuple_1)
        if meteor_rect_1.right > WINDOW_WIDTH:
            meteor_list_1.remove(meteor_tuple_1)
        if meteor_rect_1.left < WINDOW_WIDTH - WINDOW_WIDTH:
            meteor_list_1.remove(meteor_tuple_1)


# Bomb Movement
def bomb_update(bomb_list_1, speed=400):
    for bomb_tuple_1 in bomb_list_1:
        direction_1 = bomb_tuple_1[1]
        bomb_rect_1 = bomb_tuple_1[0]
        bomb_rect_1.center += direction_1 * speed * dt
        if bomb_rect_1.top > WINDOW_HEIGHT:
            bomb_list_1.remove(bomb_tuple_1)
        if bomb_rect_1.right > WINDOW_WIDTH:
            bomb_list_1.remove(bomb_tuple_1)
        if bomb_rect_1.left < 0:
            bomb_list_1.remove(bomb_tuple_1)


# Heart Movement
def heart_update(heart_list_1, speed=400):
    for heart_tuple_1 in heart_list_1:
        direction_1 = heart_tuple_1[1]
        heart_rect_1 = heart_tuple_1[0]
        heart_rect_1.center += direction_1 * speed * dt
        if heart_rect_1.top > WINDOW_HEIGHT:
            heart_list_1.remove(heart_tuple_1)
        if heart_rect_1.right > WINDOW_WIDTH:
            heart_list_1.remove(heart_tuple_1)
        if heart_rect_1.left < 0:
            heart_list_1.remove(heart_tuple_1)


# Fuel Movement
def fuel_movement(fuel_list_1, speed=400):
    for fuel_tuple_1 in fuel_list_1:
        direction_1 = fuel_tuple_1[1]
        fuel_rect_1 = fuel_tuple_1[0]
        fuel_rect_1.center += direction_1 * speed * dt
        if fuel_rect_1.top > WINDOW_HEIGHT:
            fuel_list_1.remove(fuel_tuple_1)
        if fuel_rect_1.right > WINDOW_WIDTH:
            fuel_list_1.remove(fuel_tuple_1)
        if fuel_rect_1.left < 0:
            fuel_list_1.remove(fuel_tuple_1)


# Score Display
def score_display():
    display = f"SCORE: {total_score}"
    score = font_credit.render(display, True, (200, 200, 200))
    score_rect = score.get_rect(center=((WINDOW_WIDTH - (WINDOW_WIDTH - 80)), 35))
    pygame.draw.rect(display_surface, (200, 200, 200), score_rect.inflate(30, 30), width=5, border_radius=10)
    display_surface.blit(score, score_rect)


# Life Display
def life_display():
    display = f"LIFE: {life_left}"
    life = font_credit.render(display, True, (200, 200, 200))
    life_rect = life.get_rect(center=(WINDOW_WIDTH - 80, 35))
    pygame.draw.rect(display_surface, (200, 200, 200), life_rect.inflate(30, 30), width=5, border_radius=10)
    display_surface.blit(life, life_rect)


# Shooting Timer
def shoot_timer(can_shoot_p, duration=0):
    if not can_shoot_p:
        current_time = pygame.time.get_ticks()
        if duration < current_time - shoot_time:
            can_shoot_p = True
    return can_shoot_p


pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

pygame.display.set_caption(title="Asteroid Shooter")
background = pygame.image.load("./graphics/background.png").convert()

ship_surf = pygame.image.load("./graphics/ship.png").convert_alpha()
ship_rect = ship_surf.get_rect(center=(WINDOW_WIDTH / 2, (WINDOW_HEIGHT - 100)))
ship_flip = pygame.transform.flip(ship_surf, False, True)

laser = pygame.image.load("./graphics/laser.png").convert_alpha()
laser_list = []
laser_list_p = []

meteor = pygame.image.load("./graphics/meteor.png").convert_alpha()
meteor_list = []

heart = pygame.image.load("./graphics/heart.png").convert_alpha()
heart_list = []

bomb = pygame.image.load("./graphics/bomb.png").convert_alpha()
bomb_list = []

fuel = pygame.image.load("./graphics/fuel.png").convert_alpha()
fuel_list = []

font = pygame.font.Font("./graphics/subatomic.ttf", 70)
font_credit = pygame.font.Font("./graphics/subatomic.ttf", 20)

explosion_sound = pygame.mixer.Sound("./sounds/explosion.wav")
laser_sound = pygame.mixer.Sound("./sounds/laser.ogg")
background_sound = pygame.mixer.Sound("./sounds/music.wav")

text = font.render("SPACE WARS", True, (200, 200, 200))
text_rect = text.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))

text_credit = font_credit.render("Created By : Imisioluwa Isong", True, (200, 200, 200))
text_credit_rect = text_credit.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 100))

text_credit1 = font_credit.render("Idea BY : Uchiha Madara", True, (200, 200, 200))
text_credit1_rect = text_credit1.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 150))

can_shoot = True
rapid = True
shoot_time = False
life_left = 5
total_score = 0

# Timer init
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

heart_timer = pygame.event.custom_type()
pygame.time.set_timer(heart_timer, 20000)

bomb_timer = pygame.event.custom_type()
pygame.time.set_timer(bomb_timer, 5000)

laser_timer = pygame.event.custom_type()
pygame.time.set_timer(laser_timer, 100)

fuel_timer = pygame.event.custom_type()
pygame.time.set_timer(fuel_timer, 30000)

background_sound.play(-1)
background_sound.set_volume(0.1)
has_fuel = False

while True:

    dt = (clock.tick(120)) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Tapping button to release laser
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot and text_credit1_rect.y <= -20 and life_left >= 0:
            # if ship_rect.center == [(0, WINDOW_WIDTH), (620, WINDOW_HEIGHT)]:
            laser_rect = laser.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
            laser_sound.play()
            laser_sound.set_volume(0.2)

        # Automatic release of meteor
        if event.type == meteor_timer and text_credit1_rect.y <= -20 and life_left >= 0:
            x_pos = randint(100, WINDOW_WIDTH - 100)
            y_pos = randint(-100, -50)
            meteor_rect = meteor.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(0.3, -0.3), 1)
            meteor_list.append((meteor_rect, direction))

        if event.type == laser_timer and text_credit1_rect.y <= -20:
            if has_fuel:
                x_pos = randint(0, WINDOW_WIDTH)
                y_pos = randint(WINDOW_HEIGHT - 10, WINDOW_HEIGHT)
                laser_rect_p = laser.get_rect(center=(x_pos, y_pos))
                laser_list_p.append(laser_rect_p)
                rapid_laser_update(laser_list_p)

        # Automatic release of the life
        if event.type == heart_timer and text_credit1_rect.y <= -20 and life_left >= 0:
            x_pos = randint(100, WINDOW_WIDTH - 100)
            y_pos = randint(-100, -50)
            heart_rect = heart.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(0., -0.0), 1)
            heart_list.append((heart_rect, direction))

        # Automatic release of bomb
        if event.type == bomb_timer and text_credit1_rect.y <= -20 and life_left >= 0:
            x_pos = randint(100, WINDOW_WIDTH - 100)
            y_pos = randint(-100, -50)
            bomb_rect = bomb.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(0.0, -0.0), 1)
            bomb_list.append((bomb_rect, direction))

        # Automatic release of fuel
        if event.type == fuel_timer and text_credit1_rect.y <= -20 and life_left >= 0:
            x_pos = randint(100, WINDOW_WIDTH - 100)
            y_pos = randint(-100, -50)
            fuel_rect = fuel.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(0.0, -0.0), 1)
            fuel_list.append((fuel_rect, direction))
    if life_left >= 0:
        display_surface.fill((255, 255, 255))
        display_surface.blit(background, (0, 0))

        if text_rect.y > -80:
            text_rect.y -= round(150 * dt)

        if text_credit_rect.y > -20:
            text_credit_rect.y -= round(150 * dt)

        if text_credit1_rect.y > -20:
            text_credit1_rect.y -= round(150 * dt)

        pygame.draw.rect(display_surface, "blue", text_rect.inflate(50, 30), width=7, border_radius=5)
        display_surface.blit(text, text_rect)
        display_surface.blit(text_credit, text_credit_rect)
        display_surface.blit(text_credit1, text_credit1_rect)

        if text_credit1_rect.y <= -20:

            ship_rect.center = pygame.mouse.get_pos()

            laser_update(laser_list)
            score_display()
            can_shoot = shoot_timer(can_shoot, 250)

            meteor_update(meteor_list)
            heart_update(heart_list)
            bomb_update(bomb_list)
            fuel_movement(fuel_list)

            display_surface.blit(ship_surf, ship_rect)
            score_display()
            life_display()

            for rect in laser_list:
                display_surface.blit(laser, rect)

            for meteor_tuple in meteor_list:
                display_surface.blit(meteor, meteor_tuple[0])

            for bomb_tuple in bomb_list:
                display_surface.blit(bomb, bomb_tuple[0])

            for heart_tuple in heart_list:
                display_surface.blit(heart, heart_tuple[0])

            for fuel_tuple in fuel_list:
                display_surface.blit(fuel, fuel_tuple[0])

            for laser_rect_p in laser_list_p:
                rapid_laser_update(laser_list_p)
                display_surface.blit(laser, laser_rect_p)

            # Ship in contact with Meteor
            for meteor_tuple in meteor_list:
                meteor_rect = meteor_tuple[0]
                if meteor_rect.colliderect(ship_rect):
                    meteor_list.remove(meteor_tuple)
                    life_left -= 1

            # Ship in contact with Bomb
            for bomb_tuple in bomb_list:
                bomb_rect = bomb_tuple[0]
                if bomb_rect.colliderect(ship_rect):
                    bomb_list.remove(bomb_tuple)
                    life_left -= 2

            # Laser Hitting Meteor
            for meteor_tuple in meteor_list:
                for laser_rect in laser_list:
                    meteor_rect = meteor_tuple[0]
                    if laser_rect.colliderect(meteor_rect):
                        laser_list.remove(laser_rect)
                        meteor_list.remove(meteor_tuple)
                        total_score += 1
                        explosion_sound.play()
                        explosion_sound.set_volume(0.2)

            # Meteor Passing pass player to bottom of screen
            for meteor_tuple in meteor_list:
                meteor_rect = meteor_tuple[0]
                if meteor_rect.bottom > WINDOW_HEIGHT:
                    life_left -= 1
                    meteor_list.remove(meteor_tuple)

            # Ship hitting heart for life
            for heart_tuple in heart_list:
                heart_rect = heart_tuple[0]
                if heart_rect.colliderect(ship_rect):
                    heart_list.remove(heart_tuple)
                    if life_left < 5:
                        life_left += 1

            # Ship hitting fuel for rapid fire
            for fuel_tuple in fuel_list:
                fuel_rect = fuel_tuple[0]
                if fuel_rect.colliderect(ship_rect):
                    fuel_list.remove(fuel_tuple)
                    has_fuel = True

            for laser_rect_p in laser_list_p:
                for meteor_tuple in meteor_list:
                    meteor_rect = meteor_tuple[0]
                    if laser_rect_p.colliderect(meteor_rect):
                        laser_list_p.remove(laser_rect_p)
                        meteor_list.remove(meteor_tuple)
                        total_score += 1
                        explosion_sound.play()
                        explosion_sound.set_volume(0.2)

        # Congratulating player when he gets a particular high score
        if total_score == 50:
            text_wow = font.render("WOW!", True, (200, 200, 200))
            text_wow_rect = text_wow.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
            display_surface.blit(text_wow, text_wow_rect)
            pygame.draw.rect(display_surface, "green", text_wow_rect.inflate(50, 30), width=7, border_radius=5)

        if total_score == 100:
            text_wow = font.render("KILLING IT!!", True, (200, 200, 200))
            text_wow_rect = text_wow.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
            display_surface.blit(text_wow, text_wow_rect)
            pygame.draw.rect(display_surface, "green", text_wow_rect.inflate(50, 30), width=7, border_radius=5)

    if life_left < 0:
        score_display()
        text_fail = font_credit.render("Game Over Press P to play again or Q to quit the game", True, (200, 200, 200))
        text_fail_rect = text_fail.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
        display_surface.blit(text_fail, text_fail_rect)
        pygame.draw.rect(display_surface, "red", text_fail_rect.inflate(50, 30), width=7, border_radius=5)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_p]:
            life_left = 5
            total_score = 0
            laser_list = []
            meteor_list = []
            heart_list = []
            bomb_list = []
            fuel_list = []
        elif keys[pygame.K_q]:
            pygame.quit()
            sys.exit()

    pygame.display.update()
