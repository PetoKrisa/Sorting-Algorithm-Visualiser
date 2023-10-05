import turtle as tutel
import random
import time
from time import sleep


screen = tutel.Screen()
screen.delay(0)
screen.setup(500,350)
screen.bgcolor("black")
screen.title("Sorting Visualiser by Kristóf Pető")
tutel.color("white")
tutel.hideturtle()

SPEED = 0.1
LENGTH = 50
ALGORITHM = "bubblesort"
FUNC = f"{ALGORITHM}(randomList({LENGTH}))"

def draw(lista, highlight=-2, finish=False):
    screen.tracer(0)

    tutel.clear()
    tutel.penup()
    tutel.goto(( ((screen.window_width()-30)/2)*-1, ((screen.window_height()-30)/2)*-1))
    for i in range(len(lista)):
        wUnit = ((screen.window_width()-30)/len(lista))
        hUnit =  ((screen.window_height()-100)/max(lista))
        tutel.forward(wUnit/2)
        tutel.pendown()
        tutel.left(90)
        tutel.pensize(wUnit)
        if (i==highlight or i==highlight+1) or (finish and i<=highlight):
            tutel.color("lime")

        tutel.forward(lista[i]*hUnit)
        tutel.color("white")

        tutel.penup()
        tutel.goto((tutel.xcor(), ((screen.window_height()-30)/2)*-1))
        tutel.right(90)
        tutel.forward(wUnit/2)
    screen.update()

def sortFinisher(lista):
    for i in range(len(lista)):
        sleep(SPEED)
        draw(lista,highlight=i,finish=True)

def randomList(length) -> list:
    lista = list(range(1,length+1))
    random.shuffle(lista)
    return lista


#algorithms
def bubblesort(lista):
    draw(lista)
    sleep(1)
    for i in range(len(lista)):
            for x in range(len(lista)):
                if x+1 < len(lista):
                    if lista[x] >= lista[x+1]:
                        sleep(SPEED)
                        draw(lista, highlight=x)
                        num = lista[x]
                        lista.pop(x)
                        lista.insert(x+1,num)
    sortFinisher(lista)



eval(FUNC)

tutel.done()