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


def draw_random_line(max_size=100):
    color = random.choice(['navy blue', 'red', 'orange', 'yellow', 'green', 'violet', 'magenta', 'black'])
    size = random.randint(10, max_size)
    angle = random.randint(1,360)
    ivy.color(color)
    ivy.left(angle)
    ivy.forward(size)


def draw_random_lines(number, max_size=100):
    for i in range(number):
        draw_random_line(max_size=max_size)


ivy = turtle.Turtle()
ivy.speed(0)
#draw_square_grid(10, 250, 'navy blue')
draw_random_lines(100, max_size=50)
turtle.done()