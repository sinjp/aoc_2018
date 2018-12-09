from collections import defaultdict
from itertools import cycle
import re

from blist import blist


def play_marbles(n_players, last_marble):
    players = cycle(range(1, n_players + 1))
    marble_bag = iter(range(last_marble + 1))  # First marble is 0
    scores = defaultdict(int)

    current_pos = 0
    circle = blist([next(marble_bag)])  # 0

    for marble in marble_bag:
        player = next(players)
        if marble % 23 == 0:
            remove_pos = (current_pos - 7) % len(circle)
            scores[player] += marble + circle.pop(remove_pos)
            current_pos = remove_pos
        else:
            insert_pos = (current_pos + 2) % len(circle)
            circle.insert(insert_pos, marble)
            current_pos = insert_pos
    return max(v for v in scores.values())


with open('day9.in') as f:
    m = re.search(r'^(\d+).+?(\d+)', f.read())

# Part 1
n_players = int(m.group(1))
last_marble = int(m.group(2))
print(f'Day 9 Part 1: {play_marbles(n_players, last_marble)}')  # 383475

# Part 2
print(f'Day 9 Part 2: {play_marbles(n_players, last_marble * 100)}')  # 3148209772
