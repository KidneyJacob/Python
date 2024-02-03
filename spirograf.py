from turtle import Turtle, Screen
import turtle
import random

# spirograf
# základní nastavení
turtle.colormode(255)
jean = Turtle()
jean.shape("turtle")
jean.pensize(2)
jean.speed(50)

# generování barvy
def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color

def spirograf(gap):
# průběch programu počet běhu programu 
  for number in range(int(360/gap)):
    # náhodná barva
    jean.pencolor(random_color())
  # velikost kruhu
    jean.circle(60)
  # pohyb
    jean.left(gap)
    
spirograf(6)    

my_screen = Screen()
my_screen.exitonclick()