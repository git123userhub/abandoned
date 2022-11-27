import pygame
import mygui

win = pygame.display.set_mode((900, 550))
pygame.display.set_caption("TestingGUI")

label_test = mygui.widgets.Label(
    master=win,
    position=(20, 22),
    size=(100, 20),
    background=(0, 0, 0, 0),
    foreground='black',
    bordercolor=(0, 0, 0, 0),
    borderwidth=0,
    cornerradius=1,
    text="Label:",
    font=('notosanscjkjpregular', 18, 0, 0)
)

entry = mygui.widgets.InputBox(
    master=win,
    position=(89, 20),
    size=(200, 30),
    background='white',
    foreground='black',
    bordercolor='grey35',
    active_bc='grey56',
    borderwidth=1,
    cornerradius=4,
    default_text="Input",
    text_margins=(5, 0),
    text_anchor='midleft',
    font=('notosanscjkjpregular', 18, 0, 0)
)

button = mygui.widgets.Button(
    master=win,
    position=(89, 60),
    size=(200, 30),

    background=[(65, 165, 255), (40, 140, 245)],
    foreground='white',
    bordercolor='dodgerblue',
    active_bg=[(40, 140, 245), (65, 165, 255)],

    borderwidth=1,
    cornerradius=4,
    text="Button",
    text_margins=(5, 0),
    text_anchor='center',
    font=('notosanscjkjpregular', 18, 0, 0),

    orient="vertical",
)

toggle_button = mygui.widgets.ToggleButton(
    master=win,
    position=(89, 100),
    size=(200, 30),

    background=[(65, 165, 255), (40, 140, 245)],
    foreground='white',
    bordercolor='dodgerblue',
    active_bg=[(40, 140, 245), (65, 165, 255)],

    borderwidth=1,
    cornerradius=4,
    text="Toggle Button",
    text_margins=(5, 0),
    text_anchor='center',
    font=('notosanscjkjpregular', 18, 0, 0),

    orient="vertical",
)


list_checks = []
label_checks = mygui.widgets.Label(
    master=win,
    position=(20, 140),
    size=(100, 20),
    background=(0, 0, 0, 0),
    foreground='black',
    bordercolor=(0, 0, 0, 0),
    borderwidth=0,
    cornerradius=1,
    text='Cbox:',
    font=('notosanscjkjpregular', 18, 0, 0)
)

for i in range(5):
    check_button0 = mygui.widgets.CheckButton(
        master=win,
        position=(89+i*40, 140),
        side_length=30,

        background='white',
        bordercolor='grey55',
        active_bg=[(65, 165, 255), (40, 140, 245), ],

        borderwidth=1,
        cornerradius=2,

        orient="vertical",
    )
    list_checks.append(check_button0)

label_radios = mygui.widgets.Label(
    master=win,
    position=(20, 180),
    size=(100, 20),
    background=(0, 0, 0, 0),
    foreground='black',
    bordercolor=(0, 0, 0, 0),
    borderwidth=0,
    cornerradius=1,
    text='Rbox:',
    font=('notosanscjkjpregular', 18, 0, 0)
)
list_radios = []

for i in range(5):
    radio_button = mygui.widgets.RadioButton(
        master=win,
        position=(89+i*40, 180),
        side_length=30,

        background='white',
        bordercolor='grey55',
        active_bg=[(65, 235, 65), (40, 205, 40), ],

        borderwidth=1,

        orient="vertical",
    )
    list_radios.append(radio_button)

for radio in list_radios:
    new_list = list_radios.copy()
    new_list.remove(radio)
    radio.associate_with = new_list

slider = mygui.widgets.Slider(master=win,
                              position=(89, 220),
                              size=(200, 5),
                              bar_cornerradius=3,
                              bar_color='grey',
                              bar_border_color='grey55',
                              bar_border_width=1,
                              grip_length=14,
                              grip_cornerradius=7,
                              grip_color=[(65, 165, 255), (40, 140, 245)],
                              grip_border_color=[(65, 165, 255), (40, 140, 245)],
                              grip_border_width=1,
                              min_value=50,
                              max_value=69,
                              grip_orient='vertical')

label_slider = mygui.widgets.Label(
    master=win,
    position=(20, 210),
    size=(100, 20),
    background=(0, 0, 0, 0),
    foreground='black',
    bordercolor=(0, 0, 0, 0),
    borderwidth=0,
    cornerradius=1,
    text="0",
    font=('notosanscjkjpregular', 18, 0, 0)
)

clock = pygame.time.Clock()

while True:
    mpos = pygame.mouse.get_pos()
    mprd = pygame.mouse.get_pressed()
    keys = pygame.key.get_pressed()

    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()

    entry.trigger(events, mpos)
    button.trigger(events, mpos, mprd)
    toggle_button.trigger(events, mpos)
    slider.trigger(mpos, mprd)
    for check_button in list_checks: check_button.trigger(events, mpos)
    for radio_button in list_radios: radio_button.trigger(events, mpos)
    label_slider.string = f"{slider.value()}"

    win.fill("white")

    label_test.place()
    entry.place()
    button.place()
    toggle_button.place()
    label_checks.place()
    label_radios.place()
    label_slider.place()
    slider.place()
    for check_button in list_checks: check_button.place()
    for radio_button in list_radios: radio_button.place()

    pygame.display.update()
    clock.tick(60)
