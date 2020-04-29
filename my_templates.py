import pygame

class MClock():
    def __init__(self, gclock):
        self.mclock = gclock

    def tick(self,fps):
        self.mclock.tick(fps)



class MSurface():
    def __init__(self, gsurface):
        self.msurface = gsurface

    def __str__(self):
        return "MSurface"

    def fill(self, color, rectstyle=None):
        self.msurface.fill(color, rectstyle)

    def blit(self, source, destpos, sourcerect=None):
        self.msurface.blit(source, destpos, sourcerect)
