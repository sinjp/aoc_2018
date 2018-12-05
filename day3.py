import re

with open('day3.in') as f:
    claim_lines = [r.strip() for r in f]


class Claim:
    def __init__(self, claim_string):
        m = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', claim_string)
        self.claim_id = int(m.group(1))
        self.margin_left = int(m.group(2))
        self.margin_top = int(m.group(3))
        self.width = int(m.group(4))
        self.height = int(m.group(5))


# Part 1
claims = [Claim(r) for r in claim_lines]
fabric = [[0 for x in range(1000)] for y in range(1000)]
for claim in claims:
    for x in range(claim.width):
        for y in range(claim.height):
            fabric[claim.margin_left + x][claim.margin_top + y] += 1
overlap = 0
for y in fabric:
    for x in y:
        if x > 1:
            overlap += 1
print(f'Day 3 Part 1: {overlap}')  # 116140


# Part 2
# Naive search
for claim in claims:
    overlap = 0
    for x in range(claim.width):
        for y in range(claim.height):
            if fabric[claim.margin_left + x][claim.margin_top + y] != 1:
                overlap += 1
                break
        if overlap > 0:
            break
    else:
        print(f'Day 3 Part 2: {claim.claim_id}')  # 574
