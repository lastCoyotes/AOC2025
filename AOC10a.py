from itertools import combinations

example = [
    "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
    "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
    "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
]

# expected = 7
# 2 + 3 + 2 = 7 total button presses for all 3 lines

# similar to the lights out/flip puzzles. part 1 says to ignore the curly brace portion (uh oh)
# to get the fewest total button presses we'll need to dynamically try button presses, combining button presses to isolate 1-2 lights wont help reach min number

def solve(goal, buttons):
    best = len(buttons)+1
    for k in range(len(buttons)+1):
        if k >= best:
            return best
        for subset in combinations(buttons, k):
            lights = {i: False for i in range(len(goal))}
            for b in subset:
                for x in b:
                    lights[x] = not lights[x]
            lit_lights = tuple(lights[x] for x in range(len(goal)))
            if lit_lights == goal:
                best = min(best, len(subset))
    return best

result = 0

with open("input/10.txt", 'r') as f:
    for line in f.readlines():
        i1 = line.find(']')

        pattern = line[1:i1]
        lights_goal = tuple(char == '#' for char in pattern)
        # for z, char in enumerate(pattern):
        #     if char == "#":
        #         lights_goal.append(z)
        # lights_goal = tuple(lights_goal)
        tokens = line[i1+2:].split()[:-1]
        buttons = []
        for token in tokens:
            buttons.append(eval(token[:-1] + ',)'))
        result += solve(lights_goal, buttons)

# 1367 too high
# 1351 too high
print(result)
