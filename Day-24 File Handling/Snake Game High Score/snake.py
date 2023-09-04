# Create, expand and give direction to snake body
from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Default x & y co-ordinates for snake body.
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        # Below empty list is nothing but a snake body(segment of turtle graphic screen).
        # The starting default number of snake body(segment) is 3.
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Function for adding snake body i.e. each segment in the empty list self.segment[].
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        # The for loop will run 3 times as the STARTING_POSITION list has 3 co-ordinates
        # Below we create segment square in shape, It is nothing but creating an object.
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        # position() in below line is a turtles inbuilt function which returns coordinates.
        self.add_segment(self.segments[-1].position())

    def move(self):
        # Below process is used to get the last segment of snake i.e. tail of snake on second last and second last on
        # third last and so on to move forward.
        # Just like how caterpillar walks
        for seg_num in range(len(self.segments) - 1, 0, -1):  # Here range starting from 2 and decreasing by 1 till 0
            new_x = self.segments[seg_num - 1].xcor()  # xcor of segment[1] is stored in new_x
            new_y = self.segments[seg_num - 1].ycor()  # ycor of segment[1] is stored in new_y
            self.segments[seg_num].goto(new_x, new_y)  # Both the above x,y co-ordinates are given to the segment[2]
        # The head of the snake i.e. segment[0] must be moving forward so that the rest of the body should move forward.
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
