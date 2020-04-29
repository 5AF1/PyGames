import pygame
import os
from templates.surface import *

pygame.font.init()


WIDTH, HEIGHT = 750, 750
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

WIN = MSurface(pygame.display.set_mode((WIDTH, HEIGHT)))
pygame.display.set_caption("Space Shooter Tutorial")

def ma():
    title_font = pygame.font.SysFont("comicsansms", 50)
    run = True
    while run:
        WIN.blit(BG, (0, 0))
        title_label = title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        WIN.blit(title_label, (WIDTH / 2 - title_label.get_width() / 2, 350))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

ma()


