import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define constants
GRID_SIZE = 50
INITIAL_INFECTION_RADIUS = 1
MAX_INFECTION_RADIUS = 3
INITIAL_INFECTION_RATE = 0.05
MAX_INFECTION_RATE = 0.3
INFECTION_RATE_INCREMENT = 0.01
RECOVERY_RATE = 0.02

# Define cell states
EMPTY = 0
HEALTHY = 1
INFECTED = 2
RECOVERED = 3

# Initialize the grid with random healthy cells and a few infected cells
grid = np.random.choice([EMPTY, HEALTHY], size=(GRID_SIZE, GRID_SIZE), p=[0.3, 0.7])
infected_indices = np.random.choice(np.arange(GRID_SIZE**2), size=(GRID_SIZE**2)//20, replace=False)
grid.ravel()[infected_indices] = INFECTED

# Infection parameters
current_infection_rate = INITIAL_INFECTION_RATE
current_infection_radius = INITIAL_INFECTION_RADIUS

def move_away(row, col, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    np.random.shuffle(directions)
    for d in directions:
        new_row, new_col = row + d[0], col + d[1]
        if 0 <= new_row < GRID_SIZE and 0 <= new_col < GRID_SIZE and grid[new_row, new_col] == EMPTY:
            return new_row, new_col
    return row, col

def update_grid(grid):
    global current_infection_rate, current_infection_radius
    new_grid = grid.copy()
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if grid[row, col] == INFECTED:
                # Chance to recover
                if np.random.rand() < RECOVERY_RATE:
                    new_grid[row, col] = RECOVERED
                # Spread to neighbors
                for dx in range(-current_infection_radius, current_infection_radius + 1):
                    for dy in range(-current_infection_radius, current_infection_radius + 1):
                        if 0 <= row + dx < GRID_SIZE and 0 <= col + dy < GRID_SIZE:
                            if grid[row + dx, col + dy] == HEALTHY:
                                if np.random.rand() < current_infection_rate:
                                    new_grid[row + dx, col + dy] = INFECTED
            elif grid[row, col] == HEALTHY:
                # Move away from infected cells
                for dx in range(-current_infection_radius, current_infection_radius + 1):
                    for dy in range(-current_infection_radius, current_infection_radius + 1):
                        if 0 <= row + dx < GRID_SIZE and 0 <= col + dy < GRID_SIZE:
                            if grid[row + dx, col + dy] == INFECTED:
                                new_row, new_col = move_away(row, col, new_grid)
                                new_grid[new_row, new_col] = HEALTHY
                                new_grid[row, col] = EMPTY
                                break
    # Increase infection rate and radius over time
    if current_infection_rate < MAX_INFECTION_RATE:
        current_infection_rate += INFECTION_RATE_INCREMENT
    if current_infection_radius < MAX_INFECTION_RADIUS:
        current_infection_radius += 1
    return new_grid

def update(data):
    global grid
    grid = update_grid(grid)
    mat.set_data(grid)
    return [mat]

fig, ax = plt.subplots()
cmap = plt.colormaps.get_cmap("viridis", 4)
cmap.set_under(color='black')  # color for EMPTY cells
cmap.set_over(color='purple')  # color for INFECTED cells
bounds = [EMPTY, HEALTHY, INFECTED, RECOVERED, 4]
norm = plt.Normalize(0, 3)
mat = ax.matshow(grid, cmap=cmap, norm=norm)
ani = animation.FuncAnimation(fig, update, interval=500, save_count=50)

plt.colorbar(mat, boundaries=bounds, ticks=[EMPTY, HEALTHY, INFECTED, RECOVERED])

plt.show()
