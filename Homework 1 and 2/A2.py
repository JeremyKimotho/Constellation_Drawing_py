# Jeremy Kimotho-30096043, CPSC  231 02-T06
# This is a program written in python that uses eval to evaluate expressions and turtle to plot these expressions.
# 18/10/2019

from math import *
import turtle

# CONSTANTS
WIDTH = 800
HEIGHT = 600
AXISCOLOR = "black"
#  Returns the screen (pixel based) coordinates of some (x, y) graph location base on configuration
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#  x, y: the graph location to change into a screen (pixel-based) location
#  Returns: (screenX, screenY) which is the graph location (x,y) as a pixel location in the window
def screenCoor(xo, yo, ratio, x, y):
  x_coordinate=xo+(ratio*x)
  y_coordinate=yo+(ratio*y)
  return x_coordinate, y_coordinate
#  Returns a string of the colour to use for the current expression being drawn
#  This colour is chosen based on which how many expression have previously been drawn
#  The counter starts at 0, the first or 0th expression, should be red, the second green, the third blue
#  then loops back to red, then green, then blue, again
#  counter: an integer where the value is a count (starting at 0) of the expressions drawn
#  Returns: 0 -> "red", 1 -> "green", 2 -> "blue", 3 -> "red", 4 -> "green", etc.
def getColor(counter):
    if counter==0 or counter%3==0:
      return 'red'
    elif counter==1 or counter%3==1:
      return 'green'
    elif counter==2 or counter%3==2:
      return 'blue'
#  Draws the tick and number for the x axis    
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
def drawXAxisLabelTick(pointer, screenX, screenY, text):
    # Go to the coordinate where the tick and number should be drawn. The tick drawn is 6 pixels long and the number is written 20 pixels below the point. If the number is 0 don't write it. Then go back to the point on the line so the line stays straight.
    pointer.penup()
    pointer.goto(screenX, screenY+3)
    pointer.pendown()
    pointer.goto(screenX, screenY-3)
    pointer.goto(screenX,screenY)
    pointer.penup()
    pointer.goto(screenX, screenY-20)
    pointer.pendown()
    if text!=0:
      pointer.write(text)
    pointer.penup()
    pointer.goto(screenX,screenY)
    pointer.pendown()
#  Draws the tick and number for the y axis
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
def drawYAxisLabelTick(pointer, screenX, screenY, text):
    # Go to the coordinate where the tick and number should be drawn. The tick drawn is 6 pixels long and the number is written 20 pixels to the left the point. If the number is 0 don't write it. Then go back to the point on the line so the line stays straight.
    pointer.penup()
    pointer.goto(screenX+3, screenY)
    pointer.pendown()
    pointer.goto(screenX-3, screenY)
    pointer.goto(screenX,screenY)
    pointer.penup()
    pointer.goto(screenX-10, screenY-5)
    pointer.pendown()
    if text!=0:
      pointer.write(text)
    pointer.penup()
    pointer.goto(screenX,screenY)
    pointer.pendown()
#  Draw in the window an xaxis (secondary function is to return the minimum and maximum graph locations drawn at)
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#  Returns: (xmin, ymin) where xmin is minimum x location drawn at and xmax is maximum x location drawn at
def drawXAxis(pointer, xo, yo, ratio):
    # The loop goes from the smallest x value of the graph to the largest x value on the graph in increments of 1. The x_value and y_value variables are the converted graph values to screen coordinates
    xmin=-(int((WIDTH/2)/ratio))
    xmax=int((WIDTH/2)/ratio)
    pointer.penup()
    pointer.goto(xo-int(WIDTH/2),yo)
    pointer.pendown()
    for i in range(-(int((WIDTH/2)/ratio)), int((WIDTH/2)/ratio)+1, 1):
      x_value1,y_value1=screenCoor(xo,yo,ratio,i, 0)
      pointer.goto(x_value1, y_value1)
      drawXAxisLabelTick(pointer, x_value1, y_value1, i)
    return xmin, xmax
#  Draw in the window an yaxis 
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
def drawYAxis(pointer, xo, yo, ratio):
    # The loop goes from the smallest y value of the graph to the largest y value on the graph in increments of 1. The x_value and y_value variables are the converted graph values to screen coordinates
    pointer.penup()
    pointer.goto(xo,yo-int(HEIGHT/2))
    pointer.pendown()
    for i in range(-(int((HEIGHT/2)/ratio)), int((HEIGHT/2)/ratio)+1, 1):
      x_value2,y_value2=screenCoor(xo,yo,ratio,0, i)
      pointer.goto(x_value2, y_value2)
      drawYAxisLabelTick(pointer, x_value2, y_value2, i)
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#  expr: the expression to draw (assumed to be valid)
#  xmin, ymin : the range for which to draw the expression [xmin, xmax]
def drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr):
    # The pointer is set onto the first point it'll start drawing from. The while loop draws the function and the for loop draws the local maximum and minimums. The class Coordinates is used to store the coordinates that will be looped through for the local maximum and minimums.
    class Coordinates:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    x=xmin
    x_start, y_start=screenCoor(xo,yo,ratio,xmin,eval(expr))
    pointer.penup()
    pointer.goto(x_start, y_start)
    pointer.pendown()
    i=xmin
    local=[]
    while(i<=xmax):
      x=i
      y=eval(expr)
      x_value, y_value=screenCoor(xo,yo,ratio,x,y)
      coords=Coordinates(x_value, y_value)
      local.append(coords)
      if y_value<=(WIDTH*2) and y_value>=-(WIDTH*2):
        pointer.goto(x_value,y_value)
      i+=0.01
    for i in range(1, len(local)-1):
      if local[i].y>local[i-1].y and local[i].y>local[i+1].y:
        pointer.penup()
        pointer.goto(local[i].x, local[i].y-5)
        pointer.pendown()
        pointer.color('purple')
        pointer.circle(5)
      elif local[i].y<local[i-1].y and local[i].y<local[i+1].y:
        pointer.penup()
        pointer.goto(local[i].x, local[i].y-5)
        pointer.pendown()
        pointer.color('orange')
        pointer.circle(5)

#  Setup of turtle screen before we draw
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    return pointer
#  Main function that attempts to graph a number of expressions entered by the user
#  The user is also able to designate the origin of the chart to be drawn, as well as the ratio of pixels to steps (shared by both x and y axes)
#  The window size is always 800 width by 600 height in pixels
def main():
    #Setup window
    pointer = setup()

    #Get input from user
    xo, yo = eval(input("Enter pixel coordinates of origin: "))
    ratio = int(input("Enter ratio of pixels per step: "))

    #Set color and draw axes (store discovered visible xmin/xmax to use in drawing expressions)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer, xo, yo, ratio)
    drawYAxis(pointer, xo, yo, ratio)

    #Loop and draw expressions until empty string "" is entered, change expression colour based on how many expressions have been drawn
    expr = input("Enter an arithmetic expression: ")
    counter = 0
    while expr != "":
        pointer.color(getColor(counter))
        drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
        expr = input("Enter an arithmetic expression: ")
        counter += 1
 
#Run the program
main()
