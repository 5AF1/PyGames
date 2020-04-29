import pygame
import os
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


def main():
    run = True
    FPS = 60

    clock = pygame.time.Clock()
    def redraw_window():
        #WIN.fill((0,0,0))
        WIN.blit(BG, (0,0))

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

def add(a,b):
    print(a+b)

main()