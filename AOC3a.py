input = open('input/3.txt', 'r')

result = 0

# this is a sliding window problem for each line to find the maximum joltage

for line in input:
    line = line.strip()
    # print(line)
    l = int(line[0])
    r = int(line[1])
    for i in range(len(line)-1):
        if int(line[i]) > l:
            l = int(line[i])
            r = int(line[i+1])
        for j in range(i+1,len(line)):
            if int(line[j]) > r:
                r = int(line[j])
    print(l, r)
    result += (l*10 + r)

print(result)