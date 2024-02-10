import turtle
import time
import random

turn = 0
checkpoint = False

board = [[0,0,0],
         [0,0,0],
         [0,0,0]]

check_list = []
diagonal_2 = []

def restart():
    global board
    global turn
    pointer.clear()
    pointer.speed(0)
    pointer.color("purple")
    turn = 0
    board = [[0,0,0],
            [0,0,0],
            [0,0,0]]
    drawboard()

def save():
    global board
    global turn
    with open("save_boardai.py","w") as f:
        line = 'saved_board = '+ str(board)
        line2 = "\nsaved_turn = " + str(turn)
        f.write(line)
        f.write(line2)
    f.close()

def retrieve():
    global board
    global turn
    pointer.clear()
    drawboard()
    from save_board import saved_board, saved_turn
    board = saved_board
    turn = saved_turn
    for i,m in enumerate(board):
        for index, value in enumerate(m):
            stamp_x, stamp_y = matrix_stamp(i, index)
            if value == 1:
                pointer.shape("circle")
            elif value == 2:
                pointer.shape("turtle")
            else:
                continue
            pointer.goto(stamp_x, stamp_y)
            pointer.stamp()

def matrix_stamp(listA, listB):
    y_mid = 1.5
    x_mid = 1.5
    if listA == 0:
        y_mid = 2.5
        if listB == 0:
            x_mid = 0.5
        elif listB == 2:
            x_mid = 2.5
        return x_mid, y_mid
    elif listA == 1:
        if listB == 0:
            x_mid = 0.5
        elif listB == 2:
            x_mid = 2.5
        return x_mid, y_mid
    else:
        y_mid = 0.5
        if listB == 0:
            x_mid = 0.5
        elif listB == 2:
            x_mid = 2.5
        return x_mid, y_mid

def findbox(x, y):
    if x < 1:
        if y < 1:
            return 2,0
        elif y > 1 and y <2:
            return 1,0
        else:
            return 0,0
    elif x < 2:
        if y < 1:
            return 2,1
        elif y > 1 and y < 2:
            return 1,1
        else:
            return 0,1
    else:
        if y < 1:
            return 2,2
        elif y > 1 and y < 2:
            return 1,2
        else:
            return 0,2

def traveling(x1, y1, x2, y2):
    pointer.pu()
    pointer.goto(x1, y1)
    pointer.pd()
    pointer.goto(x2,y2)
    pointer.pu()

def compTurn():
    global board
    mark = 1
    count = 0
    check_list.clear()

    for i,q in enumerate(board):
        for k, m in enumerate(q):
            if m == mark:
                count += 1
                
        if count == 2:
            for k, m in enumerate(q):
                if m == 0:
                    x, y = matrix_stamp(i, k)
                    pointer.goto(x,y)
                    pointer.stamp()
                    return True
        count = 0

    store_value = 0
    for l in range(3):
        for i in board:
            check_list.append(i[l])
        if len(check_list) == 3:
            for v, w in enumerate(check_list):
                if w == mark:
                    count += 1
            if count == 2:
                for o, p in enumerate(check_list):
                    if p == 0:
                        x,y = matrix_stamp(o,l)
                        pointer.goto(x,y)
                        pointer.stamp()
                        return True
            count = 0
            check_list.clear()

    #diagonal
    diagonalwin = False
    for i in board:
        for z in range(3):
            check_list.append(i[z])
            diagonal_2.append(i[z])
    del check_list[1:4]
    del check_list[2:5]
    del diagonal_2[:2]
    if len(check_list) == 3:
        for i in check_list:
            if i == mark:
                count += 1
    if count == 2:
        for o, p in enumerate(check_list):
            if p == 0:
                if o == 0:
                    x , y = matrix_stamp(0,0)
                elif o == 1:
                    x , y = matrix_stamp(1,1)
                else:
                    x , y = matrix_stamp(2,2)
                pointer.goto(x,y)
                pointer.stamp()
                return True
    count = 0
    c = 0
    for i in range(3):
        if diagonal_2[c] == mark:
            count += 1
            c += 2
    if count == 2:
        for o, p in enumerate(diagonal_2):
            if p == 0:
                if o == 0:
                    x,y = matrix_stamp(0,2)
                elif o == 2:
                    x,y = matrix_stamp(1,1)
                elif o == 4:
                    x,y = matrix_stamp(2,0)
                else:
                    continue
                pointer.goto(x,y)
                pointer.stamp()
                return True
    count = 0
    check_list.clear()
    diagonal_2.clear()

    while True:
        listA = random.randint(0,2)
        listB = random.randint(0,2)
        if board[listA][listB] == 0:
            x, y = matrix_stamp(listA, listB)
            pointer.goto(x,y)
            pointer.stamp()
            return True

def drawboard():
    traveling(0,1,3,1)
    traveling(0,2,3,2)
    traveling(2,3,2,0)
    traveling(1,0,1,3)

