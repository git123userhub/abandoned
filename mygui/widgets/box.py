import pygame
from mygui import graphics, common, widgets

pygame.init()

class Box(pygame.Surface):
    instance_array = []

    def __init__(self, master, size, position, background, bordercolor, borderwidth, cornerradius, orient="horizontal"):
        super().__init__([x+2 for x in size], pygame.SRCALPHA, 32)

        self.master = master
        self.rect = pygame.Rect([x+y for x, y in zip(master.get_abs_offset(), position)], size)
        self.relpos = [x-y for x, y in zip(self.rect.topleft, master.get_abs_offset())]

        self.background = background
        self.bordercolor = bordercolor
        self.borderwidth = borderwidth
        self.cornerradius = cornerradius

        self.orient = orient
        Box.instance_array.append(self)

    def _return_rendering(self):
        pos = [self.borderwidth]*2
        size = [x-self.borderwidth*2 for x in self.rect.size]

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self.background, self.cornerradius-1,
                                              orient=self.orient)
        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self.bordercolor, self.cornerradius,
                                                orient=self.orient)

        return [main_body, border_rect]

    def _render(self):
        render_rect = self._return_rendering()

        render_rect[1].draw()
        render_rect[0].draw()

    def place(self):
        self.fill((0, 0, 0, 0))
        self._render()

        self.master.blit(self, self.relpos)

    def is_hover(self, mpos):
        return self.rect.collidepoint(*mpos)

    @classmethod
    def any_active(cls, mpos):
        return any([inst.is_hover(mpos)
                    for inst in cls.instance_array
                    if isinstance(inst, (widgets.Button, widgets.InputBox, widgets.ToggleButton, widgets.Slider))])


