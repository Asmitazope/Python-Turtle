import turtle
import colorsys

t=turtle.Pen()
s=turtle.Screen()
s.bgcolor('black')
t.speed(100)
h=0
n=10
for i in range(20):
	c=colorsys.hsv_to_rgb(h,1,0.9)
	h+=1/n
	t.pencolor('red')
	t.circle(360)
	t.lt(60)
	t.pencolor('purple')
	t.circle(200)
	t.lt(60)
	t.pencolor('blue')
	t.circle(180)
	t.lt(40)
	t.pencolor('yellow')
	t.circle(i)
	t.pencolor('orange')
	t.circle(10)
	t.lt(5)
	
turtle.done()
	

