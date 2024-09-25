import turtle
from turtle import *




def coordenadas(x=str,lapiz=turtle.Turtle()):
    if x[0]=='x':
        if x[1]!='y':
            
            return goto()
        
    if x[0]=='y':
        print("y")
    if x[0]=='d':
        print("down")
    if x[0]=='u':
        print("up")
    





lineal=turtle.Turtle()

pantalla=turtle.Screen()
lineal.pencolor("black")
lineal.color("gray")



pantalla.bgcolor(
    'white'
)

while(1):
    accion=str(input("vas "))

    coordenadas(accion,lineal)


    done()  


# lineal.penup()
# lineal.goto(-300,100)
# lineal.pendown()
# lineal.goto(-300,-100)
# lineal.goto(-300,0)
# lineal.forward(50)

