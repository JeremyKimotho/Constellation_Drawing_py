import sys
import os
import turtle

WIDTH = 600
HEIGHT = 600
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"

def command_line():
  for arg in sys.argv:
    print(arg)

def read_star_info():
  pass

def axis_drawing():
  pass

def star_drawing():
  pass

def read_const_info():
  pass

def const_drawing():
  pass

def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)
    pointer.up()
    return pointer

def main():
    command_line()
    #Handle arguments
    #Read star information from file (function)
    # pointer = setup()
    #Draw Axes (function)
    #Draw Stars (function)
    #Loop getting filenames
        #Read constellation file (function)
        #Draw Constellation (function)
        #Draw bounding box (Bonus) (function)

main()