
import turtle
import time
import random
 
delay = 0.1
score = 0
 
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)
 
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"
 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)
 
big_food = turtle.Turtle()
big_food.speed(0)
big_food.shape("circle")
big_food.color("blue")
big_food.shapesize(1.5)
big_food.penup()
big_food.goto(0,-100)
 
temp_food = turtle.Turtle()
temp_food.speed(0)
temp_food.shape("circle")
temp_food.color("purple")
temp_food.shapesize(2)
temp_food.penup()
temp_food.goto(100, 0)
temp_food.hideturtle()
 
segments = []
 
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0", align="center", font=("Courier", 24, "normal"))
 
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
 
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
 
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
 
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
 
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")
 
def generate_food_location():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    return x, y
 
def generate_big_food_location():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    return x, y
 
def generate_temp_food_location():
    x = random.randint(-280, 280)
    y = random.randint(-280, 280)
    return x, y
 
def add_segment():
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    segments.append(new_segment)
 
def remove_temp_food():
    temp_food.hideturtle()
    temp_food.goto(100, 0)
    temp_food.clear()
 
def show_temp_food():
    temp_food_x, temp_food_y = generate_temp_food_location()
 
    while head.distance(temp_food_x, temp_food_y) < 20:
        temp_food_x, temp_food_y = generate_temp_food_location()
 
    temp_food.goto(temp_food_x, temp_food_y)
    temp_food.showturtle()
 
score_time = 0
temp_food_active = False
 
while True:
    wn.update()
 
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"
 
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
 
    if head.distance(food) < 20:
        food_x, food_y = generate_food_location()
 
        while head.distance(food_x, food_y) < 20:
            food_x, food_y = generate_food_location()
 
        food.goto(food_x, food_y)
        score += 1
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
        add_segment()
 
    if head.distance(big_food) < 30:
        big_food_x, big_food_y = generate_big_food_location()
 
        while head.distance(big_food_x, big_food_y) < 20:
            big_food_x, big_food_y = generate_big_food_location()
 
        big_food.goto(big_food_x, big_food_y)
        for _ in range(3):
            add_segment()
        score += 3
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
 
    if not temp_food_active:
        if score_time % 100 == 0:
            show_temp_food()
            temp_food_active = True
            score_time = 0
        score_time += 1
    else:
        if score_time % 50 == 0:
            remove_temp_food()
            temp_food_active = False
        score_time += 1
 
    if head.distance(temp_food) < 30:
        temp_food.hideturtle()
        temp_food.goto(100, 0)
        temp_food.clear()
        for _ in range(5):
            add_segment()
        score += 5
        pen.clear()
        pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
 
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
 
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
 
    move()
 
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
 
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: {}".format(score), align="center", font=("Courier", 24, "normal"))
 
    time.sleep(delay)
 
wn.mainloop()
