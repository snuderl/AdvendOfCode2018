import copy


with open('input18.txt') as f:
    data = f.read().strip().split("\n")

grid = [list(line) for line in data]


def neighouring(grid, x, y):
    trees, lumber = 0, 0
    for yy in range(-1, 2):
        yyy = y + yy
        if yyy < 0 or yyy >= len(grid):
            continue

        g = grid[yyy]

        for xx in range(-1, 2):
            xxx = x + xx
            if xxx < 0 or xxx >= len(g):
                continue
            if xx == 0 and yy == 0:
                continue

            if g[xxx] == "|":
                trees += 1
            if g[xxx] == "#":
                lumber += 1
    return trees, lumber


def step(grid):
    max_y, max_x = len(grid), len(grid[0])

    new_grid = copy.deepcopy(grid)

    for y in range(max_y):
        g = new_grid[y]
        for x in range(max_x):
            current = grid[y][x]

            trees, lumber = neighouring(grid, x, y)
            if current == ".":
                if trees >= 3:
                    g[x] = "|"
            elif current == "|":
                if lumber >= 3:
                    g[x] = "#"
            else:
                if not (lumber >= 1 and trees >= 1):
                    g[x] = "."
    return new_grid


def counts(grid):
    trees, lumber = 0, 0
    for line in grid:
        for c in line:
            if c == "|":
                trees += 1
            if c == "#":
                lumber += 1
    return trees * lumber


state = {}


def save(grid, i):
    s = ""
    for line in grid:
        s += "".join(line)
    if s in state:
        return True, i - state[s][0]
    state[s] = i, counts(grid)
    return None, None


TARGET = 1000000000

for i in range(1000):
    grid = step(grid)

    found, period = save(grid, i)
    if found:
        t = TARGET - (i - period)
        print(t, i)
        t = t % period
        t = t + (i - period)
        print(t)
        print([(x, y) for x, y in state.values() if x == t])
        break
