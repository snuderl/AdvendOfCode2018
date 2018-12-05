with open('input5.txt') as f:
    data = f.read().strip("\n")

line = list(data[:1])
for c in data[1:]:
    if len(line) > 0:
        prev = line[-1]
        if abs(ord(prev) - ord(c)) == 32:
            line.pop()
        else:
            line.append(c)
    else:
        line.append(c)

print("Solution 1 is: %s" % len(line))

data = line
chars = set([x.lower() for x in data])
_data = data

best, character = 10**9, None
for char in chars:
    data = list(x for x in _data if char != x.lower())

    line = list(data[:1])
    for c in data[1:]:
        if len(line) > 0:
            prev = line[-1]
            if abs(ord(prev) - ord(c)) == 32:
                line.pop()
            else:
                line.append(c)
        else:
            line.append(c)

    if len(line) < best:
        best, character = len(line), char

print('Solution 2 is %s' % best)