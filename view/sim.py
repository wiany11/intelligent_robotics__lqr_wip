import sys
sys.path.append('../..')
sys.path.append('.')

print(sys.path)

from math import pi, atan
from Tkinter import Tk, Canvas, mainloop
from model.inverted_pendulum import Rod, Wheel
from ctrl.render import render_rod, render_wheel
from ctrl.dynamics import state_feedback


being_pressed = False


def move_rod_to_left(event):
    rod_info.change_theta(-pi/180)


def move_rod_to_right(event):
    rod_info.change_theta(pi/180)

def released(event):
    global being_pressed
    being_pressed = False
    
def pressed(event):
    global being_pressed
    being_pressed = True
    
    x = event.x-1375
    y = 125-event.y

    sset(x, y)
    
def moving(event):
    global being_pressed
    being_pressed = False
    
    x = event.x-1375
    y = 125-event.y

    sset(x, y)
    

def sset(x, y):
    
    if y != 0:
        theta = atan(1.0 * x / y)
    else:
        theta = atan(1.0 * x / 0.0000000001)
    #print(x, y, theta)
    
    global X
    X[0] = theta
    X[1] = theta/0.001
    
    rod_info.theta = theta
    rod_info.change_theta(0)

def clock():
    global being_pressed
    canvas.after(5, clock)
    global X
    tmp_X = X
    
    X = state_feedback(X, 0.001)
    #print(X[0], X[2])
    rod_info.set_theta(X[0])
    #rod_info.start_x = origin_x + X[2]*10000
    #wheel_info.center_x = origin_x + X[2]*10000
    rod_info.start_x += X[3]*10
    wheel_info.center_x += X[3]*10
    print("X ="),
    print(X)
    canvas.coords(rod, render_rod(canvas_height, rod_info))
    canvas.coords(wheel, render_wheel(canvas_height, wheel_info))
    if being_pressed:
        X = tmp_X
    else:
        pass

origin_x = 200.0
X = [0, 0, 0, 0]

rod_info = Rod(200, 100)
wheel_info = Wheel(200, 100)

canvas_height = 500    


tk = Tk() 

    

canvas = Canvas(tk, bg="#FFFFFF", width=1500, height=canvas_height)
canvas.pack()


canvas.create_rectangle(0, 425, 1500, 500, fill="#444444")

canvas.create_oval(1275, 25, 1475, 225, fill="#ffffff", width=1)
canvas.create_rectangle(1275, 125, 1476, 226, fill="#ffffff", width=0)
canvas.create_line(1275, 125, 1475, 125)

rod = canvas.create_line(render_rod(canvas_height, rod_info), width=4, tags="hour")
wheel = canvas.create_oval(render_wheel(canvas_height, wheel_info), fill="#646464")#, outline="#555555")


#panel = canvas.create_line(1350, 150, 1350, 50, width=4)

canvas.focus_set()
canvas.bind("<Left>", move_rod_to_left)
canvas.bind("<Right>", move_rod_to_right)
canvas.bind("<ButtonPress-1>", pressed)
canvas.bind("<ButtonRelease-1>", released)
canvas.bind("<B1-Motion>", moving)
clock()
mainloop()
