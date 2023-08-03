from vpython import *

# Changing Scene Color
scene.background = color.yellow

# Origin Sphere
sphere(radius=0.25, color=color.blue, opacity=0.8)

# Axis lines
xaxis = cylinder(radius=0.1,
                 color=vector(0.75, 0.75, 0.75),
                 opacity=1,
                 pos=vector(-5, 0, 0),
                 axis=vector(10, 0, 0))

yaxis = cylinder(radius=xaxis.radius,
                 color=xaxis.color,
                 opacity=xaxis.opacity,
                 pos=vector(0, -5, 0),
                 axis=vector(0, 10, 0))

zaxis = cylinder(radius=xaxis.radius,
                 color=xaxis.color,
                 opacity=xaxis.opacity,
                 pos=vector(0, 0, -5),
                 axis=vector(0, 0, 10))

# Creating Dumbell
bar = cylinder(radius=0.5,
               color=color.cyan,
               pos=vector(-2, -1, 0.5),
               axis=vector(1, 2, 3))

sphere1 = sphere(radius=1.25,
                 color=color.red,
                 pos=bar.pos)

sphere2 = sphere(radius=sphere1.radius,
                 color=sphere1.color,
                 pos=bar.pos + bar.axis)
