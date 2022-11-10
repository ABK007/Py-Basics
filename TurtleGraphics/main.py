from turtle import Turtle, Screen 
import random

james_the_turtle = Turtle()  # Initializing the turtle object

james_the_turtle.shape("arrow") # Changing the shape of turtle object

james_the_turtle.color("red") # changing the color of the turtle object

my_screen = Screen()    # Initializing the screen object 


def random_color():
    """returns a tuple of (r, g, b)"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Code for creating the square
# james_the_turtle.forward(100)
# james_the_turtle.right(90)
# james_the_turtle.forward(100)
# james_the_turtle.right(90)
# james_the_turtle.forward(100)
# james_the_turtle.right(90)
# james_the_turtle.forward(100)


# drawing a dashed line
# for i in range(20):
#     james_the_turtle.forward(5)
#     james_the_turtle.penup()
#     james_the_turtle.forward(5)
#     james_the_turtle.pendown()


# drawing an equilateral triangle
# for i in range(3):
#     james_the_turtle.forward(100)
#     james_the_turtle.right(120)
#     # james_the_turtle.forward(100)
#     # james_the_turtle.right(120)
#     # james_the_turtle.forward(100)
    
# james_the_turtle.color("black")
    
# # drawing a square
# for i in range(4):
#     james_the_turtle.forward(100)
#     james_the_turtle.right(90)
    

# james_the_turtle.color("green")
    
# # drawing a pentagon
# for i in range(5):
#     james_the_turtle.forward(100)
#     james_the_turtle.right(72)
    
    
# james_the_turtle.color("blue")
    
# # drawing a pentagon
# for i in range(6):
#     james_the_turtle.forward(100)
#     james_the_turtle.right(60)



# # drawing triangle, square, penta, hexa, hepta, octa, nona and decagon 
# color = ["red", "black", "blue", "green", "yellow", "cyan", "orange", "pink"]
# for number in range(3,11):
#     angle = 360/number
#     color_number = number - 3
#     james_the_turtle.color(color[color_number])
#     for i in range(number):
#         james_the_turtle.forward(100)
#         james_the_turtle.right(angle)
        

# drawing a random walk
# steps = (25, -25)
# angle = (0, 90, 180, 270)

# color = ["medium blue", "green", "chartreuse", "crimson", "salmon", "cyan", "orange", "dodger blue"]

my_screen.colormode(255)

# for i in range(200):
#     james_the_turtle.speed(10) # increasing speed
#     james_the_turtle.pensize(10) # Increasing pen width
#     james_the_turtle.pencolor(random_color()) # randomizing color 
#     james_the_turtle.forward(random.choice(steps)) # randomizing steps
#     james_the_turtle.setheading(random.choice(angle)) # randomizing angle
    

# Drawing a spirograph

def draw_spirograph(size_of_gap):
    """ Draws a spirograph"""
    for i in range(int(360/size_of_gap)):
        current_heading = james_the_turtle.heading()
        james_the_turtle.speed("fastest") # increasing speed
        james_the_turtle.pencolor(random_color()) # randomizing color 
        james_the_turtle.circle(150)
        james_the_turtle.setheading(current_heading + 10) 
        

draw_spirograph(10)
    


    
    














my_screen.exitonclick() # Screen will close on a click

