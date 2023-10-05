import turtle
import random

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("#3A8CD5")
turtleScreen.title("Catch The Turtle")

lion = turtle.Turtle()
panter = turtle.Turtle()

lion.penup()
lion.shape("turtle")
lion.speed(10)

panter.penup()
panter.hideturtle()
panter .goto(0,250)
style = ('Courier', 30, 'bold')
plus = 0



def Score():

    global plus
    plus+= 1
    panter.clear()
    panter.write(f"SKOR : {plus}", font=style, align="center")


lion.onclick(lambda x, y: Score())

for i in range(10):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    lion.goto(x, y)
    turtleScreen.delay(1000)
    turtleScreen.update()











turtle.done()