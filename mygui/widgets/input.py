from mygui.widgets import Label
from mygui import common
import pygame

class InputBox(Label):
    def __init__(self, master, size, position, background, foreground, bordercolor, borderwidth, cornerradius,
                 default_text, text_anchor='topleft', text_margins=(0, 0), font: list[str, int, bool, bool]=(None, 20, 0, 0),
                 active_bg=None, active_fg=None, active_bc=None, multiline=False, orient="horizontal"):

        self.inactive_bg = background
        self.inactive_fg = foreground
        self.inactive_bc = bordercolor

        self.active_bg = active_bg if active_bg else background
        self.active_fg = active_fg if active_fg else foreground
        self.active_bc = active_bc if active_bc else bordercolor

        self._active = False
        self.multiline = multiline

        super().__init__(master, size, position, background, foreground, bordercolor,
                         borderwidth, cornerradius, default_text, text_anchor, text_margins, font, orient)

    def trigger(self, events, mpos):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(*event.pos) and event.button == 1:
                    self._active = not self._active

                else:
                    self._active = False

            if self._active:
                self.background = self.active_bg
                self.foreground = self.active_fg
                self.bordercolor = self.active_bc

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.string = self.string[0:-1]
                    elif event.key == pygame.K_DELETE:
                        self.string = ''
                    elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER] and self.multiline:
                        self.string += '\n'
                    else:
                        self.string = self.string + event.unicode if common.is_normal_text(event.unicode) else self.string

            else:
                self.background = self.inactive_bg
                self.foreground = self.inactive_fg
                self.bordercolor = self.inactive_bc

            if self.is_hover(mpos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

            elif not self.is_hover(mpos) and not self.any_active(mpos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def is_active(self):
        return self._active

