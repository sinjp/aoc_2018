from collections import defaultdict
import re

with open('day4.in') as f:
    logs = [r[1:].strip().split('] ') for r in f]
logs.sort()

# Build asleep / awake timelines for each night's shift
guards_asleep = defaultdict(int)
guard = asleep_time = None
for ix, (dt, action) in enumerate(logs):
    time = int(dt[-2:])
    if 'begins shift' in action:
        guard = int(re.search(r'#(\d+)', action).group(1))
    elif 'falls asleep' in action:
        asleep_time = time
    elif 'wakes up' in action:
        for m in range(asleep_time, time):
            guards_asleep[(guard, m)] += 1

# Find guard asleep the most
guard_totals = defaultdict(int)
for (guard, m), total in guards_asleep.items():
    guard_totals[guard] += total
sleepiest_guard = max(guard_totals, key=guard_totals.get)

# Find minute sleepiest guard was asleep the most
minutes = {}
for (guard, m), total in guards_asleep.items():
    if guard == sleepiest_guard:
        minutes[m] = total
sleepiest_minute = max(minutes, key=minutes.get)

print(f'Day 4 Part 1: {sleepiest_guard * sleepiest_minute}')  # 103720

# Part 2
freq_asleep_guard, freq_asleep_minute = max(guards_asleep, key=guards_asleep.get)
print(f'Day 4 Part 2: {freq_asleep_guard * freq_asleep_minute}')  # 110913
