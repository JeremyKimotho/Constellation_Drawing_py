# Jeremy Kimotho-30096043, CPSC  231 02-T06
# This is a program written in python that uses turtle to plot circles and lines. It will also indicate any points of 
# intersection between the given circle and line- if there is no intersection that will be indictated. 
# 26/09/2019

import turtle
import math

# Window Setup
width=800
height=600
turtle.screensize(width, height)
turtle.setup(width,height,0,0)
turtle.setworldcoordinates(0, 0, width, height)

# Axis Drawing
c_yaxis=300
c_xaxis=400
turtle.hideturtle()
turtle.speed('fast')
turtle.color('black')
turtle.penup()
turtle.goto(0, c_yaxis)
turtle.pendown()
turtle.goto(width, c_yaxis)
turtle.penup()
turtle.goto(c_xaxis, height)
turtle.pendown()
turtle.goto(c_xaxis, 0)

# Collecting Variables
xc=float(input('Please enter the x coordinate of the center of the circle: '))
yc=float(input('Please enter the y coordinate of the center of the circle: '))
r=float(input('Please enter the radius of the circle: '))
x1=float(input('Please enter the starting x coordinate of the line: '))
y1=float(input('Please enter the starting y coordinate of the line: '))
x2=float(input('Please enter the end x coordinate of the line: '))
y2=float(input('Please enter the end y coordinate of the line: '))

# Calculations of a,b,c for discriminant
a = math.pow((x2-x1), 2) + math.pow((y2-y1), 2)
b = 2*(((x1-xc)*(x2-x1)) + ((y1-yc)*(y2-y1)))
c = math.pow(x1-xc, 2) + math.pow(y1-yc, 2) - math.pow(r, 2)

# Calculating Discriminant
discriminant = math.pow(b,2) - (4*a*c)

# Setting Start Position of Turtle
turtle.penup()
turtle.goto(xc-200+r, yc-200)
turtle.pendown()

# Circle Drawing
turtle.color('red')
turtle.circle(r)

# Setting Start Position of Turtle
turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()

# Line Drawing
turtle.color('blue')
turtle.goto(x2, y2)

# Determining Number of intersections, and drawing circles around them if necessary
r_intsct=5
if(discriminant>0 or discriminant==0):
  alpha1 = (-b + math.sqrt(discriminant))/(2*a)
  alpha2 = (-b - math.sqrt(discriminant))/(2*a)
  if(alpha1>0 and alpha1<1):
    # Calculating Coordinates of Intersection
    xi_1 = ((1-alpha1)*x1) + (alpha1*x2)
    yi_1 = ((1-alpha1)*y1) + (alpha1*y2)
    # Drawing Circles of intersection
    turtle.color('green')
    turtle.penup()
    turtle.goto(xi_1,yi_1-r_intsct)
    turtle.pendown()
    turtle.circle(r_intsct)
  if(alpha2>0 and alpha2<1):
    # Calculating Coordinates of Intersection
    xi_2 = ((1-alpha2)*x1) + (alpha2*x2)
    yi_2 = ((1-alpha2)*y1) + (alpha2*y2)
    # Drawing Circles of intersection
    turtle.color('green')
    turtle.penup()
    turtle.goto(xi_2,yi_2-r_intsct)
    turtle.pendown()
    turtle.circle(r_intsct)
  if((alpha1>1 or alpha1<0) and (alpha2>1 or alpha2<0)):
    print(alpha1, alpha2)
    # No Intersection Text
    turtle.color('green')
    turtle.penup()
    turtle.goto(260,c_yaxis)
    turtle.pendown()
    turtle.write('No Intersection!', font=('Courier', 25))
elif(discriminant<0):
  # No Intersection Text
  turtle.color('green')
  turtle.penup()
  turtle.goto(260,c_yaxis)
  turtle.pendown()
  turtle.write('No Intersection!', font=('Courier', 25))

# Resetting Position of turtle
turtle.penup()
turtle.goto(0,0)
turtle.color('black')
turtle.showturtle()

turtle.exitonclick()










































































































































































































