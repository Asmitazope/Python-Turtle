import turtle as t
import colorsys as c
t.setup(750,750)
t.speed(0)
t.tracer(10)
t.width(2)
t.bgcolor('black')

for i in range(25):
    for j in range(15):
        t.color(c.hsv_to_rgb(j/15,j/15,1))
        t.right(90)
        t.circle(200-i*4,90)
        t.left(90)
        t.circle(200-i*4,90)
        t.right(180)
        t.circle(50,24)

t.hideturtle()
t.done()
