import turtle
import random

s = turtle.Screen()
s.title("Turtle Run")

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


dice = [1,2,3,4,5,6]

for i in range(20):
    if player1.pos() >= (200, 100):
        print("player one wins")
        break
    elif player2.pos() >= (200, -100):
        print("player two wins")
        break
    else:
        turn1 = input("Player one, press enter to advance")
        turn1 = random.choice(dice)
        print("Dice number is: ", turn1,"\nYou advance", turn1*10)
        player1.pendown()
        player1.forward(20*turn1)

        turn2 = input("Player two, Press enter to advance")
        turn2 = random.choice(dice)
        print("Dice number is: ",turn2 ,"\nYou advance" , turn2*10)
        player2.pendown()
        player2.forward(20*turn2)


turtle.done() 