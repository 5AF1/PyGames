import pygame


class MSurface():
    def __init__(self, gsurface):
        self.msurface = gsurface

    def fill(self, color, rectstyle=None):
        self.msurface.fill(color, rectstyle)

    def blit(self, source, destpos, sourcerect=None):
        self.msurface.blit(source, destpos, sourcerect)
