import turtle

window = turtle.Screen()

marty = turtle.Turtle()

hexagon = 0
numShapes = 0
newPos = 15

while numShapes < 6:
    

    while(hexagon != 6):
        marty.forward(50)
        marty.left(60)
        
        hexagon += 1

    marty.penup()
    marty.goto(newPos,newPos)
    marty.pendown()
    numShapes +=1
    hexagon = 0
    newPos += 15

    







