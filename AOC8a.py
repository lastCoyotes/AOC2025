# turn puzzle input into list of tuples 
with open('input/8.txt') as file:
    data = [tuple([int(x) for x in data.strip().split(',')]) for data in file]
# print(data)

# implementing Kruskal's algorithm to make a minimum spanning forest/tree

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

# form the first 1000 pairs
junctions = []
for _ in range(1000):
    best = indices[_]
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

# sort the connected length of junctions
s = sorted([len(x) for x in junctions])
# the last three elements are the 3 largest trees
total = s[-1] * s[-2] * s[-3]
print(total)