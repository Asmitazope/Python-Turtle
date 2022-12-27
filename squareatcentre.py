import turtle
import colorsys
t=turtle.Pen()
s=turtle.Screen()
s.bgcolor('black')
h=0
n=10
t.speed(100)
for i in range(200):
	c=colorsys.hsv_to_rgb(h,0.5,1)
	h+=1/n
	t.lt(90)
	t.lt(20)
	t.circle(160)
	t.shape('square')
	t.lt(30)
	t.shape('triangle')
	t.color(c)

turtle.done()
