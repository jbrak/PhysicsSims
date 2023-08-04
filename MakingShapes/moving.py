from vpython import *

# origin
sphere(radius=0.5, pos=vector(0, 0, 0))

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

# Define particle
pos0 = vector(-5, 0, 0)
pos1 = vector(5, 5, 0)

particle = box(pos=pos0, size=vector(1, 1, 1), color=color.white)


# Create Movment Function
def step(obj, start, end, distance):
    movementvector = hat(end - start) * distance

    obj.pos += movementvector


# Graph
graph(width=800, height=250)
xDots = gdots(color=color.green)
yDots = gdots(color=color.magenta)

# Movement Engine
y = mag(pos1 - pos0) / 10

t=0
while True:
    step(particle, pos0, pos1, y)
    if particle.pos == pos1 or particle.pos == pos0:
        y = -y

    print(particle.pos, y)
    print(particle.pos == pos1, "\n")
    rate(10)
    xDots.plot(t, particle.pos.x)
    yDots.plot(t, particle.pos.y)
    t+=1
