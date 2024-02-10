import pygame as pg
import random
import time
import math

pg.init()
pg.mixer.init()
pg.font.init()

pg.mouse.set_cursor(*pg.cursors.diamond)

sq_length = 8
bomb_num = 10
sq_width = 32
width, height = 700, 700

window = pg.display.set_mode((width, height))
pg.display.set_caption("Minesweeper")
icon = pg.image.load("bomb.png")
pg.display.set_icon(icon)

class Flag(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("red-flag.png")
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def remove_flag(self):
        self.kill()
        del self

bomb_positions_coor = []

rects_clicked_sim_x = []
rects_clicked_sim_y = []
zero_coors = []
flag_coors = []

clock = pg.time.Clock()

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
LIGHT_GREEN = (0,128,0)

all_rects = []
all_rects_clicked = []


def grid_to_coors(row, column):
    xcor = (row*32) + (width - play_width)/2
    ycor = (column*32) + (height - play_height)/2
    return xcor, ycor

def coors_to_grid(xcor, ycor):
    row = (xcor - width/2 - play_width/2)/32
    column = (ycor - height/2 - play_height/2)/32
    return row, column

def within_boundaries(xcor, ycor):
    if (width - play_width)/2 <= xcor < (width + play_width)/2:
        if (height - play_height)/2 <= ycor < (height + play_height)/2:
            return True
    return False

def background():
    for row in range(sq_length + 1):
        pg.draw.line(window, BLACK, (int(width/2-play_width/2),int(height/2-play_height/2 + sq_width*row)), (int(width/2+play_width/2),int(height/2-play_height/2 + sq_width*row)))
    for column in range(sq_length + 1):
        pg.draw.line(window, BLACK, (int(width/2-play_width/2 + sq_width*column),int(height/2-play_height/2)), (int(width/2 - play_width/2 + sq_width*column),int(height/2+play_height/2)))
            
def create_squares():
    count = 0
    for row_index, rows in enumerate(bombs):
        count += 1
        for column_index, columns in enumerate(rows):
            xcor, ycor = grid_to_coors(row_index, column_index)
            if count%2 == 0:
                color = GREEN
            else:
                color = LIGHT_GREEN
            new_rect = pg.Rect(int(xcor), int(ycor), sq_width, sq_width)
            all_rects.append(new_rect)
            pg.draw.rect(window, color, new_rect)
            count += 1




def touching_bomb(xcor, ycor):
    bombs_touched = 0 # if there are squares touching no bombs, they are all revealed, and the outer edge touching bombs as well
    for coors in bomb_positions_coor:
        if coors != (xcor, ycor):
            if abs(xcor - coors[0])/32 <= 1 and abs(ycor - coors[1])/32 <= 1:
                bombs_touched += 1
        else:
            bombs_touched = -1
            break
    return bombs_touched

def simulate_clicking(rect, num_bombs_touching):
    pg.draw.rect(window, WHITE, rect)
    row, column = coors_to_grid(rect.x, rect.y)
    if bombs[int(row)][int(column)] != True:
        bombs[int(row)][int(column)] = None

    font = pg.font.SysFont("Verdana", 20)
    label = font.render(str(num_bombs_touching), 1, (0,0,0))
    window.blit(label, (rect.x + 10, rect.y + 3))

    all_rects_clicked.append((rect.x, rect.y))

def touching_no_bombs(xcor, ycor):
    global rects_clicked_sim_x, rects_clicked_sim_y
    rects_clicked_sim_x.clear()
    rects_clicked_sim_y.clear()
    temp_xcor = xcor
    temp_ycor = ycor
    
    # right side
    while touching_bomb(temp_xcor, ycor) == 0 and temp_xcor < (width + play_width)/2:
        for rect in all_rects:
            if rect.collidepoint((temp_xcor, ycor)):
                simulate_clicking(rect, "")
                rects_clicked_sim_x.append(temp_xcor)
                zero_coors.append((rect.x, rect.y))
        temp_xcor += sq_width
    rects_clicked_sim_x.append(temp_xcor)

    temp_xcor = xcor

    # left side
    while touching_bomb(temp_xcor, ycor) == 0 and temp_xcor >= (width - play_width)/2:
        for rect in all_rects:
            if rect.collidepoint((temp_xcor, ycor)):
                simulate_clicking(rect, "")
                rects_clicked_sim_x.append(temp_xcor)
                zero_coors.append((rect.x, rect.y))
        temp_xcor -= sq_width
    rects_clicked_sim_x.append(temp_xcor)

    # down
    while touching_bomb(xcor, temp_ycor) == 0 and temp_ycor < (height + play_height)/2:
        for rect in all_rects:
            if rect.collidepoint((xcor, temp_ycor)):
                simulate_clicking(rect, "")
                rects_clicked_sim_y.append(temp_ycor)
                zero_coors.append((rect.x, rect.y))
        temp_ycor += sq_width
    rects_clicked_sim_y.append(temp_ycor)
    
    temp_ycor = ycor

    # up
    while touching_bomb(xcor, temp_ycor) == 0 and temp_ycor >= (height - play_height)/2:
        for rect in all_rects:
            if rect.collidepoint((xcor, temp_ycor)):
                simulate_clicking(rect, "")
                rects_clicked_sim_y.append(temp_ycor)
                zero_coors.append((rect.x, rect.y))
        temp_ycor -= sq_width
    rects_clicked_sim_y.append(temp_ycor)

    temp_ycor = ycor

    for coors in zero_coors:
        if touching_bomb(coors[0], coors[1]) == 0:
            rect1 = pg.Rect(coors[0] + sq_width, coors[1] + sq_width, sq_width, sq_width)
            rect2 = pg.Rect(coors[0] - sq_width, coors[1] + sq_width, sq_width, sq_width)
            rect3 = pg.Rect(coors[0] + sq_width, coors[1] - sq_width, sq_width, sq_width)
            rect4 = pg.Rect(coors[0] - sq_width, coors[1] - sq_width, sq_width, sq_width)
            rect5 = pg.Rect(coors[0] , coors[1] + sq_width, sq_width, sq_width)
            rect6 = pg.Rect(coors[0] , coors[1] - sq_width, sq_width, sq_width)
            rect7 = pg.Rect(coors[0] + sq_width, coors[1] , sq_width, sq_width)
            rect8 = pg.Rect(coors[0] - sq_width, coors[1] , sq_width, sq_width)
            rects = [rect1, rect2, rect3, rect4, rect5, rect6, rect7, rect8]
            for rect in rects:
                if within_boundaries(rect.x, rect.y):
                    if touching_bomb(rect.x, rect.y) > 0:
                        simulate_clicking(rect, touching_bomb(rect.x, rect.y))
                        all_rects_clicked.append((rect.x, rect.y))
                    elif touching_bomb(rect.x, rect.y) == 0:
                        simulate_clicking(rect, "")
                        all_rects_clicked.append((rect.x, rect.y))
            
    zero_coors.clear()

    rects_clicked_sim_x = list(set(rects_clicked_sim_x))
    rects_clicked_sim_y = list(set(rects_clicked_sim_y))

        
def reset_same_board():
    window.fill((0,70,128))
    create_squares()
    all_rects_clicked.clear()
    click = 1
    zero_coors.clear()
    flag_coors.clear()
    rects_clicked_sim_x.clear()
    rects_clicked_sim_y.clear()

start_screen = True
def start_menu():
    global start_screen, bomb_num, sq_length

    while start_screen:
        window.fill((0,70,128)) # 90 INSTEAD OF 0
        button = pg.Rect(100, 300, 200, 75)
        button2 = pg.Rect(400, 300, 200, 75)
        button3 = pg.Rect(100, 500, 200, 75)
        button4 = pg.Rect(400, 500, 200, 75)
        buttons = [button, button2, button3, button4]
        pg.draw.rect(window, (GREEN), button)
        pg.draw.rect(window, (GREEN), button2)
        pg.draw.rect(window, (GREEN), button3)
        pg.draw.rect(window, (GREEN), button4)
        for rect in buttons:
            if rect.collidepoint(pg.mouse.get_pos()):
                pg.draw.rect(window, (0,255,130), rect)
        font = pg.font.SysFont("Verdana", 40)
        title_font = pg.font.SysFont("Verdana", 80)
        title = title_font.render("MINESWEEPER", 1, BLACK)
        easy = font.render("Easy", 1, BLACK)
        medium = font.render("Medium", 1, BLACK)
        hard = font.render("Hard", 1, BLACK)
        quit_button = font.render("Quit", 1, BLACK)
        window.blit(title, (50, 100))
        window.blit(easy, (150, 315))
        window.blit(medium, (430,315))
        window.blit(hard, (150, 515))
        window.blit(quit_button, (450, 515))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    quit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pg.mouse.get_pos()
                for i, rect in enumerate(buttons):
                    if rect.collidepoint(mouse_pos):
                        if rect == button:
                            sq_length = 8
                            bomb_num = 10
                        elif rect == button2:
                            sq_length = 14
                            bomb_num = 40
                        elif rect == button3:
                            sq_length = 20
                            bomb_num = 99
                        elif rect == button4:
                            quit()
                start_screen = False

        pg.display.update()




elapsed_time = 0
click = 0
flag_count = 0

game_over_count = 0


all_flags = pg.sprite.Group()

start_menu()

play_width, play_height = sq_width*sq_length, sq_width*sq_length
bombs = [[False for _ in range(sq_length)] for _ in range(sq_length)]

bomb_int = bomb_num
while bomb_num > 0:
    for i, lists in enumerate(bombs):
        for index, m in enumerate(lists):
            bomb_chance = random.randint(1,sq_length*2)
            if bomb_chance > 1:
                continue
            if bomb_num > 0:
                if m == False:
                    bombs[i][index] = True
                    bomb_num -= 1

bomb_num = bomb_int
for a, b in enumerate(bombs):
    for c, d in enumerate(b):
        if d == True:
            xcor, ycor = grid_to_coors(a,c)
            bomb_positions_coor.append((int(xcor), int(ycor))) 

print(bomb_positions_coor)

reset_same_board()
time.sleep(0.5)


flags_available = bomb_num
game_running = True
while game_running:

    if start_screen:
        reset_same_board()
    for i in bombs:
        for m in i:
            if m == None:
                game_over_count += 1

    if game_over_count == sq_length**2 - bomb_num:
        game_running = None
    
    game_over_count = 0

    clock.tick(60)
    
    background()

    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                game_running = False

        if event.type == pg.MOUSEBUTTONUP and event.button == 1 and start_screen == False:
            if click == 2:
                mouse_pos = pg.mouse.get_pos()
                for i, rect in enumerate(all_rects):
                    if rect.collidepoint(mouse_pos):
                        if (rect.x, rect.y) not in all_rects_clicked:
                            all_rects_clicked.append((rect.x, rect.y))
                            bombs_touching = touching_bomb(rect.x, rect.y)
                            if bombs_touching == 0:
                                touching_no_bombs(rect.x, rect.y)
                                for i in rects_clicked_sim_x:
                                    touching_no_bombs(i, rect.y)
                                for i in rects_clicked_sim_y:
                                    touching_no_bombs(rect.x,i)

                            elif bombs_touching > 0:
                                simulate_clicking(rect, bombs_touching)
                            else:
                                if (rect.x, rect.y) in bomb_positions_coor:
                                    pg.draw.circle(window, (255,0,0), (rect.x + 16, rect.y + 16), 13)
                                    game_running = False
                                    # clock.tick()
                                    # while elapsed_time < 3000:
                                    #     elapsed_time += clock.get_rawtime()
                                    #     clock.tick()
                                    #     pg.draw.circle(window, (255,0,0), (rect.x + 16, rect.y + 16), 13 * int(elapsed_time/500))
                                        
                        break
            else:
                if click != 1:
                    click += 1
                    reset_same_board()
                    continue
                # odd number of blocks and not a perfect square, and greater than 4
                # If didnt actually click on anywhere connected to 0, then doesnt work properly

                not_touching = []
                mouse_pos = pg.mouse.get_pos()
                for rect in all_rects:
                    if touching_bomb(rect.x, rect.y) == 0:
                        not_touching.append((rect.x, rect.y))


                differences = []
                for index, coors in enumerate(not_touching):
                    difference = math.sqrt((mouse_pos[0] - not_touching[index][0])**2 + (mouse_pos[1] - not_touching[index][1])**2)
                    differences.append(difference)

                not_touching_rect_index = differences.index(min(differences))
                my_rect = not_touching[not_touching_rect_index]

                differences.clear()

                touching_no_bombs(my_rect[0], my_rect[1])
                for i in rects_clicked_sim_x:
                    touching_no_bombs(i, my_rect[1])
                for i in rects_clicked_sim_y:
                    touching_no_bombs(my_rect[0], i)


                
                click += 1

        elif event.type == pg.MOUSEBUTTONUP and event.button == 3 and not start_screen: # RIGHT CLICK
            x = 0
            y = 0
            mouse_pos = pg.mouse.get_pos()
            for rect in all_rects:
                if rect.collidepoint(mouse_pos):
                    x = rect.x
                    y = rect.y
                    break

            if not within_boundaries(x, y):
                continue

            if (x,y) not in flag_coors and (x,y) not in all_rects_clicked:
                all_flags.add(Flag(x,y))
                flag_coors.append((x,y))
                all_rects_clicked.append((x,y))
                flags_available -= 1

            elif (x,y) in flag_coors:
                for flag in all_flags:
                    if (flag.rect.x, flag.rect.y) == (x,y):
                        flag.remove_flag()
                        row, column = coors_to_grid(x, y)
                        color = GREEN
                        if row % 2 == 0 and column % 2 == 0:
                            color = LIGHT_GREEN
                        elif row % 2 == 1 and column % 2 == 1:
                            color = LIGHT_GREEN
                        pg.draw.rect(window, color, (x, y, sq_width, sq_width))
                        break
                flag_coors.remove((x,y))
                all_rects_clicked.remove((x,y))
                flags_available += 1

            all_flags.draw(window)

    pg.display.update()



time.sleep(1)

while game_running == False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()

        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                quit()


    window.fill(BLACK)

    pg.font.init()
    font = pg.font.SysFont("Verdana", 40)
    label = font.render("YOU LOSE", 1, (255,255,255))
    window.blit(label, (int((width - label.get_width())/2), int(height/2 - label.get_height()/2)))
    pg.display.update()

if game_running == None:
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()

            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    quit()


        window.fill(BLACK)

        pg.font.init()
        font = pg.font.SysFont("Verdana", 40)
        label = font.render("YOU WIN", 1, (255,255,255))
        window.blit(label, (int((width - label.get_width())/2), int(height/2 - label.get_height()/2)))
        pg.display.update()