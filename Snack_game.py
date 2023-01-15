
from tkinter import *
import time
import random

Game_Run = True

gm_width = 700
gm_height = 700
item = 25
color1 = "red"
color2 = "white"

game_x = gm_width // item
game_y = gm_height // item

s_x = game_x // 2
s_y = game_y // 2
x_walk = 0
y_walk = 0

s_list = []
s_size = 7

root = Tk()
root.title("Игра Змейка")
root.resizable(0, 0)
root.wm_attributes("-topmost", 1)
canvas = Canvas(root, width=gm_width, height=gm_height, bd=0, highlightthickness=0)
canvas.pack()
root.update()

apple_color1 = "purple"
apple_color2 = "white"
apple_list = []
apple_size = 100
for i in range(apple_size):
    x = random.randrange(game_x)
    y = random.randrange(game_y)
    id1 = canvas.create_oval(x * item, y * item, x * item + item, y * item + item,
                             fill=apple_color2)
    id2 = canvas.create_oval(x * item + 2, y * item + 2, x * item + item - 2,
                             y * item + item - 2, fill=apple_color1)
    apple_list.append([x, y, id1, id2])
print(apple_list)


def s_paint_item(canvas, x, y):
    global s_list
    id1 = canvas.create_rectangle(x * item, y * item, x * item + item, y * item + item, fill=color2)
    id2 = canvas.create_rectangle(x * item + 1, y * item + 1, x * item + item - 1, y * item + item - 1, fill=color1)
    s_list.append([x, y, id1, id2])


s_paint_item(canvas, s_x, s_y)


def delete_item():
    if len(s_list) >= s_size:
        temp_item = s_list.pop(0)
        canvas.delete(temp_item[2])
        canvas.delete(temp_item[3])


def find_apple():
    global s_size
    for i in range(len(apple_list)):
        if apple_list[i][0] == s_x and apple_list[i][1] == s_y:
            s_size = s_size + 1
            canvas.delete(apple_list[i][2])
            canvas.delete(apple_list[i][3])


def s_move(event):
    global s_x
    global s_y
    global x_walk
    global y_walk

    if event.keysym == "Up":
        x_walk = 0
        y_walk = -1
        delete_item()
    elif event.keysym == "Down":
        x_walk = 0
        y_walk = 1
        delete_item()
    elif event.keysym == "Left":
        x_walk = -1
        y_walk = 0
        delete_item()
    elif event.keysym == "Right":
        x_walk = 1
        y_walk = 0
        delete_item()
    s_x = s_x + x_walk
    s_y = s_y + y_walk
    s_paint_item(canvas, s_x, s_y)
    find_apple()


canvas.bind_all("<KeyPress-Left>", s_move)
canvas.bind_all("<KeyPress-Right>", s_move)
canvas.bind_all("<KeyPress-Up>", s_move)
canvas.bind_all("<KeyPress-Down>", s_move)


def game_over():
    global Game_Run
    Game_Run = False


def off_border():
    if s_x > game_x or s_x < 0 or s_y > game_y or s_y < 0:
        game_over()


def touch_self(f_x, f_y):
    global Game_Run
    if not (x_walk == 0 and y_walk == 0):
        for i in range(len(s_list)):
            if s_list[i][0] == f_x and s_list[i][1] == f_y:
                Game_Run = False


while Game_Run:
    delete_item()
    find_apple()
    off_border()
    touch_self(s_x + x_walk, s_y + y_walk)
    s_x = s_x + x_walk
    s_y = s_y + y_walk
    s_paint_item(canvas, s_x, s_y)
    root.update_idletasks()
    root.update()
    time.sleep(0.07)

