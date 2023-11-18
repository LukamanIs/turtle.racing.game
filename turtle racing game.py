import turtle
import random

WIDTH, HEIGHT = 500, 500
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)
screen.title("Turtle Race")
COLORS = ["red", "blue", "green", "orange", "yellow"]

def number_of_racers():
    racers = 0
    while True:
        racers = screen.textinput("racers", "Enter the number of racers(2 - 5): ")
        if racers is None:
            turtle.bye()
            exit()
        if racers.isdigit():
            racers = int(racers)
        else:
            turtle.write("try again and use a number", align="center", font=('Arial', '30', 'bold'))
            continue
        if 2 <= racers <= 5:
            return racers
        else:
            turtle.write("Number not in the range of 2 - 5", align="center", font=('Arial', '30', 'bold'))

def race(colors):
    turtles = create_racers(colors)
    while True:
        for turtle in turtles:
            distance = random.randrange(3, 20)
            turtle.forward(distance)

            y = turtle.ycor()
            if y >= HEIGHT // 2 - 10:
                return colors[turtles.index(turtle)]

def create_racers(colors):
    turtles = []
    spacing_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()  # Create a new turtle for each racer
        racer.color(color)
        racer.shape("turtle")
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH/2 + (i + 1) * spacing_x, -HEIGHT/2 + 20)
        racer.pendown()
        turtles.append(racer)
    return turtles

racers = number_of_racers()
random.shuffle(COLORS)
colors = COLORS[:racers]
winner = race(colors)
turtle.write("The winner is the turtle with color:"+ winner ,align="center", font=('Arial', '20', 'bold'))

turtle.hideturtle()
turtle.done()
