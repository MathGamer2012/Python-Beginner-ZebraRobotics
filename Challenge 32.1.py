import turtle
import random


window = turtle.Screen()
marty = turtle.Turtle()

color = ["red", "blue", "cyan", "green", "yellow"]


for i in range(1,21):
    colour = random.choice(color)
    size = random.randint(10,100)
    num = random.randint(0,150)
    num1 = random.randint(0,150)
    marty.penup()
    marty.goto(num,num)
    marty.pendown()
    marty.color("black",colour)
    marty.begin_fill()
    marty.circle(size)
    marty.end_fill()
    




