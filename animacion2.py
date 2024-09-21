
import turtle
import math


turtle.bgcolor("black")
turtle.pencolor("black")
turtle.shape("triangle")
turtle.speed(-2)
turtle.fillcolor("orangered")

phi=137.508 *(math.pi/180)

for i in range (180+40):
    r=4*math.sqrt(i)
    theta= i*phi
    x= r*math.cos(theta)
    y= r*math.sin(theta)
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(i*137.508)
    turtle.pendown()
    if i<160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()

        # Dibujar pétalos elípticos grandes y perpendiculares al centro
        turtle.circle(80, 60)  # Primer arco de la elipse (más grande)
        turtle.left(120)  # Cambiamos la dirección para la otra mitad
        turtle.circle(80, 60)  # Segundo arco de la elipse

        turtle.end_fill()

turtle.hideturtle()

turtle.done()