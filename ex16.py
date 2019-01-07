import copy


reg = [0, 0, 0, 0]


class OP:
    def __init__(self, op, i):
        self.op = op
        self.i = i

    def __call__(self, a, b, c):
        val_b = b if self.i else reg[b]
        reg[c] = self.op(reg[a], val_b)


def seti(a, b, c):
    reg[c] = a


def gtir(a, b, c):
    reg[c] = 1 if a > reg[b] else 0


def gtri(a, b, c):
    reg[c] = 1 if reg[a] > b else 0


def gtrr(a, b, c):
    reg[c] = 1 if reg[a] > reg[b] else 0


def eqir(a, b, c):
    reg[c] = 1 if a == reg[b] else 0


def eqri(a, b, c):
    reg[c] = 1 if reg[a] == b else 0


def eqrr(a, b, c):
    reg[c] = 1 if reg[a] == reg[b] else 0


operations = [
    OP(lambda x, y: x + y, False),
    OP(lambda x, y: x + y, True),
    OP(lambda x, y: x * y, False),
    OP(lambda x, y: x * y, True),
    OP(lambda x, y: x & y, False),
    OP(lambda x, y: x & y, True),
    OP(lambda x, y: x | y, False),
    OP(lambda x, y: x | y, True),
    OP(lambda x, y: x, False),
    seti,
    gtir, gtri, gtrr,
    eqir, eqri, eqrr
]


def possible_opcodes(before, after, a, b, c):
    global reg
    res = []
    for i, op in enumerate(operations):
        reg = copy.copy(before)
        op(a, b, c)
        if reg == after:
            res.append(i)
    return res    


with open('input16.txt') as f:
    lines, program = f.read().split("\n\n\n")


it = iter(lines.strip().split("\n"))
import re
i = 0

constraints = {i: set(range(len(operations))) for i in range(len(operations))}

for line in it:
    print(line)
    before = map(int, re.search(r"\[(.*)\]", line).groups()[0].split(", "))
    opcode, a, b, c = map(int, next(it).split(" "))
    v = next(it)
    print(v)
    after = map(int, re.search(r"\[(.*)\]", v).groups()[0].split(", "))
    try:
        next(it)
    except StopIteration:
        pass

    possible = possible_opcodes(before, after, a, b, c)
    constraints[opcode] = constraints[opcode] & set(possible)
    if len(possible) >= 3:
        i += 1
print(i)
#print(constraints)


def solve(constraints):
    for key, value in constraints.items():
        if len(value) == 1:
            rem = next(iter(value))
            for k, v in constraints.items():
                if k != key and rem in v:
                    v.remove(rem)
    return constraints

for _ in range(20):
    constraints = solve(constraints)
constraints = {k: next(iter(v)) for k, v in constraints.items()}
print(constraints)

reg = [0, 0, 0, 0]
for line in program.strip().split("\n"):
    opcode, a, b, c = map(int, line.split(" "))
    op = operations[constraints[opcode]]
    op(a, b, c)
print(reg)