import turtle

screen = turtle.Screen()

turtle.tracer(2)
turtle.bgcolor('black')
turtle.pensize(2)
turtle.fillcolor("yellow")
turtle.delay(10)



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


for i in range(12):  # Cambiar de 7 a 8 para tener 8 pétalos
    turtle.begin_fill()
    turtle.forward(50)
    turtle.lt(25)
    turtle.circle(20, 180)
    turtle.lt(25)
    turtle.forward(50)
    turtle.end_fill()
    
    turtle.penup()
    turtle.goto(0, 0)  # Volver al centro
    turtle.left(360 / 11)  # Rotar para el siguiente pétalo
    turtle.pendown()

# Dibujar el centro de la flor
turtle.fillcolor("orangered")
turtle.color("orange")
turtle.penup()
turtle.goto(-20, 0)
turtle.begin_fill()
turtle.circle(20)
turtle.end_fill()

# Ocultar la tortuga
turtle.hideturtle()




turtle.done()
