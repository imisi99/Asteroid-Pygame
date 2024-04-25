import sys
import pygame


def laser_update(laser_list, speed=70):
    for rect in laser_list:
        rect.y -= round(speed * dt)

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
# laser_rect = laser.get_rect(midbottom=ship_rect.midtop)
laser_list = []

font = pygame.font.Font("./graphics/subatomic.ttf", 70)
font_credit = pygame.font.Font("./graphics/subatomic.ttf", 20)

text = font.render("SPACE WARS", True, (200, 200, 200))
text_rect = text.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2)))

text_credit = font_credit.render("Created By : Imisioluwa Isong", True, (200, 200, 200))
text_credit_rect = text_credit.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 100))

text_credit1 = font_credit.render("Director : Ichigo Kurosaki", True, (200, 200, 200))
text_credit1_rect = text_credit1.get_rect(center=((WINDOW_WIDTH / 2), (WINDOW_HEIGHT / 2) + 150))

text_field_rect = pygame.rect.Rect(200, 200, 400, 400)
# test_rect = pygame.rect.Rect(300, 500, 200, 150)

while True:

    dt = (clock.tick(120)) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            laser_rect = laser.get_rect(midbottom=ship_rect.midtop)
            laser_list.append(laser_rect)

    display_surface.fill((200, 200, 200))
    display_surface.blit(background, (0, 0))

    # if ship_rect.y > 0:
    #     ship_rect.y -= 1

    if text_rect.y > -80:
        text_rect.y -= round(200 * dt)

    if text_credit_rect.y > -20:
        text_credit_rect.y -= round(200 * dt)

    if text_credit1_rect.y > -20:
        text_credit1_rect.y -= round(200 * dt)

    pygame.draw.rect(display_surface, "blue", text_rect.inflate(50, 30), width=7, border_radius=5)
    display_surface.blit(text, text_rect)
    display_surface.blit(text_credit, text_credit_rect)
    display_surface.blit(text_credit1, text_credit1_rect)

    if text_credit1_rect.y <= -20:

        ship_rect.center = pygame.mouse.get_pos()
        display_surface.blit(ship_surf, ship_rect)
        # pygame.draw.rect(display_surface, (200, 200, 200), test_rect, width=10, border_radius=5)
        # pygame.draw.lines(display_surface, (200, 200, 200), False, ((0, 0), (70, 100), (100, 160), (160, 250)), 5)
        for rect in laser_list:
            laser_update(laser_list)
            display_surface.blit(laser, rect)

    pygame.display.update()
