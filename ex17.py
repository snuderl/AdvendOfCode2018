import re
import sys

sys.setrecursionlimit(5000)

with open("input17.txt") as f:
    data = f.read().strip().split("\n")


regex = re.compile(r'([xy])=(\d+).*\w=(\d+)\.\.(\d+)')
max_x, min_x, max_y, min_y = -1000, 1000, -1000, 1000

clay = set()
for line in data:
    #print(line)
    c, x, y1, y2 = regex.search(line).groups()
    x, y1, y2 = int(x), int(y1), int(y2)

    if c == 'x':
        max_x = max(x, max_x)
        min_x = min(x, min_x)
        for i in range(y1, y2 + 1):
            max_y = max(i, max_y)
            min_y = min(i, min_y)
            clay.add((x, i))
    else:
        max_y = max(x, max_y)
        min_y = min(x, min_y)
        for i in range(y1, y2 + 1):
            max_x = max(i, max_x)
            min_x = min(i, min_x)
            clay.add((i, x))

min_x -= 1
max_x += 1

def moves(x, y):
    mov = [(0, 1), (-1, 0), (1, 0)]
    r = []
    for m in mov:
        arg = (x + m[0], y + m[1])
        if arg in water:
            return True

        if arg[1] <= max_y and (min_x <= arg[0] <= max_x) and arg not in clay and arg not in water:
            r.append(arg)
            water.add(arg)
    return r


def draw():
    l = [["."] * (max_x - min_x + 1) for _ in range(max_y + 1)]
    for x, y in clay:
        x = x - min_x
        l[y][x] = "#" 

    for x, y in water:
        if (x, y) in clay:
            print("error")
            sys.exit(1)
        x = x - min_x
        l[y][x] = "~" if (x + min_x, y) in stuck else "|"

    for line in l:
        print("".join(line))
    print()


def flow(x, y, moves=[-1, 1]):
    down = (x, y + 1)
    if down[1] > max_y:
        return True

    if down in water:
        if down not in stuck:
            return True

    if down not in clay:
        #print("down", down)
        water.add(down)
        flowed = flow(down[0], down[1])
        if flowed:
            return flowed

    flowed = False
    st = []
    for m in moves:
        arg = (x + m, y)
        if arg in water:
            continue
        if min_x <= arg[0] <= max_x and arg not in clay and arg not in water:
            st.append(arg)
            water.add(arg)
            flowed |= flow(arg[0], arg[1], [m])

    if not flowed:
        for arg in st:
            stuck.add(arg)
        stuck.add((x, y))
    else:
        for i in range(x + 1, max_x):
            if (i, y) in stuck:
                stuck.remove((i, y))
            else:
                break
        for i in range(x - 1, min_x, -1):
            if (i, y) in stuck:
                stuck.remove((i, y))
            else:
                break

    #draw()
    return flowed


print(max_y, min_x, max_x)

stuck = set()
water = set()
flow(500, 0)

draw()

#print(stuck)
print(len(water))