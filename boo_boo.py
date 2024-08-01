import turtle
import random

from test import draw_square


def draw_square_grid(level, size, color):
    draw_square(ivy, size, color, pensize=level+1, fill=False)
    if level == 0:
        pass
    else:
        for _ in range(4):

            ivy.right(90)
            ivy.forward(size/4)
            ivy.left(90)
            ivy.backward(size/4)
            draw_square_grid(level - 1, size / 2, color)
            ivy.forward(size / 4)
            ivy.left(90)
            ivy.forward(size/4)
            ivy.right(90)

            ivy.forward(size)
            ivy.left(90)


def draw_random_line(max_size=100, last_color=None, color=None):
    if color is None:
        colors = ['navy blue', 'red', 'orange', 'yellow', 'green', 'violet', 'magenta', 'black']
        filtered_colors = []
        for this_color in colors:
            if last_color != color:
                filtered_colors.append(this_color)
        color = random.choice(filtered_colors)
    size = random.randint(10, max_size)
    angle = random.randint(1,360)
    ivy.color(color)
    ivy.left(angle)
    ivy.forward(size)
    return color


def draw_random_path(number, max_size=100, color=None):
    last_color = None
    for i in range(number):
        last_color = draw_random_line(max_size=max_size, last_color=last_color, color=color)


def draw_random_paths(n=50, n_per_path=100):
    for _ in range(n):
        ivy.penup()
        ivy.home()
        ivy.pendown()
        draw_random_path(n_per_path, max_size=50, color='grey')
        ivy.color('red', 'red')
        ivy.begin_fill()
        ivy.circle(10)
        ivy.end_fill()


#TODO:alex
# 3. draw a dot at the end (of a different color)

ivy = turtle.Turtle()
ivy.speed(0)
#draw_square_grid(10, 250, 'navy blue')
#draw_random_path(100, max_size=50, color='grey')
draw_random_paths()
turtle.done()