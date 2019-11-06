import sys
import os
import turtle
from os import path

WIDTH = 600
HEIGHT = 600
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"

# The function takes in graph points an input and returns the equivalent coordinates on the turtle window. xo,yo are the coordinate points of the graph location 0,0. The ratio is the number of pixels between 0 and 1.
def screenCoor(x, y):
    xo=WIDTH/2
    yo=HEIGHT/2
    ratio=300
    x_coordinate=float(xo+(ratio*x))
    y_coordinate=float(yo+(ratio*y))
    return x_coordinate, y_coordinate

#  Collects data from the command line input using the number of arguments. Checks inputted star_file to ensure it exists and then prompts for constellation files until user enters blank input. Constellation files are also checked for validity. Function then returns three variables in all situations where an error doesn't occur. These are first the star_file the user entered, then a list of the constellation files the user entered, and finally a code of 0, 1, or 2. The code determines if the star and constellations will just be drawn (0), if the star and constellation files will be drawn and the names written in the drawing window (1) or finally if the star and constellation files will be drawn and the names printed to the screen. All the situations that do not result in an error have one of the three coded outcomes.
def command_line():
    if len(sys.argv)==1:
        print('prompt for a stars-location-file, then loop prompting for valid constellation files until the user enters an empty string (“”)')
        star_file=input('Enter a stars-location-file: ')
        if path.exists(star_file)==False:
            print(f'The file entered {star_file} does not exist.')
            sys.exit(1)
        const_file=input('Enter a constellation file: ')
        const_files=[]
        while const_file!='':
            if path.isfile(const_file)==False:
                print(f'The constellation file you entered {const_file} is invalid.')
                sys.exit(1)
            const_files.append(const_file)
            const_file=input('Enter a constellation file: ')
        print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
        return star_file, const_files, 0

    elif len(sys.argv)==2:
        if sys.argv[1]=='-names':
            print('prompt for a stars-location-file and when drawing named stars write their names to drawing window, then loop prompting for valid constellation files until “” entered”')
            star_file=input('Enter a stars-location-file: ')
            if path.exists(star_file)==False:
                print(f'The file entered {star_file} does not exist.')
                sys.exit(1)
            const_file=input('Enter a constellation file: ')
            const_files=[]
            while const_file!='':
                if path.isfile(const_file)==False:
                    print(f'The constellation file you entered {const_file} is invalid.')
                    sys.exit(1)
                const_files.append(const_file)
                const_file=input('Enter a constellation file: ')
            print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
            return star_file, const_files, 1

        else:
            print('use arg1 as stars-location-file, and loop prompting for valid constellation files until “” entered')
            star_file=sys.argv[1]
            if path.exists(star_file)==False:
                print(f'The file entered {star_file} does not exist.')
                sys.exit(1)
            const_file=input('Enter a constellation file: ')
            const_files=[]
            while const_file!='':
                if path.isfile(const_file)==False:
                    print(f'The constellation file you entered {const_file} is invalid.')
                    sys.exit(1)
                const_files.append(const_file)
                const_file=input('Enter a constellation file: ')
            print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
            return star_file, const_files, 0

    elif len(sys.argv)==3:
        if sys.argv[1]=='-names':
            print('use arg2 as stars-location-file and when drawing named stars write their name to screen, loop prompting for valid constellation files until “” entered')
            star_file=sys.argv[2]
            if path.exists(star_file)==False:
                print(f'The file entered {star_file} does not exist.')
                sys.exit(1)
            const_file=input('Enter a constellation file: ')
            const_files=[]
            while const_file!='':
                if path.isfile(const_file)==False:
                    print(f'The constellation file you entered {const_file} is invalid.')
                    sys.exit(1)
                const_files.append(const_file)
                const_file=input('Enter a constellation file: ')
            print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
            return star_file, const_files, 1

        elif sys.argv[2]=='-names':
            print('use arg1 as stars-location-file and when drawing named stars write their name to drawing window, loop prompting for valid constellation files until “” entered')
            star_file=sys.argv[1]
            if path.exists(star_file)==False:
                print(f'The file entered {star_file} does not exist.')
                sys.exit(1)
            const_file=input('Enter a constellation file: ')
            const_files=[]
            while const_file!='':
                if path.isfile(const_file)==False:
                    print(f'The constellation file you entered {const_file} is invalid.')
                    sys.exit(1)
                const_files.append(const_file)
                const_file=input('Enter a constellation file: ')
            print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
            return star_file, const_files, 2

        else:
            print('Invalid argument. Neither input was -names')
            sys.exit(1)
    elif len(sys.argv)==4:
        print('Too many arguments have been listed, try listing between 0 and 2 arguments.')
        sys.exit(1)

