import turtle
import random
from colour import Color
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


def draw_random_line():
#TODO: 1. Length, Angle and color
    color = random.choice(['navy blue', 'red', 'orange', 'yellow', 'green', 'violet', 'magenta', 'black'])
    size = random.randint(100, 300)
    angle = random.randint(25,360)
    ivy.color(color)
    ivy.left(angle)
    ivy.forward(size)




ivy = turtle.Turtle()
ivy.speed(0)
#draw_square_grid(10, 250, 'navy blue')
draw_random_line()
turtle.done()