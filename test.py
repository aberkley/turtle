import turtle
from colour import Color

def draw_polygon(n, line_color='black', fill_color=None, size=100):
    if fill_color is None:
        fill_color = line_color
    bob.color(line_color, fill_color)
    bob.begin_fill()
    for i in range(n):
        bob.forward(size)
        bob.left(360/n)
    bob.end_fill()


def draw_rainbow_polygons(size=100):
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    n = len(colors)
    for i, color in enumerate(colors):
        draw_polygon(n - i + 2, color, size=size)


def draw_two_rainbow_polygons(size=100):
    draw_rainbow_polygons(size=50)
    bob.penup()
    bob.right(90)
    bob.forward(200)
    bob.pendown()
    draw_rainbow_polygons(size=50)

#TODO:alex
#  1. join 6 Serpinksi triangles to make a hexagon
#  2. square version (has 9 sub-squares, the middle one is empty)

def move(size):
    bob.penup()
    bob.forward(size)
    bob.pendown()


def draw_star(angle, size=200, line_color='red', fill_color='white'):
    move(-size*0.5)

    # .hex
    bob.begin_fill()
    n = int(360 / (180 - angle))
    for i in range(n):
        x = i / (n-1)
        color = Color(red=0.5*(1+x), green=0, blue=0.5*(1+x))
        bob.color(color.hex, fill_color)
        bob.forward(size)
        bob.left(angle)
    bob.end_fill()


# Sierpinski triange
def draw_triangle(size, color, orientation):
    bob.color(color, color)
    bob.begin_fill()
    for _ in range(3):
        bob.forward(size)
        if orientation == 'up':
            bob.left(120)
        elif orientation == 'down':
            bob.right(120)
        else:
            raise ValueError('Orientation must be "up" or "down"')
    bob.end_fill()


def sierpinski_triangle(level, size, color):
    if level == 0:
        draw_triangle(size, color, 'up')
    else:
        sierpinski_triangle(level-1, size*0.5, color)
        bob.forward(size*0.5)
        sierpinski_triangle(level-1, size*0.5, color)
        bob.left(120)
        bob.forward(size*0.5)
        bob.right(120)
        sierpinski_triangle(level-1, size*0.5, color)
        bob.left(120)
        bob.left(120)
        bob.forward(size*0.5)
        bob.left(120)


def draw_square(size, color):
    bob.pendown()
    bob.color(color, color)
    bob.begin_fill()
    for _ in range(4):
        bob.forward(size)
        bob.left(90)
    bob.end_fill()
    bob.penup()


def draw_serpinski_square(level, size, color):
    if level == 0:
        draw_square(size, color)
    else:
        draw_serpinski_square(level-1, size/3, color)
        bob.forward(size/3)
        draw_serpinski_square(level-1, size/3, color)
        bob.forward(size/3)
        draw_serpinski_square(level-1, size/3, color)
        bob.left(90)
        bob.forward(size/3)
        bob.right(90)
        draw_serpinski_square(level-1, size/3, color)
        bob.left(90)
        bob.forward(size/3)
        bob.right(90)
        draw_serpinski_square(level-1, size/3, color)
        bob.backward(size/3)
        draw_serpinski_square(level-1, size/3, color)
        bob.backward(size/3)
        draw_serpinski_square(level-1, size/3, color)
        bob.right(90)
        bob.forward(size/3)
        bob.left(90)
        draw_serpinski_square(level-1, size/3, color)
        bob.right(90)
        bob.forward(size/3)
        bob.left(90)


def sierpinski_hexagon(level, size, color=None):
    colors = ['maroon', 'tan', 'turquoise', 'olive', 'navy blue', 'violet']
    for color in colors:
        sierpinski_triangle(level, size, color)
        bob.forward(size)
        bob.left(60)


def draw_fast_squares(level, size):
    n = pow(3, level)
    new_size = size / pow(3, level+1)
    #for across in range(n):
    #    bob.forward(new_size)
    #    bob.left(90)
    bob.backward(new_size*2)
    bob.left(90)
    bob.forward(new_size)
    bob.right(90)
    for up in range(n):
        bob.forward(new_size*3)
        draw_square(new_size, 'yellow')
#    for across in range(n):
    for up in range(n):
        bob.backward(new_size*3)
    bob.forward(new_size*2)
    bob.right(90)
    bob.forward(new_size)
    bob.left(90)



def draw_fast_sierpinski_square(levels, size, color):
    draw_square(size, color)
    for level in range(levels):
        draw_fast_squares(level, size)


bob = turtle.Turtle()
bob.speed(0)
bob.penup()
bob.setx(-300)
bob.sety(-300)
bob.pendown()
draw_fast_sierpinski_square(4, 500, 'red')
#draw_triangle(50, 'green', 'up')
turtle.done()
