serial_number = 7857

power = [[0] * 300 for _ in range(300)]
for x in range(1, 301):
    rack_id = x + 10
    for y in range(1, 301):
        power_level = (rack_id * y + serial_number) * rack_id
        hd = (power_level % 1000) / 100
        power[x - 1][y - 1] = hd - 5


def create_sum_sum(power):
    cumulative_power = [[0] * (len(power[0]) + 1) for _ in range(len(power) + 1)]
    for x in range(len(power)):
        for y in range(len(power[x])):
            cumulative_power[x + 1][y + 1] = (
                power[x][y] +
                cumulative_power[x + 1][y] +
                cumulative_power[x][y + 1] -
                cumulative_power[x][y]
            )
    return cumulative_power


def cum_sum(x1, y1, x2, y2):
    return (
        cumulative_power[x2 + 1][y2 + 1] -
        cumulative_power[x1][y2 + 1] -
        cumulative_power[x2 + 1][y1] +
        cumulative_power[x][y]
    )


cumulative_power = create_sum_sum(power)


a = create_sum_sum([[1, 2], [3, 4]])

best_pow = 0
best_pos = None
best_k = 0

for k in range(1, 301):
    for x in range(0, 301 - k):
        for y in range(0, 301 - k):
            # s = 0
            # for i in range(3):
            #     for k in range(3):
            #         s += power[x + i][y + k]
            s = cum_sum(x, y, x + (k - 1), y + (k - 1))
            if s > best_pow:
                best_pow, best_pos, best_k = s, (x + 1, y + 1), k


print(best_pow, best_pos, best_k)
