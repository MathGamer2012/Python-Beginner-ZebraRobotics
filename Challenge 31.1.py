import turtle
import random

window = turtle.Screen()
marty = turtle.Turtle()

num = random.randint(1,100)
num2 = random.randint(1,100)
num3 = random.randint(1,100)
num4 = random.randint(1,100)
num5 = random.randint(1,100)
num6 = random.randint(1,100)

def square():
    marty.forward(100)
    marty.left(90)
    marty.forward(100)
    marty.left(90)
    marty.forward(100)
    marty.left(90)
    marty.forward(100)
    marty.left(90)
    
marty.penup()
marty.goto(num,num)
marty.pendown()
marty.color("black", "red")
marty.begin_fill()
square()
marty.end_fill()
marty.penup()
marty.goto(num3,num4)
marty.pendown()
marty.color("black", "yellow")
marty.begin_fill()
square()
marty.end_fill()
marty.penup()
marty.goto(num5,num6)
marty.pendown()
marty.color("black", "orange")
marty.begin_fill()
square()
marty.end_fill()
marty.penup()


