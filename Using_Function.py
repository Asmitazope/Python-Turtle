# Python program to draw 
# Spiral  Helix Pattern
# using Turtle Programming
 

import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
#s.bgcolor('black')
t.speed(100)

def Circle():
		n=60
		h=0
		for i in range(100):
			c=colorsys.hsv_to_rgb(h,1,0.9)
			h+=1/n
			t.color(c)
			t.circle(5*i)
			t.circle(-5*i)
			t.left(i)
			
			return Circle()
		
def CircleFlower():
	for i in range(100):
		n=60
		h=0
		c=colorsys.hsv_to_rgb(h,1,0.5)
		h+=1/n
		t.color(c)
		t.circle(i*5)
		t.left(60)
		t.right(60)
		t.right(40)
		return CircleFlower()
		

def Shape(x):
	switcher={
	0:'Circle',
	1:'CircleFlower'	}
	f=return switcher.get(x,"Invalid")
	return f()

	
turtle.done()