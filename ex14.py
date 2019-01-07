line = list(map(int, "37"))
target = list(map(int, "939601"))
l_target = len(target)
print(target)

import time
start = time.time()

p1, p2 = 0, 1
line_l = 2
while True:
    c1 = line[p1]
    c2 = line[p2]
    new = c1 + c2
    if new >= 10:
        line.append(new // 10)
        line_l += 1
        if line[-l_target:] == target:
            break
        line.append(new % 10)
        line_l += 1
    else:
        line.append(new)
        line_l += 1
    p1 = (p1 + c1 + 1) % line_l
    p2 = (p2 + c2 + 1) % line_l

    # if len(line) < l_target:
    #     found = True
    #     for i in range(1, l_target + 1):
    #         if target[-i] != line[-i]:
    #             found = False
    #             break
    #     if found:
    #         break

    if line[-l_target:] == target:
        break

print(time.time() - start)
print(len(line) - len(target))

s = 939601
print("".join(map(str, line[s:(s+10)])))
