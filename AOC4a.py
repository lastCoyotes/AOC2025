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

# expected result: 13

# naive approach is to iterate through each cell that contains a paper roll (@)
# check all 8 orthogonal positions surrounding it
# if there is less than 4 @'s surrounding it, increment total.

# i can make checking neighbors easier by adding .'s surrounding the border, but i worry it may affect solving part 2.

result = 0
grid = []
for line in input:
    grid.append(line.strip())

# 8 neighbors of a cell for iterating through
dir = [
    (-1, -1), (0, -1), (1, -1),
    (-1,  0),          (1,  0),
    (-1,  1), (0,  1), (1,  1)
]

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

print(result)