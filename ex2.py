from collections import defaultdict

with open('input2.txt') as f:
    data = f.read().split("\n")


twos = 0
threes = 0
for line in data:
    c = defaultdict(int)
    for char in line:
        c[char] += 1

    two_ = 0
    threes_ = 0
    for v in c.values():
        if v == 2:
            two_ = 1
        if v == 3:
            threes_ = 1
    twos += two_
    threes += threes_

print("Solution 1: %s" % (twos * threes))

sol = None

for i, line in enumerate(data[:-1]):
    if sol:
        break
    for line2 in data[i + 1:]:
        if sol:
            break

        if len(line) != len(line2):
            break

        d = 0
        for a, b in zip(line, line2):
            if a != b:
                d += 1
                if d > 1:
                    break
        if d == 1:
            sol = line, line2
            break


word = "".join([a for a, b in zip(*sol) if a == b])
print(len(word), len(line), d)
print("Solution 2 is : %s" % word)
