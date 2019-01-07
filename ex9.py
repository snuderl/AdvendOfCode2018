import re
from collections import defaultdict

with open('input9.txt') as f:
    line = f.read().strip()

players, last_marble = map(int, re.search(r'(\d+).*worth (\d+)', line).groups())


class Node:
    def __init__(self, prev, next, val):
        self.next = next
        self.prev = prev
        self.val = val


class LL:
    def __init__(self, val=0):
        self.head = Node(None, None, val)
        self.head.prev = self.head
        self.head.next = self.head

    def pos2(self, val):
        c = self.head.next
        node = Node(c, c.next, val)
        node.prev.next = node
        node.next.prev = node
        self.head = node

    def remove7(self):
        m = self.head
        for _ in range(7):
            m = m.prev
        self.head = m.next
        self.head.prev = m.prev
        self.head.prev.next = m.next
        return m.val


player = -1
val = 0
marbles = [0]
current = 0

scores = defaultdict(int)

linkedlist = LL()
while val != last_marble:
    player = (player + 1) % players
    val += 1

    if val % 23 == 0:
        removed = linkedlist.remove7()
        scores[player] += val + removed
        #print(player, val)
    else:
        linkedlist.pos2(val)

print(max(scores.items(), key=lambda x: x[1]))
