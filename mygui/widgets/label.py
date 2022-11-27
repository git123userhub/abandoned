from mygui.widgets import Box
from mygui import common, graphics
import pygame

class Label(Box):
    def __init__(self, master, size, position, background, foreground, bordercolor, borderwidth, cornerradius,
                 text, text_anchor='topleft', text_margins=(0, 0), font: list[str, int, bool, bool]=(None, 20, 0, 0),
                 orient="horizontal"):

        self.string = text
        self.font = font
        self.foreground = foreground
        self.margins = text_margins
        self.anchor = text_anchor

        super().__init__(master, size, position, background, bordercolor, borderwidth, cornerradius, orient)

    def _render(self):
        render_rect = self._return_rendering()

        render_rect[1].draw()

        text_surf = graphics.render_multiline(pygame.font.SysFont(*self.font), self.string, True, self.foreground)
        render_rect[0].blit(text_surf, common.anchor_calculation(render_rect[0], text_surf, self.anchor, *self.margins))

        render_rect[0].draw()
