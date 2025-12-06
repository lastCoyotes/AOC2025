input = open('input/6.txt', 'r')
lines = [line.replace('\n', '') for line in input]

total = 0
x = 0
numbers = []
answers = []

for i in range(len(lines[0])-1,-1,-1):
    if lines[0][i] == ' ' and lines[1][i] == ' ' and lines[2][i] == ' ' and lines[3][i] == ' ':
        continue
    numbers.append(int(lines[0][i]+lines[1][i]+lines[2][i]+lines[3][i]))
    if lines[4][i] == '*':
        x = 1
        for n in numbers:
            x *= n
        answers.append(x)
        numbers = []
    if lines[4][i] == '+':
        x = 0
        for n in numbers:
            x += n
        answers.append(x)
        numbers = []
    
print(sum(answers))