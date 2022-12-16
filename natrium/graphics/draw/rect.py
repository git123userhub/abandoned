import pygame
from natrium.graphics.draw import ellipse
from natrium.graphics import color, transform
from natrium import common

class RoundRect:
    def __init__(self, surface, rect, color, radius=0, antialias=True, gaussian=0):
        self.main_surf = pygame.Surface([x+2 for x in rect.size], pygame.SRCALPHA, 32)

        if isinstance(radius, int):
            radius = [radius]*4

        elif isinstance(radius, (list, tuple)):
            if len(radius) == 2:
                radius *= 2
            elif len(radius) != 4:
                raise ValueError("Radius must be an integer or a list of 2 or 4 integers.")

        max_radius = max(*radius)

        deflated_rect = rect.inflate(-max_radius*2+1, -max_radius*2+1)
        deflated_rect.topleft = (radius[0], radius[0])

        if antialias:
            for i, pos in  \
            enumerate([deflated_rect.topleft, deflated_rect.topright,
                       deflated_rect.bottomleft, deflated_rect.bottomright]):
                ellipse.instant_ellipse(self.main_surf, pos, radius[i], radius[i], color)

        pygame.draw.rect(self.main_surf, color, pygame.Rect(0, 0, *[x+2 for x in rect.size]),
                         width=0,
                         border_top_left_radius=radius[0],
                         border_top_right_radius=radius[1],
                         border_bottom_left_radius=radius[2],
                         border_bottom_right_radius=radius[3]
                         )

        self.main_surf = transform.gaussian_blur_surface(self.main_surf, gaussian)

        self.surface = surface
        self.position = [x-gaussian*2 for x in rect.topleft]

    def blit(self, *args, **kwargs):
        self.main_surf.blit(*args, **kwargs)

    def get_size(self):
        return self.main_surf.get_size()

    def draw(self):
        self.surface.blit(self.main_surf, self.position)

    def fill(self, *args, **kwargs):
        self.main_surf.fill(*args, **kwargs)

class RoundRectGrad2:
    def __init__(self, surface, rect, c1, c2, radius=0, antialias=True, gaussian=0, orient="horizontal"):
        self.main_surf = pygame.Surface([x+2 for x in rect.size], pygame.SRCALPHA, 32)
        grad_surf = color.Color2(c1, c2).gradient([x+2+gaussian*4 for x in rect.size], orient)

        if isinstance(radius, int):
            radius = [radius]*4

        elif isinstance(radius, (list, tuple)):
            if len(radius) == 2:
                radius *= 2
            elif len(radius) != 4:
                raise ValueError("Radius must be an integer or a list of 2 or 4 integers.")

        max_radius = max(*radius)

        deflated_rect = rect.inflate(-max_radius*2+1, -max_radius*2+1)
        deflated_rect.topleft = (radius[0], radius[0])

        if antialias:
            for i, pos in \
                    enumerate([deflated_rect.topleft, deflated_rect.topright,
                               deflated_rect.bottomleft, deflated_rect.bottomright]):
                ellipse.instant_ellipse(self.main_surf, pos, radius[i], radius[i], [255]*4)

        pygame.draw.rect(self.main_surf, 'white', pygame.Rect(0, 0, *[x+2 for x in rect.size]),
                         width=0,
                         border_top_left_radius=radius[0],
                         border_top_right_radius=radius[1],
                         border_bottom_left_radius=radius[2],
                         border_bottom_right_radius=radius[3]
                         )

        self.surface = surface
        self.position = [x-(gaussian*2) for x in rect.topleft]

        self.main_surf = transform.gaussian_blur_surface(self.main_surf, gaussian)

        self.blit(grad_surf, [0, 0], special_flags=pygame.BLEND_RGBA_MIN)

    def blit(self, *args, **kwargs):
        self.main_surf.blit(*args, **kwargs)

    def get_size(self):
        return self.main_surf.get_size()

    def draw(self):
        self.surface.blit(self.main_surf, self.position)

    def fill(self, *args, **kwargs):
        self.main_surf.fill(*args, **kwargs)

