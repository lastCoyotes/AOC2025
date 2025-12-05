input = open('input/2.txt', 'r')

input_ranges = input.read().split(",")
# print(input_ranges)

# if invalid IDs are only IDs with numbers repeated twice, then ranges with EVEN length will have the potential to be invalid.
# further supported by the fact that 101 is a valid ID, as there are no leading 0's in an ID.

# instead of checking one by one. we only need to check certain halves of the input ranges.
# if EITHER the first value or the second value of the ID range is an even amount of digits, then we check further for invalid IDs within their range (inclusive)

# finding invalid ID's can be done faster than linear time too
# instead of incrementing through the range and seeing if its an ID with a number repeated twice,
# construct a number consisting of a repeated integer that fits within the range.

# PART 2:
# part 2 takes the problem one step further by requiring you to catch all IDs with repeated digits, not just numbers repeated twice. but n times
# to find these other values, we cant rely on working on just even, divisible length IDs,
# we need to find the prime factors of the length of a ID's digits and repeat numbers with in its range


result = 0

for ID_range in input_ranges:
    boundary = ID_range.split('-')
    # print(boundary)
    # print("LENGTHS: " + str(len(boundary[0])) + " " + str(len(boundary[1])))
    # # n and m are lists of factors of the length of their respective IDs to check for repeatable units
    # n = []
    # for i in range(1, len(boundary[0])+1):
    #     if len(boundary[0]) % i == 0:
    #         n.append(i)
    # m = []
    # for i in range(1, len(boundary[1])+1):
    #     if len(boundary[1]) % i == 0:
    #         m.append(i)
    # print(n)
    # print(m)
    for i in range(int(boundary[0]) , int(boundary[1])+1):
            s = str(i)
            n = len(s)
            for size in range(n//2, 0, -1):
                pattern = s[:size]
                if pattern*(n//size) == s:
                    result += i
                    break

print(result)
