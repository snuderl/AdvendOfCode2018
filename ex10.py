import re

with open('input10.txt') as f:
    data = f.read().strip().split("\n")

regex = re.compile(r'<(.*)>.*<(.*)>')

points = []
for line in data:
    pos_str, vel_str = regex.search(line).groups()
    pos = map(int, pos_str.split(","))
    vel = map(int, vel_str.split(","))
    points.append((pos, vel))


def calculate(time, render=False):
    p = []

    min_x, max_x = 10**9, -10**9
    min_y, max_y = 10**9, -10**9
    for (x, y), (v_x, v_y) in points:
        x, y = x + (v_x * i), y + (v_y * i)
        p.append((x, y))

        min_x = min(x, min_x)
        max_x = max(x, max_x)
        min_y = min(y, min_y)
        max_y = max(y, max_y)

    if render:
        draw(min_x, max_x, min_y, max_y, p)

    bound = (max_x - min_x) + (max_y - min_y)
    return bound, p


def draw(min_x, max_x, min_y, max_y, points):
    screen = []
    for _ in range(max_y - min_y + 1):
        screen.append(["."] * (max_x - min_x + 1))

    for (x, y) in points:
        #print(x - min_x), len(screen)
        #print(y - min_y), len(screen[x - min_x])
        screen[y - min_y][x - min_x] = "#"

    for row in screen:
        print("".join(row))


for i in range(10900, 10910, 1):
    print("\n" * 10)
    print("Time to wait: ", i)
    calculate(i, True)
    a = raw_input("test")
