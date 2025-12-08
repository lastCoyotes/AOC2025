input = open('input/7.txt', 'r')
lines = [line.replace('\n', '') for line in input]

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

# expected result: 21. all beam splitters except the 5th one on the last row are hit.

# naive approach, iterate left to right, replacing each "." with a "|". increment a variable "count" when a "|" is right above a splitter "^"

# a faster approach involves not changing the state of the input at all, and rather keep track of the position of the beams and the splitters.
# since beams can recombine, we only really need to keep track of splitters that be hit, and where the beam "is" is where we explore below in rows.

count = 0
paths = set()
# add index of S to store where the beam starts
paths.add(lines[0].find("S"))

# start at 1, not 0
# go every other line because we only need to search the lines with ^'s
for i in range(2, len(lines),2):
    for c in range(len(lines[i])):
        # splitter will be hit by a beam we have
        if lines[i][c] == "^" and c in paths:
            paths.discard(c)
            paths.add(c-1)
            paths.add(c+1)
            count += 1

print(count)