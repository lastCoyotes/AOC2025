input = open('input/1.txt', 'r')

result: int = 0
position: int = 50

for line in input:
    line = line.strip()

    if line[0] == 'R':
        position += int(line[1:])
    if line[0] == 'L':
        position -= int(line[1:])
    position = position % 100
    if position == 0:
        result += 1

print(result)
