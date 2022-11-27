import pygame
import mygui

win = pygame.display.set_mode((800, 450))
surface = pygame.Surface((800, 450), pygame.SRCALPHA, 32)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    win.fill("white")
    surface.fill((0, 0, 0, 0))

    mygui.graphics.draw.instant_ellipse(surface, (75, 75), 25, 25, 'grey59')
    mygui.graphics.draw.instant_ellipsegrad2(surface, (75, 125), 25, 25, 'grey59', 'grey19')
    mygui.graphics.draw.instant_ellipsegrad3(surface, (75, 175), 25, 25, 'grey19', 'grey59', 'grey19')

    mygui.graphics.draw.instant_rect(surface, pygame.Rect(100, 50, 49, 49), 'grey59', 20)
    mygui.graphics.draw.instant_rectgrad2(surface, pygame.Rect(100, 100, 49, 49), 'grey59', 'grey19', 20)
    mygui.graphics.draw.instant_rectgrad3(surface, pygame.Rect(100, 150, 49, 49), 'grey19', 'grey59', 'grey19', 20)

    mygui.graphics.draw.instant_rect(surface, pygame.Rect(150, 50, 49, 49), 'grey59', 15)
    mygui.graphics.draw.instant_rectgrad2(surface, pygame.Rect(150, 100, 49, 49), 'grey59', 'grey19', 15)
    mygui.graphics.draw.instant_rectgrad3(surface, pygame.Rect(150, 150, 49, 49), 'grey19', 'grey59', 'grey19', 15)

    win.blit(surface, (0, 0))
    pygame.display.update()
