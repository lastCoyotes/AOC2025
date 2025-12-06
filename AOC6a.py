import re

input = open('input/6.txt', 'r')
lines = [line.strip() for line in input]

data = []

for line in lines:
    data.append(re.split(r'\s+', line))

results = []

for i in range(len(data[0])):
    if data[4][i] == "+":
        results.append(int(data[0][i])+int(data[1][i])+int(data[2][i])+int(data[3][i]))
    if data[4][i] == "*":
        results.append(int(data[0][i])*int(data[1][i])*int(data[2][i])*int(data[3][i]))

print(sum(results))