from collections import OrderedDict
import re

with open('day7.in') as f:
    steps = []
    step_ids = set()  # A-Z
    for line in f:
        m = re.search(r'^Step ([A-Z]) must be finished before step ([A-Z]) can begin', line)
        req, step = m.groups()
        steps.append((step, req))
        step_ids.add(step)
        step_ids.add(req)

# Build step requirements
step_reqs = OrderedDict((step, []) for step in sorted(step_ids))
for step, req in steps:
    step_reqs[step].append(req)

order = ''
while step_reqs:
    for step, reqs in step_reqs.items():
        if not reqs:
            # No requirements left, step can be completed and removed as a prerequisite
            for s in step_reqs:
                try:
                    step_reqs[s].remove(step)
                except ValueError:
                    continue
            order += step
            step_reqs.pop(step)
            break  # Maintain alphabetical order

print(f'Day 7 Part 1: {order}')  # LFMNJRTQVZCHIABKPXYEUGWDSO


# Part 2
# Reset step requirements
step_reqs = OrderedDict((step, []) for step in sorted(step_ids))
for step, req in steps:
    step_reqs[step].append(req)

# Generate step timings
timings = {}
t = 60
for s in step_reqs:
    t += 1
    timings[s] = t

# Initialise workers
available = ['elf' for _ in range(5)]
working = []

# Simulate time
sec = 0
while step_reqs:
    # Start available steps with available elves
    for step, reqs in step_reqs.items():
        # Ignore steps already underway
        if step in [w['step'] for w in working]:
            continue
        if (not reqs) and available:
            # No requirements left, step can be started
            available.pop()
            working.append({'step': step, 'time_left': timings[step]})

    # Finish workers
    # Loop backwards to allow safe working list deletions
    for i, _ in reversed(list(enumerate(working))):
        working[i]['time_left'] -= 1
        if working[i]['time_left'] == 0:
            # Remove from other step's prerequisites
            for step in step_reqs:
                try:
                    step_reqs[step].remove(working[i]['step'])
                except ValueError:
                    continue
            # Remove completed step
            step_reqs.pop(working[i]['step'])
            # Move worker to available
            working.remove(working[i])
            available.append('elf')
    sec += 1

print(f'Day 7 Part 2: {sec}')  # 1180
