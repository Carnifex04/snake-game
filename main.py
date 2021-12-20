import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

is_game_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

speed = 0.10
while is_game_on:
    screen.update()
    time.sleep(speed)
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 13:
        food.location()
        snake.extend()
        scoreboard.increment_score()
        if speed > 0.02:
            speed -= 0.0075

    # detect collision with wall
    if snake.head.xcor() > 286 or snake.head.xcor() < -299 or snake.head.ycor() > 286 or snake.head.ycor() < -286:
        scoreboard.reset()
        snake.reset()

    # detect collision with itself
    for segment in snake.snake_segment[1:]:
        if snake.head.distance(segment) < 7:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
