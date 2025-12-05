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
# expected result: 3 (5, 11, 17 all fall within the given ranges)

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

result = 0
for num in numbers:
    for s, e in mergedRanges:
        if s <= num <= e:
            result += 1
print(result)

# because ranges can overlap, i should clean up the input to check against ranges faster.
# these values are inclusive, so naively, i could use a set and individually put each value into it to check against at O(1) time.
# but the values in the actual input are 15 digit numbers with huge ranges in between. that would be too much to store individually.

# gather the ranges, sort them, then merge overlapping ranges.
# then check the numbers against the merged values.
