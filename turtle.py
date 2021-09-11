import  turtle
from tkinter import *
import random


#virus
''''
turtle.speed(250)
turtle.color('white')
turtle.bgcolor('black')

i = 200
while i > 0:
	turtle.left(i)
	turtle.forward(i*3)
	i = i - 1
	
turtle.done()


# triangle
screen = turtle.Screen()
screen.bgcolor('white')
t = turtle.Turtle()
t.speed(0)

colors = ["firebrick", "dark cyan"]

for i in range(150):
	t.color(random.choice(colors))
	t.forward(i*5)
	t.left(120)
	
t.up()
t.goto(-120,200)
t.down()
t.hideturtle()
turtle.done()
'''