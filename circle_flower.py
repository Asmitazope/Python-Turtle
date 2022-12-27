import turtle
import colorsys
t=turtle.Pen()
s=turtle.Screen
s.bgcolor('black')
t.speed(1000)
h=0

n=55
for i in range(100):
	c=colorsys.hsv_to_rgb(h,1,0.5)
	h+=1/n
	t.color(c)
	t.circle(i*5)
	t.left(60)
	t.right(60)
	t.right(40)
turtle.done()