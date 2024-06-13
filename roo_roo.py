import math
import turtle


def draw_circle(size, pensize=1):
    bob.pensize(pensize)
    bob.penup()
    bob.right(90)
    bob.forward(size)
    bob.left(90)
    bob.pendown()
    bob.circle(size)
    bob.penup()
    bob.left(90)
    bob.forward(size)
    bob.right(90)


def draw_circular_rings(level, size, n, r):
    draw_circle(size, level+1)
    if level == 0:
        pass
    else:
        angle = 360 / n
        new_size = size / r
        for _ in range(n):
            bob.left(angle)
            bob.forward(size)
            draw_circular_rings(level - 1, new_size, n, r)
            bob.backward(size)


bob = turtle.Turtle()
bob.speed(0)
#TODO: put your code here...
#draw a ring
#draw more rings on that ring and so on
#draw_circular_rings(3, 100, 10, 2.5)
draw_circle(100)
bob.left(90)
bob.forward(100)
bob.left(45)
bob.pendown()
bob.forward(60)
bob.left(120)
bob.forward(70)
bob.penup()
bob.left(100)
bob.forward(145)
bob.left(90)
bob.pendown()
bob.forward(70)
bob.left(120)
bob.forward(79)


turtle.done()
#TODO
#1 cat drawing
#2 pixel drawing of a spider


def draw_cat(level, size):
    draw_circle(size, level)

    bob.circle(size)
    bob.forward(size)




