input = open('input/1.txt', 'r')

result: int = 0
position: int = 50

for line in input:
    line = line.strip()
    # print(line[0] + " " + line[1:])
    if position+int(line[1:]) >= 100 or position+int(line[1:]) <= 0:
        if position != 0:
            result += 1
    if line[0] == 'R':
        position += int(line[1:])
    if line[0] == 'L':
        position -= int(line[1:])
    result += int(line[1:]) // 100
    position %= 100


print("RES: " + str(result))