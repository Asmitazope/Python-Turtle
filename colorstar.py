import turtle
import colorsys

t=turtle.Pen()
s=turtle.Screen()
s.bgcolor('black')
h=0
n=40
t.speed(1000)
for i in range(n+20):
		c=colorsys.hsv_to_rgb(h,1,1)
		h+=1/n
		t.forward(100)
		t.lt(90)
		t.left(60)
		t.lt(90)
		t.forward(100)
		t.lt(90)
		t.circle(60)
		t.color(c)
		t.circle(70)
		t.circle(80)
		
		#t.lt(60)	
		t.circle(70)
		#t.lt(60)	
		t.circle(90)		
		#t.lt(60)	
		t.circle(95)
turtle.done()