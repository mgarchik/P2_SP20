# Turtle recursion
import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

my_screen = turtle.Screen()
my_screen.bgcolor('white')

# draw a shape using goto
my_turtle.fillcolor('red')
my_turtle.begin_fill()  # starts a shape to fill in
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()

# pick up turtle
my_turtle.up()
my_turtle.goto(-200, -200)
my_turtle.down()
my_turtle.fillcolor('blue')
my_turtle.begin_fill()
my_turtle.goto(0, 0)
my_turtle.goto(0, -200)
my_turtle.goto(-200, -200)
my_turtle.end_fill()

# draw using headings
my_turtle.up()
my_turtle.goto(0, 0)
my_turtle.down()
my_turtle.width(4)

my_turtle.fillcolor('yellow')
my_turtle.begin_fill()
my_turtle.setheading(90)
my_turtle.forward(50)
my_turtle.left(30)

# Recursive rectangle pattern


my_screen.exitonclick()