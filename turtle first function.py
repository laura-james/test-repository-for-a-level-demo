import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")      # Set the window background color
wn.title("Hello, Tess!")      # Set the window title
alex = turtle.Turtle()    # Create a turtle, assign to alex
dan = turtle.Turtle()    # Create a turtle, assign to dan

dan.shape("turtle")
dan.speed(100)
dan.pu()
dan.goto(-100,100)
dan.pd()

alex.shape("turtle")
alex.speed(100)
alex.pu()
alex.goto(100,-100)
alex.pd()


def square(sidelen,turtle):
    turtle.begin_fill()
    for x in range(0, 4):
        #move forward sidelen
        turtle.forward(sidelen)
        #rotate 90 degrees to the left
        turtle.left(90)
    turtle.end_fill()

def hexagon(sidelen,turtle):
   # turtle.begin_fill()
    for x in range(0, 6):
        #move forward sidelen
        turtle.forward(sidelen)
        #rotate 90 degrees to the left
        turtle.left(60)
    #turtle.end_fill()


for y in range(0, 10):
    dan.color("red","blue")
    square(100,dan)
    dan.right(36)

    alex.color("green","red")
    hexagon(50,alex)
    alex.right(36)
for c in ["yellow", "red", "purple", "blue"]:
    alex.color(c)
    alex.forward(50)
    alex.left(90)

turtle.exitonclick()
