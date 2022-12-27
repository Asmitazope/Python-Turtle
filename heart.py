import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
  
turtle.pensize(2)  
  
# To design curve  
def curve():  
    for i in range(200):  
        t.right(1)  
        t.forward(1)  
  
t. speed(3)  
t.color("red", "pink")  

  #first   
t.begin_fill()  
t.left(140)  
t.forward(150)
curve()  
  
t.left(140)  
curve()  
t.forward(150)
t.end_fill()  
t.hideturtle() 


#second
t.begin_fill()  
t.left(140)  
t.forward(150)
curve()  
  
t.left(140)  
curve()  
t.forward(150)
t.end_fill()  
t.hideturtle() 

#third
t.begin_fill()  
t.left(140)  
t.forward(150)
curve()  
  
t.left(140)  
curve()  
t.forward(150)
t.end_fill()  
t.hideturtle()     
  
turtle.mainloop()  