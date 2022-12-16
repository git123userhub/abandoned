import pygame
from natrium.widgets import Label
from natrium import graphics, common

class Button(Label):
    def __init__(self, master, size, position, anchor, style,
                 text, text_anchor='topleft', text_margins=(0, 0), font: list[str, int, bool, bool]=(None, 20, 0, 0),
                 command=lambda: None, click_once=True):

        if not issubclass(type(self), Button):
            if style['widget'] != "Button":
                raise ValueError(f"Button does not support style of widget {style['widget']}")

        self._onclick = False
        self._onhover = False

        self.command = command
        self.click_once = click_once

        super().__init__(master, size, position, anchor, style, text, text_anchor, text_margins, font)
        self._render_const_hoverstyle = self._return_hover_rendering()
        self._render_const_activestyle = self._return_active_rendering()

        self._render_const_hovertext = graphics.render_multiline(self.font_object(), self.string, True, self['hover_fg'])
        self._render_const_activetext = graphics.render_multiline(self.font_object(), self.string, True, self['active_fg'])

        self._render_select = 0

    def _return_hover_rendering(self):
        pos = [self['borderwidth']]*2
        size = [x-self['borderwidth']*2 for x in self.rect.size]

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self['hover_bg'], self['cornerradius'],
                                              orient=self['gradial_orient'])
        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self['hover_bc'], self['cornerradius'],
                                                orient=self['gradial_orient'])

        return [main_body, border_rect]

    def _return_active_rendering(self):
        pos = [self['borderwidth']]*2
        size = [x-self['borderwidth']*2 for x in self.rect.size]

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self['active_bg'], self['cornerradius'],
                                              orient=self['gradial_orient'])
        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self['active_bc'], self['cornerradius'],
                                                orient=self['gradial_orient'])

        return [main_body, border_rect]

    def trigger(self, events, mpos, mprd):
        self._onclick = False
        self._onhover = False
        if self.click_once:
            for event in events:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.rect.collidepoint(*event.pos) and event.button == 1:
                        self._onclick = True
                        self.command()

        self._render_select = 0
        if self.rect.collidepoint(*mpos):
            self._render_select = 1
            self._onhover = True

            if mprd[0]:
                self._render_select = 2
                self._onclick = True

                if not self.click_once: self.command()

        if self._onhover:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif not self._onhover and not self.any_active(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def _render(self):
        self._render_style[0].fill((0, 0, 0, 0))
        pos = [self['borderwidth']]*2

        select_style_list = [self._render_const_style, self._render_const_hoverstyle,
                             self._render_const_activestyle]
        select_text_list = [self._render_const_text, self._render_const_hovertext,
                            self._render_const_activetext]
        selected = select_style_list[self._render_select]
        selected_text = select_text_list[self._render_select]

        self._render_text = selected_text.copy()

        self._render_style = [selected[0].main_surf.copy(),
                              selected[1].main_surf.copy()]
        self.blit(self._render_style[1], (0, 0))

        self._render_style[0].blit(self._render_text,
                                   common.anchor_calculation(self._render_style[0],
                                                             self._render_text,
                                                             self.text_anchor,
                                                             *self.text_margins))

        self.blit(self._render_style[0], pos)

    def onclick(self):
        return self._onclick

    def onhover(self):
        return self._onhover

class ToggleButton(Label):
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value
        self._render_const_text = graphics.render_multiline(self.font_object(), self.string, True, self['foreground'])
        self._render_const_activetext = graphics.render_multiline(self.font_object(), self.string, True, self['active_fg'])

    def __init__(self, master, size, position, anchor, style,
                 text, text_anchor='topleft', text_margins=(0, 0),
                 font: list[str, int, bool, bool]=(None, 20, 0, 0),
                 command=lambda: None):

        if not issubclass(type(self), ToggleButton):
            if style['widget'] != "ToggleButton":
                raise ValueError(f"ToggleButton does not support style of widget {style['widget']}")

        self._active = False
        self._onclick = False
        self._onhover = False

        self.command = command

        super().__init__(master, size, position, anchor, style, text, text_anchor, text_margins, font)
        self._render_const_activestyle = self._return_active_rendering()
        self._render_const_activetext = graphics.render_multiline(self.font_object(), self.string, True, self['active_fg'])

        self._render_select = 0

    def _return_active_rendering(self):
        pos = [self['borderwidth']]*2
        size = [x-self['borderwidth']*2 for x in self.rect.size]

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self['active_bg'], self['cornerradius'],
                                              orient=self['gradial_orient'])
        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self['active_bc'], self['cornerradius'],
                                                orient=self['gradial_orient'])

        return [main_body, border_rect]


    def trigger(self, events, mpos):
        self._onclick = False
        self._onhover = False
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(*event.pos) and event.button == 1:
                    self._active = not self._active
                    self._onclick = True

        self._render_select = 0
        if self._active:
            self._render_select = 1
            self.command()

        if self.is_hover(mpos):
            self._onhover = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif not self.is_hover(mpos) and not self.any_active(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def _render(self):
        pos = [self['borderwidth']]*2

        select_style_list = [self._render_const_style, self._render_const_activestyle]
        select_text_list = [self._render_const_text, self._render_const_activetext]
        selected = select_style_list[self._render_select]
        selected_text = select_text_list[self._render_select]

        self._render_style = [selected[0].main_surf.copy(),
                              selected[1].main_surf.copy()]
        self._render_text = selected_text.copy()

        self.blit(self._render_style[1], (0, 0))

        self._render_style[0].blit(self._render_text,
                                   common.anchor_calculation(self._render_style[0],
                                                             self._render_text,
                                                             self.text_anchor,
                                                             *self.text_margins))

        self.blit(self._render_style[0], pos)

    def on_click(self):
        return self._onclick

    def on_hover(self):
        return self._onhover

    def active(self):
        return self._active

class CheckButton(ToggleButton):
    def __init__(self, master, side_length, position, anchor, style):

        if not issubclass(type(self), CheckButton):
            if style['widget'] != "CheckButton":
                raise ValueError(f"CheckButton does not support style of widget {style['widget']}")

        super().__init__(master, [side_length]*2, position, anchor, style, '')

    def _return_rendering(self):
        pos = [self['borderwidth']]*2
        size = [x-self['borderwidth']*2 for x in self.rect.size]

        pos2 = [x*4 for x in pos]
        size2 = [x-(x/3) for x in size]

        bg_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self['background'], self['cornerradius'],
                                            orient=self['gradial_orient'])

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos2, size2), (0, 0, 0, 0), self['cornerradius']-1,
                                              orient=self['gradial_orient'])

        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self['bordercolor'], self['cornerradius'],
                                                orient=self['gradial_orient'])

        return [main_body, bg_body, border_rect]

    def _return_active_rendering(self):
        pos = [self['borderwidth']]*2
        size = [x-self['borderwidth']*2 for x in self.rect.size]

        pos2 = [x*4 for x in pos]
        size2 = [x-(x/3) for x in size]

        bg_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self['background'], self['cornerradius'],
                                            orient=self['gradial_orient'])

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos2, size2), self['active_bg'], self['cornerradius']-1,
                                              orient=self['gradial_orient'])

        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self['bordercolor'], self['cornerradius'],
                                                orient=self['gradial_orient'])

        return [main_body, bg_body, border_rect]

    def _render(self):
        pos = [self['borderwidth']]*2
        pos2 = [x*4 for x in pos]

        select_style_list = [self._render_const_style, self._render_const_activestyle]
        selected = select_style_list[self._render_select]
        self._render_style = [selected[0].main_surf.copy(),
                              selected[1].main_surf.copy(),
                              selected[2].main_surf.copy()]

        self.blit(self._render_style[-1], (0, 0))
        self.blit(self._render_style[1], pos)

        self._render_style[0].blit(self._render_text,
                                   common.anchor_calculation(self._render_style[0],
                                                             self._render_text,
                                                             self.text_anchor,
                                                             *self.text_margins))

        self.blit(self._render_style[0], pos2)