class RoundRectGrad3:
    def __init__(self, surface, rect, c1, c2, c3, radius=0, antialias=True, gaussian=0, orient="horizontal"):
        self.main_surf = pygame.Surface([x+2 for x in rect.size], pygame.SRCALPHA, 32)
        grad_surf = color.Color3(c1, c2, c3).gradient([x+2+gaussian*4 for x in rect.size], orient)

        if isinstance(radius, int):
            radius = [radius]*4

        elif isinstance(radius, (list, tuple)):
            if len(radius) == 2:
                radius *= 2
            elif len(radius) != 4:
                raise ValueError("Radius must be an integer or a list of 2 or 4 integers.")

        max_radius = max(*radius)

        deflated_rect = rect.inflate(-max_radius*2+1, -max_radius*2+1)
        deflated_rect.topleft = (radius[0], radius[0])

        if antialias:
            for i, pos in \
                    enumerate([deflated_rect.topleft, deflated_rect.topright,
                               deflated_rect.bottomleft, deflated_rect.bottomright]):
                ellipse.instant_ellipse(self.main_surf, pos, radius[i], radius[i], [255]*4)

        pygame.draw.rect(self.main_surf, 'white', pygame.Rect(0, 0, *[x+2 for x in rect.size]),
                         width=0,
                         border_top_left_radius=radius[0],
                         border_top_right_radius=radius[1],
                         border_bottom_left_radius=radius[2],
                         border_bottom_right_radius=radius[3]
                         )

        self.surface = surface
        self.position = [x-gaussian*2 for x in rect.topleft]

        self.blit(grad_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)

    def blit(self, *args, **kwargs):
        self.main_surf.blit(*args, **kwargs)

    def get_size(self):
        return self.main_surf.get_size()

    def draw(self):
        self.surface.blit(self.main_surf, self.position)

    def fill(self, *args, **kwargs):
        self.main_surf.fill(*args, **kwargs)

class DynamicRect:
    def __new__(cls, surface, rect, colors, radius, antialias=True, gaussian=0, orient="horizontal"):
        if isinstance(colors[0], int) or common.is_str(colors) or isinstance(colors, pygame.Color):
            return RoundRect(surface, rect, colors, radius, antialias, gaussian)

        elif isinstance(colors[0], (list, tuple, pygame.Color, str)) and len(colors) == 2:
            return RoundRectGrad2(surface, rect, *colors, radius, antialias, gaussian, orient)

        elif isinstance(colors[0], (list, tuple, pygame.Color, str)) and len(colors) == 3:
            return RoundRectGrad3(surface, rect, *colors, radius, antialias, gaussian, orient)

        else:
            raise ValueError("Colors argument must be a Sequence[IsColor] with a length of 2-3 or a single color.")

def instant_rect(surface, rect, color, radius=0, gaussian=0, antialias=True):
    surf = RoundRect(surface, rect, color, radius, antialias, gaussian)
    surf.draw()

def instant_rectgrad2(surface, rect, c1, c2, radius=0, antialias=True, gaussian=0, orient="horizontal"):
    surf = RoundRectGrad2(surface, rect, c1, c2, radius, antialias, gaussian, orient)
    surf.draw()

def instant_rectgrad3(surface, rect, c1, c2, c3, radius=0, antialias=True, gaussian=0, orient="horizontal"):
    surf = RoundRectGrad3(surface, rect, c1, c2, c3, radius, antialias, gaussian, orient)
    surf.draw()

def instant_dynamicrect(surface, rect, colors, radius=0, antialias=True, gaussian=0, orient="horizontal"):
    surf = DynamicRect(surface, rect, colors, radius, antialias, gaussian, orient)
    surf.draw()