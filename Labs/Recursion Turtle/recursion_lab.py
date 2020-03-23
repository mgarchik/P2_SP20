from math import sqrt
'''
Turtle Recursion (30pts)

1)  Using the turtle library, create the H fractal pattern as shown in the image (htree4.jpg) in this directory. (15pts)

2)  Using the turtle library, create any of the other recursive patterns in the directory. (10pts)

3)  Create your own work of art with a repeating pattern of your making.  It must be a repeated pattern using recursion. Snowflakes, trees, and spirals are a common choice.  Or you can create a third one from the directory. (5pt)


 Each fractal should
 - be recursive
 - have a depth of at least 4
 - be contained on the screen

  Have fun!

'''

import turtle

my_turtle = turtle.Turtle()
my_turtle.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor('white')

def h_recursion(x, y, width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()

        # upper right
        my_turtle.goto(x + width / 2, y)
        my_turtle.goto(x + width / 2, y + height / 2)

        my_turtle.up()
        my_turtle.goto(x + width / 2, y)
        my_turtle.down()

        # lower right
        my_turtle.goto(x + width / 2, y)
        my_turtle.goto(x + width / 2, y - height / 2)

        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()

        # upper left
        my_turtle.goto(x - width / 2, y)
        my_turtle.goto(x - width / 2, y + height / 2)

        my_turtle.up()
        my_turtle.goto(x - width / 2, y)
        my_turtle.down()

        # lower left
        my_turtle.goto(x - width / 2, y)
        my_turtle.goto(x - width / 2, y - height / 2)

        h_recursion(x + width / 2, y + height / 2, width / 2, height / 2, depth - 1)
        h_recursion(x + width / 2, y - height / 2, width / 2, height / 2, depth - 1)
        h_recursion(x - width / 2, y + height / 2, width / 2, height / 2, depth - 1)
        h_recursion(x - width / 2, y - height / 2, width / 2, height / 2, depth - 1)


# h_recursion(0, 0, 200, 200, 4)

my_screen.clear()
my_turtle.home()
colors = ['black', 'red', 'orange', 'yellow', 'green', 'blue', 'purple']


def sierpenski(x, y, size, depth):
    deg = 0

    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()
        my_turtle.fillcolor(colors[depth])
        my_turtle.begin_fill()
        for i in range(3):
            my_turtle.setheading(deg)
            my_turtle.forward(size)
            deg += 120
        my_turtle.end_fill()
        sierpenski(x, y, size / 2, depth - 1)
        sierpenski(x + size / 2, y, size / 2, depth - 1)
        sierpenski(x + size / 4, y + (sqrt(3) * size / 4), size / 2, depth - 1)



# sierpenski(-240, -200, 500, 6)

my_screen.clear()
my_turtle.home()


def semi(x, y, size, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()

        my_turtle.fillcolor(colors[depth])
        my_turtle.begin_fill()
        my_turtle.goto(x + size * 2, y)
        my_turtle.setheading(90)
        my_turtle.circle(size, 180)
        my_turtle.end_fill()

        semi(x, y, size / 2, depth - 1)
        semi(x + size, y, size / 2, depth - 1)


# semi(-240, -200, 200, 6)

my_screen.clear()
my_turtle.home()

def koch(x, y, length, depth, first=False):
    if first:
        for i in range(3):
            if depth > 0:
                my_turtle.up()
                my_turtle.goto(x, y)
                my_turtle.down()

                koch(my_turtle.xcor(), my_turtle.ycor(), length, depth - 1, False)
                my_turtle.left(60)
                koch(my_turtle.xcor(), my_turtle.ycor(), length, depth - 1, False)
                my_turtle.right(120)
                koch(my_turtle.xcor(), my_turtle.ycor(), length, depth - 1, False)
                my_turtle.left(60)
                koch(my_turtle.xcor(), my_turtle.ycor(), length, depth - 1, False)
            else:
                my_turtle.forward(length)
            my_turtle.right(120)
            x, y = my_turtle.pos()
    else:
        if depth > 0:
            my_turtle.up()
            my_turtle.goto(x, y)
            my_turtle.down()

            koch(my_turtle.xcor(), my_turtle.ycor(), length, depth - 1, False)
            my_turtle.left(60)
            koch(my_turtle.xcor(), my_turtle.ycor(), length, depth - 1, False)
            my_turtle.right(120)
            koch(my_turtle.xcor(), my_turtle.ycor(), length, depth - 1, False)
            my_turtle.left(60)
            koch(my_turtle.xcor(), my_turtle.ycor(), length, depth - 1)
        else:
            my_turtle.forward(length)


my_turtle.setheading(0)
koch(-200, 100, 3, 4, True)



my_screen.exitonclick()
