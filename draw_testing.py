from natrium import graphics
import pygame

win = pygame.display.set_mode((0, 0))
pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
timer = 0
hue = 0
active = True

clock = pygame.time.Clock()

while True:
    events = pygame.event.get()
    mpos = pygame.mouse.get_pos()
    mprd = pygame.mouse.get_pressed()
    if active:
        timer = min((timer + 0.01) % 12, 3)
        hue = (hue + 0.5) % 360

    pygame.display.set_caption(str(clock.get_fps()))

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                active = not active

        if event.type == pygame.ACTIVEEVENT:
            timer = 0

    color = pygame.Color((0, 0, 0))
    color.hsva = (hue, 100, 100, 100)
    color2 = pygame.Color((0, 0, 0))
    color2.hsva = (abs(hue-180), 100, 100, 100)
    color3 = pygame.Color((0, 0, 0))
    color3.hsva = (abs(hue-360), 100, 100, 100)

    backgroundsurf = graphics.draw.RoundRectGrad3(win, pygame.Rect(0, 0, *pygame.display.get_window_size()),
                                                  color, color2, color3, True).draw()

    originalsurf = graphics.draw.RoundRect(win, pygame.Rect(*[x-50 for x in mpos], 100, 100),
                            (100, 100, 100, 100), 12, True, timer % 5)

    mod_surf = pygame.Surface.copy(originalsurf.main_surf)
    mod_center = mod_surf.get_rect().center
    mod_surf = pygame.transform.rotate(mod_surf, hue)
    mod_rect = mod_surf.get_rect(center=mod_center)

    win.blit(mod_surf, [x+y-50-int(timer*2) for x, y in zip(mpos, mod_rect.topleft)])


    pygame.display.update()
    clock.tick(60)
