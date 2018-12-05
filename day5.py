with open('day5.in') as f:
    polymer = f.read().strip()


def react(polymer):
    for c in 'abcdefghijklmnopqrstuvwxyz':
        r = c + c.upper()
        polymer = polymer.replace(r, '').replace(r[::-1], '')
    return polymer


def run_reaction(polymer):
    """Python didn't like the recursive solution."""
    prev_polymer = None
    while polymer != prev_polymer:
        prev_polymer = polymer
        polymer = react(polymer)
    return polymer


reacted_polymer = run_reaction(polymer)
print(f'Day 5 Part 1: {len(reacted_polymer)}')  # 9238

# Part 2
lengths = {}
for s in 'abcdefghijklmnopqrstuvwxyz':
    polymer = reacted_polymer.replace(s, '').replace(s.upper(), '')
    polymer = run_reaction(polymer)
    lengths[s] = len(polymer)

min_length = min(v for v in lengths.values())
print(f'Day 5 Part 2: {min_length}')  # 4052
