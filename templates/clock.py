import pygame

class MClock():
    def __init__(self, gclock):
        self.mclock = gclock

    def tick(self,fps):
        self.mclock.tick(fps)
