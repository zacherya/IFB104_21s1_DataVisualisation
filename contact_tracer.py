# -----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item for QUT's teaching unit
#  IFB104, "Building IT Systems", Semester 1, 2021.  By submitting
#  this code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
student_number = 10772693  # put your student number here as an integer
student_name = 'Zachery Adams'  # put your name here as a character string
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
# --------------------------------------------------------------------#


# -----Task Description-----------------------------------------------#
#
#  CONTACT TRACER
#
#  This assessment item tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "visualise".  You are required to
#  complete this function so that when the program runs it fills
#  a grid with various symbols, using data stored in a list to
#  determine which symbols to draw and where.  See the various
#  "client requirements" in Blackboard for full details.
#
#  Note that this assessable assignment is in multiple parts,
#  simulating incremental release of instructions by the client.
#  This single template file will be used for all parts and you will
#  submit your final solution as a single Python 3 file only, whether
#  or not you complete all requirements for the assignment.
#
# --------------------------------------------------------------------#


# -----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should NOT change
# any of the code in this section.
#

# Import standard Python modules needed to complete this assignment.
# You should not need to use any other modules for your solution.
# In particular, your solution must NOT rely on any non-standard
# Python modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.
from turtle import *
from math import *
from random import *
from sys import exit as abort
from os.path import isfile
import time

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values unless
# instructed.
cell_size = 100  # pixels (default is 100)
grid_width = 9  # squares (default is 9)
grid_height = 7  # squares (default is 7)
x_margin = cell_size * 2.75  # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2  # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', cell_size // 5, 'normal')  # font for the coords
big_font = ('Arial', cell_size // 4, 'normal')  # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'


#
# --------------------------------------------------------------------#


# -----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  Do NOT change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour='light grey',
                          line_colour='slate grey',
                          draw_grid=True,
                          label_spaces=True):  # NO! DON'T TOUCH THIS!

    # Set up the drawing canvas with enough space for the grid and
    # spaces on either side
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0)  # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)

        # Draw the vertical grid lines
        setheading(90)  # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = cell_size // 3  # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('a')), align='center', font=small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = cell_size // 10, cell_size // 10  # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align='right', font=small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(cell_size // 6)

    # Optionally mark the blank spaces ... NO! YOU CAN'T CHANGE ANY OF THIS CODE!
    if label_spaces:
        # Left side
        goto(-((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align='right', font=big_font)
        # Right side
        goto(((grid_width + 1.5) * cell_size) // 2, -(cell_size // 3))
        write('This space\nintentionally\nleft blank', align='left', font=big_font)

        # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends.  Call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor=True):
    tracer(True)  # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()


#
# --------------------------------------------------------------------#


# -----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "visualise" function.  ALL of your solution code
#  must appear in this area.  Do NOT put any of your code in other
#  parts of the program and do NOT change any of the provided code
#  except as allowed in the main program below.
#

# Complete the visualisation using the provided data set
# we define in arrays as we use the values multiple times, good practice to make one reference point
element_desc = "Seasons\nThrough A\nWindow"  # Write for label in sidebar, title at top strips the new lines
element_titles = ["Summer", "Autumn", "Winter", "Spring"]  # store names of elements (Order is crucial)
element_bullets = ["A. ", "B. ", "C. ", "D. "]  # define bullet points for labels

x_axis_letters = 'abcdefghijklmnopqrstuvwxyz'

sidebar_obj = []  # objects stored here are reference points for drawings in the side bar (off grid)
grid_obj = {}  # objects stored here will be reference points for drawings made on the grid, it will store locations
final_obj = None  # the object stored here will be the reference point for the final variant drawn on the left

speed_of_instructions = 0.25


class GridManager:
    def __init__(self, grid_bottom_x, grid_bottom_y):
        # Bottom corner position of grid
        self.gbx = grid_bottom_x
        # Bottom corner position of grid
        self.gby = grid_bottom_y

        # store values same as instructions. we treat these values as instructions in GridManager functions
        self.column = 'a'
        self.row = 1

        # store in the instance to redraw when a direction instruction is passed
        self.currentCanvasType = 0

        # setup the GridManager so the GridManager functions can run as expected - Dependant
        self.reset()

    def __convertGridPos(self, column, row):  # converts grid position to actual postion on window
        # gets the grid bottom corner and adds the cell size which is multiplied by the column index number
        # column letter is converted to a number
        gridto_xpos = self.gbx + (self.__convertColumn(column)[0] * cell_size) - cell_size
        # gets the grid bottom corner and adds the cell size which is multiplied by the row index number
        gridto_ypos = self.gby + (row * cell_size) - cell_size
        # return x and y in array
        return [gridto_xpos, gridto_ypos]

    def __convertColumn(self, column_letter):
        # convert any letters pass to lower case
        letter = column_letter.lower()
        # define output array
        # we use an array because the data_generator file may change and we don't know if instructions may pass
        # more then one letter so we cycle through each character convert it to a number and return the whole array
        # when using convertColumn you would get the [0] object in the array returned for the first letter
        # EXPECTED INPUT: "a"
        # POTENTIAL INPUT IF GENERATOR CHANGES: "ab"
        # Access first character as number convertColumn("a")[0] -> 1
        output = []
        for character in letter:
            number = ord(character) - 96
            output.append(number)
        return output

    def plotCanvas(self, canvas_type):
        if self.currentCanvasType != canvas_type:
            # If the last known canvas is not updated, update it to the one we want to plot
            self.currentCanvasType = canvas_type
        if (self.column + str(self.row)) in grid_obj:
            # use canvas obj in array and redraw object
            # if the canvas already has the same season as the one needing to be drawn over then we won't re-draw
            # as this would be using unnessacary computing power
            switch_values = {"A": 0, "B": 1, "C": 2, "D": 3}
            if grid_obj[self.column + str(self.row)].season != switch_values[canvas_type]:
                grid_obj[self.column + str(self.row)].switchDrawing(canvas_type)
            else:
                grid_obj[self.column + str(self.row)].drawBorderBox()

        else:
            # create obj in ref point as canvas object doesn't exist at grid position specified
            # Do Draw
            convertedPosition = self.__convertGridPos(self.column, self.row)
            canvas = Canvas(canvas_type, convertedPosition[0], convertedPosition[1])
            # Create a new canvas object - this can be used repeatedly on the grid or on the
            # sidebar. Defining the element number that corresponds to the position inx
            # where the canvas will be drawn - this method allows us to touch the drawing
            canvas.draw(True)  # call the class to start the drawing of the object
            grid_obj.update({self.column + str(self.row): canvas})  # add newly created canvas object to grid references

    def reset(self):
        # reset the grid managers turtle and navigator
        penup()
        hideturtle()
        tracer(False)
        goto(self.gbx, self.gby)

    def moveTo(self, pos_x, pos_y):

        # example of expected value in position 'c',3
        # set position sticks in grid manager

        # we don't make the turtle move here because individual Canvas objects with their own turtle are generated
        # we will change the column values to what is passed from the instructions as we convert that later on.

        # despite the main thread turtle not moving we still want to ensure it stays the bottom left corner
        # self.reset() 

        self.column = pos_x
        self.row = pos_y

    def navigate(self, direction, steps):
        # if steps are zero then we would just be redrawing the same image. The process would involve deleting objects
        # from the computers memory and recreating it and this uses computer resources that are not needed
        if steps != 0:
            # for each index in range of steps
            for idx in range(steps):
                if direction == "North":
                    self.row = self.row + 1
                elif direction == "East":
                    self.column = x_axis_letters[(x_axis_letters.find(self.column) + 1) % 26]
                elif direction == "South":
                    self.row = self.row - 1
                elif direction == "West":
                    self.column = x_axis_letters[(x_axis_letters.find(self.column) - 1) % 26]
                self.plotCanvas(self.currentCanvasType)
                # sleep between instructions to mimic client briefing example
                time.sleep(speed_of_instructions)


class Canvas:
    def __init__(self, season_ref, x, y):
        # reference to element position in element_title array (defined outside of Canvas class)
        self.season = self.__validateSeason(season_ref)

        # scalable factor based on cell size, canvas drawing are built around 100x100 canvas
        self.scale_factor = 100 // cell_size

        # starting reference point for canvas object
        self.home_x = x
        self.home_y = y

        # Create a new turtle object for the canvas object. We will be able to reference the drawings and delete them at
        # a later stage if required
        self.tur = Turtle()
        self.__home()  # Home is defined as the bottom left corner of the canvas
        self.tur.hideturtle()  # make canvas object turtle invisible
        tracer(False)  # make canvas load as fast as possible

    def __validateSeason(self, season_ref):
        switch_values = {"A": 0, "B": 1, "C": 2, "D": 3}
        if type(season_ref) == int:
            return season_ref
        elif season_ref in switch_values:
            return switch_values[season_ref]
        else:
            return 0

    def __home(self):
        # customer defined method for making the class objects turtle go back home/starting point of canvas object
        # resets the head and ensures pen is up before moving
        self.tur.penup()
        self.tur.goto(self.home_x, self.home_y)
        self.tur.setheading(0)

    def __goto(self, scaled_x, scaled_y):
        # custom defined method for goign to a certain position on the mini canvas
        # using this method we can ensure non of our objects draw outside the canvas and allow us to draw confidently
        # new objects. Scale x and Scale y use numbers 0-1 and that is a scale of position from the cell_size
        # which determines the position of the object. This method allows for a scalable solution

        # home x and y are defined when the object is created, it allows us to form a beacon or reference point as to
        # where a common starting/reference point of the canvas is. From this we can add our scaled x and y onto this
        # to form an accurate position on the mini canvas
        x = self.home_x + (scaled_x * cell_size)
        y = self.home_y + (scaled_y * cell_size)

        # check scaled_x isn't outside assumed bounds of canvas
        if scaled_x < 0 or scaled_x > 1:
            x = 0

        # check scaled_x isn't outside assumed bounds of canvas
        if scaled_y < 0 or scaled_y > 1:
            y = 0

        # tell object turtle to move to that position on the screen
        self.tur.goto(x, y)

    def destroy(self):
        self.tur.clear()
        del self.tur

    def switchDrawing(self, season):
        switch_to = self.__validateSeason(season)
        self.season = switch_to
        self.tur.clear()
        self.tur = Turtle()
        self.__home()
        self.draw(True)

    def __square(self, size):
        # draw simple square with width and width
        self.tur.pendown()
        self.tur.setheading(0)
        self.tur.forward(cell_size)
        self.tur.setheading(90)
        self.tur.forward(cell_size)
        self.tur.setheading(180)
        self.tur.forward(cell_size)
        self.tur.setheading(-90)
        self.tur.forward(cell_size)
        self.tur.setheading(0)
        self.tur.penup()

        # Reset for next function
        self.__home()

    def __rectangle(self, lth, wth):
        # draw simple rectangle with length and width
        lth = lth * self.scale_factor
        wth = wth * self.scale_factor
        self.tur.pendown()
        self.tur.setheading(0)
        self.tur.forward(lth)
        self.tur.setheading(90)
        self.tur.forward(wth)
        self.tur.setheading(180)
        self.tur.forward(lth)
        self.tur.setheading(-90)
        self.tur.forward(wth)
        self.tur.setheading(0)

        # Reset for next function
        self.tur.penup()
        self.__home()

    def __sky(self, sky_color):
        previous_color = self.tur.pencolor()
        self.tur.color(sky_color)

        # simple square which acts as the background but doubles as the colour of the sky
        self.tur.begin_fill()
        self.__square(cell_size)
        self.tur.end_fill()

        # Reset for next function
        self.tur.color(previous_color)
        self.__home()

    def __sun_rays(self, side, rising):
        # Pre define reusable variables or store initial values
        previous_color = self.tur.pencolor()
        rotate_offset = 0
        pos_offset = 0
        rays = round(self.scale_factor * 3)  # sun rays
        ray_offset = 90 / rays  # space between sun rays

        if rising:
            rotate_offset = 90
            pos_offset = 50

        if side == "r":
            # set colour of rays to the same as the sun
            self.tur.color('darkgoldenrod2')
            # loop through the amount of specified rays and generate the ray from the assumed suns position
            for i in range(rays):
                self.tur.goto(self.home_x + (100 * self.scale_factor),
                              self.home_y + ((100 - pos_offset) * self.scale_factor))
                self.tur.penup()
                self.tur.setheading((180 - rotate_offset) + (ray_offset * i))
                self.tur.forward(20 * self.scale_factor)
                self.tur.pendown()
                self.tur.circle(10 * self.scale_factor, 90)
                self.tur.circle(10 * self.scale_factor, -90)

            self.tur.penup()
            self.tur.color(previous_color)

        elif side == "l":
            # set colour of rays to the same as the sun
            self.tur.color('darkgoldenrod2')
            # loop through the amount of specified rays and generate the ray from the assumed suns position
            for i in range(rays):
                self.tur.goto(self.home_x + (0 * self.scale_factor),
                              self.home_y + ((100 - pos_offset) * self.scale_factor))
                self.tur.penup()
                self.tur.setheading((270 + rotate_offset) + (ray_offset * i))
                self.tur.forward(20 * self.scale_factor)
                self.tur.pendown()
                self.tur.circle(10 * self.scale_factor, 90)
                self.tur.circle(10 * self.scale_factor, -90)

            self.tur.penup()
            self.tur.color(previous_color)

        # Reset for next function
        self.__home()

    def __sun(self, side, rising):
        previous_color = self.tur.pencolor()
        pos_offset = 0
        rotate_offset = 0

        if rising:
            pos_offset = 25
            rotate_offset = 90

        # draw sun on the right side of the canvas
        if side == "r":
            self.tur.goto(self.home_x + ((75 + pos_offset) * self.scale_factor),
                          self.home_y + ((100 - pos_offset) * self.scale_factor))

            self.tur.color('darkgoldenrod2')
            self.tur.pendown()
            self.tur.begin_fill()

            self.tur.setheading(270 - rotate_offset)
            self.tur.circle((25 * self.scale_factor), 90)
            self.tur.setheading(90 - rotate_offset)
            self.tur.forward(25 * self.scale_factor)
            self.tur.setheading(180 - rotate_offset)
            self.tur.forward(25 * self.scale_factor)

            self.tur.end_fill()
            self.tur.penup()
            self.tur.color(previous_color)

        # draw sun on the left side of the canvas
        elif side == "l":
            self.tur.goto(self.home_x + ((0 + pos_offset) * self.scale_factor),
                          self.home_y + ((75 - pos_offset) * self.scale_factor))

            self.tur.color('darkgoldenrod2')
            self.tur.pendown()
            self.tur.begin_fill()

            self.tur.setheading(0 + rotate_offset)
            self.tur.circle((25 * self.scale_factor), 90)
            self.tur.setheading(180 + rotate_offset)
            self.tur.forward(25 * self.scale_factor)
            self.tur.setheading(270 + rotate_offset)
            self.tur.forward(25 * self.scale_factor)

            self.tur.end_fill()
            self.tur.penup()
            self.tur.color(previous_color)

        # Reset for next function
        self.__home()

    def __lawn(self, lawn_color):
        previous_color = self.tur.pencolor()
        self.tur.color(lawn_color)

        # draw a simple rectangle for the floor (grass)
        self.tur.begin_fill()
        self.__rectangle(100, 50)
        self.tur.end_fill()

        # Reset for next function
        self.tur.color(previous_color)
        self.__home()

    def __snowman(self, scaled_x, scaled_y):
        previous_color = self.tur.pencolor()

        self.__goto(scaled_x, scaled_y)

        # Create loop for snowman body balls
        balls = 3
        for i in range(balls):
            self.tur.setheading(0)
            self.tur.pendown()
            self.tur.color("white")
            self.tur.begin_fill()
            self.tur.circle(((i * 2) - 10) * self.scale_factor)
            self.tur.end_fill()
            self.tur.color("black")
            self.tur.circle(((i * 2) - 10) * self.scale_factor)
            self.tur.penup()

            # Don't make the needle progress on the last ball so we can make eyes
            if i != max(range(balls)):
                self.tur.setheading(270)
                self.tur.forward(((i * 2) - 8.5) * self.scale_factor)

        # Snow man eyes from top ball
        self.tur.setheading(270)
        self.tur.forward((10 - ((balls - 1) * 2) * self.scale_factor))
        self.tur.setheading(180)
        self.tur.forward((8 - ((balls - 1) * 2) * self.scale_factor) // 2)
        self.tur.dot(2 * self.scale_factor, "black")
        self.tur.setheading(0)
        self.tur.forward((8 - ((balls - 1) * 2) * self.scale_factor))
        self.tur.dot(2 * self.scale_factor, "black")

        # Reset for next function
        self.tur.color(previous_color)
        self.__home()

    def __snowflake(self, branch, scaled_x=0, scaled_y=0):
        previous_color = self.tur.pencolor()
        if branch:
            for i in range(3):
                for j in range(3):
                    self.tur.forward(2 * self.scale_factor)
                    self.tur.backward(2 * self.scale_factor)
                    self.tur.right(45)
                self.tur.left(90)
                self.tur.backward(2 * self.scale_factor)
                self.tur.left(45)
            self.tur.right(90)
            self.tur.forward(8 * self.scale_factor)
        else:
            self.__goto(scaled_x, scaled_y)
            self.tur.color('white')
            self.tur.left(45)
            self.tur.pendown()
            for i in range(8):
                self.__snowflake(True)
                self.tur.left(45)
            # Reset for next function
            self.tur.color(previous_color)
            self.__home()

    def __flower(self, flower_type, scaled_x, scaled_y):
        previous_color = self.tur.pencolor()
        previous_pensize = self.tur.pensize()
        self.__goto(scaled_x, scaled_y)

        if flower_type == "normal":
            # Draw Flower Stalk
            self.tur.pencolor('green')
            self.tur.pensize(3 * self.scale_factor)
            self.tur.setheading(270)
            self.tur.pendown()
            self.tur.forward(15 * self.scale_factor)
            self.tur.penup()
            self.tur.setheading(90)
            self.tur.forward(15 * self.scale_factor)

            # Prepare for drawing petals
            self.tur.pencolor('red')
            self.tur.pensize(1 * self.scale_factor)
            self.tur.pendown()
            self.tur.begin_fill()
            self.tur.fillcolor('pink')
            self.tur.setheading(0)

            # Draw Petals
            for petal in range(4):
                self.tur.circle(6 * self.scale_factor, 90)
                self.tur.setheading(180 - (petal * 90))
                self.tur.circle(6 * self.scale_factor, 90)
            self.tur.end_fill()
            self.tur.penup()

            # Draw Flower Pistil
            self.tur.dot(4 * self.scale_factor, 'yellow')

            # Reset for next function
            self.tur.color(previous_color)
            self.tur.pensize(previous_pensize)
            self.__home()

    def __tallgrass(self, scaled_x=0, scaled_y=0):
        previous_color = self.tur.pencolor()
        previous_pensize = self.tur.pensize()

        self.tur.setheading(90)
        self.__goto(scaled_x, scaled_y)
        self.tur.color("darkgreen")
        self.tur.pensize(2)

        # Draw left stems
        for stem in range(3):
            for iteration in range(10):  # create illusion of a curved line with forward and angle
                self.tur.pendown()
                self.tur.forward(1.5 * self.scale_factor)
                self.tur.left(3 * ((stem * 2) + 1))
                self.tur.penup()
            self.tur.setheading(90)
            self.__goto(scaled_x, scaled_y)

        # Draw right stems
        for stem in range(3):  # three stems
            for iteration in range(10):  # create illusion of a curved line with forward and angle
                self.tur.pendown()
                self.tur.forward(1.5 * self.scale_factor)
                self.tur.right(3 * ((stem * 2) + 1))
                self.tur.penup()
            self.tur.setheading(90)
            self.__goto(scaled_x, scaled_y)

        # Reset for next function
        self.tur.color(previous_color)
        self.tur.pensize(previous_pensize)
        self.__home()

    def __clouds(self, side):
        previous_color = self.tur.pencolor()

        # draw clouds on the right side of canvas
        if side == "r":
            self.__goto(0.8, 1)
            self.tur.pendown()
            self.tur.color("azure2")
            self.tur.begin_fill()
            self.tur.setheading(180)
            self.tur.circle(5 * self.scale_factor, 210)
            self.tur.right(180)
            self.tur.circle(5 * self.scale_factor, 210)
            self.tur.right(180)
            self.tur.circle(5 * self.scale_factor, 210)
            self.tur.right(180)
            self.__goto(1, 1)
            self.__goto(0.74, 1)
            self.tur.end_fill()
            self.tur.penup()

        # draw clouds on the left side of canvas
        if side == "l":
            self.__goto(0.25, 1)
            self.tur.pendown()
            self.tur.color("azure2")
            self.tur.begin_fill()
            self.tur.setheading(180)
            self.tur.circle(5 * self.scale_factor, 210)
            self.tur.right(180)
            self.tur.circle(5 * self.scale_factor, 210)
            self.tur.right(180)
            self.tur.circle(5 * self.scale_factor, 210)
            self.tur.right(180)
            self.__goto(0, 1)
            self.__goto(0.25, 1)
            self.tur.end_fill()
            self.tur.penup()

        # Reset for next function
        self.tur.color(previous_color)
        self.__home()

    def __bird(self, scaled_x, scaled_y):
        previous_color = self.tur.pencolor()

        self.tur.setheading(0)
        self.tur.speed(0)
        self.tur.color("black")
        self.tur.penup()

        self.__goto(scaled_x, scaled_y)
        self.tur.pendown()
        self.tur.left(45)
        self.tur.forward(5 * self.scale_factor)
        self.tur.right(90)
        self.tur.forward((5 * self.scale_factor) / 2.0)
        self.tur.penup()

        self.tur.setheading(0)

        self.__goto(scaled_x, scaled_y)
        self.tur.pendown()
        self.tur.left(135)
        self.tur.forward(5 * self.scale_factor)
        self.tur.left(90)
        self.tur.forward((5 * self.scale_factor) / 2.0)
        self.tur.penup()

        # Reset for next function
        self.tur.color(previous_color)
        self.__home()

    def __window(self, closed_percent):
        previous_color = self.tur.pencolor()

        # Setup for window frame
        self.__goto(0, 0)
        self.tur.color("burlywood3")

        # Draw Window Frame
        self.tur.pendown()
        self.tur.begin_fill()
        self.__goto(0.1, 0)
        self.__goto(0.1, 0.9)
        self.__goto(0.9, 0.9)
        self.__goto(0.9, 0)
        self.__goto(1, 0)
        self.__goto(1, 1)
        self.__goto(0, 1)
        self.__goto(0, 0)
        self.tur.end_fill()
        self.tur.penup()

        # Draw Window Sill
        self.tur.color("burlywood4")
        self.__goto(0.1, 0)
        self.tur.pendown()
        self.tur.begin_fill()
        self.__goto(0.1, 0.1)
        self.__goto(0, 0.1)
        self.__goto(0.1, 0.2)
        self.__goto(0.9, 0.2)
        self.__goto(1, 0.1)
        self.__goto(0.9, 0.1)
        self.__goto(0.9, 0)
        self.__goto(0.1, 0)
        self.tur.end_fill()
        self.tur.penup()
        self.tur.color("coral4")
        self.__goto(0, 0.1)
        self.tur.pendown()
        self.tur.forward(cell_size)
        self.tur.penup()

        # Draw Window (Handle)
        self.tur.color("coral4")
        y_pos = (closed_percent / 100) * 0.85
        self.__goto(0, y_pos)
        self.tur.setheading(0)
        self.tur.begin_fill()
        self.__rectangle(cell_size, cell_size * 0.05)
        self.tur.end_fill()
        self.__goto(0, y_pos)
        self.tur.begin_fill()
        self.__rectangle(cell_size * 0.09, cell_size - (cell_size * y_pos))
        self.tur.end_fill()
        self.__goto(0.9, y_pos)
        self.tur.begin_fill()
        self.__rectangle(cell_size * 0.09, cell_size - (cell_size * y_pos))
        self.tur.end_fill()

        # Reset for next function
        self.tur.color(previous_color)
        self.__home()

    def __tree(self, thickness, branch_length, setup, scaled_x=0, scaled_y=0):
        if setup:
            self.tur.left(90)
            self.__goto(scaled_x, scaled_y)

        previous_color = self.tur.pencolor()
        self.tur.pendown()
        # shadow effect
        t = cos(radians(self.tur.heading() + 45)) / 8 + 0.25
        self.tur.pencolor(t, t, t)
        self.tur.pensize(thickness / 1.2)
        self.tur.forward(branch_length)  # draw branches

        if thickness > 0:
            # use random to create unique trees across seasons and each run of the program, canvas will always change
            b = random() * 15 + 10  # right branch deflection angle
            c = random() * 15 + 10  # left branch deflection angle
            d = branch_length * (random() * 0.25 + 0.7)  # The length of the next branch
            # Right turn a certain angle, draw the right branch
            self.tur.right(b)
            self.__tree(thickness - 1, d, False)
            # left turn a certain angle, draw the left branch
            self.tur.left(b + c)
            self.__tree(thickness - 1, d, False)
            self.tur.right(c)
        else:
            self.tur.right(90)
            # Use mathematical formula based on heading of turtle to determine offset of leaf colour from base colour
            thickness = cos(radians(self.tur.heading() - 45)) / 4 + 0.5
            leaf_radii = 3
            if element_titles[self.season] == "Summer":
                # Set appropriate colour for Season leaves
                # R G B - Leave green whole value and modify Red and Blue to offset green
                self.tur.pencolor(thickness * 0.4, thickness, thickness * 0.4)
                self.tur.fillcolor(thickness * 0.4, thickness, thickness * 0.4)
            elif element_titles[self.season] == "Autumn":
                # Add autumn fallen leaves
                if random() > 0.6:  # decrease to increase fallen leaf count
                    self.tur.penup()
                    # distribution/scatter of leaves
                    t = self.tur.heading()
                    an = -100 + random() * -40
                    self.tur.setheading(an)
                    dis = int(100 * random() * 0.5 + 40 * random() * 0.3 + 20 * random() * 0.2)
                    self.tur.forward(dis)
                    self.tur.setheading(t)
                    # colour leaves
                    self.tur.pendown()
                    self.tur.right(90)
                    thickness = cos(radians(self.tur.heading() - 45)) / 4 + 0.5
                    self.tur.pencolor(thickness, thickness * 0.5, thickness * 0.5)
                    self.tur.fillcolor(thickness, thickness * 0.5, thickness * 0.5)
                    self.tur.begin_fill()
                    self.tur.circle(2)
                    self.tur.left(90)
                    self.tur.end_fill()
                    self.tur.penup()
                    #
                    t = self.tur.heading()
                    self.tur.setheading(an)
                    self.tur.backward(dis)
                    self.tur.setheading(t)
                # Set appropriate colour for Season leaves
                # R G B - Leave red whole value and largely offset Green and Blue to create dying leaves appearance
                self.tur.pencolor(thickness, thickness * 0.9, thickness * 0.85)
                self.tur.fillcolor(thickness, thickness * 0.9, thickness * 0.85)
            elif element_titles[self.season] == "Winter":
                #  No Leaves in winter
                leaf_radii = 0
                pass
            elif element_titles[self.season] == "Spring":
                # Set appropriate colour for Season leaves
                # R G B - Leave red whole value and modify G & B evenly to create flower effect (Light red = pink)
                self.tur.pencolor(thickness, thickness * 0.7, thickness * 0.7)
                self.tur.fillcolor(thickness, thickness * 0.7, thickness * 0.7)

            self.tur.begin_fill()
            self.tur.circle(leaf_radii)
            self.tur.left(90)
            self.tur.end_fill()

        self.tur.penup()
        self.tur.backward(branch_length)  #
        self.tur.color(previous_color)
        if setup:
            self.tur.home()

    def drawBorderBox(self):
        # Border box will be called by the grid manager typically unless changed. It is also called from an
        # internal canvas function that is only run if GridManager calls it.
        # We enable tracing at this stage to match the client's example provided. Canvas draws instantly, border
        # is drawn at a fast pace but visibly drawn
        tracer(True)
        self.tur.speed('fastest')
        self.tur.showturtle()
        self.__square(cell_size)
        self.tur.hideturtle()
        tracer(False)

    def draw(self, border_box=False):
        # Determine the what the canvas object will be drawing, matching element no with the value in the position
        # of the element no that lays in element_titles - if index is out of range, canvas does not draw
        self.__home()
        if element_titles[self.season] == "Summer":
            # Draw Summer Sky
            self.__sky('deepskyblue')
            # Draw Sun already Risen on the right
            self.__sun('r', False)
            self.__sun_rays('r', False)
            # Draw Vibrant Lawn
            self.__lawn('chartreuse4')
            # Draw Tree
            self.__tree(6, 10, True, 0.6, 0.35)
            # Draw Tall Grass
            self.__tallgrass(0.12, 0.32)
            self.__tallgrass(0.32, 0.17)
            self.__tallgrass(0.9, 0.42)
            self.__tallgrass(0.74, 0.23)
            # Draw Birds
            self.__bird(0.21, 0.82)
            self.__bird(0.26, 0.68)
            self.__bird(0.43, 0.76)
            # Draw Window
            self.__window(100)

        elif element_titles[self.season] == "Autumn":
            # Draw Sky
            self.__sky('bisque2')
            # Draw Sun setting on the right
            self.__sun('r', True)
            # Draw Dying Lawn
            self.__lawn('darkseagreen')
            # Draw Tree
            self.__tree(6, 10, True, 0.6, 0.35)
            # Draw Window
            self.__window(65)

        elif element_titles[self.season] == "Winter":
            # Draw Sky
            self.__sky('cadetblue3')
            # Draw Snow Covered Lawn
            self.__lawn('azure1')
            # Draw Snow Flakes
            self.__snowflake(False, 0.25, 0.75)
            self.__snowflake(False, 0.85, 0.63)
            self.__snowflake(False, 0.45, 0.86)
            # Draw Clouds
            self.__clouds("r")
            # Draw Tree
            self.__tree(6, 12, True, 0.6, 0.35)
            # Draw Snowman
            self.__snowman(0.85, 0.45)
            # Draw Window
            self.__window(20)

        elif element_titles[self.season] == "Spring":
            # Draw Sky
            self.__sky('cyan3')
            # Draw Sun already Risen on the left
            self.__sun('l', False)
            # Draw Vibrant Lawn
            self.__lawn('chartreuse4')
            # Draw Tree
            self.__tree(6, 10, True, 0.6, 0.35)
            # Draw Birds
            self.__bird(0.23, 0.76)
            self.__bird(0.65, 0.82)
            self.__bird(0.87, 0.89)
            self.__bird(0.91, 0.74)
            # Draw Flowers
            self.__flower("normal", 0.3, 0.43)
            self.__flower("normal", 0.41, 0.23)
            self.__flower("normal", 0.21, 0.29)
            self.__flower("normal", 0.76, 0.22)
            self.__flower("normal", 0.83, 0.46)
            # Draw Window
            self.__window(80)

        if border_box:
            self.drawBorderBox()
        # Needed to tell the the program to not expect any more turtle commands from this turtle instance
        # refer to https://docs.python.org/3/library/turtle.html
        # the screen doesn't update until the turtle is finished, unless tracer is set to True
        self.tur.hideturtle()
        self.tur.penup()
        self.tur.getscreen().update()


def drawContainerSquare():
    # draw simple square - used for drawing around canvas object when created
    pendown()
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    setheading(-90)
    forward(cell_size)
    setheading(0)
    penup()


def drawSidebarTitle(top_pos, side_pos, defer):
    # goto position of title - defer by the amount of lines
    goto(side_pos, top_pos - ((cell_size * defer) // 2))
    write(element_desc, align='left', font=big_font)
    home()  # move turtle back home


def drawSidebarElement(element_no, top_pos, side_pos, defer_from_title):
    # Draw Image
    spacing = 1.5  # spacing between images
    image_top_spacing = spacing + (0.25 * defer_from_title)  # spacing from title or desc of drawings
    x = side_pos  # start from defined side position
    y = (top_pos - (cell_size * image_top_spacing)) - ((cell_size * spacing) * element_no)  # determine top position to
    # start from

    canvas = Canvas(element_no, x, y)  # Create a new canvas object - this can be used repeatedly on the grid or on the
    # sidebar. Defining the element number that corresponds to the position in
    # element_title and provide the x and y position of the bottom left corner
    # where the canvas will be drawn - this method allows us to touch the drawing
    canvas.draw()  # call the class to start the drawing of the object
    sidebar_obj.append(canvas)  # add newly created canvas object to sidebar array so we can call upon the drawing

    goto(x, y)  # goto the bottom left corner of the newly created canvas with the main turtle object
    drawContainerSquare()  # draw border around canvas object

    # Write Element Title Enplaning Image
    text_top_spacing = (spacing + 0.3) + (0.25 * defer_from_title)
    goto(side_pos, (top_pos - (cell_size * text_top_spacing)) - ((cell_size * spacing) * element_no))
    write(element_bullets[element_no] + element_titles[element_no], align='left', font=small_font)
    home()


def drawFinalVariant(element_no, top_pos, side_pos):
    # Draw Image
    spacing = 1.5  # spacing between images
    x = side_pos  # start from defined side position
    y = (top_pos - ((grid_height * cell_size) / 2) - (cell_size / 2))  # Margin from top

    canvas = Canvas(element_no, x, y)  # Create a new canvas object - this can be used repeatedly on the grid or on the
    # sidebar. Defining the element number that corresponds to the position in
    # element_title and provide the x and y position of the bottom left corner
    # where the canvas will be drawn - this method allows us to touch the drawing
    canvas.draw()  # call the class to start the drawing of the object

    global final_obj
    final_obj = canvas  # add newly created canvas object to sidebar array so we can call upon the drawing

    goto(x, y)  # goto the bottom left corner of the newly created canvas with the main turtle object
    drawContainerSquare()  # draw border around canvas object

    # Write Element Title Enplaning Image
    goto(x - 7.5, (cell_size * 0.1) - y)
    write("Final Variant:", align='left', font=small_font)
    home()


def isDirection(step_val):
    directions = ['North', 'South', 'East', 'West']
    if step_val in directions:
        return True
    else:
        return False


def visualise(data_set):
    # Define additional Re-usable Variables for functions
    grid_top_pos = (grid_height * cell_size) // 2  # get the position of the top of the grid
    left_side_of_grid = -((((grid_width + 3.5) * cell_size) / 2) + 1.5)
    right_side_of_grid = ((grid_width + 1.5) * cell_size) // 2  # define position of the right side of the grid
    title_defer = 1.5  # Add .5 from .5 for each additional title line space required so 3 lines = 1.5 & 2 lines = 1

    # Determine the left-bottom coords of the grid or 1a (Starting Position/Reference)
    left_edge = -(grid_width * cell_size) // 2
    bottom_edge = -(grid_height * cell_size) // 2

    # Write Title explaining elements
    drawSidebarTitle(grid_top_pos, right_side_of_grid, title_defer)

    # Draw each element - each element number represents a position in element_title array which holds a canvas type id
    drawSidebarElement(0, grid_top_pos, right_side_of_grid, title_defer)
    drawSidebarElement(1, grid_top_pos, right_side_of_grid, title_defer)
    drawSidebarElement(2, grid_top_pos, right_side_of_grid, title_defer)
    drawSidebarElement(3, grid_top_pos, right_side_of_grid, title_defer)

    # NOTE
    # Delete the object we created in sidebar - enable the below if we want to destroy canvas objects from the board
    # this will remove the object from memory and allocate more room for more objects on low memory computers
    # the number corresponds to the position of the canvas class object in sidebar_obj array
    # ---- sidebar_obj[0].destroy()
    # ---- sidebar_obj.pop(0)

    # Check dataset has been given
    if data_set:
        print("**** Data set provided!")

        # Declare the GridManager object to handle movements around the grid
        # It can also read passed instructions and will handle the management of drawing and storing Canvas objects
        grid = GridManager(left_edge, bottom_edge)

        print("**** Initiating execution of instructions...")

        instruction_count = 1
        for instruction in data_set:
            # MODES = North, South, East, West, Start, Change
            # Check the instruction type and proceed with appropriate functions
            # Checking is conducted to ensure the instruction is read and executed correctly

            print("* Executing Instruction " + str(instruction_count) + "/" + str(len(data_set)) + " -> " + str(
                instruction))

            if isDirection(instruction[0]):
                # Start direction code
                # Expected Array Variables = [GridManager Direction Instruction, Steps In Direction]
                grid.navigate(instruction[0], instruction[1])
            elif instruction[0] == "Start":
                # Expected Array Variables = [GridManager Instruction, x Position, y Position, Canvas Type]
                grid.moveTo(instruction[1], instruction[2])
                grid.plotCanvas(instruction[3])
                time.sleep(speed_of_instructions)
            elif instruction[0] == "Change":
                # Expected Array Variables = [GridManager Instruction, Canvas Type]
                grid.plotCanvas(instruction[1])

            instruction_count = instruction_count + 1

        print("**** Instructions Executed!")

        grid.reset()

        # As per Client Briefing #3 Add last drawn variant to the left
        drawFinalVariant(grid.currentCanvasType, grid_top_pos, left_side_of_grid)


#
# --------------------------------------------------------------------#


# -----Initialisation Steps-------------------------------------------#
#
# This code checks that the programmer's identity has been provided
# and whether or not the data generation function is available.  You
# should NOT change any of the code in this section.
#

# Confirm that the student has declared their authorship
if not isinstance(student_number, int):
    print('\nUnable to run: No student number supplied',
          '(must be an integer)\n')
    abort()
if not isinstance(student_name, str):
    print('\nUnable to run: No student name supplied',
          '(must be a character string)\n')
    abort()

### Define the function for generating data sets, using the
### client's "raw data" function if available, but otherwise
### creating a dummy function that returns an empty list
if isfile('data_generator.py'):
    print('\nNote: Data module found\n')
    from data_generator import raw_data


    def data_set(new_seed=None):
        seed(new_seed)
        return raw_data(grid_width, grid_height)
else:
    print('\nNote: No data module available\n')


    def data_set(dummy_parameter=None):
        return []

#
# --------------------------------------------------------------------#


# -----Main Program to Create Drawing Canvas--------------------------#
#
# This main program sets up the canvas, ready for you to start
# drawing your solution.  Do NOT change any of this code except
# as indicated by the comments marked '*****'.  Do NOT put any of
# your solution code in this area.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and other elements, by
# ***** providing arguments to this function call
create_drawing_canvas(label_spaces=False)

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slooooowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's
# ***** overall theme
combined_titles = ""
for arr_value in element_titles:
    if arr_value == element_titles[len(element_titles) - 1]:
        combined_titles += arr_value
    else:
        combined_titles += arr_value + ', '
title(element_desc.replace('\n', ' ') + " (" + combined_titles + ")")

### Call the student's function to process the data set
### ***** While developing your program you can call the
### ***** "data_set" function with a fixed seed for the
### ***** random number generator, but your final solution must
### ***** work with "data_set()" as the argument to "visualise",
### ***** i.e., for any data set that can be returned by
### ***** calling function "data_set" with no seed.

visualise(data_set())  # <-- no argument for "data_set" when assessed

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
# --------------------------------------------------------------------#
