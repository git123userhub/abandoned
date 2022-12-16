
def _identity_style(dictionary, identity):
    return dict(**dictionary, widget=identity)

def button_style(
        borderwidth,
        cornerradius,

        background,
        foreground,
        bordercolor,

        hover_bg,
        hover_fg,
        hover_bc,

        active_bg,
        active_fg,
        active_bc,

        gradial_orient,
        ):
    style = dict(borderwidth=borderwidth, cornerradius=cornerradius,
                background=background, foreground=foreground, bordercolor=bordercolor,
                hover_bg=hover_bg, hover_fg=hover_fg, hover_bc=hover_bc,
                active_bg=active_bg, active_fg=active_fg, active_bc=active_bc,
                gradial_orient=gradial_orient
                )

    return _identity_style(style, "Button")

def inputbox_style(
        borderwidth,
        cornerradius,

        background,
        foreground,
        bordercolor,

        active_bg,
        active_fg,
        active_bc,

        gradial_orient,
):
    style = dict(borderwidth=borderwidth, cornerradius=cornerradius,
                 background=background, foreground=foreground, bordercolor=bordercolor,
                 active_bg=active_bg, active_fg=active_fg, active_bc=active_bc,
                 gradial_orient=gradial_orient
                 )

    return _identity_style(style, "InputBox")

def label_style(
        borderwidth,
        cornerradius,

        background,
        foreground,
        bordercolor,

        gradial_orient,
):
    style = dict(borderwidth=borderwidth, cornerradius=cornerradius,
                 background=background, foreground=foreground, bordercolor=bordercolor,
                 gradial_orient=gradial_orient
                 )

    return _identity_style(style, "Label")

def togglebutton_style(
        borderwidth,
        cornerradius,

        background,
        foreground,
        bordercolor,

        active_bg,
        active_fg,
        active_bc,

        gradial_orient,
):
    style = dict(borderwidth=borderwidth, cornerradius=cornerradius,
                background=background, foreground=foreground, bordercolor=bordercolor,
                active_bg=active_bg, active_fg=active_fg, active_bc=active_bc,
                gradial_orient=gradial_orient
                )

    return _identity_style(style, "ToggleButton")

def checkbutton_style(
        borderwidth,
        cornerradius,

        background,
        bordercolor,

        active_bg,

        gradial_orient,
):
    style = dict(borderwidth=borderwidth, cornerradius=cornerradius,
                background=background, bordercolor=bordercolor,
                active_bg=active_bg,
                gradial_orient=gradial_orient,

                foreground=(0, 0, 0, 0),
                active_fg=(0, 0, 0, 0),
                active_bc=bordercolor
                )

    return _identity_style(style, "CheckButton")

def radiobutton_style(
        borderwidth,

        background,
        bordercolor,

        active_bg,

        gradial_orient,
):
    style = dict(borderwidth=borderwidth,
                 background=background, bordercolor=bordercolor,
                 active_bg=active_bg,
                 gradial_orient=gradial_orient,

                 foreground=(0, 0, 0, 0),
                 active_fg=(0, 0, 0, 0),
                 active_bc=bordercolor
                 )

    return _identity_style(style, "RadioButton")

def slider_style(
        bar_cornerradius,
        grip_cornerradius,
        bar_color,
        grip_color,
        bar_bordercolor,
        grip_bordercolor,
        bar_borderwidth,
        grip_borderwidth,
        grip_gradial_orient="horizontal",
        bar_gradial_orient="horizontal"
        ):
    style = dict(bar_borderwidth=bar_borderwidth, bar_cornerradius=bar_cornerradius,
                 grip_borderwidth=grip_borderwidth, grip_cornerradius=grip_cornerradius,
                 bar_color=bar_color, bar_bordercolor=bar_bordercolor,
                 grip_color=grip_color, grip_bordercolor=grip_bordercolor,
                 grip_gradial_orient=grip_gradial_orient,
                 bar_gradial_orient=bar_gradial_orient)

    return _identity_style(style, "Slider")

__all__ = ['slider_style', 'label_style', 'inputbox_style', 'button_style', 'togglebutton_style', 'checkbutton_style',
           'radiobutton_style']