import turtle
import random

alphabet = {
    'A': ((0,0),(0.5,1),(0.75,0.5),(0.25,0.5),(0.75,0.5),(1,0)),
    'B': ((0,0),(0,1),(0.625 ,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5),(0.625,0.5),(0.75,0.375),(0.75,0.125),(0.625,0),(0,0)),
    'C': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'D': ((0,0),(0,1),(0.625 ,1),(0.75,0.875),(0.75,0.125),(0.625,0),(0,0)),
    'E': ((0.75,0),(0,0),(0,0.5),(0.75,0.5),(0,0.5),(0,1),(0.75,1)),
    'F': ((0,0),(0,0.5),(0.75,0.5),(0,0.5),(0,1),(0.75,1)),
    'G': ((0.75,0.5),(0.625,0.5),(0.75,0.5),(0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'H': ((0,0),(0,1),(0,0.5),(0.75,0.5),(0.75,1),(0.75,0)),
    'I': ((0,0),(0.25,0),(0.125,0),(0.125,1),(0,1),(0.25,1)),
    'J': ((0,0.125),(0.125,0),(0.375,0),(0.5,0.125),(0.5,1)),
    'K': ((0,0),(0,1),(0,0.5),(0.75,1),(0,0.5),(0.75,0)),
    'L': ((0,0),(0,1),(0,0),(0.75,0)),
    'M': ((0,0),(0,1),(0.5,0),(1,1),(1,0)),
    'N': ((0,0),(0,1),(0.75,0),(0.75,1)),
    'O': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875),(0.75,0.125)),
    'P': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5)),
    'Q': ((0.75,0.125),(0.625,0),(0.125,0),(0,0.125),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875),(0.75,0.125),(0.875,0)),
    'R': ((0,0),(0,1),(0.625,1),(0.75,0.875),(0.75,0.625),(0.625,0.5),(0,0.5),(0.625,0.5),(0.875,0)),
    'S': ((0,0.125),(0.125,0),(0.625,0),(0.75,0.125),(0.75,0.375),(0.675,0.5),(0.125,0.5),(0,0.625),(0,0.875),(0.125,1),(0.625,1),(0.75,0.875)),
    'T': ((0,1),(0.5,1),(0.5,0),(0.5,1),(1,1)),
    'U': ((0,1),(0,0.125),(0.125,0),(0.625,0),(0.75,0.125),(0.75,1)),
    'V': ((0,1),(0.375,0),(0.75,1)),
    'W': ((0,1),(0.25,0),(0.5,1),(0.75,0),(1,1)),
    'X': ((0,0),(0.375,0.5),(0,1),(0.375,0.5),(0.75,1),(0.375,0.5),(0.75,0)),
    'Y': ((0,1),(0.375,0.5),(0.375,0),(0.375,0.5),(0.75,1)),
    'Z': ((0,1),(0.75,1),(0,0),(0.75,0)),
}

myPen = turtle.Turtle()
myPen.hideturtle()
myPen.speed()
window = turtle.Screen()
window.bgcolor("#000000")
myPen.pensize(10)

def displayMessage(message,fontSize,color,x,y):
  myPen.color(color)
  message=message.upper()
  
  for character in message:
    if character in alphabet:
      letter=alphabet[character]
      myPen.penup()
      for dot in letter:
        myPen.goto(x + dot[0]*fontSize, y + dot[1]*fontSize)
        myPen.pendown()
        
      x += fontSize
      
    if character == " ":
      x += fontSize
    x += characterSpacing 

#Main Program Starts Here
fontSize = 50
characterSpacing = 13
fontColor = "yellow"

message = "here type your name"
displayMessage(message,fontSize,fontColor,-200,0)
turtle.done()