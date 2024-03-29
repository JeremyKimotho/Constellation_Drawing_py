# Jeremy Kimotho-30096043, CPSC  231 02-T06
# A program written in python that draws stars and constellations between the stars by reading files with the appropriate information.
# 12/11/2019

import sys
import os
import turtle
from os import path

WIDTH = 600
HEIGHT = 600
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
NONAME_STARCOLOR = "grey"
BONUS_BOXCOLOR = "orange"

# The function takes in graph points an input and returns the equivalent coordinates on the turtle window. xo,yo are the coordinate points of the graph location 0,0. The ratio is the number of pixels between 0 and 1.
def screenCoor(x, y):
    xo=WIDTH/2
    yo=HEIGHT/2
    ratio=300
    x_coordinate=float(xo+(ratio*x))
    y_coordinate=float(yo+(ratio*y))
    return x_coordinate, y_coordinate

# The function that changes the colour of the constellation lines. It goes from red to green to yellow and cycles through those three colours
def colour_cycler(counter):
    if counter==0 or counter%3==0:
      return 'red'
    elif counter==1 or counter%3==1:
      return 'green'
    elif counter==2 or counter%3==2:
      return 'yellow'

#  Collects data from the command line input using the number of arguments. Checks inputted star_file to ensure it exists and then prompts for constellation files until user enters blank input. Constellation files are also checked for validity. Function then returns three variables in all situations where an error doesn't occur. These are first the star_file the user entered, then a list of the constellation files the user entered, and finally a code of 0, 1, or 2. The code determines if the star and constellations will just be drawn (0), if the star and constellation files will be drawn and the names written in the drawing window (1) or finally if the star and constellation files will be drawn and the names printed to the screen. All the situations that do not result in an error have one of the three coded outcomes.
def command_line():
    if len(sys.argv)==1:
        star_file=input('Enter a stars-location-file: ')
        if path.exists(star_file)==False:
            print(f'The file entered {star_file} does not exist.')
            sys.exit(1)
        const_file=input('Enter a constellation file: ')
        const_files=[]
        while const_file!='':
            if path.isfile(const_file)==False:
                print(f'The constellation file you entered {const_file} is invalid.')
            else:
                const_files.append(const_file)
            const_file=input('Enter a constellation file: ')
        print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
        return star_file, const_files, 0

    elif len(sys.argv)==2:
        if sys.argv[1]=='-names':
            star_file=input('Enter a stars-location-file: ')
            if path.exists(star_file)==False:
                print(f'The file entered {star_file} does not exist.')
                sys.exit(1)
            const_file=input('Enter a constellation file: ')
            const_files=[]
            while const_file!='':
                if path.isfile(const_file)==False:
                    print(f'The constellation file you entered {const_file} is invalid.')
                else:
                    const_files.append(const_file)
                const_file=input('Enter a constellation file: ')
            print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
            return star_file, const_files, 1

        else:
            star_file=sys.argv[1]
            if path.exists(star_file)==False:
                print(f'The file entered {star_file} does not exist.')
                sys.exit(1)
            const_file=input('Enter a constellation file: ')
            const_files=[]
            while const_file!='':
                if path.isfile(const_file)==False:
                    print(f'The constellation file you entered {const_file} is invalid.')
                else:
                    const_files.append(const_file)
                const_file=input('Enter a constellation file: ')
            print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
            return star_file, const_files, 0

    elif len(sys.argv)==3:
        if sys.argv[1]=='-names':
            star_file=sys.argv[2]
            if path.exists(star_file)==False:
                print(f'The file entered {star_file} does not exist.')
                sys.exit(1)
            const_file=input('Enter a constellation file: ')
            const_files=[]
            while const_file!='':
                if path.isfile(const_file)==False:
                    print(f'The constellation file you entered {const_file} is invalid.')
                else:
                    const_files.append(const_file)
                const_file=input('Enter a constellation file: ')
            print(f'You entered the star file {star_file} and {len(const_files)} valid constellation file(s).')
            return star_file, const_files, 1

        elif sys.argv[2]=='-names':
            star_file=sys.argv[1]
            if path.exists(star_file)==False:
                print(f'The file entered {star_file} does not exist.')
                sys.exit(1)
            const_file=input('Enter a constellation file: ')
            const_files=[]
            while const_file!='':
                if path.isfile(const_file)==False:
                    print(f'The constellation file you entered {const_file} is invalid.')
                else:
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

