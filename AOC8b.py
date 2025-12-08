# turn puzzle input into list of tuples 
with open('input/8.txt') as file:
    data = [tuple([int(x) for x in data.strip().split(',')]) for data in file]
# print(data)

# implementing Kruskal's algorithm to make a minimum spanning forest/tree
# the only different in part 2 is to keep forming connections until a circuit is made.

# sort the indices by distance
indices = []
for i in range(len(data)):
    for j in range(i+1, len(data)):
        xx = data[i][0] - data[j][0]
        yy = data[i][1] - data[j][1]
        zz = data[i][2] - data[j][2]
        distance = xx*xx + yy*yy + zz*zz
        indices.append([i, j, distance])
indices.sort(key = lambda s: s[2])

junctions = []
for index in range(len(indices)):
    best = indices[index]
    a = data[best[0]]
    b = data[best[1]]
    aIndex, bIndex = -1, -1
    for i, junction in enumerate(junctions):
        if a in junction:
            aIndex = i
        if b in junction:
            bIndex = i
    if aIndex == -1 and bIndex == -1:
        junctions.append({a, b})
    elif aIndex == -1:
        junctions[bIndex].add(a)
    elif bIndex == -1:
        junctions[aIndex].add(b)
    elif aIndex != bIndex:
        for bb in junctions[bIndex]:
            junctions[aIndex].add(bb)
        del junctions[bIndex]

    # break the moment a circuit is formed
    if len(junctions) == 1 and len(junctions[0]) == len(data):
        print(a[0] * b[0])
        break