class RadioButton(CheckButton):
    def __init__(self, master, side_length, position, anchor, style, associate_with=()):

        if style['widget'] != "RadioButton":
            raise ValueError(f"RadioButton does not support style of widget {style['widget']}")

        super(RadioButton, self).__init__(master, side_length, position, anchor, style)

        self.associate_with = associate_with

    def trigger(self, events, mpos):
        self._onclick = False
        self._onhover = False

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(*event.pos) and event.button == 1:
                    self._active = True
                    self._onclick = True

        for radio in self.associate_with:
            if radio.on_click():
                self._active = False

        self._render_select = 1 if self._active else 0

        if self.is_hover(mpos):
            self._onhover = True
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)

        elif not self.is_hover(mpos) and not self.any_active(mpos):
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def _return_rendering(self):
        pos = [self.rect.width//2-3]*2
        pos2 = [x+3 for x in pos]

        main_body = graphics.draw.DynamicEllipse(self, pos2, self['cornerradius']-4, self['cornerradius']-4, self['background'],
                                                 orient=self['gradial_orient'])

        bg_body = graphics.draw.DynamicEllipse(self, pos2, self['cornerradius'], self['cornerradius'],
                                               [self['inactive_bg']]*2,
                                               orient=self['gradial_orient'])

        border_rect = graphics.draw.DynamicEllipse(self, pos2, self.rect.width//2, self.rect.width//2, self['bordercolor'],
                                                   orient=self['gradial_orient'])

        return [main_body, bg_body, border_rect]
