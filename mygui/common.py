def is_char(arg):
    return len(arg) == 1 and isinstance(arg, str)

def is_str(arg):
    return len(arg) > 1 and isinstance(arg, str)

def anchor_calculation(parent_surface, child_surface, anchor, centermargin_x, centermargin_y):
    pw, ph = parent_surface.get_size()
    cw, ch = child_surface.get_size()
    mx, my = centermargin_x, centermargin_y # This is supposed to place the surface a little towards the center

    anchor_dictionary = {
        'topleft': [0+mx, 0+my],
        'topright': [pw-cw-mx, 0+my],
        'bottomleft': [0+mx, ph-ch-my],
        'bottomright': [pw-cw-mx, ph-ch-my],
        'center': [pw//2-cw//2, ph//2-ch//2],
        'midtop': [pw//2-cw//2, my],
        'midbottom': [pw//2-cw//2, ph-ch-my],
        'midleft': [mx, ph//2-ch//2],
        'midright': [pw-cw-mx, ph//2-ch//2],
    }

    return anchor_dictionary.get(anchor, [0, 0])

def is_normal_text(string):
    boolean_list = [ord(c) > 31 for c in string]
    return all(boolean_list)

def nearest_to(x, y, near_val):
    if abs(x-near_val) < abs(y-near_val):
        return x
    elif abs(x-near_val) == abs(y-near_val):
        return x+y/2
    else:
        return y

