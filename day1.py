from itertools import cycle

with open('day1.in') as f:
    freq_changes = [int(f) for f in f.readlines()]

# Part 1
frequency = sum(freq_changes)
print(f'Day 1 Part 1: {frequency}')  # 497

# Part 2
frequency = 0
history = {frequency}
for change in cycle(freq_changes):
    frequency += change
    if frequency in history:
        print(f'Day 1 Part 2: {frequency}')  # 558
        break
    else:
        history.add(frequency)
