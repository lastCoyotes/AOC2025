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

invalid_IDs = []
result = 0

for ID_range in input_ranges:
    boundary = ID_range.split('-')
    print(boundary)
    # check if either ID is an even length of digits
    if len(boundary[0]) % 2 == 0 or len(boundary[1]) % 2 == 0:
        # begin constructing IDs that repeat numbers twice, then add them to the invalid IDs list if they are within the bounds
        half = len(boundary[0]) // 2
        # print(boundary[0][0:half + (len(boundary[0]) == 1)])
        id = boundary[0][0:half + (len(boundary[0]) == 1)]
        while int(id + id) < int(boundary[1]):
            if int(id + id) >= int(boundary[0]):
                invalid_IDs.append(int(id + id))
            id = str(int(id) + 1)

# print(invalid_IDs)
for number in invalid_IDs:
    result += number

print(result)
