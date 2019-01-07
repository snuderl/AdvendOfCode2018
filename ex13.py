import sys


with open('input13.txt') as f:
    data = list(list(line) for line in f.read().split("\n"))

carts = {}
for row in range(len(data)):
    r = data[row]
    for col in range(len(r)):
        track = r[col]
        if track in ['v', '<', '>', '^']:
            carts[(row, col)] = track, 0


def turn(direction, i):
    left = {
        '>': '^',
        '^': '<',
        '<': 'v',
        'v': '>',
    }
    right = {v: k for k, v in left.items()}

    if i == 1:
        return direction
    if i == 0:
        return left[direction]
    if i == 2:
        return right[direction]

print ("starting")
print(carts)

time = 1
while True:
    if len(carts) <= 1:
        break
    _carts = sorted(carts.items())
    crashed = set()
    new_carts = {}
    for pos, (direction, i) in _carts:
        if pos in crashed:
            continue
        #print(pos, direction)
        x, y = pos
        if direction == '>':
            y += 1
            track = data[x][y]
            if track == '\\':
                direction = "v"
            if track == '/':
                direction = "^"
            if track == "+":
                direction = turn(direction, i)
                i = (i + 1) % 3

        elif direction == "<":
            y -= 1
            track = data[x][y]
            if track == '/':
                direction = "v"
            if track == '\\':
                direction = "^"
            if track == "+":
                direction = turn(direction, i)
                i = (i + 1) % 3

        elif direction == "^":
            x -= 1
            track = data[x][y]
            if track == '/':
                direction = ">"
            if track == '\\':
                direction = "<"
            if track == "+":
                direction = turn(direction, i)
                i = (i + 1) % 3

        elif direction == "v":
            x += 1
            track = data[x][y]
            if track == '/':
                direction = "<"
            if track == '\\':
                direction = ">"
            if track == "+":
                direction = turn(direction, i)
                i = (i + 1) % 3

        new_pos = (x, y)
        if new_pos in carts or new_pos in new_carts:
            print("crash", new_pos, time)
            new_carts.pop(new_pos, None)
            crashed.add(new_pos)
            continue

        new_carts[new_pos] = (direction, i)
        carts.pop(pos)

    carts = new_carts
    #print(carts)
    time += 1
    #if time == 10:
    #    break

print(carts)
