from natrium import *
import pygame

class Panel(widgets.Box):
    def __init__(self, master, size, position, style, anchor):
        if style['widget'] != 'Panel':
            raise ValueError(f"Panel does not support style of widget {style['widget']}")

        self.child_list = []
        super().__init__(master, size, position, anchor, style)

    def blit(self, widget, destination):
        self.child_list.append([widget, destination])

    def _return_rendering(self):
        pos = [self['borderwidth']]*2
        size = [x-self['borderwidth']*2 for x in self.rect.size]

        main_body = graphics.draw.DynamicRect(self, pygame.Rect(pos, size), self['background'], self['cornerradius']-1,
                                              orient=self['gradial_orient'])
        for child, dest in self.child_list:
            main_body.blit(child, dest)

        border_rect = graphics.draw.DynamicRect(self, pygame.Rect(0, 0, *self.rect.size), self['bordercolor'], self['cornerradius'],
                                                orient=self['gradial_orient'])

        return [main_body, border_rect]

    def return_children(self):
        return self.child_list

    def _render(self):
        render_rect = self._return_rendering()

        render_rect[1].draw()
        render_rect[0].draw()
