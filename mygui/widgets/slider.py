import pygame
from mygui import widgets, common

class Slider(widgets.Box):
    def __init__(self, master, position, size, bar_cornerradius, grip_length, grip_cornerradius,
                 bar_color, grip_color, bar_border_color, grip_border_color,
                 bar_border_width, grip_border_width, grip_orient="horizontal", bar_orient="horizontal",
                 min_value=0, max_value=100):
        super().__init__(master, size, position, bar_color, bar_border_color, bar_border_width, bar_cornerradius,
                         bar_orient)

        self.grip = widgets.Box(master, [grip_length]*2,
                                [x-y for x, y in zip(self.rect.midleft, [grip_length//2-1]*2)],
                                grip_color, grip_border_color, grip_border_width,
                                grip_cornerradius, grip_orient)

        self.grip.rect.inflate([grip_cornerradius*2]*2)

        self.min_value = min_value
        self.max_value = max_value
        self._value = 0

        self._active = False

    def trigger(self, mpos, mprd):
        is_between = self.rect.left < self.grip.rect.centerx < self.rect.right
        self._active = (self.grip.is_hover(mpos) and mprd[0] and is_between) or (self._active and mprd[0] and is_between)

        if not is_between:
            self.grip.rect.centerx = common.nearest_to(self.rect.left+1, self.rect.right-1, self.grip.rect.centerx)
        elif self._active:
            self.grip.rect.centerx = mpos[0]

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

        if self.grip.is_hover(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif not self.grip.is_hover(mpos) and not self.any_active(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def value(self):
        return self._value

    def place(self):
        super().place()
        self.grip.place()
