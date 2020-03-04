# Universal Gravity Calculator (12pts)
# In physics, the force of gravity between two objects can be calculated using the equation:
# F = G * (m1 * m2) / r**2
# F is the force of gravity in Newtons
# G is the universal gravity constant (6.67e-11)
# m1 is the mass of first object in kg
# m2 is the mass of the second object in kg
# r is the center to center distance between the objects in meters


# Make a calculator that does all of the following
# (3pts) takes the inputs for mass 1, mass 2, and distance between the two objects (m1, m2, and r)
# (4pts) contains exceptions for any potential errors (value and dividebyzero).
# (2pts) keeps asking for inputs until they are valid (see while loop from notes)
# (3pts) calculates the force of gravity in Newtons and print the result to the user in scientific notation to two decimals.

def grav(m1, m2, r):
    g = 6.67e-11
    try:
        answer = float(g * (m1 * m2) / r ** 2)
    except ZeroDivisionError:
        answer = "Silly! Dividing by zero? You can't do that!"
    except ValueError:
        answer = "That somehow is not a number"
    return answer



done = False
while not done:
    try:
        mass1 = float(input("Mass 1:"))
        done = True
    except:
        print("That is not a number, enter a number")

done = False
while not done:
    try:
        mass2 = float(input("Mass 2:"))
        done = True
    except:
        print("That is not a number, enter a number")

done = False
while not done:
    try:
        r = float(input("Distance between objects:"))
        g = 6.67e-11
        answer = float(g * (mass1 * mass2) / r ** 2)
        done = True
    except ZeroDivisionError:
        answer = "Silly! Dividing by zero? You can't do that!"
    except ValueError:
        answer = "That somehow is not a number"
    except:
        print("That is not a number, enter a number")


print("The force of gravity is {:.2e}N".format(answer))
