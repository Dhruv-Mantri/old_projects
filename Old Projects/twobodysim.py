import turtle
import math

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(-5,-5,5,5) # sets bottom left and top right of the screen

m1 = 1 #2
m2 = 1
x1, y1 = -3,0
x2, y2 = 3,0
vx1, vy1 = 0, 0.25
vx2, vy2 = 0, -0.25 #-0.5

interval = 0.0001

i = 0

def distance(x1,x2,y1,y2):
    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
    return distance

def gravity(m1,m2,x1,x2,y1,y2):
    gravity = m1*m2/(distance(x1,x2,y1,y2))**2
    return gravity

turtle1 = turtle.Turtle()
turtle1.pu()
turtle1.shape("circle")
turtle1.color("red")
turtle1.speed(0)
turtle1.goto(x1,y1)
turtle1.pd()

turtle2 = turtle.Turtle()
turtle2.pu()
turtle2.shape("circle")
turtle2.color("blue")
turtle2.speed(0)
turtle2.goto(x2,y2)
turtle2.pd()

while True:
    i += 1

    #update gravity
    f12 = gravity(m1, m2, x1, x2, y1, y2)
    f12_theta = math.atan2(y2-y1, x2-x1)

    #update positions
    x1, y1 = vx1*interval+x1, vy1*interval+ y1
    x2, y2 = vx2*interval+x2, vy2*interval+ y2

    #update velocity
    vx1 += f12*math.cos(f12_theta)/m1*interval
    vy1 += f12*math.sin(f12_theta)/m1*interval
    vx2 -= f12*math.cos(f12_theta)/m2*interval
    vy2 -= f12*math.sin(f12_theta)/m2*interval


    #update sprites
    if i%4000 == 0:
        turtle1.goto(x1, y1)
        turtle2.goto(x2,y2)



turtle.done()