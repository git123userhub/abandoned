from natrium import *

class Seperator(widgets.Box):
    def __init__(self, master, position, length, color, orient="vertical", anchor='topleft'):
        style_box = {
            'borderwidth':0,
            'cornerradius':1,
            'bordercolor':(0, 0, 0, 0),
            'background':color,
            'gradial_orient':orient
        }
        dims = [length, 1] if orient == "horizontal" else [1, length]
        super().__init__(master, dims, style_box, anchor, position)
