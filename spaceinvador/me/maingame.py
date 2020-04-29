import pygame.event
import os
import random
import time
from my_templates import *
from ships_and_laser import *

class MainGame():
    def __init__(self):
        pygame.init()

        self.WIDTH, self.HEIGHT = 750, 750

        self.redraw_func = self.main_menu
        self.update_func = self.main_menu_event
        self.return_func = pygame.quit

        self.WINDOW_SIZE = (self.WIDTH, self.HEIGHT)
        self.asset_load()

        self.GAME_WINDOW = MSurface(pygame.display.set_mode(self.WINDOW_SIZE))
        pygame.display.set_caption("Space Invador")
        pygame.display.set_icon(self.YELLOW_SPACE_SHIP)

        self.title_font = pygame.font.SysFont("comicsansms",50)

        self.loop()



    def simloop(self):
        title_font = pygame.font.SysFont("comicsansms", 50)
        while self.run:
            self.clock.tick(self.FPS)

            self.GAME_WINDOW.blit(self.BG, (0, 0))
            title_label = title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
            self.GAME_WINDOW.blit(title_label, (self.WIDTH / 2 - title_label.get_width() / 2, 350))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

        pygame.quit()


    def asset_load(self):

        # Load images
        self.RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
        self.GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
        self.BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

        # Player player
        self.YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

        # Lasers
        self.RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
        self.GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
        self.BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
        self.YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

        # Background
        self.BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (self.WIDTH, self.HEIGHT))
        #self.BACKGROUND = pygame.image.load(os.path.join("assets", "background-black.png"))

        self.YELLOW ={
            #'x': self.WIDTH/2,
            #'y': self.HEIGHT,
            'x': 300,
            'y': 630,
            'win_dim': self.WINDOW_SIZE,

            'ship': self.YELLOW_SPACE_SHIP,
            'laser': self.YELLOW_LASER,

            'health': 100,
            'vel':6,
            'laser_vel':10,
            'cool':1,
            'heat':15,

        }
        self.RED = {
            'x_range': [300, 300],
            'y_range': [630, 630],
            'win_dim': self.WINDOW_SIZE,

            'ship': self.RED_SPACE_SHIP,
            'laser': self.RED_LASER,

            'health': 100,
            'vel': 6,
            'laser_vel': 10,
            'cool': 1,
            'heat': 15,
        }
        self.GREEN = {
            'x_range': [300, 300],
            'y_range': [630, 630],
            'win_dim': self.WINDOW_SIZE,

            'ship': self.GREEN_SPACE_SHIP,
            'laser': self.GREEN_LASER,

            'health': 100,
            'vel': 6,
            'laser_vel': 10,
            'cool': 1,
            'heat': 15,
        }
        self.BLUE = {
            'x_range': [300, 300],
            'y_range': [630, 630],
            'win_dim': self.WINDOW_SIZE,

            'ship': self.BLUE_SPACE_SHIP,
            'laser': self.BLUE_LASER,

            'health': 100,
            'vel': 6,
            'laser_vel': 10,
            'cool': 1,
            'heat': 15,
        }


    def main_menu(self):
        self.GAME_WINDOW.fill((0, 0, 0))
        self.GAME_WINDOW.blit(self.BG, (0, 0))

        title_label = self.title_font.render("Press the mouse to begin...", 1, (255, 255, 255))
        self.GAME_WINDOW.blit(title_label, (self.WIDTH / 2 - title_label.get_width() / 2, 350))

        pygame.display.update()

    def main_menu_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.set_main_game()


    def set_main_game(self):
        self.redraw_func = self.main_game
        self.update_func = self.main_game_event

        self.main_font = pygame.font.SysFont("comicsansms", 50)
        self.lost_font = pygame.font.SysFont("comicsansms", 60)


        self.player = Player(self.YELLOW)
        self.enemies = []

    def main_game(self):
        self.GAME_WINDOW.fill((0, 0, 0))
        self.GAME_WINDOW.blit(self.BG, (0, 0))
        self.player.draw(self.GAME_WINDOW)



        pygame.display.update()


    def main_game_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.player.move(-self.player.velocity,0)
        if keys[pygame.K_d]:
            self.player.move(self.player.velocity, 0)
        if keys[pygame.K_w]:
            self.player.move(0,-self.player.velocity)
        if keys[pygame.K_s]:
            self.player.move(0, self.player.velocity)
        if keys[pygame.K_SPACE]:
            self.player.shoot()



    def loop(self):
        self.run = True
        self.FPS = 60
        self.clock = MClock(pygame.time.Clock())
        while self.run:
            self.clock.tick(self.FPS)
            self.redraw_func()
            self.update_func()

        pygame.quit()



a = MainGame()
