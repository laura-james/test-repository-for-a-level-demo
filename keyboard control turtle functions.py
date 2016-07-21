import turtle

turtle.shape("turtle")
turtle.speed(100)

def moveForward():
    turtle.setheading(0)
    turtle.forward(10)

def moveUp():
    turtle.setheading(90)
    turtle.forward(10)

def moveDown():
    turtle.setheading(-90)
    turtle.forward(10)

def moveBack():
    turtle.setheading(180)
    turtle.forward(10)

def colorRed():
    turtle.color("red")

def colorBlue():
    turtle.color("blue")
def stampme():
    turtle.stamp()
def writepos():
    turtle.write(str(turtle.xcor())+" "+str(turtle.ycor()))

turtle.onkey(moveForward,"Right")
turtle.onkey(moveBack,"Left")
turtle.onkey(moveUp,"Up")
turtle.onkey(moveDown,"Down")
turtle.onkey(colorRed,"a")
turtle.onkey(colorBlue,"s")
turtle.onkey(writepos,"space")


turtle.listen()
turtle.exitonclick()