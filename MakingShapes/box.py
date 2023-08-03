from vpython import *

# First Box
box()

# Adjusting Parameters
box(pos=vector(1, 0, 0), size=vector(1, .3, .2), color=color.yellow)

# Creating a Better Purple
purpleHSV = (vector(148, 0, 211)) / 255
purpleRGB = color.hsv_to_rgb(purpleHSV)

box(pos=vector(-1, 0, 0), size=vector(1, .2, .2), color=purpleHSV)

# Creating a Mowhawk
box(pos = vector(0, .6, 0), size = vector(.5, .2, 1), color = color.red)

# Creating The Eyeballs
box(pos = vector(-.2,.2,.6), size = vector(.2, .2, .2), color = color.black)
box(pos = vector(.2,.2,.6), size = vector(.2, .2, .2), color = color.black)

# Creating the Mouth
box(pos = vector(x,-.2,.6), size= vector(.75, .2, .2), color = color.blue)