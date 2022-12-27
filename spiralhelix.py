# Python program to draw 
# Spiral  Helix Pattern
# using Turtle Programming
 

import turtle
import colorsys
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor('black')
t.speed(100)
n=10
h=0
for i in range(100):
		c=colorsys.hsv_to_rgb(h,1,0.9)
		h+=1/n
		t.color(c)
		t.circle(5*i)
		t.circle(-5*i)
		t.left(i)
		