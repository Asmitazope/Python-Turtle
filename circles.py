# Python program to draw 
# Spiral  Helix Pattern
# using Turtle Programming
 

import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(100)

def Circle():
		n=60
		h=0
		for i in range(100):
			c=colorsys.hsv_to_rgb(h,0.6,0.6)
			h+=1/n
			t.color(c)
			'''
			t.circle(5*i)
			t.circle(-5*i)
			t.left(i)
			'''
			t.forward(i)
			t.down()
			t.backward(i)


Circle()
turtle.done()