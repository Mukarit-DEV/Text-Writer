import turtle
t = turtle.Turtle()
sc = turtle.Screen()
sc.setup(1500, 1000)
sc.title("Name_writer")
sc.bgcolor("black")
t.color("green")
t.width(3)
t.speed(8)

t.penup()
t.back(700)
t.pendown()

def let_a():
    t.penup()
    t.forward(50)
    t.pendown()
    t.left(90)
    t.forward(50)
    t.back(25)
    for n in range(360):
        t.left(1)
        t.forward(0.4)
    t.penup()
    t.back(25)
    t.right(90)
    t.forward(10)
    t.pendown()
#let_a()

def let_b():
    t.left(90)
    t.forward(80)
    t.back(55)
    for n in range(360):
        t.right(1)
        t.forward(0.4)
    t.penup()
    t.back(25)
    t.right(90)
    t.forward(60)
    t.pendown()
#let_b()

def let_c():
    t.penup()
    t.left(90)
    t.forward(37)
    t.right(90)
    t.forward(40)
    t.left(120)
    t.pendown()
    for n in range(300):
        t.left(1)
        t.forward(0.4)
    t.penup()
    t.left(30)
    t.back(15)
    t.right(90)
    t.forward(10)
    t.pendown()
#let_c()

def let_d():
    t.penup()
    t.forward(50)
    t.left(90)
    t.pendown()
    t.forward(80)
    t.back(55)
    for n in range(360):
        t.left(1)
        t.forward(0.4)
    t.penup()
    t.back(25)
    t.right(90)
    t.forward(10)
    t.pendown()
#let_d()

def let_e():
    t.penup()
    t.left(90)
    t.forward(25)
    t.right(90)
    t.pendown()
    t.forward(45)
    t.left(90)
    for n in range(315):
        t.left(1)
        t.forward(0.4)
    t.penup()
    t.left(45)
    t.back(15)
    t.right(90)
    t.forward(17)
    t.pendown()
#let_e()

def let_f():
    t.left(90)
    t.forward(55)
    for n in range(110):
        t.right(1)
        t.forward(0.4)
    t.penup()
    for n in range(110):
        t.left(1)
        t.back(0.4)
    t.back(10)
    t.right(90)
    t.pendown()
    t.forward(25)
    t.penup()
    t.back(25)
    t.right(90)
    t.forward(45)
    t.left(90)
    t.forward(39)
    t.pendown()
#let_f()

def let_g():
    t.penup()
    t.forward(50)
    t.left(90)
    t.pendown()
    t.forward(50)
    t.back(25)
    for n in range(360):
        t.left(1)
        t.forward(0.4)
    t.back(30)
    for n in range(140):
        t.right(1)
        t.back(0.4)
    t.penup()
    for n in range(140):
        t.left(1)
        t.forward(0.4)
    t.forward(5)
    t.right(90)
    t.forward(10)
    t.pendown()
#let_g()

def let_h():
    t.left(90)
    t.forward(80)
    t.back(55)
    for n in range(180):
        t.right(1)
        t.forward(0.4)
    t.forward(25)
    t.penup()
    t.left(90)
    t.forward(10)
    t.pendown()
#let_h()

def let_i():
    t.left(90)
    t.forward(37)
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(3)
    t.penup()
    t.back(50)
    t.right(90)
    t.forward(10)
    t.pendown()
#let_i()

def let_j():
    t.penup()
    t.forward(35)
    t.pendown()
    t.left(90)
    t.forward(37)
    t.penup()
    t.forward(10)
    t.pendown()
    t.forward(3)
    t.penup()
    t.back(50)
    t.pendown()
    t.back(5)
    for n in range(110):
        t.right(1)
        t.back(0.4)
    t.penup()
    for n in range(110):
        t.left(1)
        t.forward(0.4)
    t.forward(5)
    t.right(90)
    t.forward(10)
    t.pendown()
#let_j()

def let_k():
    t.left(90)
    t.forward(80)
    t.back(55)
    t.right(45)
    t.forward(30)
    t.back(30)
    t.right(90)
    t.forward(35)
    t.penup()
    t.left(45)
    t.forward(10)
    t.pendown()
#let_k()

def let_l():
    t.left(90)
    t.forward(80)
    t.back(80)
    t.right(90)
    t.penup()
    t.forward(10)
    t.pendown()
#let_l()

def let_m():
    t.left(90)
    t.forward(50)
    t.back(25)
    for n in range(180):
        t.right(1)
        t.forward(0.4)
    t.forward(25)
    t.back(25)
    for n in range(180):
        t.right(1)
        t.back(0.4)
    t.back(25)
    t.penup()
    t.right(90)
    t.forward(10)
    t.pendown()
#let_m()

def let_n():
    t.left(90)
    t.forward(50)
    t.back(25)
    for n in range(180):
        t.right(1)
        t.forward(0.4)
    t.forward(25)
    t.left(90)
    t.penup()
    t.forward(10)
#let_n()

def let_o():
    t.penup()
    t.left(90)
    t.forward(25)
    t.pendown()
    for n in range(360):
        t.right(1)
        t.forward(0.4)
    t.penup()
    t.back(25)
    t.right(90)
    t.forward(60)
    t.pendown()
