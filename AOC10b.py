from z3 import *

def solve(goal, buttons):
    n = len(goal)
    X = IntVector('x', len(buttons))

    s = Optimize()
    # cant press a button negative times
    for _ in range(len(buttons)):
        s.add([x >= 0 for x in X])

    A = []
    for button in buttons:
        row = [0 for _ in range(n)]
        for w in button:
            row[w] = 1
        A.append(row)

    for i in range(n):
        s.add(Sum(X[k]*A[k][i] for k in range(len(buttons))) == goal[i])
    s.minimize(Sum(X))

    # check if it satisfies then get the model
    if s.check() == sat:
        model = s.model()
        return sum(model[k].as_long() for k in model)
    else:
        print("No solution found.")

result = 0

with open("input/10.txt", 'r') as f:
    for line_num, line in enumerate(f.readlines()):
        i1 = line.find(']')

        pattern = line[1:i1]
        lights_goal = tuple(char == '#' for char in pattern)
        tokens = line[i1+2:].split()
        buttons = []
        for token in tokens[:-1]:
            buttons.append(eval(token[:-1] + ',)'))
        buttons = tuple(buttons)
        joltage_goal = eval('(' + tokens[-1][1:-1] + ',)')
        result += solve(joltage_goal, buttons)

print(result)