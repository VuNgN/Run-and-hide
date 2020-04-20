import turtle
import random
import time
import math
import os






# hàm bắt đầu game
def playGame():
    os.system("afplay gamemusic.mp3&")
    intro.hideturtle()
    for i in range(10):
        rim.undo()
    rim.penup()
    rim.goto(-300, -300)
    rim.pendown()
    rim.color("#0066CC")
    rim.seth(0)
    for i in range(4):
        rim.forward(600)
        rim.left(90)
    startButtom.hideturtle()
    endButtom.hideturtle()
    mouse.hideturtle()
    rim.hideturtle()
    screen.bgcolor("#99FFFF")
    rim.penup()
    rim.goto(-20, 35)
    rim.pendown()

    rim.color("#FF3300")
    rim.write("3", False, align="left", font=("Arial", 60, "normal"))
    rim.undo()
    time.sleep(1.0)
    rim.write("2", False, align="left", font=("Arial", 60, "normal"))
    rim.undo()
    time.sleep(1.0)
    rim.write("1", False, align="left", font=("Arial", 60, "normal"))
    rim.undo()
    time.sleep(1.0)

    #tạo máy bay

    screen.bgpic("")
    player.color("#008800")
    player.shape("turtle")
    player.pensize(40)
    player.penup()
    player.showturtle()



    #tạo tốc độ
    global speed
    speed= 1
    global speedEnemi
    speedEnemi= 3
    global  maxspeed
    maxspeed = 10


    # tạo mây

    for i in range(5):
        cloud[i].color("#99FFFF")
        cloud[i].shapesize(1,10,40)
        cloud[i].goto(random.randint(-220,220),random.randint(-250,250))
        cloud[i].color("#fff")
        cloud[i].penup()
        cloud[i].showturtle()




    global enemi_number
    #tạo địch
    enemi_number = 2

    for i in range(enemi_number):
        enemy[i].color("#99FFFF")
        enemy[i].shapesize(1,2,1)
        enemy[i].pensize(20)
        enemy[i].goto(random.randint(-270,-220),random.randint(-20,20))
        enemy[i].color("#FF3300")
        enemy[i].penup()
        enemy[i].showturtle()
        d = math.sqrt(pow(player.xcor()-enemy[i].xcor(),2)+pow(player.ycor()-enemy[i].ycor(),2))

    # hàm kết thúc game
    gameOver = False

    def addEnemy():
        global speedEnemi
        global enemi_number
        if speedEnemi == maxspeed:
            enemi_number += 1
            speedEnemi = 8

    #khoảng cách từ player đến enemy
    def khoang_cach(x,y):
        z=0
        for i in range(enemi_number):
            z = math.sqrt(pow(x.xcor() - y.xcor(), 2) + pow(x.ycor() - y.ycor(), 2))
        if z < 20 : return True
        return False

    # đi lên
    def moveUp():
        global speed
        speed += 1
        global speedEnemi
        if speedEnemi <= maxspeed:
            speedEnemi += 0
            for i in range(enemi_number):
                enemy[i].forward(3)
    # đi xuống
    def moveDown():
        global speed
        speed -= 1


    # sang trái
    def moveLeft():
        # đối với player
        player.left(30)
        # đối với enemi
        global speedEnemi
        if speedEnemi <= maxspeed :
            speedEnemi += 1
        for i in range(enemi_number):
            enemy[i].left((30))




    # sang phải
    def moveRight():
        #đối với player
        player.right(30)
        #đối với enemi
        global speedEnemi
        if speedEnemi <= maxspeed :
            speedEnemi += 1
        for i in range(enemi_number):
            enemy[i].right((30))


    start_time = time.time()


    # hàm di chuyển
    turtle.listen()
    turtle.onkey(moveUp, "Up")
    turtle.onkey(moveDown, "Down")
    turtle.onkey(moveLeft, "Left")
    turtle.onkey(moveRight, "Right")


    # hàm khởi chạy
    while True:

        # điều kiện khi player va vào enemi
        for i in range(enemi_number):
            if khoang_cach(player,enemy[i]):
                for j in range(2):
                    player.dot(30,"#FF6600")
                    os.system("afplay collision.mp3")
                gameOver = True

        # điều kiện giới hạn di chuyển đối với cloud
        for i in range(5):
            cloud[i].forward(2)
            if cloud[i].xcor() <= -280 or cloud[i].xcor() >= 280:
                cloud[i].color("#99FFFF")
                cloud[i].left(180)
                cloud[i].color("#fff")
            if cloud[i].ycor() <= -280 or cloud[i].ycor() >= 280:
                cloud[i].color("#99FFFF")
                cloud[i].left(180)
                cloud[i].color("#fff")

        # điều kiện di chuyển với player
        player.forward(speed)
        if player.xcor() <= -280 or player.xcor() >= 280:
            for i in range(50):
                player.dot(30,"#FF6600")
            gameOver = True
        if player.ycor() <= -280 or player.ycor() >= 280:
            for i in range(50):
                player.dot(30,"#FF6600")
            gameOver = True

        #điều kiện di chuyển với enemi
        for i in range(enemi_number):
            enemy[i].showturtle()
            enemy[i].forward(speedEnemi)
            if enemy[i].xcor() <= -280:
                enemy[i].hideturtle()
                enemy[i].speed()
                enemy[i].goto(random.randint(230,270),player.ycor())
                enemy[i].seth(180)
            if enemy[i].xcor() >= 280:
                enemy[i].hideturtle()
                enemy[i].goto(random.randint(-270,-230),player.ycor())
                enemy[i].seth(0)
            if enemy[i].ycor() <= -280:
                enemy[i].hideturtle()
                enemy[i].goto(player.xcor(), random.randint(230, 270))
                enemy[i].seth(270)
            if enemy[i].ycor() >= 280:
                enemy[i].hideturtle()
                enemy[i].goto(player.xcor(), random.randint(-270,-230))
                enemy[i].seth(90)


        # điều kiện kết thúc
        if gameOver :
            os.system("killall afplay")
            os.system("afplay gameover.mp3&")
            time.sleep(3)
            player.reset()
            player.color("#6600FF")
            for i in range(enemi_number):
                enemy[i].reset()
                enemy[i].color("#6600FF")
            for j in range(5):
                cloud[j].reset()
                cloud[j].color("#6600FF")
            break



