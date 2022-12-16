import pygame
from natrium.graphics import color
from pygame import gfxdraw
from natrium import common

class Ellipse(pygame.Surface):

    def __init__(self, surface, center, r1, r2, color, antialias=True, seperate_surface=True):
        super().__init__((r1*2+1, r2*2+1), pygame.SRCALPHA, 32)
        p1 = r1 if not seperate_surface else center[0]
        p2 = r2 if not seperate_surface else center[1]
        surf = self if not seperate_surface else surface

        if antialias:
            gfxdraw.aaellipse(surf, p1, p2, r1, r2, pygame.Color(color))
            gfxdraw.aaellipse(surf, p1, p2, r1, r2, pygame.Color(color))

        gfxdraw.filled_ellipse(surf, p1, p2, r1, r2, pygame.Color(color))

        self.surface = surface
        self.center = [center[0]-r1, center[1]-r2]

    def draw(self):
        self.surface.blit(self, self.center)

class EllipseGrad2(pygame.Surface):

    def __init__(self, surface, center, r1, r2, c1, c2, antialiase=True, orient="horizontal"):
        super().__init__((r1*2+1, r2*2+1), pygame.SRCALPHA, 32)
        grad_surf = color.Color2(c1, c2).gradient([r1*2+1, r2*2+1], orient)

        if antialiase:
            gfxdraw.aaellipse(self, r1, r2, r1, r2, [255]*4)
            gfxdraw.aaellipse(self, r1, r2, r1, r2, [255]*4)

        gfxdraw.filled_ellipse(self, r1, r2, r1, r2, [255]*4)

        self.surface = surface
        self.center = [center[0]-r1, center[1]-r2]

        self.blit(grad_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    def draw(self):
        self.surface.blit(self, self.center)

class EllipseGrad3(pygame.Surface):

    def __init__(self, surface, center, r1, r2, c1, c2, c3, antialiase=True, orient="horizontal"):
        super().__init__((r1*2+1, r2*2+1), pygame.SRCALPHA, 32)
        grad_surf = color.Color3(c1, c2, c3).gradient([r1*2+1, r2*2+1], orient)

        if antialiase:
            gfxdraw.aaellipse(self, r1, r2, r1, r2, [255]*4)
            gfxdraw.aaellipse(self, r1, r2, r1, r2, [255]*4)

        gfxdraw.filled_ellipse(self, r1, r2, r1, r2, [255]*4)

        self.surface = surface
        self.center = [center[0]-r1, center[1]-r2]


        self.blit(grad_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    def draw(self):
        self.surface.blit(self, self.center)

class DynamicEllipse:
    def __new__(cls, surface, center, r1, r2, colors, antialias=True, orient="horizontal"):
        if isinstance(colors[0], int) or common.is_str(colors) or isinstance(colors, pygame.Color):
            return Ellipse(surface, center, r1, r2, colors, antialias, orient)

        elif isinstance(colors[0], (list, tuple, pygame.Color, str)) and len(colors) == 2:
            return EllipseGrad2(surface, center, r1, r2, *colors, antialias, orient)

        elif isinstance(colors[0], (list, tuple, pygame.Color, str)) and len(colors) == 3:
            return EllipseGrad3(surface, center, r1, r2, *colors, antialias, orient)

        else:
            raise ValueError("Colors argument must be a Sequence[IsColor] with a length of 2-3 or a single color.")


def instant_ellipse(surface, center, r1, r2, color, antialias=True, seperate_surface=True):
    surf = Ellipse(surface, center, r1, r2, color, antialias, seperate_surface=seperate_surface)
    surf.draw()

def instant_ellipsegrad2(surface, center, r1, r2, c1, c2, antialias=True, orient="horizontal"):
    surf = EllipseGrad2(surface, center, r1, r2, c1, c2, antialias, orient)
    surf.draw()

def instant_ellipsegrad3(surface, center, r1, r2, c1, c2, c3, antialias=True, orient="horizontal"):
    surf = EllipseGrad3(surface, center, r1, r2, c1, c2, c3, antialias, orient)
    surf.draw()

def instant_dynamicellipse(surface, center, r1, r2, colors, antialias=True, orient="horizontal"):
    surf = DynamicEllipse(surface, center, r1, r2, colors, antialias, orient)
    surf.draw()

