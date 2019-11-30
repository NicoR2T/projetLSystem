#!/usr/bin/env python3
from turtle import *
color('black')
tracer(1000.0)
title('Dessin en cours...')
X = []
Y = []
angle_list = []

def sauvegarder():
    x = xcor()
    y = ycor()
    X.append(x)
    Y.append(y)
    angle_list.append(heading())

def déplacer():
    if(len(X)==0):
     print("La règle ou l'axiome est mal renseignée")
    else:
     x = X[-1]
     y = Y[-1]
     angle = angle_list[-1]
     del X[-1]
     del Y[-1]
     del angle_list[-1]
     goto(x,y)
     setheading(angle)

left(30.0);
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
sauvegarder()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
right(30.0);
pd(); fd(5.0);
pd(); fd(5.0);
right(30.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
sauvegarder()
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
pd(); fd(5.0);
right(30.0);
pd(); fd(5.0);
déplacer()
left(30.0);
sauvegarder()
left(30.0);
pd(); fd(5.0);
left(30.0);
sauvegarder()
pd(); fd(5.0);
déplacer()
right(30.0);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
déplacer()
title('Dessin fini')
exitonclick()