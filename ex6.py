with open('input6.txt') as f:
    data = list([map(int, x.split(", ")) for x in f.read().strip().split("\n")])

max_x = max(data, key=lambda x: x[0])[0] + 1
max_y = max(data, key=lambda x: x[1])[1] + 1

grid = []
for y in range(max_y):
    grid.append([None] * max_x)

for i, (x, y) in enumerate(data):
    for a in range(max_y):
        for b in range(max_x):
            distance = abs(y - a) + abs(x - b)
            if grid[a][b] is None:
                grid[a][b] = (i, distance)
            else:
                _, d = grid[a][b]
                if distance < d:
                    grid[a][b] = (i, distance)
                if distance == d:
                    grid[a][b] = (None, distance)

counts = {}
for a in range(max_y):
    for b in range(max_x):
        val, dist = grid[a][b]
        if val:
            if a == 0 or b == 0:
                counts[val] = None
            else:
                if counts.get(val, 0) is not None:
                    counts[val] = counts.get(val, 0) + 1

print(max(counts.items(), key=lambda x: x[1]))

grid = []
for y in range(max_y):
    grid.append([0] * max_x)

for a in range(max_y):
    for b in range(max_x):
        d = grid[a][b]
        for i, (x, y) in enumerate(data):
            distance = abs(y - a) + abs(x - b)
            d += distance
            if d >= 10000:
                break
        grid[a][b] = d

d = 0
for a in range(max_y):
    for b in range(max_x):
        if grid[a][b] < 10000:
            d += 1
print(d)
