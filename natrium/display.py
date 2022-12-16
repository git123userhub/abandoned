import pygame
import sys
from natrium import widgets, graphics

class Window:
    def __init__(self, size, background, gradial_orient='horizontal', title="Window", icon=None,
                 resizable=True):
        flags = pygame.SRCALPHA
        if resizable:
            flags |= pygame.RESIZABLE

        self._disp = pygame.display.set_mode(size, flags)
        pygame.display.set_caption(title)

        if icon:
            pygame.display.set_icon(pygame.image.load(icon))

        self.background = background
        self.gradial_orient = gradial_orient

        self._clock = pygame.time.Clock()
        self._events = []
        self._mpos = (0, 0)
        self._mprd = None

    def trigger(self):
        self._events = pygame.event.get()
        self._mpos = pygame.mouse.get_pos()
        self._mprd = pygame.mouse.get_pressed()

        for event in self._events:
            if event.type == pygame.QUIT:
                pygame.quit()

        self._disp.fill((0, 0, 0))
        graphics.draw.instant_dynamicrect(
            self._disp,
            pygame.Rect(0, 0, *self.get_size()),
            self.background,
            0,
            True,
            0,
            self.gradial_orient
        )

    def listen(self, widget):
        params = []

        if isinstance(widget, (widgets.InputBox, widgets.Button, widgets.ToggleButton)):
            params.append(self._events)

        params.append(self._mpos)

        if isinstance(widget, (widgets.Button, widgets.Slider)):
            params.append(self._mprd)

        widget.trigger(*params)

    def time_since_process(self):
        return pygame.time.get_ticks() / 1000

    def get_abs_offset(self):
        return self._disp.get_abs_offset()

    def get_size(self):
        return self._disp.get_size()

    def blit(self, surf, dest):
        self._disp.blit(surf, dest)

    def get_rate(self):
        return self._clock.get_fps()

    def refresh(self):
        pygame.display.update()
        self._clock.tick(62)
