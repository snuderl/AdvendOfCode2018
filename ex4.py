import re
from collections import defaultdict

with open('input4.txt') as f:
    data = f.read().split("\n")


pattern = re.compile(r'(\d+)-(\d+)-(\d+) (\d+):(\d+)] (.*)$')
guard_id = re.compile(r'#(\d+)')

guards = defaultdict(int)
sleep_map = defaultdict(lambda: [0] * (60 * 60))

chronological = sorted([x for x in data if x])
iterator = iter(chronological)
for line in iterator:
    year, month, day, _, minute, action = pattern.search(line).groups()
    if "#" in action:
        guard = guard_id.search(action).groups()[0]
        continue

    if action == 'falls asleep':
        _, _, _, _, minute2, action2 = pattern.search(next(iterator)).groups()
        assert action2 == "wakes up"

        for i in range(
          int(minute),
          int(minute2),
        ):
            sleep_map[guard][i] += 1
    else:
      raise Exception("error")

most_asleep, schedule = max(sleep_map.items(), key=lambda x: sum(x[1]))
minute, times = max(enumerate(schedule), key=lambda x: x[1])
print("Solution #1 is %s" % (int(most_asleep) * minute))

times_max = -1
best_guard = None
for guard, schedule in sleep_map.items():
    times = max(schedule)
    if times > times_max:
        times_max = times
        best_guard = guard, schedule
print("Solution #2 is %s" % (int(best_guard[0]) * best_guard[1].index(times_max)))
