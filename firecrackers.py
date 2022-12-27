import turtle
import colorsys
t=turtle.Pen()
s=turtle.Screen()
h=0
n=2
t.speed(5000)
s.bgcolor('black')

for i in range(500):
	c=colorsys.hsv_to_rgb(h,1,1)
	h+=1/n
	t.color(c)
	t.left(60)
	t.right(35)
	t.backward(i)
	t.forward(i)
	
for j in range(300):
	c=colorsys.hsv_to_rgb(h,0.5,0.5)
	h+=1/n
	t.color(c)
	t.left(35)
	t.right(60)
	t.backward(j)
	t.forward(j)
	
turtle.done()