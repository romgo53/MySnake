import turtle
import time
import random

# Set up screen
screen = turtle.Screen()
screen.title("Snake Game, by Rom")
screen.bgcolor("green")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turns off the screen updates


# ScoreBoard
score = 0
score_board = turtle.Turtle()
score_board.penup()
score_board.hideturtle()

score_board.setposition(-290, 270)

# Snake head
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")

snake.color("black")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"
segments = []

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)


# Moving the snake
def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)

    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)

    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)

    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    score_board.score = score


# Change direction of snake
def go_up():
    snake.direction = "up"


def go_down():
    snake.direction = "down"


def go_left():
    snake.direction = "left"


def go_right():
    snake.direction = "right"


def pause():
    snake.direction = "stop"


def exit():
    screen.bye()


# Keyboard bindings
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")
screen.onkeypress(pause, "space")
screen.onkeypress(exit, "Escape")

# main game loop
while True:
    screen.update()

    # check for collision with food
    if snake.distance(food.xcor(), food.ycor()) < 20:
        # move food to random spot
        score += 1
        score_board.undo()
        score_board.goto(-290, 270)
        score_board.write(f"Score: {score}", False, align="left", font=("Arial", 14, "normal"))
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        food.goto(x, y)

        # add segment to body
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

    # move end segments first in reverse order
    if len(segments) > 0:
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

    # move segment 0 to where the head is
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(0.1)

    # check for collision with border
    if snake.xcor() > 299 or snake.xcor() < -299 or snake.ycor() > 299 or snake.ycor() < -299:
        score_board.goto(0, 0)
        score_board.write(f"Game Over \n   score: {score}", False, align="center", font=("Arial", 20, "bold"))
        snake.direction = "stop"
        turtle.bgcolor("red")
        turtle.title("Game Over")
        time.sleep(3)
        exit()