# Reads the star information collected from the command line arguments. Creates a class StarInformation that has name and star data as what it collects. A list stars is created which will be used to store the dictionaries created from the StarInformation class. The information is read through line-by-line and the last variable checked to see if a name(s) is provided. If there is a name or multiple, they will all be used to create a dictionary with the same data but different name. If no name is provided the star will remain nameless but the data still collected. The data for the star is saved as tuples, the data is the value and the names the keys in our dictionaries. The function returns the list stars that contains dictionaries.
def read_star_info(star_file):
    class StarInformation:
        def __init__(self, name, data):
            self.name = name
            self.data = data
    stars=[]
    try:
        sf=open(star_file, 'r')
        lines=sf.readlines()
        for line in lines:
            splits=line.split(',')
            if len(splits)>=6:
                try:
                    float(splits[0])
                    float(splits[1])
                    float(splits[4])
                    star_info=(float(splits[0]), float(splits[1]), float(splits[4]))
                    names=splits[6].split(';')
                    if names[0]=='\n':
                        names[0]=''
                    else:
                        names[-1]=names[-1][0:-1]
                    for star in names:
                        each_star=StarInformation(star, star_info)
                        stars.append(each_star)
                        if star!='':
                            print(f'{star} is at ({star_info[0]}, {star_info[1]}) with magnitude {star_info[2]}')
                except ValueError:
                    print(f'The information in the star file {star_file} is of the wrong data type')
                    sys.exit(1)
            else:
                print(f'The star file {star_file} doesn’t have the required amount of entries separated by commas')
                sys.exit(1)
        sf.close()
        return stars
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

# Takes as input the processed star data from the read_star_info file and draws the stars in that list. Also takes the code collected in the command line arguments function that determine if the names should be written in the drawing window or printed to the screen.
def star_drawing(pointer, code, stars):
    for star in stars:
        if star.name=='':
            circle_radius=(10 / (star.data[2] + 2)) / 2
            pointer.color(NONAME_STARCOLOR)
            pointer.penup()
            pointer.goto(screenCoor(star.data[0],star.data[1]))
            pointer.pendown()
            pointer.begin_fill()
            pointer.circle(circle_radius)
            pointer.end_fill()
            if code==1:
                pointer.write(star.name,font=("Arial", 5, "normal"))
            elif code==2:
                print(star.name)
        else: 
            circle_radius=(10 / (star.data[2] + 2)) / 2
            pointer.color(STARCOLOR)
            pointer.penup()
            pointer.goto(screenCoor(star.data[0],star.data[1]))
            pointer.pendown()
            pointer.begin_fill()
            pointer.circle(circle_radius)
            pointer.end_fill()
            if code==1:
                pointer.write(star.name,font=("Arial", 5, "normal"))
            elif code==2:
                print(star.name)

# Takes as input the constellation files that were added during the command line argument collection and extends that to the list of const files it gets from the  user at the start of the function. Then loops through all the const files and makes tuples line-by-line and these tuples are the star edge or constellation edges. These tuples are grouped into a list single constellation that consists of one constellation. This list is then appended to the list processed const data. Lastly prints to the console the title of every constellation and the stars it connects. Returns list of lists (of tuples).
def read_const_info(const_files):
    class ConstInformation:
        def __init__(self, name, data):
            self.name = name
            self.data = data
    const_files_2=[]
    const_file=input('Enter a constellation file: ')
    while const_file!='':
        if path.isfile(const_file)==False:
            print(f'The constellation file you entered {const_file} is invalid.')
        else:
            const_files_2.append(const_file)
        const_file=input('Enter a constellation file: ')
    all_files=const_files+const_files_2
    all_files=list(dict.fromkeys(all_files))
    processed_const_data=[]
    for const_file in all_files:
        try:
            cf=open(const_file, 'r')
            lines=cf.readlines()
            single_constellation=[]
            const_names=[]
            for i in range(1, len(lines)):
                star_edge=lines[i].split(',')
                const_info=(star_edge[0], star_edge[1][0:-1])
                single_constellation.append(ConstInformation(lines[0][0:-1], const_info))
                const_names.append(star_edge[0])
                const_names.append(star_edge[1][0:-1])
                const_names=list(dict.fromkeys(const_names))
            processed_const_data.append(single_constellation)
            print(f'{lines[0][0:-1]} constellation contains {const_names}')
            cf.close()
        except IOError:
            print(f'There was an error in opening the constellation file {const_file}')
            sys.exit(1)
    return processed_const_data
    
