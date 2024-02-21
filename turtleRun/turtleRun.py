import turtle
import random
import time

s = turtle.Screen()
s.title("Turtle Run")
s.setup(600, 600)

player1 = turtle.Turtle()
player2 = turtle.Turtle()

player1.hideturtle()
player1.shape("turtle")
player1.color("red")
player1.shapesize(2, 2, 2)
player1.pensize(3)

player2.hideturtle()
player2.shape("turtle")
player2.color("blue")
player2.shapesize(2, 2, 2)
player2.pensize(3)



player1.penup()
player1.goto(200, 100)
player1.pendown()
player1.circle(40)
player1.penup()
player1.goto(-200, 125)

player2.penup()
player2.goto(200, -100)
player2.pendown()
player2.circle(40)
player2.penup()
player2.goto(-200, -75)

player1.showturtle()
player2.showturtle()

player1.direction = 'stop'
player2.direction = 'stop'


def up():
    player1.direction = 'up'
def down():
    player2.direction = 'down'

s.listen()
s.onkeypress(up, 'Up')
s.onkeypress(down, 'Down')

showText = True


text = turtle.Turtle()
text.speed(0)
text.penup()
text.color('black')
text.hideturtle()
text.goto(0, -260)
text.write('Player 1, press Up', align='center', font=('verdana', 24, 'normal'))

dice = [1,2,3,4,5,6]

player1Turn = True
player2Turn = False

execute = True

while execute: 
    if player1.pos() >= (200, 100):
        text.clear()
        text.write('Player 1 wins', align='center', font=('verdana', 24, 'normal'))
        time.sleep(2)
        execute = False
    elif player2.pos() >= (200, -100):
        text.clear()
        text.write('Player 2 wins', align='center', font=('verdana', 24, 'normal'))
        time.sleep(2)
        execute = False
    else:
        if player1.direction == 'up' and player1Turn == True:
            turn1 = random.choice(dice)
            text1 = "Dice number is: "+ " " + str(turn1)
            text.clear()
            text.write( arg=text1, align='center', font=('verdana', 24, 'normal'))
            player1.pendown()
            player1.forward(20*turn1)
            player1.direction = "stop"
            player1Turn = False
            time.sleep(2)
            text.clear()
            player2Turn = True
            showText = False
        if player2.direction == 'down' and player2Turn == True:
            turn2 = random.choice(dice)
            text2 = "Dice number is: " + " " + str(turn2)
            text.clear()
            text.write(arg=text2, align='center', font=('verdana', 24, 'normal'))
            player2.pendown()
            player2.forward(20*turn2)
            player2.direction = "stop"
            player2Turn = False
            time.sleep(2)
            text.clear()
            player1Turn = True
            showText = True
        if showText:
            text.write('Player 1, press Up', align='center', font=('verdana', 24, 'normal'))
        else:
            text.write('Player 2, press Down', align='center', font=('verdana', 24, 'normal'))
            

           
            
            

turtle.done() 