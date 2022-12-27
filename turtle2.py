#1

import turtle
import colorsys

t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.speed(100)
n=30
h=1
colors=['red','blue','green']

'''

for i in range(120):
    #c=colorsys.hsv_to_rgb(0.5,h,0.5)
    # #h+=1
    #t.color(c)
    t.pencolor(colors[i%2])
    t.left(30)
    t.circle(i*2)
    t.right(2)
'''
while(True):
    t.pencolor('green')
    t.left(30)
    t.circle(120)
    t.right(2)


turtle.done()


