from natrium.widgets import Label
from natrium.common import ascii
from natrium import graphics, common
import pygame

class InputBox(Label):
    @property
    def string(self):
        return self._string

    @string.setter
    def string(self, value):
        self._string = value
        self._show_string = self.show_as * len(self._string) if self.show_as else self._string

        self._render_const_text = graphics.render_multiline(self.font_object(), self._show_string, True, self['foreground'])
        self._render_const_activetext = graphics.render_multiline(self.font_object(), self._show_string, True, self['active_fg'])

    def __init__(self, master, size, position, anchor, style,
                 default_text, text_anchor='topleft', text_margins=(0, 0), font: list[str, int, bool, bool]=(None, 20, 0, 0),
                 multiline=False, show_as=None):

        if style['widget'] != "InputBox":
            raise ValueError(f"Label does not support style of widget {style['widget']}")

        # style['inactive_bg'] = style['background']
        # style['inactive_fg'] = style['foreground']
        # style['inactive_bc'] = style['bordercolor']

        self._active = False
        self.multiline = multiline
        self._show_string = default_text
        self.show_as = show_as
        self._scroll_offset = 0

        super().__init__(master, size, position, anchor, style, default_text, text_anchor, text_margins, font)
        self._render_const_activestyle = self._return_active_rendering()
        self._render_const_activetext = graphics.render_multiline(self.font_object(), self._show_string, True, self['active_fg'])

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
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._active = False
                if self.rect.collidepoint(*event.pos) and event.button == 1:
                    self._active = not self._active

            self._render_select = 0
            if self._active:
                self._render_select = 1

                if event.type == pygame.KEYDOWN:
                    self.string = self.string + event.unicode if ascii(event.unicode) > 31 else self.string

                    if event.key == pygame.K_BACKSPACE:
                        self.string = self.string[0:-1]
                    elif event.key == pygame.K_DELETE:
                        self.string = ''
                    elif event.key in [pygame.K_RETURN, pygame.K_KP_ENTER] and self.multiline:
                        self.string += '\n'

                    elif event.key == pygame.K_RIGHT and \
                            self.font_object().size(self._show_string)[0] > self.rect.width:
                        self._scroll_offset -= 10

                    elif event.key == pygame.K_LEFT:
                        self._scroll_offset = min(0, self._scroll_offset+10)

            if self.is_hover(mpos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_IBEAM)

            elif not self.is_hover(mpos) and not self.any_active(mpos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        self.string = self.string

    def is_active(self):
        return self._active

    # def _render(self):
    #     render_rect = self._return_rendering()
    #     render_rect[1].draw()
    #     new_margins = [self.text_margins[0]+self._scroll_offset, self.text_margins[1]]
    #
    #     text_surf = graphics.render_multiline(pygame.font.SysFont(*self.font),
    #                                           self._show_string, True, self['foreground'])
    #     render_rect[0].blit(text_surf,
    #                         common.anchor_calculation(render_rect[0], text_surf,
    #                                                   self.text_anchor, *new_margins))
    #
    #     render_rect[0].draw()

    def _render(self):
        pos = [self['borderwidth']]*2
        new_margins = [self.text_margins[0]+self._scroll_offset, self.text_margins[1]]

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
                                                             *new_margins))

        self.blit(self._render_style[0], pos)

