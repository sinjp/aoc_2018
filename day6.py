from collections import Counter
from itertools import chain, product

with open('day6.in') as f:
    points = [eval(line) for line in f]

# Simplify origin
min_x = min(p[0] for p in points)
min_y = min(p[1] for p in points)
norm_points = [(x - min_x, y - min_y) for x, y in points]
max_x = max(p[0] for p in norm_points)
max_y = max(p[1] for p in norm_points)

# Create grid
grid = [[None for y in range(max_y)] for x in range(max_x)]


def dist(p1, p2):
    """Manhatten distance."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


# Check distance to points from each coordinate
for ix, iy in product(range(max_x), range(max_y)):
    dists = []
    for p in norm_points:
        dists.append((p, dist(p, (ix, iy))))
    dists.sort(key=lambda x: x[1])
    # Check closest 2 points aren't the same distance away
    if dists[0][1] != dists[1][1]:
        grid[ix][iy] = dists[0][0]
# Find biggest non infinite area i.e. most commonly closest point
counts = Counter(chain.from_iterable(grid))
for p, count in counts.most_common():
    # Find finite areas only i.e. not edge points
    if 0 < p[0] < max_x and 0 < p[1] < max_y:
        print(f'Day 6 Part 1: {count}')  # 5975
        break

# Part 2
grid = [[0 for y in range(max_y)] for x in range(max_x)]
for ix, iy in product(range(max_x), range(max_y)):
    total_dist = 0
    for point in norm_points:
        total_dist += dist(point, (ix, iy))
    if total_dist < 10000:
        grid[ix][iy] = 1
print(f'Day 6 Part 2: {sum(chain.from_iterable(grid))}')  # 38670
