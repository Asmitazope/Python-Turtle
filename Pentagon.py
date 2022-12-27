import turtle
import colorsys
 
t=turtle.Pen()
s=turtle.Screen()

t.left(65)

s.bgcolor('black')

t.speed(3000)

h=0

n=40

for i in range(1000):
	c=colorsys.hsv_to_rgb(h,1,0.9)
	
	h+=1/n
	
	t.color(c)
	
	t.left(74)
	
	t.forward(i)

turtle.done()

