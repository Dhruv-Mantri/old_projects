import turtle
import math

screen = turtle.Screen()
screen.screensize(700,700)
screen.setworldcoordinates(-5,-5,5,5) # sets bottom left and top right of the screen

m1 = 1
m2 = 1
m3 = 1
m4 = 1
r = 1


vx1,vy1 = 0, -0.25
vx2,vy2 = -0.25, 0
vx3,vy3 = 0, 0.25
vx4,vy4 = 0.25, 0

x1,y1 = 2,2
x2,y2 = 2,-2
x3,y3 = -2, -2
x4, y4 = -2, 2

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

turtle4 = turtle.Turtle()
turtle4.pu()
turtle4.shape("circle")
turtle4.color("purple")
turtle4.speed(0)
turtle4.goto(x4,y4)
turtle4.pd()

while True:
    i += 1

    #update gravity
    f12 = gravity(m1, m2, x1, x2, y1, y2)
    f13 = gravity(m1, m3, x1, x3, y1, y3)
    f14 = gravity(m1, m4, x1, x4, y1, y4)
    f23 = gravity(m2, m3, x2, x3, y2, y3)
    f24 = gravity(m2, m4, x2, x4, y2, y4)
    f34 = gravity(m3, m4, x3, x4, y3, y4)
    f12_theta = math.atan2(y2-y1, x2-x1)
    f13_theta = math.atan2(y3-y1,x3-x1)
    f14_theta = math.atan2(y4-y1,x4-x1)
    f23_theta = math.atan2(y3-y2,x3-x2)
    f24_theta = math.atan2(y4-y2,x4-x2)
    f34_theta = math.atan2(y4-y3,x4-x3)


    #update positions
    x1, y1 = vx1*interval+x1, vy1*interval+ y1
    x2, y2 = vx2*interval+x2, vy2*interval+ y2
    x3, y3 = vx3*interval+x3, vy3*interval+ y3
    x4, y4 = vx4*interval+x4, vy4*interval+ y4

    #update velocity
   
    vx1 += f12*math.cos(f12_theta)/m1*interval + f13*math.cos(f13_theta)/m1*interval + f14*math.cos(f14_theta)/m1*interval
    vy1 += f12*math.sin(f12_theta)/m1*interval + f13*math.sin(f13_theta)/m1*interval + f14*math.sin(f14_theta)/m1*interval
    vx2 += f12*math.cos(f12_theta+math.pi)/m2*interval + f23*math.cos(f23_theta)/m2*interval + f24*math.cos(f24_theta)/m2*interval
    vy2 += f12*math.sin(f12_theta+math.pi)/m2*interval + f23*math.sin(f23_theta)/m2*interval + f24*math.sin(f24_theta)/m2*interval
    vx3 += f13*math.cos(f13_theta+math.pi)/m3*interval + f23*math.cos(f23_theta+math.pi)/m3*interval + f34*math.cos(f34_theta)/m3*interval
    vy3 += f13*math.sin(f13_theta+math.pi)/m3*interval + f23*math.sin(f23_theta+math.pi)/m3*interval + f34*math.sin(f34_theta)/m3*interval
    vx4 += f14*math.cos(f14_theta+math.pi)/m4*interval + f24*math.cos(f24_theta+math.pi)/m4*interval + f34*math.cos(f34_theta+math.pi)/m4*interval
    vy4 += f14*math.sin(f14_theta+math.pi)/m4*interval + f24*math.sin(f24_theta+math.pi)/m4*interval + f34*math.sin(f34_theta+math.pi)/m4*interval

    #update sprites
    if i%2000 == 0:
        turtle1.goto(x1, y1)
        turtle2.goto(x2, y2)
        turtle3.goto(x3, y3)
        turtle4.goto(x4, y4)

turtle.done()