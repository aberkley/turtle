import turtle


def draw_circle(size):
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

def draw_circular_rings(level, size):
    draw_circle(size)
    if level == 0:
        pass
    else:
        bob.penup()
        bob.forward(size)
        bob.pendown()
        draw_circular_rings(level - 1, size / 2)


bob = turtle.Turtle()
bob.speed(1)
#TODO: put your code here...
#draw a ring
#draw more rings on that ring and so on
draw_circular_rings(3, 100)
turtle.done()