import pygame as pg

pg.init()
pg.mixer.init()

window_width = 800
window_height = 600

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (200,0,0)
GREEN = (0,200,0)
BLUE = (0, 0, 200)
FPS = 30

screen = pg.display.set_mode((window_width,window_height))
pg.display.set_caption("Brickbreaker")
icon = pg.image.load("brick-breaker.png")
pg.display.set_icon(icon)
clock = pg.time.Clock()

block = pg.Rect(325, 530, 150, 25)
ball = pg.Rect(390, 400, 20, 20)

def menu():
    pass

def setup():
    brick_size = (100, 50)
    y = 25
    for i in range(5):
        y += brick_size[1]
        x = 0
        for j in range(int(window_width/brick_size[0])):
            rect = pg.Rect(x, y, brick_size[0] - 2, brick_size[1] - 2)
            rects.append(rect)
            x += brick_size[0]

    rects.append(pg.Rect(350, 325, brick_size[0] - 2, brick_size[1] - 2))

def end_screen(win):
    screen.fill(BLACK)
    if win:
        print("You win")
    else:
        print("You lose")
    pg.display.update()
    end = True
    while end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end = False

rects = []

running = True
moveLeft = False
moveRight = False
win = False

block_speed = 7
ball_speed_y = 5
ball_speed_x = 5
ball_velocity_y = 1
ball_velocity_x = 0

setup()

while running:

    screen.fill(BLACK)
    pg.draw.rect(screen, WHITE, block)
    pg.draw.rect(screen, WHITE, ball)
    for rect in rects:
        pg.draw.rect(screen, WHITE, rect)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                moveLeft = True
            elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                moveRight = True

        if event.type == pg.KEYUP:
            if event.key == pg.K_a or event.key == pg.K_LEFT:
                moveLeft = False
            elif event.key == pg.K_d or event.key == pg.K_RIGHT:
                moveRight = False


    # movement
    if moveLeft and block.x > 0:
        block.x -= block_speed
    elif moveRight and block.x < window_width - block.width:
        block.x += block_speed

    ball.y += ball_speed_y * ball_velocity_y
    ball.x += ball_speed_x * ball_velocity_x

    #  COLLISIONS
    # Collision with Player
    if block.colliderect(ball):
        if ball.collidepoint(ball.x, block.top):
            ball_velocity_y = -1
            distance = ball.x + 10 - block.centerx
            if abs(distance) <= block.width / 4:
                ball_speed_x = 5
            else:
                ball_speed_x = 7

            if distance < 0:
                ball_velocity_x = -1
            elif distance > 0:
                ball_velocity_x = 1
            else:
                ball_velocity_x = 0
        else:
            ball_velocity_x *= -1


    # collision with bricks
    index = ball.collidelist(rects)
    if index != -1:
        rect = rects[index]

        if ball.collidepoint(ball.x, rect.bottom):
            ball_velocity_y = 1
        elif ball.collidepoint(ball.x, rect.top):
            ball_velocity_y = -1
        # else:
        if ball.collidepoint(rect.right, ball.y):
            ball_velocity_x = 1
        elif ball.collidepoint(rect.left, ball.y):
            ball_velocity_x = -1

        # if ball_velocity_y < 0:
        #     ball_velocity_y = 1
        # else:
        #     ball_velocity_y = -1
        #     # ball_velocity_x *= -1

        rects.remove(rect)

    # Collision with boundary
    if ball.x < 0:
        ball_velocity_x = 1
    elif ball.x > 780:
        ball_velocity_x = -1

    if ball.y < 0:
        ball_velocity_y = 1
    elif ball.y > 620:
        running = False

    if len(rects) == 0:
        win = True
        running = False

    pg.display.update()

    clock.tick(30)

end_screen(win)