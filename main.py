import sys
from random import randint, uniform
import pygame


# Laser Movement
def laser_update(laser_list, speed=300):
    for rect in laser_list:
        rect.y -= round(speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect)


# Meteor Movement
def meteor_update(meteor_list, speed=400):
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rect = meteor_tuple[0]
        meteor_rect.center += direction * speed * dt
        if meteor_rect.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)
        if meteor_rect.right > WINDOW_WIDTH:
            meteor_list.remove(meteor_tuple)
        if meteor_rect.left < 0:
            meteor_list.remove(meteor_tuple)


# Score Display
def score_display():
    display = f"SCORE: {total_score}"
    score = font_credit.render(display, True, (200, 200, 200))
    score_rect = score.get_rect(center=((WINDOW_WIDTH - (WINDOW_WIDTH-80)), 35))
    pygame.draw.rect(display_surface, (200, 200, 200), score_rect.inflate(30, 30), width=5, border_radius=10)
    display_surface.blit(score, score_rect)


# Life Display
def life_display():
    display = f"LIFE: {life_left}"
    life = font_credit.render(display, True, (200, 200, 200))
    life_rect = life.get_rect(center=(WINDOW_WIDTH-80, 35))
    pygame.draw.rect(display_surface, (200, 200, 200), life_rect.inflate(30, 30), width=5, border_radius=10)
    display_surface.blit(life, life_rect)


# Shooting Timer
def shoot_timer(can_shoot_p, duration=500):
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


meteor = pygame.image.load("./graphics/meteor.png").convert_alpha()
meteor_list = []


font = pygame.font.Font("./graphics/subatomic.ttf", 70)
font_credit = pygame.font.Font("./graphics/subatomic.ttf", 20)


explosion_sound = pygame.mixer.Sound("./sounds/explosion.wav")
laser_sound = pygame.mixer.Sound("./sounds/laser.ogg")
background_sound = pygame.mixer.Sound("./sounds/music.wav")


text = font.render("SPACE WARS", True, (200, 200, 200))
text_rect = text.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))


text_credit = font_credit.render("Created By : Imisioluwa Isong", True, (200, 200, 200))
text_credit_rect = text_credit.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 100))


text_credit1 = font_credit.render("Director : Amaechi Daniel", True, (200, 200, 200))
text_credit1_rect = text_credit1.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 150))


can_shoot = True
shoot_time = False
life_left = 5
total_score = 0

# Meteor Timer init
meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

background_sound.play(-1)

while True:

    dt = (clock.tick(120)) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Tapping button to release laser
        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            # if ship_rect.center == [(0, WINDOW_WIDTH), (620, WINDOW_HEIGHT)]:
            laser_rect = laser.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)
            can_shoot = False
            shoot_time = pygame.time.get_ticks()
            laser_sound.play()

        # Automatic release of meteor
        if event.type == meteor_timer and text_credit1_rect.y <= -20:
            x_pos = randint(100, WINDOW_WIDTH - 100)
            y_pos = randint(-100, -50)
            meteor_rect = meteor.get_rect(center=(x_pos, y_pos))
            direction = pygame.math.Vector2(uniform(0.5, -0.5), 1)
            meteor_list.append((meteor_rect, direction))

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
        can_shoot = shoot_timer(can_shoot, 300)
        meteor_update(meteor_list)

        display_surface.blit(ship_surf, ship_rect)
        score_display()
        life_display()

        for rect in laser_list:
            display_surface.blit(laser, rect)

        for meteor_tuple in meteor_list:
            display_surface.blit(meteor, meteor_tuple[0])

        # Ship in contact with Meteor
        for meteor_tuple in meteor_list:
            meteor_rect = meteor_tuple[0]
            if meteor_rect.colliderect(ship_rect):
                meteor_list.remove(meteor_tuple)
                life_left -= 1

        # Laser Hitting Meteor
        for meteor_tuple in meteor_list:
            for laser_rect in laser_list:
                meteor_rect = meteor_tuple[0]
                if laser_rect.colliderect(meteor_rect):
                    laser_list.remove(laser_rect)
                    meteor_list.remove(meteor_tuple)
                    total_score += 1
                    explosion_sound.play()

        # Meteor Passing pass player to bottom of screen
        for meteor_tuple in meteor_list:
            meteor_rect = meteor_tuple[0]
            if meteor_rect.bottom > WINDOW_HEIGHT:
                life_left -= 1
                meteor_list.remove(meteor_tuple)

    # Congratulating player when he gets a particular high score
    if total_score == 50:
        text_wow = font.render("Congratulations!", True, (200, 200, 200))
        text_wow_rect = text_wow.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
        display_surface.blit(text_wow, text_wow_rect)
        pygame.draw.rect(display_surface, "red", text_wow_rect.inflate(50, 30), width=7, border_radius=5)
    if life_left < 0:
        break

    pygame.display.update()
