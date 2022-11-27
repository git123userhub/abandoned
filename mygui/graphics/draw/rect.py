import pygame
from pygame import gfxdraw
from mygui.graphics.draw import ellipse
from mygui.graphics import color
from mygui import common

class RoundRect(pygame.Surface):
    def __init__(self, surface, rect, color, radius=0, antialias=True):
        super().__init__([x+2 for x in rect.size], pygame.SRCALPHA, 32)

        deflated_rect = rect.inflate(-radius*2+1, -radius*2+1)
        deflated_rect.topleft = (radius, radius)

        if antialias:
            for pos in [deflated_rect.topleft, deflated_rect.topright, deflated_rect.bottomleft, deflated_rect.bottomright]:
                ellipse.instant_ellipse(self, pos, radius, radius, color)

        pygame.draw.rect(self, color, pygame.Rect(0, 0, *[x+2 for x in rect.size]), border_radius=radius)

        self.surface = surface
        self.position = rect.topleft

    def draw(self):
        self.surface.blit(self, self.position)

class RoundRectGrad2(pygame.Surface):
    def __init__(self, surface, rect, c1, c2, radius=0, antialias=True, orient="horizontal"):
        super().__init__([x+2 for x in rect.size], pygame.SRCALPHA, 32)
        grad_surf = color.Color2(c1, c2).gradient([x+2 for x in rect.size], orient)

        deflated_rect = rect.inflate(-radius*2+1, -radius*2+1)
        deflated_rect.topleft = (radius, radius)

        if antialias:
            for pos in [deflated_rect.topleft, deflated_rect.topright, deflated_rect.bottomleft, deflated_rect.bottomright]:
                ellipse.instant_ellipse(self, pos, radius, radius, [255]*4, seperate_surface=False)

        pygame.draw.rect(self, "white", pygame.Rect(0, 0, *[x+2 for x in rect.size]), border_radius=radius)

        self.surface = surface
        self.position = rect.topleft

        self.blit(grad_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    def draw(self):
        self.surface.blit(self, self.position)

class RoundRectGrad3(pygame.Surface):
    def __init__(self, surface, rect, c1, c2, c3, radius=0, antialias=True, orient="horizontal"):
        super().__init__([x+2 for x in rect.size], pygame.SRCALPHA, 32)
        grad_surf = color.Color3(c1, c2, c3).gradient([x+2 for x in rect.size], orient)

        deflated_rect = rect.inflate(-radius*2+1, -radius*2+1)
        deflated_rect.topleft = (radius, radius)

        if antialias:
            for pos in [deflated_rect.topleft, deflated_rect.topright, deflated_rect.bottomleft, deflated_rect.bottomright]:
                ellipse.instant_ellipse(self, pos, radius, radius, [255]*4, seperate_surface=False)

        pygame.draw.rect(self, "white", pygame.Rect(0, 0, *[x+2 for x in rect.size]), border_radius=radius)

        self.surface = surface
        self.position = rect.topleft

        self.blit(grad_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    def draw(self):
        self.surface.blit(self, self.position)

class DynamicRect:
    def __new__(cls, surface, rect, colors, radius, antialias=True, orient="horizontal"):
        if isinstance(colors[0], int) or common.is_str(colors) or isinstance(colors, pygame.Color):
            return RoundRect(surface, rect, colors, radius, antialias)

        elif isinstance(colors[0], (list, tuple, pygame.Color, str)) and len(colors) == 2:
            return RoundRectGrad2(surface, rect, *colors, radius, antialias, orient)

        elif isinstance(colors[0], (list, tuple, pygame.Color, str)) and len(colors) == 3:
            return RoundRectGrad3(surface, rect, *colors, radius, antialias, orient)

        else:
            raise ValueError("Colors argument must be a Sequence[IsColor] with a length of 2-3 or a single color.")

def instant_rect(surface, rect, color, radius=0, antialias=True):
    surf = RoundRect(surface, rect, color, radius, antialias)
    surf.draw()

def instant_rectgrad2(surface, rect, c1, c2, radius=0, antialias=True, orient="horizontal"):
    surf = RoundRectGrad2(surface, rect, c1, c2, radius, antialias, orient)
    surf.draw()

def instant_rectgrad3(surface, rect, c1, c2, c3, radius=0, antialias=True, orient="horizontal"):
    surf = RoundRectGrad3(surface, rect, c1, c2, c3, radius, antialias, orient)
    surf.draw()

def instant_dynamicrect(surface, rect, colors, radius=0, antialias=True, orient="horizontal"):
    surf = DynamicRect(surface, rect, colors, radius, antialias, orient)
    surf.draw()