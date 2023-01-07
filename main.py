import time
from turtle import Turtle, Screen
from snake import Snakegame, Line
from food import Food
from scorecard import Scorecard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("snake game")
snake = Snakegame()
food = Food()
line = Line()
screen.tracer(0)
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")
game_on = True
scoreboard = Scorecard()
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()
    if snake.head.xcor() < -250 or snake.head.ycor() < -250 or 250 < snake.head.xcor() or 250 < snake.head.ycor():
        scoreboard.reset()

        snake.reset_snake()
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset_snake()

screen.exitonclick()
