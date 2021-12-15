from turtle import *
import time

bgcolor('black')
Screen()
Screen().title('ANALOG CLOCK  BY ENDALE YOHANNES.')
tracer(0)


def clock_background():
    hideturtle()
    setheading(180)
    color('orange')
    pensize(10)
    penup()
    goto(0, 200)
    pendown()
    begin_fill()
    circle(200, steps=12)
    color('white')
    end_fill()
    for j in range(60):
        penup()
        color('black')
        goto(0, 0)
        forward(186)
        pendown()
        pensize(1)
        backward(8)
        left(6)
    right(90)
    for i in range(12):
        color('black')
        penup()
        goto(0, 0)
        if 2 <= i <= 8:
            forward(165)
        else:
            forward(145)
        pendown()
        write(str(12 - i), font=('roman', 20, 'bold'))
        left(30)


def draw_center():

    penup()
    goto(-25, -120)
    pendown()
    color('purple')
    write('ENDALE', font=('forte', 12, 'bold'))
    penup()
    goto(6, 0)
    pendown()
    color('black')
    begin_fill()
    circle(6)
    end_fill()


def set_hr(sec):
    goto(0, 0)
    setheading(90)
    color('black')
    hr = sec // 3600
    hr %= 12
    hr += -3
    deg_hr = 360 / 12 * hr
    pensize(6)
    right(deg_hr)
    forward(50)
    stamp()


def set_min(sec):
    setheading(90)
    color("black")
    penup()
    goto(0, 0)
    mi = sec // 60
    mi %= 60
    deg_mi = 360 / 60 * mi
    pensize(3)
    right(deg_mi)
    pendown()
    forward(90)
    stamp()


def set_sec(sec):
    setheading(90)
    color("black")
    penup()
    goto(0, 0)
    sec %= 60
    deg_sec = 360 / 60 * sec
    pensize(1)
    right(deg_sec)
    pendown()
    forward(135)
    stamp()
    penup()
    goto(0, 0)
    pendown()


while True:
    total_second = time.time()
    clock_background()
    draw_center()
    set_hr(total_second)
    set_min(total_second)
    set_sec(total_second)
    update()
    time.sleep(1)
    clear()