# Takes as input the pointer which is the turtle from the setup functions, the const data from the const info function and the star data from the star info function. The const info is a list in tuples of two which are the pairs of stars which the constellation goes from, these are the pairs referred to in the first loop. The star data comes in a list of dictionaries. With the names as keys and the star data as the values. The names are what we are searching for in the second loop. Once the correct star is found by name the data is recorded  and used as the start and end point of one line of the constellation. The bonus has been added to this function, works by looping through all stars in given constellation and checks if it's smaller than the current smallest, if it is it gets replaced. 
def const_drawing(pointer,processed_const_data, processed_star_data):
    counter=0
    for single_c in processed_const_data:
        edges=[]
        name=''
        smallest_x=2
        smallest_y=2
        biggest_x=-2
        biggest_y=-2
        for pair in single_c:
            name=pair.name
            for star in processed_star_data:
                if pair.data[0]==star.name:
                    line1=(star.data[0], star.data[1])
                    if star.data[0]>biggest_x:
                        biggest_x=star.data[0]
                    elif star.data[0]<smallest_x:
                        smallest_x=star.data[0]
                    if star.data[1]>biggest_y:
                        biggest_y=star.data[1]
                    elif star.data[1]<smallest_y:
                        smallest_y=star.data[1]
                elif pair.data[1]==star.name:
                    line2=(star.data[0], star.data[1])
                    if star.data[0]>biggest_x:
                        biggest_x=star.data[0]
                    elif star.data[0]<smallest_x:
                        smallest_x=star.data[0]
                    if star.data[1]>biggest_y:
                        biggest_y=star.data[1]
                    elif star.data[1]<smallest_y:
                        smallest_y=star.data[1]
            pointer.penup()
            pointer.goto(screenCoor(line1[0], line1[1]))
            pointer.pendown()
            pointer.color(colour_cycler(counter))
            pointer.goto(screenCoor(line2[0], line2[1]))
        if name=='CYG':
            smallest_y=smallest_y-0.08
        edges.append((smallest_x, smallest_y, biggest_x, biggest_y))
        pointer.penup()
        pointer.goto(screenCoor(edges[0][0], edges[0][1]))
        pointer.pendown()
        pointer.color(BONUS_BOXCOLOR)
        pointer.goto(screenCoor(edges[0][2], edges[0][1]))
        pointer.goto(screenCoor(edges[0][2], edges[0][3]))
        pointer.goto(screenCoor(edges[0][0], edges[0][3]))
        pointer.goto(screenCoor(edges[0][0], edges[0][1]))
        pointer.penup()
        pointer.goto(screenCoor((edges[0][0]+edges[0][2])/2, edges[0][3]))
        pointer.write(name,font=("Arial", 8, "normal"))
        try: 
            ef=open(name+'_.dat', 'w')
            ef.write(str(edges[0][0])+'\n')
            ef.write(str(edges[0][2])+'\n')
            ef.write(str(edges[0][1])+'\n')
            ef.write(str(edges[0][3]))
            ef.close()
        except IOError:
            print('There was an error creating a file to store the smallest and largest values of x and y.')
            sys.exit(1)
        counter+=1   

#  Setup of turtle screen before we draw
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

# Calls all other functions and is what we run. 
def main():
    # Command Line argument function runs which asks for stars and constellations
    star_file, const_files, code=command_line()
    # Star info is collected from files given in the command line function
    processed_star_data=read_star_info(star_file)
    # Drawing window is setup
    pointer = setup()
    # Draw Axes (function)
    pointer.color(AXISCOLOR)
    axis_drawing(pointer)
    # Draw Stars (function)
    star_drawing(pointer, code, processed_star_data)
    # Constellation info is then collected again and added to any that was collected in command line function
    processed_const_data=read_const_info(const_files)
    # Draw Constellation
    const_drawing(pointer, processed_const_data, processed_star_data)
    
# Run the program 
main()
# Keeps turtle window open till clicked
turtle.exitonclick()