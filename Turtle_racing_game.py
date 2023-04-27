import turtle
import random
#my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

my_screen.setup(height=400, width=500)
user_answer_colour = my_screen.textinput(title="Make your guessing", prompt="Predict which turtle is going to win.")
#print(user_answer_colour)

colours = ["red", 'green', 'blue', 'yellow', 'purple', 'pink']
Y_coordinate = -70
turtles =[]

for index in range(0, 6):
    my_turtle = turtle.Turtle()
    my_turtle.shape('turtle')
    my_turtle.color(colours[index])
    my_turtle.penup()
    my_turtle.goto(x=-230, y=Y_coordinate)
    Y_coordinate = Y_coordinate + 30
    turtles.append(my_turtle)

#print(turtles)

keepgoing_turtles = True


while keepgoing_turtles:
    for player_turtle in turtles:
        player_turtle.forward(random.randint(0, 10))

        if player_turtle.xcor() >=230:
            keepgoing_turtles = False
            winning_colour = player_turtle.pencolor()
            #print(winning_colour)
            if winning_colour == user_answer_colour:
                print(f"You've won the {winning_colour} turtle is winner")
            else:
                print(f"You've lost the game, The winning turtle is {winning_colour}")
my_screen.exitonclick()
