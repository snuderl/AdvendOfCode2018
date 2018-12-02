from itertools import cycle

with open('input1.txt') as f:
  data = f.read()

parsed = []
for line in data.split("\n"):
  if line:
    print(line)
    num = int(line[1:])
    if line[0] == "-":
      num *= -1
    parsed.append(num)

print("Solution 1 is: %s" % sum(parsed))

seen = set()
c = 0
for n in cycle(parsed):
  c += n
  if c in seen:
    print("Solution 2 is: %s" % c)
    break
  seen.add(c)
