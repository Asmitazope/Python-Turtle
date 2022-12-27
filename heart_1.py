import turtle
t=turtle.Turtle()

turtle.Screen().bgcolor('black')

turtle.pensize(4)
t.speed(10)

def drawcurve():
    for i in range(200):
        t.right(1)
        t.forward(1)

t.color('red','pink')

t.begin_fill()
t.left(140)

t.forward(111.65)

drawcurve()

t.left(120)

drawcurve()

t.forward(111.65)

t.end_fill()
t.penup()

t.goto(77,-40)

t.pendown()
t.hideturtle()
turtle.done()