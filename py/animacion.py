from turtle import*
import turtle
import time
import math




screen = turtle.Screen()



letras=turtle.Turtle()



tracer(2)
h=0
bgcolor('black')
pensize(2)
color('yellow')

time.sleep(5)


#image_files = []

for i in range(195):
    h+=0.006
    lt(179)
    backward(i*0.1)
    circle(i*0.3,120)
    rt(14)
    forward(i*0.1)
    circle(i*0.3,120)
    #filename = f"frame_{i:03d}.gif"
    #screen.getcanvas().postscript(file=f"frame_{i:03d}.ps")
   #image_files.append(filename)



turtle.penup()
letras.goto(0, 250)  
letras.color("white")  
letras.write("Pa ti, sashis :D", align="center", font=("Arial", 24, "normal"))
letras.color('black')




turtle.shape('turtle')
turtle.pencolor('orangered')
turtle.fillcolor('orange')
phi=137.508 *(math.pi/180)

for i in range(300):
    r=4*math.sqrt(i)
    theta= i*phi
    x=r*math.cos(theta)
    y=r*math.sin(theta)
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(i*137.508)
    turtle.pendown()
    turtle.stamp()
    screen.update()
    #filename = f"frame_{i+195:03d}.gif"
    #screen.getcanvas().postscript(file=f"frame_{i+195:03d}.ps")
    #image_files.append(filename)

letras.clear()
letras.goto(0, 250)  
letras.color("white")  
letras.write("TKM <3", align="center", font=("Arial", 24, "normal"))
letras.color('black')

time.sleep(2)

turtle.clear()



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



done()




