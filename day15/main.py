from collections import defaultdict

data = [int(x) for x in open('data.txt').read().split(',')]

def find_last(l, v, i):
    initial = i
    while  l[i] != v:
        if i == 0:
            return 0
        i -= 1
    return initial - i + 1


def part1(data):
    SIZE = 2020
    numbers = [0] * SIZE
    for i, n in enumerate(data):
        numbers[i] = n
    i += 1
    while i < SIZE:
        previous = numbers[i - 1]
        numbers[i] = find_last(numbers, previous, i - 2)
        i += 1
    return numbers[-1]

def part2(data):
    SIZE = 30000000
    seen = defaultdict(list)
    for i, n in enumerate(data):
        seen[n].append(i)
    i += 1
    while i < SIZE:
        last_seen = seen[n][:-1]
        if len(last_seen) == 0:
            n = 0
        else:
            n = i - 1 - last_seen[-1]
        seen[n] = seen[n][-1:] + [i]
        i += 1
    return n

print(part1(data))
print(part2(data))