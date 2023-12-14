import pygame
import sys
import numpy as np

# Initialize Pygame
pygame.init()

# Set up display
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Colorful Pixel Wars")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 50, 255)
grey = (125, 125, 125)
green = (0, 255, 50)
brown = (130, 100, 50)
orange = (255, 175, 0)

# Set up pause
pause = False

# Set up grid
cell_size = 5
rows, cols = height // cell_size, width // cell_size
teams = [blue, grey, green, brown, orange]
grid = np.random.choice([0, *range(1, len(teams) + 1)], size=(rows, cols))

# Function to get neighbors of a cell
def get_neighbors(i, j):
    neighbors = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if 0 <= x < rows and 0 <= y < cols and (x != i or y != j):
                neighbors.append((x, y))
    return neighbors

# Function to update the grid
# Function to update the grid
def update_grid():
    global grid
    new_grid = grid.copy()

    for i in range(rows):
        for j in range(cols):
            # Skip white pixels
            if grid[i, j] == 0:
                continue

            neighbors = get_neighbors(i, j)
            allies = [neighbor for neighbor in neighbors if grid[neighbor] == grid[i, j]]
            enemies = [neighbor for neighbor in neighbors if grid[neighbor] != grid[i, j]]

            # Determine the battle result using a random number generator
            if allies and enemies:
                odds = len(allies) / (len(allies) + len(enemies))
                if np.random.rand() < odds:
                    # Win the battle
                    enemy_to_change = enemies[np.random.choice(len(enemies))]
                    new_grid[enemy_to_change] = grid[i, j]
                else:
                    # Lose the battle
                    new_team = allies[np.random.choice(len(allies))]
                    new_grid[i, j] = grid[new_team]

    grid = new_grid


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause

    # Update game logic
    if not pause:
        update_grid()

    # Clear the screen
    screen.fill(white)

    # Draw the grid
    for i in range(rows):
        for j in range(cols):
            if grid[i, j] != 0:
                pygame.draw.rect(screen, teams[grid[i, j] - 1], (j * cell_size, i * cell_size, cell_size, cell_size))

    # Update the display
    pygame.display.flip()

    # Control the frame rate
    pygame.time.Clock().tick(240)
