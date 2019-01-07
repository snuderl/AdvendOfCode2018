with open('input8.txt') as f:
    nums = list(map(int, f.read().strip().split(" ")))


totalSum = 0


def process():
    child, meta = nums.pop(0), nums.pop(0)
    l = [process() for _ in range(child)]

    metas = []
    for _ in range(meta):
        metas.append(nums.pop(0))

    global totalSum
    totalSum += sum(metas)

    if child == 0:
        return sum(metas)
    else:
        return sum(l[m - 1] for m in metas if (m - 1) < len(l))


print(process())
print(totalSum)
