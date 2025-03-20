import pygame as pg
import sys
import time
from pygame.locals import *

current_player = 'x'
current_winner = None
is_draw = None

WIDTH = 400
HEIGHT = 400
BACKGROUND = (255, 255, 255)
LINE_COLOR = (0, 0, 0)

grid = [[None]*3, [None]*3, [None]*3]

pg.init()
FPS = 30
clock = pg.time.Clock()

screen = pg.display.set_mode((WIDTH, HEIGHT + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")

size = 80

def game_initiating_window():
    screen.fill(BACKGROUND)
    pg.draw.line(screen, LINE_COLOR, (WIDTH / 3, 0), (WIDTH / 3, HEIGHT), 7)
    pg.draw.line(screen, LINE_COLOR, (WIDTH / 3 * 2, 0), (WIDTH / 3 * 2, HEIGHT), 7)
    pg.draw.line(screen, LINE_COLOR, (0, HEIGHT / 3), (WIDTH, HEIGHT / 3), 7)
    pg.draw.line(screen, LINE_COLOR, (0, HEIGHT / 3 * 2), (WIDTH, HEIGHT / 3 * 2), 7)
    draw_status()

def draw_status():
    global is_draw
    if current_winner is None:
        message = current_player.upper() + "'s Turn"
    else:
        message = current_winner.upper() + " won!"
    if is_draw:
        message = "Game Draw!"
    font = pg.font.Font(None, 40)
    text = font.render(message, True, (255, 255, 255))
    screen.fill((0, 0, 0), (0, HEIGHT, WIDTH, 100))
    text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT + 50))
    screen.blit(text, text_rect)
    pg.display.update()

def check_win():
    global grid, current_winner, is_draw
    for row in range(0, 3):
        if (grid[row][0] == grid[row][1] == grid[row][2]) and (grid[row][0] is not None):
            current_winner = grid[row][0]
            pg.draw.line(screen, (250, 0, 0),
                         (0, (row + 1)*HEIGHT / 3 - HEIGHT / 6),
                         (WIDTH, (row + 1)*HEIGHT / 3 - HEIGHT / 6), 4)
            break
    for col in range(0, 3):
        if (grid[0][col] == grid[1][col] == grid[2][col]) and (grid[0][col] is not None):
            current_winner = grid[0][col]
            pg.draw.line(screen, (250, 0, 0),
                         ((col + 1) * WIDTH / 3 - WIDTH / 6, 0),
                         ((col + 1) * WIDTH / 3 - WIDTH / 6, HEIGHT), 4)
            break
    if (grid[0][0] == grid[1][1] == grid[2][2]) and (grid[0][0] is not None):
        current_winner = grid[0][0]
        pg.draw.line(screen, (250, 0, 0), (20, 20), (380, 380), 4)
    if (grid[0][2] == grid[1][1] == grid[2][0]) and (grid[0][2] is not None):
        current_winner = grid[0][2]
        pg.draw.line(screen, (250, 0, 0), (380, 20), (20, 380), 4)
    if (all([all(row) for row in grid]) and current_winner is None):
        is_draw = True
    draw_status()

def drawXO(row, col):
    global grid, current_player
    pos_x = (col - 1) * WIDTH / 3 + WIDTH / 6
    pos_y = (row - 1) * HEIGHT / 3 + HEIGHT / 6
    grid[row-1][col-1] = current_player
    if current_player == 'x':
        pg.draw.line(screen, (0, 0, 0), (pos_x - size // 2, pos_y - size // 2), (pos_x + size // 2, pos_y + size // 2), 5)
        pg.draw.line(screen, (0, 0, 0), (pos_x - size // 2, pos_y + size // 2), (pos_x + size // 2, pos_y - size // 2), 5)
        current_player = 'o'
    else:
        pg.draw.circle(screen, (0, 0, 0), (pos_x, pos_y), size // 2, 5)
        current_player = 'x'
    pg.display.update()

def user_click():
    x, y = pg.mouse.get_pos()
    col = x // (WIDTH / 3) + 1
    row = y // (HEIGHT / 3) + 1
    if (row <= 3 and col <= 3 and grid[row-1][col-1] is None):
        drawXO(row, col)
        check_win()

def reset_game():
    global grid, current_winner, current_player, is_draw
    time.sleep(10)
    current_player = 'x'
    is_draw = False
    game_initiating_window()
    current_winner = None
    grid = [[None]*3, [None]*3, [None]*3]

game_initiating_window()

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            user_click()
            if (current_winner or is_draw):
                reset_game()
    pg.display.update()
    clock.tick(FPS)