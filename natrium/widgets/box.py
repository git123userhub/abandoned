import pygame
from natrium import graphics, widgets, common

pygame.init()

class Box(pygame.Surface):
    instance_array = []

    def __init__(self, master, size, position, anchor, style):
        super().__init__([x+2 for x in size], pygame.SRCALPHA, 32)

        self.master = master
        anchor_calc = common.anchor_calculation(self.master, self, anchor, *position)
        self.rect = pygame.Rect(
                                [x+y for x, y in
                                 zip(master.get_abs_offset(), anchor_calc)
                                 ],
                                size)

        self.relpos = [x-y for x, y in zip(self.rect.topleft, master.get_abs_offset())]
        self.anchor = anchor

        self.style = style.copy()
        self._render_style = self._return_rendering()

        Box.instance_array.append(self)

    def _return_rendering(self):
        pos = [self['borderwidth']]*2
        size = [x-self['borderwidth']*2 for x in self.rect.size]

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self['background'], self['cornerradius'],
                                              orient=self['gradial_orient'])
        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self['bordercolor'], self['cornerradius'],
                                                orient=self['gradial_orient'])

        return [main_body, border_rect]

    def _render(self):
        # self._render_style = self._return_rendering()

        self._render_style[1].draw()
        self._render_style[0].draw()

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

    def __getitem__(self, item):
        return self.style[item]

    def __setitem__(self, key, value):
        self.style[key] = value


