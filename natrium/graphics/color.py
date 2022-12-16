import pygame
from pygame import gfxdraw

class Color2:
    def __init__(self, color1, color2):
        self.color1 = pygame.Color(color1)
        self.color2 = pygame.Color(color2)

    def gradient(self, size, orient="horizontal"):
        if orient == "horizontal":
            gradient_surf = pygame.Surface((2, 1), pygame.SRCALPHA, 32)
            gfxdraw.pixel(gradient_surf, 0, 0, self.color1)
            gfxdraw.pixel(gradient_surf, 1, 0, self.color2)

        elif orient == "vertical":
            gradient_surf = pygame.Surface((1, 2), pygame.SRCALPHA, 32)
            gfxdraw.pixel(gradient_surf, 0, 0, self.color1)
            gfxdraw.pixel(gradient_surf, 0, 1, self.color2)

        else:
            return None

        gradient_surf = pygame.transform.smoothscale(gradient_surf, size)
        return gradient_surf

class Color3:
    def __init__(self, color1, color2, color3):
        self.color1 = pygame.Color(color1)
        self.color2 = pygame.Color(color2)
        self.color3 = pygame.Color(color3)

    def gradient(self, size, orient="horizontal"):
        if orient == "horizontal":
            gradient_surf = pygame.Surface((3, 1), pygame.SRCALPHA, 32)
            gfxdraw.pixel(gradient_surf, 0, 0, self.color1)
            gfxdraw.pixel(gradient_surf, 1, 0, self.color2)
            gfxdraw.pixel(gradient_surf, 2, 0, self.color3)

        elif orient == "vertical":
            gradient_surf = pygame.Surface((1, 3), pygame.SRCALPHA, 32)
            gfxdraw.pixel(gradient_surf, 0, 0, self.color1)
            gfxdraw.pixel(gradient_surf, 0, 1, self.color2)
            gfxdraw.pixel(gradient_surf, 0, 2, self.color3)

        else:
            return None

        gradient_surf = pygame.transform.smoothscale(gradient_surf, size)
        return gradient_surf
