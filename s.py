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

left(22.5);
left(22.5);
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
right(22.5);
pd(); fd(5.0);
pd(); fd(5.0);
right(22.5);
sauvegarder()
right(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
left(22.5);
pd(); fd(5.0);
déplacer()
left(22.5);
sauvegarder()
left(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
right(22.5);
pd(); fd(5.0);
déplacer()
déplacer()
déplacer()
déplacer()
title('Dessin fini')
exitonclick()