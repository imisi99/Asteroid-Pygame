import sys
from random import randint
import pygame


def laser_update(laser_list, speed=300):
    for rect in laser_list:
        rect.y -= round(speed * dt)
        if rect.bottom < 0:
            laser_list.remove(rect)


def meteor_update(meteor_list, speed=400):
    for rect in meteor_list:
        rect.y += round(speed * dt)
        if rect.top > WINDOW_HEIGHT:
            meteor_list.remove(rect)


def score_display():
    display = f"SCORE: {len(laser_list)}"
    score = font_credit.render(display, True, (200, 200, 200))
    score_rect = score.get_rect(center=((WINDOW_WIDTH - (WINDOW_WIDTH-80)), 35))
    pygame.draw.rect(display_surface, (200, 200, 200), score_rect.inflate(30, 30), width=5, border_radius=10)
    display_surface.blit(score, score_rect)


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

text = font.render("SPACE WARS", True, (200, 200, 200))
text_rect = text.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))

text_credit = font_credit.render("Created By : Imisioluwa Isong", True, (200, 200, 200))
text_credit_rect = text_credit.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 100))

text_credit1 = font_credit.render("Director : Amaechi Daniel", True, (200, 200, 200))
text_credit1_rect = text_credit1.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 150))

can_shoot = True
shoot_time = False

meteor_timer = pygame.event.custom_type()
pygame.time.set_timer(meteor_timer, 500)

while True:

    dt = (clock.tick(120)) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and can_shoot:
            laser_rect = laser.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)
            can_shoot = False
            shoot_time = pygame.time.get_ticks()

        if event.type == meteor_timer and text_credit1_rect.y <= -20:
            x_pos = randint(100, WINDOW_WIDTH - 100)
            y_pos = randint(-50, -30)
            meteor_rect = meteor.get_rect(center=(x_pos, y_pos))
            meteor_list.append(meteor_rect)

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

        for rect in laser_list:
            display_surface.blit(laser, rect)

        for rect in meteor_list:
            display_surface.blit(meteor, rect)

    # Make it so that the ship doesn't shoot until it is in the bottom of the screen display
    # Congratulating player when he gets a particular high score
    # if len(laser_list) == 5:
    #     text_wow = font.render("Congratulations!", True, (200, 200, 200))
    #     text_wow_rect = text_wow.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))
    #     display_surface.blit(text_wow, text_wow_rect)
    #     pygame.draw.rect(display_surface, "red", text_wow_rect.inflate(50, 30), width=7, border_radius=5)

    pygame.display.update()