# tạo screen
screen = turtle.Screen()
screen.title("RUN and HIDE")
screen.tracer(3)


# tạo khung
global rim
rim = turtle.Turtle()

# tạo số enemy
global enemi_number
enemi_number = 2

global speedEnemi

# tạo enemy
global enemy
enemy = []
for i in range(enemi_number):
    enemy.append(turtle.Turtle())
    enemy[i].reset()
    enemy[i].color("#99FFFF")

# tạo mây
global cloud
cloud = []
for j in range(5):
    cloud.append(turtle.Turtle())
    cloud[j].reset()
    cloud[j].color("#99FFFF")


# tạo player
global player
player = turtle.Turtle()
player.reset()
player.color("#FFCC66")

# tạo nút start
startButtom = turtle.Turtle()
startButtom.reset()
startButtom.color("#FFCC66")

# tạo nút end
endButtom = turtle.Turtle()
endButtom.reset()
endButtom.color("#FFCC66")

# tạo chuột
mouse = turtle.Turtle()
mouse.reset()
mouse.color("#FFCC66")

global intro
intro = turtle.Turtle()

global endGame

screen.bgcolor("black")
player.reset()
player.color("#6600FF")
player.hideturtle()
player.seth(90)
for i in range(enemi_number):
    enemy[i].hideturtle()
for j in range(5):
    cloud[j].hideturtle()
startButtom.reset()
startButtom.color("#6600FF")
startButtom.hideturtle()
endButtom.reset()
endButtom.color("#6600FF")
endButtom.hideturtle()
mouse.reset()
mouse.color("#6600FF")
mouse.hideturtle()
rim.penup()
rim.goto(-300,-300)
rim.pendown()
rim.color("#fff")
rim.pensize(15)
for i in range(4):
    rim.forward(600)
    rim.left(90)
rim.hideturtle()
os.system("afplay intromusic.mp3&")
intro.pensize(30)
intro.penup()
intro.goto(-210, 0)
intro.hideturtle()
intro.color("#FF99FF")
intro.write("V", True, align="left", font=("Times New Roman", 70, "normal"))
time.sleep(0.5)
intro.color("#CC99FF")
intro.write("ũ", True, align="left", font=("Times New Roman", 70, "normal"))
time.sleep(0.5)
intro.color("#9999FF")
intro.write("N", True, align="left", font=("Times New Roman", 70, "normal"))
time.sleep(0.5)
intro.color("#6699FF")
intro.write("g", True, align="left", font=("Times New Roman", 70, "normal"))
time.sleep(0.5)
intro.color("#3399FF")
intro.write("u", True, align="left", font=("Times New Roman", 70, "normal"))
time.sleep(0.5)
intro.color("#0099FF")
intro.write("y", True, align="left", font=("Times New Roman", 70, "normal"))
time.sleep(0.5)
intro.color("#3399CC")
intro.write("ễ", True, align="left", font=("Times New Roman", 70, "normal"))
time.sleep(0.5)
intro.color("#6699CC")
intro.write("n", True, align="left", font=("Times New Roman", 70, "normal"))
intro.goto(-100, -40)
time.sleep(0.5)
intro.color("#CC99CC")
intro.write("entertainment", True, align="left", font=("Times New Roman", 40, "normal"))
time.sleep(3)
for i in range(20):
    intro.undo()