def read_star_info(star_file):
    try:
        sf=open(star_file, 'r')
        lines=sf.readlines()
        for line in lines:
            splits=line.split(',')
            # print(splits)
            # The lines are getting split correctly but I'm not sure how to proceed when there are multiple names for a star  or when they're no names for a star given. Note that when the names do exist an are split, they'll end up with the next line command \n at the end of it e.g. If a star was called ZETA it will appear in the split list as  ZETA\n. If there are multiple names it will only appear on the last one.
            # When there are two names create  two different star info tuples or lists and then assign them the names.
            if len(splits)>=6:
                try:
                    float(splits[0])
                    float(splits[1])
                    float(splits[4])
                    star_info=[splits[0], splits[1], splits[4]]
                except ValueError:
                    print(f'The information in the star file {star_file} is of the wrong type')
            else:
                print(f'The star file {star_file} doesn’t have the required amount of entries separated by commas')
    except IOError:
        print(f'There was an error in opening the star file {star_file}')
        sys.exit(1)

# Draws only the x-axis. 0,yo is the point halfway up the y-axis and most negative value on x-axis - the graph coordinates are -1,0. The ticks list contains the increments that the axis will go up in.
def drawXAxis(pointer):
    yo=WIDTH/2
    pointer.penup()
    pointer.goto(0,yo)
    pointer.pendown()
    ticks=[-1, - 0.75, - 0.5, - 0.25, 0, 0.25, 0.5, 0.75, 1]
    for i in range(0, len(ticks),1):
        x_value1,y_value1=screenCoor(ticks[i],0)
        pointer.goto(x_value1, y_value1)
        pointer.penup()
        pointer.goto(x_value1, y_value1+3)
        pointer.pendown()
        pointer.goto(x_value1, y_value1-3)
        pointer.goto(x_value1,y_value1)
        pointer.penup()
        pointer.goto(x_value1-5, y_value1-13)
        pointer.pendown()
        if ticks[i]!=0:
            pointer.write(ticks[i])
        pointer.penup()
        pointer.goto(x_value1,y_value1)
        pointer.pendown()

# Draws only the y-axis. xo,0 is the point halfway down the x-axis and most negative value on y-axis - the graph coordinates are 0,-1. The ticks list contains the increments that the axis will go up in.    
def drawYAxis(pointer):
    xo=WIDTH/2
    pointer.penup()
    pointer.goto(xo,0)
    pointer.pendown()
    ticks=[-1, - 0.75, - 0.5, - 0.25, 0, 0.25, 0.5, 0.75, 1]
    for i in range(0, len(ticks),1):
        x_value1,y_value1=screenCoor(0,ticks[i])
        pointer.goto(x_value1, y_value1)
        pointer.penup()
        pointer.goto(x_value1+3, y_value1)
        pointer.pendown()
        pointer.goto(x_value1-3, y_value1)
        pointer.goto(x_value1,y_value1)
        pointer.penup()
        pointer.goto(x_value1+8, y_value1-7)
        pointer.pendown()
        if ticks[i]!=0:
            pointer.write(ticks[i])
        pointer.penup()
        pointer.goto(x_value1,y_value1)
        pointer.pendown()

# Runs the functions that draw the x and y axis
def axis_drawing(pointer):
    drawXAxis(pointer)
    drawYAxis(pointer)

def star_drawing():
    pass

def read_const_info():
    pass

def const_drawing():
    pass

# The function that changes the colour of the constellation lines. It goes from red to green to yellow and cycles through those three colours
def colour_cycler(counter):
    if counter==0 or counter%3==0:
      return 'red'
    elif counter==1 or counter%3==1:
      return 'green'
    elif counter==2 or counter%3==2:
      return 'yellow'

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
    star_file, const_files, code=command_line()
    read_star_info(star_file)
    #Handle arguments
    #Read star information from file (function)
    # pointer = setup()
    #Draw Axes (function)
    # pointer.color(AXISCOLOR)
    # axis_drawing(pointer)
    #Draw Stars (function)
    #Loop getting filenames
        #Read constellation file (function)
        #Draw Constellation (function)
        #Draw bounding box (Bonus) (function)
    # expr = input("Enter an arithmetic expression: ")
    # while expr != "":
        # expr = input("Enter an arithmetic expression: ")

main()