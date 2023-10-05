import turtle as tutel
import imp
import random

screen = tutel.Screen()
screen.delay(0)
screen.setup(500,350,startx=1,starty=1)
screen.bgcolor("black")
screen.title("Sorting Visualiser")
tutel.color("white")
tutel.hideturtle()


def draw(lista, highlight):
    screen.tracer(0)
    tutel.penup()
    tutel.goto((-240,-160))
    for i in range(len(lista)):
        tutel.pendown()
        tutel.left(90)
        tutel.width(10)
        if i==highlight:
            tutel.color("lime")
        tutel.forward(lista[i]*5)
        tutel.color("white")
        tutel.penup()
        tutel.goto((tutel.xcor(),-160))
        tutel.right(90)
        tutel.forward(12)
    screen.update()

draw([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], 0)

def randomList(length) -> list:
    lista = range(1,length)
    return random.shuffle(lista)

def bubbleSort(lista):
    for i in range(len(lista)):
        #upload to git

bubbleSort([5,3,7,4,2,1,6])

tutel.done()