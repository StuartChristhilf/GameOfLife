import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
width, height = 900, 900
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Conway's Game of Life")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# set up pause
pause = False

# Set up grid
cell_size = 3
rows, cols = height // cell_size, width // cell_size
grid = np.random.choice([0, 1], size=(rows, cols))

# Function to update the grid based on Conway's Game of Life rules
def update_grid():
    global grid
    new_grid = grid.copy()

    for i in range(rows):
        for j in range(cols):
            neighbors = sum(grid[i-1:i+2, j-1:j+2].ravel()) - grid[i, j]

            if grid[i, j] == 1:
                if neighbors < 2 or neighbors > 3:
                    new_grid[i, j] = 0
            else:
                if neighbors == 3:
                    new_grid[i, j] = 1

    grid = new_grid

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pause == False:
                    pause = True
                elif pause == True:
                    pause = False             
    # Update game logic
    if pause == False:
        update_grid()

    # Clear the screen
    screen.fill(white)

    # Draw the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] == 1:
                pygame.draw.rect(screen, black, (j * cell_size, i * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(10)
