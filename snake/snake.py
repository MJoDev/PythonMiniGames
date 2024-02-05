import turtle
import time
import random

delay = 0.1

s = turtle.Screen()
s.setup(600, 600)
s.title("Snake")

snake = turtle.Turtle()
speed = 1
snake.speed(speed)
snake.shape("square")
snake.penup()
snake.goto(0,0)
snake.direction = 'stop'
snake.color('green')
speed = 1

score = 0
highest_score = 0

food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)
food.speed(0)

body = []

text = turtle.Turtle()
text.speed(0)
text.penup()
text.color('black')
text.hideturtle()
text.goto(0, -260)
text.write('Score: 0 \tHighest Score: 0', align='center', font=('verdana', 24, 'normal'))

def up():
    snake.direction = 'up'
def down():
    snake.direction = 'down'
def right():
    snake.direction = 'right'
def left():
    snake.direction = 'left'

def movement():
    if snake.direction == 'up':
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == 'down':
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == 'right':
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == 'left':
        x = snake.xcor()
        snake.setx(x - 20)

s.listen()
s.onkeypress(up, 'Up')
s.onkeypress(down, 'Down')
s.onkeypress(right, 'Right')
s.onkeypress(left, 'Left')


while True:
    s.update()

    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(2)
        for i in body:
            i.clear()
            i.hideturtle()
        snake.home()
        snake.direction = 'stop'
        score = 0
        body.clear()
        text.clear()
        text.write("Score:{}\tHighest score:{}".format(score,highest_score), align='center', font=('verdadna', 24, 'normal'))


    if snake.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250 )
        food.goto(x,y)
        speed = speed +2
        snake.speed(speed)
        new_body = turtle.Turtle()
        new_body.penup()
        new_body.shape('square')
        new_body.color('green')
        new_body.speed(0)
        body.append(new_body)
        score += 10
        text.clear()
        text.write("Score:{}\tHighest score:{}".format(score,highest_score), align='center', font=('verdadna', 24, 'normal'))
        if score > highest_score:
            highest_score = score
            text.clear()
            text.write("Score:{}\tHighest score:{}".format(score,highest_score), align='center', font=('verdadna', 24, 'normal'))

    total = len(body)
    for i in range(total -1,0,-1):
        x = body[i-1].xcor()
        y = body[i-1].ycor()
        body[i].goto(x,y)
    if total > 0: 
        x = snake.xcor()
        y = snake.ycor()
        body[0].goto(x,y)

    movement()

    for i in body:
        if i.distance(snake) < 20:
            for i in body:
                i.clear()
                i.hideturtle()
            snake.home()
            body.clear()
            score = 0
            text.clear()
            text.write("Score:{}\tHighest score:{}".format(score,highest_score), align='center', font=('verdadna', 24, 'normal'))

    time.sleep(delay)


turtle.done()