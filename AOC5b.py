input = open('input/5.txt', 'r')
lines = [line.strip() for line in input]

test = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32"
    ]
# expected result: 14, the second half of the input is irrelevant. 

# separate the ranges from the numbers between the blank ('') line
ranges = sorted((tuple(map(int, line.split('-'))) for line in lines[:lines.index('')]), key=lambda x: x[0])
numbers = list(map(int, lines[lines.index('')+1:]))

# merge the intervals 

mergedRanges = []
start, end = ranges[0]
for cs, ce in ranges[1:]:
    if cs <= end:
        end = max(end, ce)
    else:
        mergedRanges.append((start, end))
        start, end = cs, ce
mergedRanges.append((start, end))

# part 1 solution
# result = 0
# for num in numbers:
#     for s, e in mergedRanges:
#         if s <= num <= e:
#             result += 1
# print(result)

result = 0
for s, e in mergedRanges:
    result += e - s + 1 #inclusive

print(result)


