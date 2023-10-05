import turtle
import random


turtleScreen = turtle.Screen()
turtleScreen.bgcolor('#7989F1')
turtleScreen.title("Catch The Turtle")
FONT = ('Times New Roman', 20, 'normal')

gridSize = 10
xCoordinat = [-20, -10, 0, 10, 20]
yCoordinat = [-10, 0, 10, 20]
turtleList = []
score = 0
gameOver = False


#Score Turtle
scoreTurtle = turtle.Turtle()

#countdownTimer
countdownTurtle = turtle.Turtle()

def setupScoreTurtle():
    topHeight = turtleScreen.window_height() / 2
    y = topHeight * 0.9
    scoreTurtle.hideturtle()
    scoreTurtle.color("dark red")
    scoreTurtle.penup()

    scoreTurtle.setpos(0, y=y)
    scoreTurtle.write(arg="Score : ", move=False, align='center', font=FONT)


def  countdown(time):
    global gameOver
    topHeight = turtleScreen.window_height() / 2
    y = topHeight * 0.9
    countdownTurtle.hideturtle()
    countdownTurtle.color("dark red")
    countdownTurtle.penup()

    countdownTurtle.setpos(0, y=y-30)


    if time > 0:
        countdownTurtle.clear()
        countdownTurtle.write(arg=f"Time : {time}", move=False, align='center', font=FONT)
        turtleScreen.ontimer(lambda: countdown(time - 1), 1000)
    else:
        countdownTurtle.clear()
        countdownTurtle.write(arg="Game Over", move=False, align='center', font=FONT)
        gameOver = True
        hideTurtles()


def makeTurtle(x, y):
    t = turtle.Turtle()

    def handleClick(x, y):
        global score
        score += 1
        scoreTurtle.clear()
        scoreTurtle.write(arg=f"Score : {score}", move=False, align='center', font=FONT)

    t.onclick(handleClick)
    t.penup()
    t.shape('turtle')
    t.shapesize(2, 2)
    t.color('dark green')
    t.goto(x*gridSize, y*gridSize)
    turtleList.append(t)

def setupTurtles():
    for xx in xCoordinat:
        for yy in yCoordinat:
            makeTurtle(xx, yy)



def hideTurtles():
    for t in turtleList:
        t.hideturtle()


def showTurtlesRandom():
    if  gameOver ==False :
        hideTurtles()
        random.choice(turtleList).showturtle()
        turtleScreen.ontimer(showTurtlesRandom, 700)



turtle.tracer(0)

setupScoreTurtle()
setupTurtles()
hideTurtles()
countdown(10)
showTurtlesRandom()

turtle.tracer(1)


turtle.mainloop()