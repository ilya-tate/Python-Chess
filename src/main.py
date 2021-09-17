# Libs
import pygame
# Files
from config import *
import pieces

# Board reference
# 0 is white square
# 1 is black square
BOARD_REF = [
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0]
]

def create_display():
    icon = pygame.image.load(DISPLAY_ICON)
    pygame.display.set_caption(DISPLAY_NAME)
    pygame.display.set_icon(icon)
    display = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
    display.fill(COLORS["yellow"])
    create_board(display)

def create_board(display):
    square_w = DISPLAY_W / 8
    square_h = DISPLAY_H / 8
    row = -1
    for i in BOARD_REF:
        row += 1
        for col, val in enumerate(i):
            # Make black square rectangle every other square
            if val:
                pygame.draw.rect(display, COLORS["gray"], (col * square_w, row * square_h, square_w, square_h))

def main():
    pygame.init()

    create_display()

    running = True
    while running:
        # Frames
        pygame.time.delay(FRAME_TIME)

        for event in pygame.event.get():

            # On window close
            if event.type == pygame.QUIT:
                running = False

            pygame.display.update()

    # Close window
    pygame.quit()

main()