#let_o()

def let_p():
    t.left(90)
    t.forward(50)
    t.back(80)
    t.forward(55)
    for n in range(360):
        t.right(1)
        t.forward(0.4)
    t.back(25)
    t.right(90)
    t.penup()
    t.forward(60)
    t.pendown()
#let_p()

def let_q():
    t.left(90)
    t.penup()
    t.forward(25)
    t.pendown()
    for n in range(360):
        t.right(1)
        t.forward(0.4)
    t.penup()
    t.right(90)
    t.forward(46)
    t.left(90)
    t.pendown()
    t.forward(25)
    t.back(80)
    t.forward(30)
    t.right(90)
    t.penup()
    t.forward(10)
    t.pendown()
#let_q()

def let_r():
    t.left(90)
    t.forward(50)
    t.back(25)
    for n in range(90):
        t.right(1)
        t.forward(0.4)
    t.penup()
    t.right(90)
    t.forward(48)
    t.left(90)
    t.forward(10)
    t.pendown()
#let_r()

def let_s():
    t.penup()
    t.left(90)
    t.forward(12.5)
    t.right(180)
    t.pendown()
    for n in range(270):
        t.left(1)
        t.forward(0.2)
    for n in range(270):
        t.right(1)
        t.forward(0.2)
    t.penup()
    t.forward(37.5)
    t.left(90)
    t.forward(10)
    t.pendown()
#let_s()

def let_t():
    t.penup()
    t.forward(10)
    t.left(90)
    t.forward(80)
    t.pendown()
    t.back(67.5)
    for n in range(180):
        t.left(1)
        t.back(0.2)
    t.penup()
    t.back(37.5)
    t.right(90)
    t.forward(12.5)
    t.pendown()
    t.forward(20)
    t.penup()
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(40)
    t.pendown()
#let_t()

def let_u():
    t.penup()
    t.left(90)
    t.forward(12.5)
    t.pendown()
    t.forward(37.5)
    t.left(180)
    t.forward(37.55)
    for n in range(180):
        t.left(1)
        t.forward(0.2)
    t.forward(37.5)
    t.penup()
    t.back(37.5)
    for n in range(90):
        t.right(1)
        t.back(0.2)
    t.forward(22.5)
    t.pendown()
#let_u()

def let_v():
    t.penup()
    t.left(90)
    t.forward(50)
    t.right(160)
    t.pendown()
    t.forward(55)
    t.left(135)
    t.forward(55)
    t.penup()
    t.back(55)
    t.right(65)
    t.forward(36)
#let_v()

def let_w():
    t.penup()
    t.left(90)
    t.forward(50)
    t.right(160)
    t.pendown()
    t.forward(55)
    t.left(135)
    t.forward(55)
    t.right(132.5)
    t.pendown()
    t.forward(55)
    t.left(135)
    t.forward(55)
    t.penup()
    t.back(55)
    t.right(67)
    t.forward(36)
    t.pendown()
#let_w()

def let_x():
    t.penup()
    t.left(90)
    t.forward(50)
    t.pendown()
    t.right(135)
    t.forward(72)
    t.penup()
    t.left(135)
    t.forward(50)
    t.pendown()
    t.left(135)
    t.forward(72)
    t.penup()
    t.left(135)
    t.forward(60)
    t.pendown()
#let_x()

def let_y():
    t.penup()
    t.left(90)
    t.forward(50)
    t.right(157)
    t.pendown()
    t.forward(55)
    t.left(135)
    t.forward(55)
    t.back(85)
    t.forward(35)
    t.penup()
    t.right(68)
    t.forward(36)
    t.pendown()
#let_y()

def let_z():
    t.left(90)
    t.penup()
    t.forward(50)
    t.pendown()
    t.right(90)
    t.forward(50)
    t.right(135)
    t.forward(73)
    t.left(135)
    t.forward(50)
#let_z()


res = input("Please, enter some text (Your text must contain only lowercase letters (not characters)!!!): ")

for n in range(len(res)):
    if res[n] == "a":
        let_a()
    elif res[n] == "b":
        let_b()
    elif res[n] == "c":
        let_c()
    elif res[n] == "d":
        let_d()
    elif res[n] == "e":
        let_e()
    elif res[n] == "f":
        let_f()
    elif res[n] == "g":
        let_g()
    elif res[n] == "k":
        let_k()
    elif res[n] == "l":
        let_l()
    elif res[n] == "m":
        let_m()
    elif res[n] == "n":
        let_n()
    elif res[n] == "o":
        let_o()
    elif res[n] == "p":
        let_p()
    elif res[n] == "q":
        let_q()
    elif res[n] == "r":
        let_r()
    elif res[n] == "s":
        let_s()
    elif res[n] == "t":
        let_t()
    elif res[n] == "u":
        let_u()
    elif res[n] == "v":
        let_v()
    elif res[n] == "x":
        let_x()
    elif res[n] == "y":
        let_y()
    elif res[n] == "z":
        let_z()
    elif res[n] == "w":
        let_w()
    elif res[n] == "h":
        let_h()
    elif res[n] == "i":
        let_i()
    elif res[n] == "j":
        let_j()
