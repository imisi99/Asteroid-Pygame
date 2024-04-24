import sys
import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
surface = pygame.Surface((540, 360))
ship_movement = 620
ship_movement1 = 600
credit_movement = 580
credit_movement1 = 610
text_movement = 300

clock = pygame.time.Clock()

pygame.display.set_caption(title="Asteroid Shooter")
ship_surf = pygame.image.load("./graphics/ship.png").convert_alpha()
background = pygame.image.load("./graphics/background.png").convert()

font = pygame.font.Font("./graphics/subatomic.ttf", 70)
font_credit = pygame.font.Font("./graphics/subatomic.ttf", 20)
text = font.render("SPACE WARS", True, (200, 200, 200))
text_credit = font_credit.render("Created By : Imisioluwa Isong", True, (200, 200, 200))
text_credit1 = font_credit.render("Director : Ichigo Kurosaki", True, (200, 200, 200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock.tick(60)

    display_surface.fill((200, 200, 200))
    surface.fill("red")
    display_surface.blit(surface, (270, surface.get_height()/2))
    display_surface.blit(background, (0, 0))
    # ship_movement1 -= 1
    credit_movement -= 1
    credit_movement1 -= 1
    text_movement -= 1
    display_surface.blit(ship_surf, (ship_movement1, ship_movement))
    display_surface.blit(text, (400, text_movement))
    display_surface.blit(text_credit, (450, credit_movement))
    display_surface.blit(text_credit1, (480, credit_movement1))

    pygame.display.update()
