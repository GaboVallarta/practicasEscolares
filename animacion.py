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
letras.write("Pa ti, sashis", align="center", font=("Arial", 24, "normal"))
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

# time.sleep(2)

# letras.clear()
# turtle.clear()


done()




