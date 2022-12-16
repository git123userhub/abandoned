import pygame
from natrium import widgets, common, graphics

class Slider(widgets.Box):
    def __init__(self, master, position, anchor, size, grip_length, style,
                 min_value=0, max_value=100):
        super().__init__(master, size, position, anchor, style)

        grip_style = {'background': self['grip_color'],
                      'bordercolor': self['grip_bordercolor'],
                      'borderwidth': self['grip_borderwidth'],
                      'cornerradius': self['grip_cornerradius'],
                      'gradial_orient': self['grip_gradial_orient']}

        self.grip = widgets.Box(master, [grip_length]*2,
                                [x-y for x, y in zip(self.rect.midleft, [grip_length//2]*2)], anchor,
                                grip_style)

        self.grip.rect.inflate([self['grip_cornerradius']*2]*2)

        self.min_value = min_value
        self.max_value = max_value
        self._value = 0

        self._active = False

    def is_active(self):
        return self._active

    def trigger(self, mpos, mprd):
        is_between = self.rect.left-1 < self.grip.rect.centerx < self.rect.right+1
        self._active = (self.grip.is_hover(mpos) and mprd[0] and is_between) or (self._active and mprd[0] and is_between)

        if not is_between:
            self.grip.rect.centerx = common.nearest_to(self.rect.left+1, self.rect.right-1, self.grip.rect.centerx)
        elif self._active:
            self.grip.rect.centerx = max(min(mpos[0], self.rect.right), self.rect.left)

        self.grip.relpos[0] = self.grip.rect.x

        round_val = round(
                          (
                            (self.grip.rect.centerx - self.rect.x)
                            /
                            self.rect.width
                          )
                          *
                          (self.max_value-self.min_value)
                         )
        self._value = max(min(round_val+self.min_value, self.max_value), self.min_value)

        if self.is_hover(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif not self.is_hover(mpos) and not self.any_active(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def _return_rendering(self):
        pos = [self['bar_borderwidth']]*2
        size = [x-self['bar_borderwidth']*2 for x in self.rect.size]

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size),
                                              self['bar_color'],
                                              self['bar_cornerradius'],
                                              orient=self['bar_gradial_orient'])

        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size),
                                                self['bar_bordercolor'],
                                                self['bar_cornerradius'],
                                                orient=self['bar_gradial_orient'])

        return [main_body, border_rect]

    def is_hover(self, mpos):
        return self.grip.is_hover(mpos)

    def value(self):
        return self._value

    def place(self):
        super().place()
        self.grip.place()
