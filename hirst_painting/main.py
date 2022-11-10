# import colorgram
import random
from turtle import Turtle, Screen

# Extracting colors from the image
# rgb_colors = []
# colors = colorgram.extract(r'C:\Users\Abubakar\OneDrive\Documents\GitHub\Py-Basics\hirst_painting\painting.jpg', 20)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
    
# print(rgb_colors)

def random_color():
    """returns a tuple of (r, g, b)"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


# rgb color list
colors_list = [(229, 228, 226), (225, 223, 224), (199, 175, 117),
               (124, 36, 24), (210, 221, 213), (168, 106, 57), 
               (222, 224, 227), (186, 158, 53), (6, 57, 83), 
               (109, 67, 85), (113, 161, 175), (22, 122, 174),
               (64, 153, 138), (39, 36, 36), (76, 40, 48), 
               (9, 67, 47), (90, 141, 53), (181, 96, 79), 
               (132, 40, 42), (210, 200, 151)]


jimmy = Turtle() # initializing turtle object
my_screen = Screen() # initializing Screen object


# Initial settings
my_screen.colormode(255)
jimmy.penup()
jimmy.goto(-300, -300)


# drawing dot painting with size 10 x 10
for position in range(10):
    # this for loop sets the coordinates of the turtle
    y = jimmy.ycor()
    y += 50
    jimmy.goto(-100, y)
    for dot in range(10):
        # this for loop draws the 10 spots in a line
        jimmy.dot(20, random.choice(colors_list))
        jimmy.forward(50)
    








my_screen.exitonclick()