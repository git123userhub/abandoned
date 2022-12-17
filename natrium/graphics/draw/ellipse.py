import pygame
from natrium import common
from pygame import gfxdraw
from natrium.graphics import color as colorfile

def render_ellipse(r1, r2, color, antialias=True):
    color = pygame.Color(color)
    main_surf = pygame.Surface([r1*2, r2*2], pygame.SRCALPHA, 32)

    if antialias:
        gfxdraw.aaellipse(main_surf, r1, r2, r1, r2, color)
        gfxdraw.aaellipse(main_surf, r1, r2, r1, r2, color)
    gfxdraw.filled_ellipse(main_surf, r1, r2, r1, r2, color)

    return main_surf

def render_ellipsegrad2(r1, r2, c1, c2, antialias=True, orient="horizontal"):
    main_surf = render_ellipse(r1, r2, [255, 255, 255, 255], antialias)
    grad_surf = colorfile.Color2(c1, c2).gradient([r1*2+2, r2*2+2], orient)

    main_surf.blit(grad_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    return main_surf

def render_ellipsegrad3(r1, r2, c1, c2, c3, antialias=True, orient="horizontal"):
    main_surf = render_ellipse(r1, r2, [255, 255, 255, 255], antialias)
    grad_surf = colorfile.Color3(c1, c2, c3).gradient([r1*2+2, r2*2+2], orient)

    main_surf.blit(grad_surf, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)
    return main_surf

def instant_ellipse(surface, center, r1, r2, color, antialias=True):
    main_surf = render_ellipse(r1, r2, color, antialias)
    surface.blit(main_surf, [x-y for x, y in zip(center, [r1, r2])])

def instant_ellipsegrad2(surface, center, r1, r2, color, antialias=True, orient="horizontal"):
    main_surf = render_ellipsegrad2(r1, r2, color, antialias, orient)
    surface.blit(main_surf, [x-y for x, y in zip(center, [r1, r2])])

def instant_ellipsegrad3(surface, center, r1, r2, color, antialias=True, orient="horizontal"):
    main_surf = render_ellipsegrad3(r1, r2, color, antialias, orient)
    surface.blit(main_surf, [x-y for x, y in zip(center, [r1, r2])])

def dynamic_render_ellipse(r1, r2, colors, antialias=True, orient="horizontal"):
    if isinstance(colors[0], int) or common.is_str(colors) or isinstance(colors, pygame.Color):
        return render_ellipse(r1, r2, colors, antialias)

    elif isinstance(colors[0], (list, tuple, pygame.Color, str)) and len(colors) == 2:
        return render_ellipsegrad2(r1, r2, *colors, antialias, orient)

    elif isinstance(colors[0], (list, tuple, pygame.Color, str)) and len(colors) == 3:
        return render_ellipsegrad3(r1, r2, *colors, antialias, orient)

    else:
        raise ValueError("Colors argument must be a Sequence[IsColor] with a length of 2-3 or a single color.")


def instant_dynamic_render_ellipse(surface, center, r1, r2, colors, antialias=True, orient="horizontal"):
    main_surf = dynamic_render_ellipse(r1, r2, colors, antialias, orient)
    surface.blit(main_surf, [x-y for x, y in zip(center, [r1, r2])])

