import turtle
import math

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(-5,-5,5,5) # sets bottom left and top right of the screen

m1 = 1
m2 = 1
m3 = 1
r = 1

vx3,vy3 = -0.93240737*r,-0.86473146*r
vx1,vy1 = -vx3/2,-vy3/2
vx2,vy2 = vx1,vy1

x1,y1 = 0.97000436*r,-0.24308753*r
x2,y2 = -x1,-y1
x3,y3 = 0,0

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

turtle3 = turtle.Turtle()
turtle3.pu()
turtle3.shape("circle")
turtle3.color("green")
turtle3.speed(0)
turtle3.goto(x3,y3)
turtle3.pd()

while True:
    i += 1

    #update gravity
    f12 = gravity(m1, m2, x1, x2, y1, y2)
    f13 = gravity(m1, m3, x1, x3, y1, y3)
    f23 = gravity(m2, m3, x2, x3, y2, y3)
    f12_theta = math.atan2(y2-y1, x2-x1)
    f13_theta = math.atan2(y3-y1,x3-x1)
    f23_theta = math.atan2(y3-y2,x3-x2)

    #update positions
    x1, y1 = vx1*interval+x1, vy1*interval+ y1
    x2, y2 = vx2*interval+x2, vy2*interval+ y2
    x3, y3 = vx3*interval+x3, vy3*interval+ y3

    #update velocity
    vx1 += f12*math.cos(f12_theta)/m1*interval + f13*math.cos(f13_theta)/m1*interval
    vy1 += f12*math.sin(f12_theta)/m1*interval + f13*math.sin(f13_theta)/m1*interval
    vx2 -= f12*math.cos(f12_theta)/m2*interval - f23*math.cos(f23_theta)/m2*interval
    vy2 -= f12*math.sin(f12_theta)/m2*interval - f23*math.sin(f23_theta)/m2*interval
    vx3 -= f13*math.cos(f13_theta)/m3*interval + f23*math.cos(f23_theta)/m3*interval
    vy3 -= f13*math.sin(f13_theta)/m3*interval + f23*math.sin(f23_theta)/m3*interval


    #update sprites
    if i%2000 == 0:
        turtle1.goto(x1, y1)
        turtle2.goto(x2, y2)
        turtle3.goto(x3, y3)
    # if i > 400000:
    #     turtle1.pu()
    #     turtle2.pu()
    #     turtle3.pu()



turtle.done()