os.system("killall afplay")
# tạo menu
def menu():
    screen.bgcolor("#6600FF")
    player.reset()
    player.color("#6600FF")
    player.hideturtle()
    player.seth(90)
    for i in range(enemi_number):
        enemy[i].hideturtle()
    for j in range(5):
        cloud[j].hideturtle()
    startButtom.reset()
    startButtom.color("#6600FF")
    startButtom.hideturtle()
    endButtom.reset()
    endButtom.color("#6600FF")
    endButtom.hideturtle()
    mouse.reset()
    mouse.color("#6600FF")
    mouse.hideturtle()
    rim.color("#6600FF")
    rim.penup()
    rim.pensize(15)
    rim.goto(-300, -300)
    rim.pendown()
    rim.color("#000099")
    for i in range(4):
        rim.forward(600)
        rim.left(90)
    rim.penup()
    rim.pensize(5)
    rim.penup()
    rim.goto(-270,-290)
    rim.color("black")
    rim.write("""   Sử dụng các phím Up, Down, Left, Right để di chuyển con chuột đen 
di chuyển chuột vào ô có hình TAM GIÁC để START GAME, hình VUÔNG để END GAME.""",False,align="left",font=("Arial",10,"normal"))
    rim.goto(3, 122)
    rim.color("black")
    rim.pendown()
    rim.write("""LUẬT CHƠI :
       Một con rùa bị bao vây và bị
       những quả tên lửa đuổi theo,  
       nhiệm vụ của bạn là dùng các phím
       Up để tăng tốc, Down để giảm tốc,
       Left, Right để rẽ con rùa bay.
       
CHÚ Ý : 
       Cẩn thận khi ĐẾN GẦN HÀNG RÀO vì
       TÊN LỬA sẽ phóng ra từ HÀNG RÀO.
       Chơi càng lâu độ khó Game càng tăng.
       Nếu con rùa bị
       ĐÂM PHẢI HÀNG RÀO HOẶC NHỮNG QUẢ TÊN LỬA
       thì bạn sẽ THUA .""", False, align="left", font=("Arial", 7, "normal"))


    intro.hideturtle()
    rim.color("#6600FF")
    os.system("afplay menumusic.mp3&")
    startButtom.showturtle()
    startButtom.color("#99FFFF")
    startButtom.penup()
    startButtom.shape("triangle")
    startButtom.goto(-45,50)
    startButtom.begin_fill()
    for i in range(2):
        startButtom.fd(80)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(40)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
        startButtom.fd(2)
        startButtom.left(10)
    startButtom.end_fill()
    startButtom.color("#336666")
    startButtom.goto(-5,80)

    endButtom.showturtle()
    endButtom.color("#99FFFF")
    endButtom.penup()
    endButtom.goto(-45, -250)
    endButtom.begin_fill()
    for i in range(2):
        endButtom.fd(80)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(40)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
        endButtom.fd(2)
        endButtom.left(10)
    endButtom.end_fill()
    endButtom.shape("square")
    endButtom.color("red")
    endButtom.goto(-5, -220)

    mouse.showturtle()
    mouse.shapesize(2,5,2)
    mouse.color("black")
    mouse.penup()
    mouse.goto(-5,-100)
    mouse.seth(90)
    speed_mouse = 5


    def moveUpMouse():
        global speed_mouse
        speed_mouse = 10
        mouse.seth(90)
        mouse.fd(speed_mouse)

        # đi xuống


    def moveDownMouse():
        global speed_mouse
        speed_mouse = 10
        mouse.seth(270)
        mouse.fd(speed_mouse)

        # sang trái


    def moveLeftMouse():
        speed_mouse = 10
        mouse.seth(180)
        mouse.fd(speed_mouse)

        # sang phải


    def moveRightMouse():
        speed_mouse = 10
        mouse.seth(0)
        mouse.fd(speed_mouse)

        # hàm di chuyển


    turtle.listen()
    turtle.onkey(moveUpMouse, "Up")
    turtle.onkey(moveDownMouse, "Down")
    turtle.onkey(moveLeftMouse, "Left")
    turtle.onkey(moveRightMouse, "Right")

    # hàm khởi chạy
    while True:
        mouse.fd(speed_mouse)
        speed_mouse = 0

        if math.sqrt(pow(mouse.xcor() - endButtom.xcor(), 2) + pow(mouse.ycor() - endButtom.ycor(), 2)) < 20:
            os.system("killall afplay")
            screen._destroy()

        if math.sqrt(pow(mouse.xcor() - startButtom.xcor(), 2) + pow(mouse.ycor() - startButtom.ycor(), 2)) < 20 :
            os.system("killall afplay")
            player.color("#99FFFF")
            playGame()
            os.system("killall afplay")
            screen.bgcolor("#FFCC66")
            rim.color("#FFCC66")
            rim.reset()
            startButtom.color("#FFCC66")
            startButtom.reset()
            endButtom.color("#FFCC66")
            endButtom.reset()
            mouse.color("#FFCC66")
            mouse.reset()
            break

    while True:
        menu()

menu()
