import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
GRID_SIZE = 10
CELL_SIZE = 32
WINDOW_SIZE = GRID_SIZE * CELL_SIZE  # 10x10 grid with each cell of 32x32 pixels

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the window
screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption("Move the Square")

# Set up the square's initial position
x_pos = 0
y_pos = 0

# Create the square (pygame.Rect object)
square = pygame.Rect(x_pos, y_pos, CELL_SIZE, CELL_SIZE)

# Set the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:  # Quit on 'q'
                running = False
            elif event.key == pygame.K_UP:
                # Move up
                if y_pos > 0:
                    y_pos -= CELL_SIZE
            elif event.key == pygame.K_DOWN:
                # Move down
                if y_pos < (GRID_SIZE - 1) * CELL_SIZE:
                    y_pos += CELL_SIZE
            elif event.key == pygame.K_LEFT:
                # Move left
                if x_pos > 0:
                    x_pos -= CELL_SIZE
            elif event.key == pygame.K_RIGHT:
                # Move right
                if x_pos < (GRID_SIZE - 1) * CELL_SIZE:
                    x_pos += CELL_SIZE

            # Update the position of the square
            square.x = x_pos
            square.y = y_pos

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the square (black color)
    pygame.draw.rect(screen, BLACK, square)

    # Update the screen
    pygame.display.flip()

    # Set the frame rate
    clock.tick(30)  # 30 frames per second

# Quit pygame
pygame.quit()
sys.exit()
