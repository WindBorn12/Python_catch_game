import turtle
import random
import time

#screen
game_board = turtle.Screen()
game_board.title("catch the turtle")
game_board.bgcolor("blue")
countdown_time = 20

click_allowed = True
score = 0
#turtle
Turtle_t = turtle.Turtle()
Turtle_t.shape("turtle")
Turtle_t.color("green")
Turtle_t.shapesize(2,2)

#timer
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.color("black")
timer_turtle.penup()
timer_turtle.goto(0, 200)

#score
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.color("black")
score_turtle.penup()
score_turtle.goto(0, 240)
score_turtle.write("Score: 0", align="center", font=("Arial", 24, "normal"))

def increase_score(x, y):
    global score, click_allowed
    if click_allowed:
        score += 1
        score_turtle.clear()
        score_turtle.write(f"Skor: {score}", align="center", font=("Arial", 24, "normal"))
        click_allowed = False
        game_board.ontimer(reset_click, 1000)

def reset_click():
    global click_allowed
    click_allowed = True

Turtle_t.onclick(increase_score)

def teleport ():
    random_x = random.randint(-500, 500)
    random_y = random.randint(-500, 500)
    Turtle_t.hideturtle()
    Turtle_t.penup()
    Turtle_t.goto(random_x,random_y)
    Turtle_t.pendown()
    Turtle_t.showturtle()
    time.sleep(1)
    game_board.ontimer(teleport, 500)

def countdown_timer(seconds):
    while seconds > 0:
        timer_turtle.showturtle()
        print(f"time: {seconds} second")
        time.sleep(1)
        seconds -= 1
        timer_turtle.showturtle()
        if seconds < 0:
            timer_turtle.write(f"time is up")
            turtle.done()
        else:
            timer_turtle.clear()
            timer_turtle.write(f"time: {seconds} second", align="center", font=("Arial", 24, "normal"))









teleport()
countdown_timer(countdown_time)


turtle.mainloop()