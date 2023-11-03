import pygame
import sys

# Constants
WINDOW_SIZE = (400, 400)
GRID_SIZE = 4
TILE_SIZE = WINDOW_SIZE[0] // GRID_SIZE
BG_COLOR = (200, 20, 200)
GRID_COLOR = (250, 250, 0)
FONT_SIZE = 36
FONT_COLOR = (100, 0, 0)
# COMMANDS_COLOR = (0, 0, 100)

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("15 Puzzle")
font = pygame.font.Font(None, FONT_SIZE)

# Initial board configuration
board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
for i in range(GRID_SIZE):
    for j in range(GRID_SIZE):
        board[i][j] = i * GRID_SIZE + j + 1
board[GRID_SIZE - 1][GRID_SIZE - 1] = 0  # Empty space

history = []
history.append([row[:] for row in board])
# board[0][0], board[0][1] = board[0][1], board[0][0]
# print(history)
last_move = None
step_history = []

def draw_board():
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] != 0:
                pygame.draw.rect(window, GRID_COLOR, (j * TILE_SIZE, i * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                text = font.render(str(board[i][j]), True, FONT_COLOR)
                text_rect = text.get_rect(center=(j * TILE_SIZE + TILE_SIZE / 2, i * TILE_SIZE + TILE_SIZE / 2))
                window.blit(text, text_rect)

def slide_tile(direction):
    # global last_move, history
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:  # Find the empty space
                if direction == 'left' and j < GRID_SIZE - 1:
                    board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]
                    last_move = i * GRID_SIZE + j + 1
                    step_history.append(last_move)
                    return
                if direction == 'right' and j > 0:
                    board[i][j], board[i][j - 1] = board[i][j - 1], board[i][j]
                    last_move = i * GRID_SIZE + j
                    step_history.append(last_move)
                    return
                if direction == 'up' and i < GRID_SIZE - 1:
                    board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
                    last_move = (i+1) * GRID_SIZE + j + 1
                    step_history.append(last_move)
                    return
                if direction == 'down' and i > 0:
                    board[i][j], board[i - 1][j] = board[i - 1][j], board[i][j]
                    last_move = (i-1) * GRID_SIZE + j + 1
                    step_history.append(last_move)
                    return

def undo_move():
    # global history, step_history, boardu
    if len(history) > 2:
        history.pop()
        prev_board = history[-1]
        step_history.pop()
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                board[i][j] = prev_board[i][j]




running = True
while running:
    window.fill(BG_COLOR)
    draw_board()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                slide_tile('right')
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                slide_tile('left')
            elif event.key == pygame.K_UP or event.key == pygame.K_w:
                slide_tile('down')
            elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                slide_tile('up')
            elif event.key == pygame.K_u:
                undo_move()
            elif event.key == pygame.K_p:
                print(step_history)
            elif event.key == pygame.K_r:
                # Reset the board to the initial configuration
                board = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
                for i in range(GRID_SIZE):
                    for j in range(GRID_SIZE):
                        board[i][j] = i * GRID_SIZE + j + 1
                board[GRID_SIZE - 1][GRID_SIZE - 1] = 0
                history = []
                step_history = []
            elif event.key == pygame.K_q:
                running = False
            if not history or board != history[-1]:
                history.append([row[:] for row in board])
                # print(history[-1])

pygame.quit()
sys.exit()
