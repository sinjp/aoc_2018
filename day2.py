import difflib
from itertools import combinations

with open('day2.in') as f:
    box_ids = [r.strip() for r in f.readlines()]

# Part 1
two = set()
three = set()
for box_id in box_ids:
    for c in box_id:
        if box_id.count(c) == 2:
            two.add(box_id)
        elif box_id.count(c) == 3:
            three.add(box_id)
print(f'Day 2 Part 1: {len(two) * len(three)}')  # 7221

# Part 2
id1 = id2 = ''
for box1, box2 in combinations(box_ids, 2):
    ratio = difflib.SequenceMatcher(None, box1, box2).ratio()
    if ratio == (len(box1)-1)/len(box1):
        id1, id2 = box1, box2
        break
# Unpack and find common characters
common = ''
for c in id1:
    if c in id2:
        common += c
print(f'Day 2 Part 2: {common}')  # mkcdflathzwsvjxrevymbdpoq
