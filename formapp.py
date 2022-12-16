import natrium
from natrium import widgets as natwids
import style

disp = natrium.display.Window((890, 355),
                              ['#FAFAFA', '#FAFAFA', '#D3D3D3'],
                              'vertical',
                              "Testing Form Application")
glob_font = ('sfprotextregular', 17, 0, 0)
print(natrium.common.get_fonts())

title_label = natwids.Label(
    disp,
    size=(890, 50),
    position=(0, 0),
    anchor='topleft',
    style=style.lbl_blue,
    text="Title",
    font=glob_font,
    text_anchor='center',
    text_margins=(10, 0)
)

button = natwids.Button(
    disp,
    size=(340, 40),
    position=(120, 20),
    anchor='bottomleft',
    style=style.btn_grngradient,
    text="Button",
    font=glob_font,
    text_anchor='center',
    command=lambda: print(disp.get_rate())
)

label = natwids.Label(
    disp,
    size=(140, 30),
    position=(10, 80),
    anchor='topleft',
    style=style.lbl_trn,
    text="Entry 1:",
    font=glob_font,
    text_anchor='midleft',
    text_margins=(10, 0)
)

entry = natwids.InputBox(
    disp,
    size=(340, 30),
    position=(120, 80),
    anchor='topleft',
    style=style.inp_box,
    default_text='',
    font=glob_font,
    text_anchor='midleft',
    text_margins=(5, 0)
)

label1 = natwids.Label(
    disp,
    size=(140, 30),
    position=(10, 135),
    anchor='topleft',
    style=style.lbl_trn,
    text="Entry 2:",
    font=glob_font,
    text_anchor='midleft',
    text_margins=(10, 0)
)

entry1 = natwids.InputBox(
    disp,
    size=(300, 30),
    position=(120, 135),
    anchor='topleft',
    style=style.inp_box_halfrad,
    default_text='',
    font=glob_font,
    text_anchor='midleft',
    text_margins=(5, 0),
    show_as='*'
)

show_toggle = natwids.ToggleButton(
    disp,
    size=(40, 30),
    position=(420, 135),
    anchor='topleft',
    style=style.tgbtn_grey_gradient,
    text='👁',
    font=('segoeuisymbol', 20, 0, 0),
    text_anchor='midtop',
    text_margins=(5, 0),
)

label2 = natwids.Label(
    disp,
    size=(140, 30),
    position=(10, 196),
    anchor='topleft',
    style=style.lbl_trn,
    text="0",
    font=glob_font,
    text_anchor='midleft',
    text_margins=(10, 0)
)

slider = natwids.Slider(
    disp,
    size=(340, 4),
    grip_length=24,

    position=(120, 210),
    anchor='topleft',
    style=style.sldr_style,
    min_value=-420,
    max_value=69
)

label3 = natwids.Label(
    disp,
    size=(140, 30),
    position=(10, 240),
    anchor='topleft',
    style=style.lbl_trn,
    text="Checks: ",
    font=glob_font,
    text_anchor='midleft',
    text_margins=(10, 0)
)

checkboxes = [
    natwids.CheckButton(
        disp,
        side_length=20,
        position=(120+i*30, 245),
        anchor='topleft',
        style=style.cbtn_blue
    )

    for i in range(11)
]

while True:
    disp.trigger()
    disp.listen(button)
    disp.listen(entry)
    disp.listen(entry1)
    disp.listen(show_toggle)
    disp.listen(slider)
    for cbox in checkboxes: disp.listen(cbox)

    entry1.show_as = '*' if not show_toggle.active() else None
    label2.string = str(slider.value())

    title_label.place()

    label.place()
    entry.place()

    label1.place()
    entry1.place()
    show_toggle.place()

    label2.place()
    slider.place()

    label3.place()
    for cbox in checkboxes: cbox.place()

    button.place()

    disp.refresh()
