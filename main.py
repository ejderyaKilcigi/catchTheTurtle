import turtle
import random

turtleScreen = turtle.Screen()
turtleScreen.bgcolor("#3A8CD5")
turtleScreen.title("Catch The Turtle")

lion = turtle.Turtle()
lion.penup()
lion.shape("turtle")
lion.speed(10)




for i in range(10):
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    lion.goto(x, y)
    turtleScreen.delay(1000)










turtle.done()