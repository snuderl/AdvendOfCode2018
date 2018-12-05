import re

LINE_REGEX = re.compile(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)")

with open('input3.txt') as f:
    data = f.read().split("\n")

square = []
for _ in range(1000):
    square.append([0] * 1000)

for line in data:
    _, x, y, width, height = map(int, LINE_REGEX.search(line).groups())

    for i in range(width):
        for k in range(height):
            square[x + i][y + k] += 1

c = 0
for row in square:
    c += sum(1 for x in row if x > 1)

print("Solution 1 is %s" % c)

square = []
for _ in range(1000):
    square.append([0] * 1000)

for line in data:
    _id, x, y, width, height = map(int, LINE_REGEX.search(line).groups())

    overlap = False
    for i in range(width):
        for k in range(height):
            if square[x + i][y + k] != 0:
                square[x + i][y + k] = -1
            else:
                square[x + i][y + k] = _id

for line in data:
    _id, x, y, width, height = map(int, LINE_REGEX.search(line).groups())

    same = True
    for i in range(width):
        for k in range(height):
            if square[x + i][y + k] != _id:
                same = False
                break
    if same:
        print("Solution 2 is %s" % _id)
        break
