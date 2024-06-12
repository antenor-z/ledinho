import pwmControl
import time
current_color = {"c": [0, 0, 0]}

def get_current_color():
    cc = current_color["c"]
    return "{:02x}{:02x}{:02x}".format(cc[0], cc[1], cc[2])

def write_color(color:str, save=True):
    if color.startswith("#"): 
        color = color[1:]
    if len(color) != 6: 
        raise ValueError("Invalid color code")
    for chr in color:
        if chr not in "0123456789abcdefABCDEF":
            raise ValueError("Invalid color code")
        
    red = int(color[0:2], 16)
    green = int(color[2:4], 16)
    blue = int(color[4:6], 16)

    print("RGB values:", red, green, blue)
    fade_color(current_color["c"], [red, green, blue])
    current_color["c"] = [red, green, blue]
    if save:
        with open("currentColor", "w") as fp:
            fp.write(get_current_color())

    return "ok"

def linear(start, end, steps, i):
    diff = end - start
    steps = steps - 1
    alpha = diff / steps
    return int(start + alpha * i)

def fade_color(color_start, color_end):
    n_steps = 15
    for i in range(n_steps):
        pwmControl.setPWM(
            linear(color_start[0], color_end[0], n_steps, i),
            linear(color_start[1], color_end[1], n_steps, i),
            linear(color_start[2], color_end[2], n_steps, i)
        )
        time.sleep(1 / 30)

while(True):
    color = input("Cor >> ")
    print(write_color(color))
