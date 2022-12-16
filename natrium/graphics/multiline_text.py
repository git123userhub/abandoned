import pygame

def render_multiline(font, text, antialiased, foreground):
    array_text = text.splitlines()
    if array_text:
        max_text = max(*array_text, key=len) if len(array_text) > 1 else array_text[0]
    else:
        max_text = ''

    max_width = font.size(max_text)[0]

    text_surface = pygame.Surface([max_width+1, font.get_height()*len(array_text)+1], pygame.SRCALPHA, 32)

    for i, text in enumerate(array_text):
        text2 = font.render(text, antialiased, foreground)
        text_surface.blit(text2, (0, font.get_height()*i))

    return text_surface
