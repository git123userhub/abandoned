from natrium.widgets import Box
from natrium import common, graphics
import pygame

class Label(Box):
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value
        self._render_text = graphics.render_multiline(self.font_object(), self.string, True, self['foreground'])

    @property
    def font(self):
        return self._font[0]

    @font.setter
    def font(self, value):
        self._font[0] = value
        self._font[1] = pygame.font.SysFont(*self.font[0])

    def __init__(self, master, size, position, anchor, style, text,
                     text_anchor='topleft', text_margins=(0, 0), font: list[str, int, bool, bool]=(None, 20, 0, 0)):
            if not issubclass(type(self), Label):
                if style['widget'] != "Label":
                    raise ValueError(f"Label does not support style of widget {style['widget']}")

            self._string = text
            self._font = [font, pygame.font.SysFont(*font)]
            self.text_margins = text_margins
            self.text_anchor = text_anchor

            super().__init__(master, size, position, anchor, style)
            self._render_const_style = self._return_rendering()
            self._render_const_text = graphics.render_multiline(self.font_object(), self.string, True, self['foreground'])

            self._render_text = graphics.render_multiline(self.font_object(), self.string, True, self['foreground'])

    def font_object(self):
        return self._font[1]

    def _render(self):
        pos = [self['borderwidth']]*2

        self._render_style = [self._render_const_style[0].main_surf.copy(),
                              self._render_const_style[1].main_surf.copy()]

        self.blit(self._render_style[1], (0, 0))

        self._render_style[0].blit(self._render_text,
                                   common.anchor_calculation(self._render_style[0],
                                                             self._render_text,
                                                             self.text_anchor,
                                                             *self.text_margins))

        self.blit(self._render_style[0], pos)
