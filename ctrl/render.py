def render_wheel(canvas_height, wheel_info):
    left = wheel_info.center_x - wheel_info.r
    top = canvas_height - wheel_info.center_y - wheel_info.r
    right = wheel_info.center_x + wheel_info.r
    bottom = canvas_height - wheel_info.center_y + wheel_info.r
    
    return left, top, right, bottom


def render_rod(canvas_height, rod_info):
    from_x = rod_info.start_x
    from_y = canvas_height - rod_info.start_y
    to_x = rod_info.end_x
    to_y = canvas_height - rod_info.end_y
    
    return from_x, from_y, to_x, to_y