import collections
import heapq
import itertools
import math
import re

# shapes - generated from input, placed here for visualization
a = [
    (0,0), (0,1), (0,2),
    (1,0), (1,1),
    (2,0)
]

b = [
    (0,0), (0,1),
    (1,0), (1,1), (1,2),
    (2,0),        (2,2),
]

c = [
                  (0,2),
           (1,1), (1,2),
    (2,0), (2,1),
]

d = [
    (0,0), (0,1), (0,2),
    (1,0),
    (2,0), (2,1), (2,2),
]

e = [
    (0,0),        (0,2),
    (1,0), (1,1), (1,2),
    (2,0),        (2,2),
]

f = [
                  (0,2),
    (1,0), (1,1), (1,2),
    (2,0), (2,1), (2,2),
]

# EXAMPLE shapes not PUZZLE shapes

# a = [
#     (0,0), (0,1), (0,2),
#     (1,0), (1,1),
#     (2,0), (2,1)
# ]

# b = [
#     (0,0), (0,1), (0,2),
#     (1,0), (1,1),
#            (2,1), (2,2)
# ]

# c = [
#            (0,1), (0,2),
#     (1,0), (1,1), (1,2),
#     (1,0), (1,1)
# ]

# d = [
#     (0,0), (0,1),
#     (1,0), (1,1), (1,2),
#     (1,0), (1,1)
# ]

# e = [
#     (0,0), (0,1), (0,2),
#     (1,0),
#     (2,0), (2,1), (2,2),
# ]

# f = [
#     (0,0), (0,1), (0,2),
#            (1,1),
#     (2,0), (2,1), (2,2),
# ]

shapes_ref = [a, b, c, d, e, f]

def rotate_shape(shape, num_rotations):
    #rot shape 90 degrees clockwise num_rotations of times
    #shift to have non-negative indices, then sort by row & col

    for _ in range(num_rotations):
        shape = [(y, -x) for x, y in shape]

        #find min x and y coords
        min_x = min([coord[1] for coord in shape])
        min_y = min([coord[0] for coord in shape])

        #shift to have non-negative indices
        shape = [(y-min_y, x-min_x) for y, x in shape]
    
    #sort by row then column
    shape.sort(key=lambda coord: (coord[0], coord[1]))

    return shape

def flip_shape(shape, axis):
    # flip shape across either x or y axis, 1 = x, 0 = y
    # to flip vert: (x, y) = (max_x - x, y)
    # to flip hori: (x, y) = (x, max_y - y)
    # ONLY working with 3x3 grids so max is 3

    # shift to have non negative indices, then sort by row & col

    if axis:
        shape = [(3-x, y) for x, y in shape]

        #find min x and y coords
        min_x = min([coord[1] for coord in shape])
        min_y = min([coord[0] for coord in shape])

        #shift to have non-negative indices
        shape = [(y-min_y, x-min_x) for y, x in shape]
    else:
        shape = [(x, 3-y) for x, y in shape]

        #find min x and y coords
        min_x = min([coord[1] for coord in shape])
        min_y = min([coord[0] for coord in shape])

        #shift to have non-negative indices
        shape = [(y-min_y, x-min_x) for y, x in shape]
    
    return shape

def create_empty_matrix(rows, cols):
    return [[0 for _ in range(cols)] for _ in range(rows)]

def place_shape(matrix, shape, position):
    # places the given shape at the specified position in the matrix

    # returns matrix with the new shape places, if placement isnt possible, returns None

    new_matrix = [row.copy() for row in matrix]

    for cell in shape:
        row, col = cell
        new_row = position[0] + row
        new_col = position[1] + col

        #check boundaries
        if new_row < 0 or new_row >= len(matrix) or new_col < 0 or new_col >= len(matrix[0]):
            return None
        
        new_matrix[new_row][new_col] += 1

        # check for overlap
        if new_matrix[new_row][new_col] > 1:
            return None
        
    return new_matrix

def remove_shape(matrix, shape, position):
    # removes the given shape from the matrix at the specified location

    #returns the matrix after removing the shape
    new_matrix = [row.copy() for row in matrix]
    
    for cell in shape:
        x, y = cell
        new_matrix[position[0] + x][position[1] + y] -= 1
        
    return new_matrix

def solve(matrix, shapes):
    #tries to fit all shapes into the matrix using DFS
    # returns 1 if possible, else 0
    if not shapes:
        return []
    
    current_shape = shapes[0]

    for rotation in range(4):
        rotated_shape = rotate_shape(current_shape, rotation)
        for flip in range(2):
            shape = flip_shape(rotated_shape, flip)

            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    position = (row, col)

                    new_matrix = place_shape(matrix.copy(), shape, position)
                    
                    # check if overlap
                    if new_matrix is not None:
                        for line in new_matrix:
                            print(line)
                        result = solve(new_matrix, shapes[1:])

                        if result is not None:
                            return [(shape, position, rotation, flip)] + result
    # no solution found
    print("\n")
    return None

# next steps:
# parse rest of puzzle input
# grab matrix size
# create a new list, append each shape to it as many times as in input
# pass the matrix and shape list into solver

# eg line: "41x48: 47 27 36 34 31 32\n"

# brute force DFS solution takes too long just to solve the first line
# total = 0
# with open('input/12example.txt', 'r') as f:
#     for line in f.readlines():
#         input = line.strip().split(" ")
#         size = input[0].replace(":", "").split("x") # these are still strings
#         size = [int(item) for item in size]
#         shape_count = [int(item) for item in input[1:]]
#         shape_list = []
#         for x in range(6):
#             for _ in range(shape_count[x]):
#                 shape_list.append(shapes_ref[x])
#         matrix = create_empty_matrix(*size)
#         if solve(matrix, shape_list) != None:
#             total += 1
        

# print(total)

# just see if theres enough space for the idea of the pieces fitting, not actually trying to fit them in the array

inp = open('input/12.txt').read().strip()
blobs = inp.split('\n\n')
sizes = [s.count('#') for s in blobs[:-1]]
result = 0
for line in blobs[-1].splitlines():
    dims, pieces_str = line.split(': ')
    x, y = tuple(map(int, dims.split('x')))
    pieces = [int(s) for s in pieces_str.split(' ')]
    if x*y > sum(a * b for a, b in zip(pieces, sizes)):
        result += 1
print(result)

# kay yeah. i was overcooking this one. 