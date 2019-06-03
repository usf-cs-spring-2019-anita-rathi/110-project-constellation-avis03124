#Project constellation
#Avis Ho
#Created date: 30May2019
#Python 3.7.3

import turtle
turtle.hideturtle()
#hide the arrow
turtle.setup(500,600)
#set up the size of the graph
turtle.penup()
#pen up to avoid drawing the unnecessary line
turtle.goto(-180,250)
#go to this point and start from Betelgeuse
turtle.pendown()
#pen down to start drawing
turtle.dot(10)
#make the dot of Betelgeuse
turtle.write("Betelgeuse",align="left", font=(50))
#write down the first star in the constellation, set the name is on the left and font is 50
turtle.right(70)
#turn right 70 degrees
turtle.forward(280)
#go forward 280 pixels
turtle.dot(10)
#make the dot of Alnitak
turtle.write("Alnitak",align="left", font=(50))
#write down the second star in the constellation, set the name is on the left and font is 50
turtle.right(35)
#turn right 35 degrees
turtle.forward(230)
#go forward 230 pixels
turtle.dot(10)
#make the dot of Saiph
turtle.write("Saiph",align="left", font=(50))
#write down the third star in the constellation, set the name is on the left and font is 50
turtle.backward(230)
#go backward 230 pixels to the point of Alnitak
turtle.left(125)
#turn left 125 degrees
turtle.forward(50)
#go forward 50 pixels
turtle.dot(10)
#make the dot of Alnilam
turtle.write("Alnilam",align="left", font=(50))
#write down the fourth star in the constellation, set the name is on the left and font is 50
turtle.forward(50)
#go forward 50 pixels
turtle.dot(10)
#make the dot of Mintaka
turtle.write("Mintaka",align="left", font=(50))
#write down the fifth star in the constellation, set the name is on the left and font is 50
turtle.left(50)
#turn left 50 degrees
turtle.forward(230)
#go forward 230 pixels
turtle.dot(10)
#make the dot of Meissa
turtle.write("Meissa",align="left", font=(50))
#write down the sixth star in the constellation, set the name is on the left and font is 50
turtle.backward(230)
#go backward 230 pixels to the point of Mintaka
turtle.right(140)
#turn left 140 degrees
turtle.forward(250)
#go forward 250 pixels
turtle.dot(10)
#make the dot of Rigel
turtle.write("Rigel",align="left", font=(50))
#write down the last star in the constellation, set the name is on the left and font is 50
