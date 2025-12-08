from functools import cache

input = open('input/7.txt', 'r')
grid = [line.replace('\n', '') for line in input]

test = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "..............."
]

# expected result: 40 timelines. all beam splitters except the 5th one on the last row are hit, same as part 1.

# now i need to integrate keeping count of each new "timeline" possible for a beam to take.
# because a set doesnt keep track of where the beam came from, only that there was at least 1 beam, solving part 2 will require another approach
# we can find the number of timelines by memoization/caching

start = [(r, c) for r, row in enumerate(grid) for c, char in enumerate(row) if char == "S"][0]

@cache
def explore(r, c):
    #if we reach the end of the grid, beam has reached its end
    if r >= len(grid):
        return 1
    if grid[r][c] == "." or grid[r][c] == "S":
        return explore(r+1, c)
    elif grid[r][c] == "^":
        return explore(r, c-1) + explore(r, c+1)

print(explore(*start))