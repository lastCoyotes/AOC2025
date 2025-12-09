with open('input/9.txt') as file:
    data = [tuple([int(x) for x in data.strip().split(',')]) for data in file]

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
# expected: 50 is the area using "2,5" and "11,1" as the two corners

example = [tuple([int(x) for x in line.strip().split(',')]) for line in example]

# naive approach is to just find the area made between each point which would be O(n^2)
area = 0
for i in range(len(data)):
    for j in range(i+1, len(data)):
        area = max(area, (abs(data[i][0]-data[j][0])+1)*(abs(data[i][1]-data[j][1])+1))
print(area)