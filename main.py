import numpy as np

# Ask for the size of the search area
meters = input("What is the squared footage of the area that we are searching? : ")
# convert from str type to int type
meters = int(meters)

# print a grid in the size defined by the user
grid =[]

# x's populate the unsearched area
for row in range(meters):
    grid.append([])
    for column in range(meters):
        grid[row].append('x')

# Print out the grid to the console
def print_grid(grid):
    for row in grid:
        print (" ".join(row))

# Print out the grid
print_grid(grid)

# Value that the while loop will go unto
value = meters * meters

grid = np.array(grid)
counter = 0

# Grid x and y values
x = 0
y = 0
loop = 0

# Archimedean can fuck this spiral for all I care
while counter < value:
    while y < (meters - loop):
        grid[x, y] = 0
        counter += 1
        y += 1
    y -= 1
    x += 1
    while x < (meters - loop):
        grid[x, y] = 0
        x += 1
        counter += 1
    x -= 1
    y -= 1
    while y != (-1 + loop):
        grid[x, y] = 0
        counter += 1
        y -= 1
    y += 1
    x -= 1
    while x > (0 + loop):
        grid[x, y] = 0
        counter += 1
        x -= 1
    x += 1
    y += 1

    loop += 1


print_grid(grid)
