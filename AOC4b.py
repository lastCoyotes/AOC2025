input = open('input/4.txt', 'r')

test = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@."
]

# expected result: 43


grid = []
for line in input:
    grid.append(line.strip())

# 8 neighbors of a cell for iterating through
dir = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
]

# to modify my solution to solve part 2. i should 'remove' each roll after each pass (change @ -> . )
# i cannot modify the memory until each full pass else ill count more rolls than i actually can remove
# because i dont know how many passes i need to make until no more can be removed, i should put this into a function and call it until it returns 0
# between each pass i should save the locations of each removable roll, remove that roll from the grid, then pass the new grid into the part1 function

def removableRolls(grid):
    result = 0
    removedRolls = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # check the surrounding neighbors of grid[i][j] IF the current position in the grid is a roll (@)
            if grid[i][j] == '@':
                nearby = 0
                for dx, dy in dir:
                    neighborX = i + dx
                    neighborY = j + dy

                    # stay within bounds
                    if 0 <= neighborX < len(grid) and 0 <= neighborY < len(grid[0]):
                        if grid[neighborX][neighborY] == '@':
                            nearby += 1
                if nearby < 4:
                    result += 1
                    removedRolls.append((i, j))
    return result, removedRolls

def updateGrid(grid, removedRolls):
    # convert grid into a 2d array for sake of not decompressing and recompressing each line for every character change
    expandedGrid = []
    for i in range(len(grid)):
        expandedGrid.append(list(grid[i]))

    for x, y in removedRolls:
        expandedGrid[x][y] = '.'

    updatedGrid = []
    for i in range(len(expandedGrid)):
        updatedGrid.append("".join(expandedGrid[i]))
        
    return updatedGrid

total = 0
removed = 0

while (True):
    removed, locations = removableRolls(grid)
    # print(removed)
    # print(locations)
    total += removed
    grid = updateGrid(grid, locations)

    # for i in grid:
    #     print(i)

    if removed == 0:
        break

print(total)