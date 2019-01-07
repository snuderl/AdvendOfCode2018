import re
from topo import Graph


with open('input7.txt') as f:
    data = f.read().strip().split("\n")


pattern = re.compile(r"Step (\w+) must be finished before step (\w+) can begin.")

vertices = set()
d = []
for line in data:
    a, b = pattern.search(line).groups()
    d.append((a, b))
    vertices.add(a)
    vertices.add(b)

vertices = {x: i for i, x in enumerate(sorted(vertices))}
rev = {a: b for b, a in vertices.items()}

print(vertices)

g = Graph(len(vertices))
for a, b in sorted(d, reverse=True):
    print(a, b)
    g.addEdge(vertices[a], vertices[b])
print("".join(rev[x] for x in g.topologicalSort()))