from flask import Flask, render_template
from pwmControl import setPWM

app = Flask(__name__)
current_color = {"c": "000000"}

@app.get("/")
def main():
    return render_template("index.html")


@app.get("/currentColor")
def get_current_color():
    return current_color["c"]

@app.get("/writeColor/<string:color>")
def write_color(color:str):
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
    setPWM(red, green, blue)
    current_color["c"] = color

    return "ok"

if __name__ == '__main__':
    app.run(debug=True, port=5000, host="0.0.0.0")