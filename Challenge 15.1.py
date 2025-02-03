import turtle
sides = int(input("How many equal sides are in the shape: "))
side = 0
pixel = int(input("What do you want the size of the shape be: "))
calculate = 360 / sides

window = turtle.Screen()
marty = turtle.Turtle()
print(calculate)
while(side != sides):
    marty.forward(pixel)
    marty.left(calculate)
    side += 1

