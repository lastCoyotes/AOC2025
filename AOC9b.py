import itertools
# import numpy as np
# from PIL import Image

with open('input/9.txt') as file:
    data = [tuple([int(x) for x in data.strip().split(',')]) for data in file]
print(len(data))

example = [
    "7,1",
    "11,1",
    "11,7",
    "9,7",
    "9,5",
    "2,5",
    "2,3",
    "7,3"
]
# expected: 24

"""
The largest rectangle you can make in this example using only red and green tiles has area 24.
One way to do this is between 9,5 and 2,3:
..............
.......#XXX#..
.......XXXXX..
..@OOOOOOOXX..
..OOOOOOOOXX..
..OOOOOOO@XX..
.........XXX..
.........#X#..
..............
"""

example = [tuple([int(x) for x in line.strip().split(',')]) for line in example]

cols = list(sorted(set(c for c, _ in data)))
rows = list(sorted(set(r for _, r in data)))
C, R = len(cols), len(rows)

col_map = {}
for i, c in enumerate(cols):
    col_map[c] = i

row_map = {}
for i, r, in enumerate(rows):
    row_map[r] = i

def compressPoint(col, row):
    return (col_map[col], row_map[row])

grid = [[" "] * 250 for _ in range(250)]

data.append(data[0])
for a, b in itertools.pairwise(data):
    c1, r1 = compressPoint(*a)
    c2, r2 = compressPoint(*b)
    if c1 == c2:
        for r in range(min(r1, r2), max(r1, r2)+1):
            grid[c1][r] = '#'
    else:
        for c in range(min(c1, c2), max(c1, c2)+1):
            grid[c][r1] = '#'

q = [(0, 0), (249, 0)]
while len(q) > 0:
    c, r = q.pop()
    if c < 0 or r < 0 or c >= 250 or r >= 250:
        continue
    if grid[c][r] != ' ':
        continue
    grid[c][r] = 'X'
    q.append((c-1, r))
    q.append((c+1, r))
    q.append((c, r-1))
    q.append((c, r+1))

# visualize
# for line in grid:
#     print("".join(line))

# pic = []
# for line in grid:
#     tmp = []
#     for char in line:
#         if char == "X":
#             tmp.append([0, 0, 0])
#         elif char == "#":
#             tmp.append([200, 0, 0])
#         elif char == " ":
#             tmp.append([0, 200, 50])
#     pic.append(tmp)

# a = np.array(pic, dtype=np.uint8)

# img = Image.fromarray(a)
# img.show()

result = 0
for i, a in enumerate(data):
    for j in range(i+1, len(data)):
        b = data[j]
        c1, r1 = compressPoint(*a)
        c2, r2 = compressPoint(*b)
        okay = True
        for c in range(min(c1, c2), max(c1,c2)+1):
            for r in range(min(r1, r2), max(r1, r2)+1):
                if grid[c][r] == 'X':
                    okay = False
                    break
            if not okay:
                break

        if okay:
            result = max(result, (abs(a[0] - b[0]) + 1) * (abs(a[1]-b[1]) + 1))
print(result)