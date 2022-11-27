import pygame
from mygui.widgets import Label
from mygui import graphics

class Button(Label):
    def __init__(self, master, size, position, background, foreground, bordercolor, borderwidth, cornerradius,
                 text, text_anchor='topleft', text_margins=(0, 0), font: list[str, int, bool, bool]=(None, 20, 0, 0),
                 hover_bg=None, hover_fg=None, hover_bc=None, active_bg=None, active_fg=None, active_bc=None,
                 command=lambda: None, click_once=True, orient="horizontal"):

        self.inactive_bg = background
        self.inactive_fg = foreground
        self.inactive_bc = bordercolor

        self.active_bg = active_bg if active_bg else background
        self.active_fg = active_fg if active_fg else foreground
        self.active_bc = active_bc if active_bc else bordercolor

        self.hover_bg = hover_bg if hover_bg else background
        self.hover_fg = hover_fg if hover_fg else foreground
        self.hover_bc = hover_bc if hover_bc else bordercolor

        self._onclick = False

        self.command = command
        self.click_once = click_once

        super().__init__(master, size, position, background, foreground, bordercolor,
                         borderwidth, cornerradius, text, text_anchor, text_margins, font, orient)

    def trigger(self, events, mpos, mprd):
        self._onclick = False
        if self.click_once:
            for event in events:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.rect.collidepoint(*event.pos) and event.button == 1:
                            self._onclick = True
                            self.command()

        if self.rect.collidepoint(*mpos):
            self.background = self.hover_bg
            self.foreground = self.hover_fg
            self.bordercolor = self.hover_bc

            if mprd[0]:
                self.background = self.active_bg
                self.foreground = self.active_fg
                self.bordercolor = self.active_bc
                self._onclick = True

                if not self.click_once: self.command()

        else:
            self.background = self.inactive_bg
            self.foreground  = self.inactive_fg
            self.bordercolor = self.inactive_bc

        if self.is_hover(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif not self.is_hover(mpos) and not self.any_active(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def onclick(self):
        return self._onclick

class ToggleButton(Label):
    def __init__(self, master, size, position, background, foreground, bordercolor, borderwidth, cornerradius,
                 text, text_anchor='topleft', text_margins=(0, 0), font: list[str, int, bool, bool]=(None, 20, 0, 0),
                 active_bg=None, active_fg=None, active_bc=None,
                 command=lambda: None, orient="horizontal"):

        self.inactive_bg = background
        self.inactive_fg = foreground
        self.inactive_bc = bordercolor

        self.active_bg = active_bg if active_bg else background
        self.active_fg = active_fg if active_fg else foreground
        self.active_bc = active_bc if active_bc else bordercolor
        self._active = False
        self._onclick = False

        self.command = command

        super().__init__(master, size, position, background, foreground, bordercolor,
                         borderwidth, cornerradius, text, text_anchor, text_margins, font, orient)

    def trigger(self, events, mpos):
        self._onclick = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(*event.pos) and event.button == 1:
                    self._active = not self._active
                    self._onclick = True

        if self._active:
            self.background = self.active_bg
            self.foreground = self.active_fg
            self.bordercolor = self.active_bc
            self.command()

        else:
            self.background = self.inactive_bg
            self.foreground = self.inactive_fg
            self.bordercolor = self.inactive_bc

        if self.is_hover(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif not self.is_hover(mpos) and not self.any_active(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def on_click(self):
        return self._onclick

    def is_active(self):
        return self._active

class CheckButton(ToggleButton):
    def __init__(self, master, side_length, position, background, bordercolor, borderwidth, cornerradius,
                 active_bg=None, orient="horizontal"):

        super().__init__(master, [side_length]*2, position, background, 'white',
                         bordercolor, borderwidth, cornerradius, '',
                         active_bg=active_bg, orient=orient)

    def _return_rendering(self):
        pos = [self.borderwidth]*2
        size = [x-self.borderwidth*2 for x in self.rect.size]

        pos2 = [x+4 for x in pos]
        size2 = [x-8 for x in size]

        bg_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self.inactive_bg, self.cornerradius,
                                            orient=self.orient)

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos2, size2), self.background, self.cornerradius-1,
                                              orient=self.orient)

        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self.bordercolor, self.cornerradius,
                                                orient=self.orient)

        return [main_body, bg_body, border_rect]

    def _render(self):
        render_rect = self._return_rendering()

        render_rect[2].draw()
        render_rect[1].draw()
        render_rect[0].draw()

class RadioButton(CheckButton):
    def __init__(self, master, side_length, position, background, bordercolor, borderwidth,
                 active_bg=None, associate_with=(), orient="horizontal"):
        super(RadioButton, self).__init__(master, side_length, position, background, bordercolor,
                                          borderwidth, int(side_length//2.1), active_bg, orient)

        self.associate_with = associate_with

    def trigger(self, events, mpos):
        self._onclick = False

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(*event.pos) and event.button == 1:
                    self._active = True
                    self._onclick = True

        for radio in self.associate_with:
            if radio.on_click():
                self._active = False

        if self._active:
            self.background = self.active_bg
            self.foreground = self.active_fg
            self.bordercolor = self.active_bc
            self.command()

        else:
            self.background = self.inactive_bg
            self.foreground = self.inactive_fg
            self.bordercolor = self.inactive_bc

        if self.is_hover(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif not self.is_hover(mpos) and not self.any_active(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def _return_rendering(self):
        pos = [self.rect.width//2-3]*2
        pos2 = [x+3 for x in pos]

        main_body = graphics.draw.DynamicEllipse(self, pos2, self.cornerradius-4, self.cornerradius-4, self.background,
                                                 orient=self.orient)

        bg_body = graphics.draw.DynamicEllipse(self, pos2, self.cornerradius, self.cornerradius,
                                               [self.inactive_bg]*2,
                                               orient=self.orient)

        border_rect = graphics.draw.DynamicEllipse(self, pos2, self.rect.width//2, self.rect.width//2, self.bordercolor,
                                                   orient=self.orient)

        return [main_body, bg_body, border_rect]
