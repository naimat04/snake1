from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
move_constant = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snakegame(Turtle):

    def __init__(self):
        super().__init__()
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x_coor = self.segments[seg_num - 1].xcor()
            y_coor = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(x_coor, y_coor)

        self.head.forward(move_constant)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("green")
        new_segment.pu()

        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed("fastest")
        self.color("white")
        self.pu()
        self.goto(-250, 250)
        self.pd()
        self.setheading(270)
        for i in range(4):
            self.forward(500)
            self.left(90)