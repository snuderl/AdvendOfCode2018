import re

with open('input12.txt') as f:
    data = f.read().strip().split("\n")

initial, lines = data[0], data[2:]
initial = re.search(r'state: (.*)', initial).groups()[0]


parser = re.compile(r'(.{5}) => (.)')

patterns = []
for line in lines:
    pattern, result = parser.search(line).groups()
    if result == "#":
        patterns.append(pattern)


def calc(current):
    new = ["."] * len(current)
    for i in range(2, len(current) - 2):
        sub = current[i: i + 5]
        for p in patterns:
            if sub == p:
                new[i + 2] = "#"
    new = "".join(new)
    return new


def score(curr):
    return sum(i for i, c in enumerate(current, -pad) if c == "#")

pad = 1000
score_prev = 0
diff = 0
current = "." * pad + initial + "." * pad
visited = {"".join(current): 0}
for o in range(1000):
    if diff == 62:
        score_prev += 62
        continue
    print("".join(current).strip("."))
    new = calc(current)
    if new in visited:
        print(o, "break", visited[new])
        break
    visited[new] = len(visited)
    current = new
    s = score(current)
    diff = s - score_prev
    print(o, s, diff)
    score_prev = s

s = score(current)
print(s)

# At iteration 89 score is 5873 and after that score increases by 62 per round
print(5873 + (50000000000 - 90) * 62)
