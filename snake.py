from turtle import Turtle

MOVE_DISTANCE = 14
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.length = 3
        self.snake_segment = []
        self.initial_snake()
        self.head = self.snake_segment[0]

    def initial_snake(self):
        for i in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.shapesize(0.75, 0.75)
            turtle.penup()
            turtle.setposition(x=-(14 * i), y=0)
            self.snake_segment.append(turtle)

    def extend(self):
        turtle = Turtle("square")
        turtle.color("white")
        turtle.shapesize(0.75, 0.75)
        turtle.penup()
        turtle.setposition(self.snake_segment[-1].position())
        self.snake_segment.append(turtle)
        self.length += 1

    def move(self):
        for i in range(self.length - 1, 0, -1):
            next_pos = self.snake_segment[i - 1].position()
            self.snake_segment[i].setposition(next_pos)
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

    def reset(self):
        for snake in self.snake_segment:
            snake.reset()
        self.snake_segment.clear()
        self.initial_snake()
        self.head = self.snake_segment[0]
        self.length = 3
