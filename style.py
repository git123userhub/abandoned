from natrium import styling as natstyling

btn_grngradient = natstyling.button_style(
    cornerradius=4,

    borderwidth=1,
    bordercolor=[[0, 200, 20], [0, 160, 20]],
    hover_bc=[[0, 200, 20], [0, 160, 20]],
    active_bc=[[0, 200, 20], [0, 160, 20]],

    background=[(0, 200, 50), (0, 160, 40)],
    hover_bg=[(0, 210, 50), (0, 170, 40)],
    active_bg=[(0, 180, 50), (0, 210, 60)],

    foreground='white',
    hover_fg='white',
    active_fg='white',

    gradial_orient='vertical'
)

lbl_blue = natstyling.label_style(
    cornerradius=1,

    borderwidth=0,
    bordercolor='white',

    background=['dodgerblue3', 'royalblue4'],
    foreground='white',

    gradial_orient='vertical'
)

inp_box = natstyling.inputbox_style(
    cornerradius=4,

    borderwidth=1,
    bordercolor='grey33',
    active_bc='dodgerblue',

    background=['grey89', 'white'],
    active_bg=['grey89', 'white'],

    foreground='black',
    active_fg='black',

    gradial_orient='vertical'
)

inp_box_halfrad = natstyling.inputbox_style(
    cornerradius=[4, 0, 4, 0],

    borderwidth=1,
    bordercolor='grey33',
    active_bc='dodgerblue',

    background=['grey89', 'white'],
    active_bg=['grey89', 'white'],

    foreground='black',
    active_fg='black',

    gradial_orient='vertical'
)

lbl_trn = natstyling.label_style(
    cornerradius=1,

    borderwidth=0,
    bordercolor=(0, 0, 0, 0),

    background=(0, 0, 0, 0),
    foreground='black',

    gradial_orient='horizontal'
)

tgbtn_grey_gradient = natstyling.togglebutton_style(
    cornerradius=[0, 4, 0, 4],

    borderwidth=1,
    bordercolor='grey33',
    active_bc='grey44',

    background=['grey88', 'grey66'],
    active_bg=['grey60', 'grey72'],

    foreground='black',
    active_fg='white',

    gradial_orient='vertical'
)

sldr_style = natstyling.slider_style(
    bar_cornerradius=2,
    grip_cornerradius=12,

    grip_borderwidth=1,
    bar_borderwidth=1,
    grip_bordercolor=['skyblue2', 'dodgerblue2'],
    bar_bordercolor='grey44',

    grip_color=['skyblue2', 'dodgerblue2'],
    bar_color='grey55',

    grip_gradial_orient='vertical',
    bar_gradial_orient='vertical'
)

cbtn_blue = natstyling.checkbutton_style(
    cornerradius=1,

    borderwidth=1,
    bordercolor='grey44',

    background=['grey88', 'grey77'],
    active_bg=['dodgerblue2', 'dodgerblue3'],

    gradial_orient='vertical'
)