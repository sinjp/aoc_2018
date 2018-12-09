with open('day8.in') as f:
    numbers = [int(n) for n in f.read().split()]


# Solution by sciyoshi
# https://www.reddit.com/r/adventofcode/comments/a47ubw/2018_day_8_solutions/ebc7ol0
def parse(data):
    children, metas = data[:2]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(children):
        total, score, data = parse(data)
        totals += total
        scores.append(score)

    totals += sum(data[:metas])

    if children == 0:
        return (totals,
                sum(data[:metas]),
                data[metas:])
    else:
        return (totals,
                sum(scores[k - 1] for k in data[:metas] if 0 < k <= len(scores)),
                data[metas:])


total, value, remaining = parse(numbers)

print(f'Day 8 Part 1: {total}')
print(f'Day 8 Part 2: {value}')
