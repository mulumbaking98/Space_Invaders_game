_author_ = "Stephen Mayanja"
_class_ = "SEIS 603"
_semester_ ="Summer class Final project 2018"

import turtle
import math
from turtle import *
import random
import winsound

#set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")
wn.bgpic("space_invaders_background.gif")

#register the shapes
turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

turtle.register_shape("st.gif")
turtle.register_shape("st2.gif")
turtle.register_shape("st3.gif")


# #draw the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("green")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pensize(4)
border_pen.pendown()

for side in range(4):
    border_pen.forward(600)
    border_pen.left(90)

border_pen.hideturtle()

#set score to zero
score = 0

#draw score on screen
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 270)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()


#create player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

#move player left and right
playerSpeed = 15

#create invader or invader
enemy = turtle.Turtle()

number_of_enemies = 10
enemies = []

#add enemies
for i in range(number_of_enemies):
    enemies.append(turtle.Turtle())

for enemy in enemies:
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    enemy.setposition(x,y)

enemySpeed = 2

#create the player's defense (bullet)
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("square")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletSpeed = 70

#define bullet state
#ready - ready to fire
##fire - bullet is firing
bulletSate = "ready"


def move_left():
    x = player.xcor()
    x -= playerSpeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerSpeed
    if x > 280:
        x = 280
    player.setx(x)

#fire bullet
def fire_bullet():
    #declare bulletsate as global if it needs to be changed
    global bulletSate
    if bulletSate == "ready":
        winsound.PlaySound("laser", winsound.SND_ASYNC)
        bulletSate = "fire"
    #moe bullet just above the player
        x = player.xcor()
        y = player.ycor() + 10
        bullet.setposition(x,y)
        bullet.showturtle()

#work on collision
def isCollision(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))

    if distance < 25:
        return True
    else:
        return False



#create keyboard bindings
wn.onkey(move_left,"Left")
wn.onkey(move_right,"Right")
wn.onkey(fire_bullet, "space")
wn.listen()


#main game loop

while True:

     for enemy in enemies:
#move enemy
          x = enemy.xcor()
          x += enemySpeed
          enemy.setx(x)

#reverse on hitting the end
          if enemy.xcor() < -280:
              #move all the enemies
              for e in enemies:
                  y = e.ycor()
                  y -= 40
                  e.sety(y)
                  #change direction
              enemySpeed *= -1


          if enemy.xcor() > 280:
              for e in enemies:
                  y = e.ycor()
                  y -= 40
                  e.sety(y)
              enemySpeed *= -1


    #collision btn bullet and enemy
          if isCollision(bullet, enemy):
              winsound.PlaySound("explosion", winsound.SND_ASYNC)

          #reset bullet
              bullet.hideturtle()
              bulletSate = "ready"
              bullet.setposition(0, -400)
              x = random.randint(-200, 200)
              y = random.randint(100, 250)
              enemy.setposition(x, y)
          #update score
              score += 10
              scorestring = "Score: %s" %score
              score_pen.clear()
              score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))

           #reset enemy to starting pos
              enemy.setposition(-200, 250)

          if isCollision(player, enemy):
             player.hideturtle()
             enemy.hideturtle()
             print("Game Over")
             break

     # move the bullet
     if bulletSate == "fire":
         y = bullet.ycor()
         y += bulletSpeed
         bullet.sety(y)

     # check state of bullet
     if bullet.ycor() > 275:
         bullet.hideturtle()
         bulletSate = "ready"

wn.mainloop()