def victory_screen(winner_shape,winline, dia_2):
    global board
    global turn
    score.clear()
    board = [[5,5,5],
            [5,5,5],
            [5,5,5]]
    pointer.speed(3)
    pointer.color("blue")
    if winline == "H":
        y = pointer.ycor()
        if y < 1:
            traveling(0,0.5,3,0.5)
        elif 1 < y < 2:
            traveling(0,1.5,3,1.5)
        else:
            traveling(0,2.5,3,2.5)
    elif winline == "V":
        x = pointer.xcor()
        if x < 1:
            traveling(0.5,3,0.5,0)
        elif 1 < x < 2:
            traveling(1.5,3,1.5,0)
        else:
            traveling(2.5,3,2.5,0)
    else:
        if dia_2 == False:
            traveling(0,3,3,0)
        elif dia_2:
            traveling(0,0,3,3)
    pointer.goto(1.5,1.5)
    pointer.color("black")
    pointer.write(f"{winner_shape} wins", move=False, align="center", font=style)
    pointer.goto(0.6,0.5)
    pointer.write("Press 'R' to replay", move=False, align="center", font=mini_style)
    pointer.goto(1,0.2)
    pointer.write("Press 'O' to open saved game", move=False, align="center", font=mini_style)
    pointer.speed(0)
    pointer.color("purple")
    
def clickFunc(x,y):
    global turn
    if turn % 2 == 0:
        pointer.shape("circle")
        mark = 1
        shape = "O"
        other_shape = "X"
        pointer.goto(x,y)
        if pointer.xcor() > 0 and pointer.xcor() < 3:
            if pointer.ycor() > 0 and pointer.ycor() < 3:
                x, y = findbox(pointer.xcor(),pointer.ycor()) # -----> find box region and seal it off
                if board[x][y] == 0:
                    score.clear()
                    score.goto(0.3,2.8)
                    score.write(f"Move: {other_shape}", move=False, align="center", font=mini_style)
                    x_mid = 1
                    y_mid = 1
                    if x == 2:
                        y_mid = 0
                    elif x == 0:
                        y_mid = 2
                    if y == 2:
                        x_mid = 2
                    elif y == 0:
                        x_mid = 0
                    pointer.goto(x_mid+0.5, y_mid+0.5)
                    pointer.stamp()
                    board[x][y] = mark
                    turn += 1
    else:
        pointer.shape("turtle")
        score.clear()
        mark = 2
        shape = "X"
        other_shape = "O"
        score.goto(0.3,2.8)
        score.write(f"Move: {other_shape}", move=False, align="center", font=mini_style)
        add_turn = compTurn()
        if add_turn:
            turn += 1
    
    count = 0
    check_list.clear()          
    for i in board:
        for k, m in enumerate(i):
            if m == mark:
                count += 1
        if count == 3:
            victory_screen(shape, "H",False)
            return
        count = 0

    for q in range(3):
        for i in board:
            check_list.append(i[q])
        if len(check_list) == 3:
            for v, w in enumerate(check_list):
                if w == mark:
                    count += 1
            if count == 3:
                victory_screen(shape,"V",False)
                return
            count = 0
            check_list.clear()

    #diagonal
    diagonalwin = False
    diag_2 = False
    for i in board:
        for z in range(3):
            check_list.append(i[z])
            diagonal_2.append(i[z])
    del check_list[1:4]
    del check_list[2:5]
    del diagonal_2[:2]
    if len(check_list) == 3:
        for i in check_list:
            if i == mark:
                count += 1
    if count == 3:
        diagonalwin = True
    count = 0
    p = 0
    for i in range(3):
        if diagonal_2[p] == mark:
            count += 1
            p += 2
    if count == 3:
        diagonalwin = True
        diag_2 = True
    if diagonalwin:
        victory_screen(shape, "D", dia_2=diag_2)
        return
    count = 0
    check_list.clear()
    diagonal_2.clear()

    if turn == 9:
        score.clear()
        pointer.goto(1.5,1.5)
        pointer.color("black")
        pointer.write("Game Over - Draw", move=False, align="center", font=style)
        pointer.goto(0.6,0.5)
        pointer.write("Press 'R' to replay", move=False, align="center", font=mini_style)
        pointer.goto(1,0.2)
        pointer.write("Press 'O' to open saved game", move=False, align="center", font=mini_style)
        pointer.speed(0)
        pointer.color("purple")
        return

screen = turtle.Screen()
screen.screensize(700,700) #sets the size of screen in pixels 
screen.setworldcoordinates(0,0,3,3) #sets up coordinate system
screen.onclick(clickFunc)

pointer = turtle.Turtle()
pointer.up()
style = ("Roboto", 60, "normal")
mini_style = ("Roboto",24,"normal")
pointer.shapesize(5, 5)
pointer.width(10)
pointer.hideturtle()
pointer.shape("circle")
pointer.color("purple")
pointer.speed(0)

score = turtle.Turtle()
score.pu()
mini_style = ("Roboto",24,"normal")
score.hideturtle()
score.color("black")
score.speed(0)

drawboard()
turtle.onkey(restart, "r")
turtle.onkey(save, "s")
turtle.onkey(retrieve, "o")
turtle.listen()

turtle.done()