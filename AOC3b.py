input = open('input/3.txt', 'r')

result = 0

# unlike a two pointers problem in part 1. finding the top 12 values of each line will be best solved with a heap, but i need to preserve the order they are in in each line
# this problem would best be solved by sliding a window across the line of values.
# line 1 from the input:
test = "2215452689925244273244333436189317446384838478525478824435233342352236255624326767355438753493222423"
#                ^^                   ^       ^                                                     ^^^^^^^^     
# should expect: 999893222423
# this can be achieved by starting the 12 digit number at the very end of the line. (A)
# the left most digit will go from its current position to the left (B)
# if it finds a number that is larger (or equal), it will set its digit to that value (C)
#   the next digit (n+1) will change its value to the previous digit (n) was holding if its larger or equal to its (n+1) current value
# repeat this with the next digit in line but it cannot go past the index of the digit to its left.

for line in input:
    line = line.strip()

    # convert line into a list of numbers so were not working with strings the whole time
    num = []
    for i in range(len(line)):
        num.append(int(line[i]))
    joltage = num[-12:] # (A)
    # print(joltage)

    for i in range(len(num) - 13, -1, -1): # (B)
        for j in range(len(joltage)): #(C)
            if num[i] >= joltage[j]:
                num[i], joltage[j] = joltage[j], num[i] 
            else:
                break

    # the 12 batteries are picked, convert it to a base 10 number then add to total sum
    value = 0
    for i in range(len(joltage)):
        value = value * 10 + joltage[i]

    result += value

print(result)