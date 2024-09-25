
import turtle
import math


tallo=turtle.Turtle()


tallo.fillcolor("green")
tallo.begin_fill()

tallo.pencolor("green")
tallo.pendown()
tallo.setheading(0)
tallo.forward(5)

tallo.setheading(270)
tallo.forward(310)
tallo.penup()

tallo.goto(0,0)
tallo.pendown()

tallo.setheading(180)
tallo.forward(5)
tallo.setheading(270)
tallo.forward(310)

tallo.setheading(0)
tallo.forward(10)

tallo.end_fill()

tallo.fillcolor("green")
tallo.begin_fill()

tallo.penup()
tallo.goto(0,-200)
tallo.setheading(0)
tallo.pendown()

tallo.circle(80, 60)  
tallo.left(120)  
tallo.circle(80, 60)  

tallo.end_fill()


tallo.fillcolor("green")
tallo.begin_fill()

tallo.penup()
tallo.goto(0,-200)
tallo.setheading(120)
tallo.pendown()

tallo.circle(80, 60)  
tallo.left(120)  
tallo.circle(80, 60)  

tallo.end_fill()

tallo.hideturtle()

turtle.done()