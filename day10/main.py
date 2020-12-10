data = [int(x) for x in open('data.txt').read().split('\n')]

def part1(data):
    data = sorted([0] + data)
    threes = 1
    ones = 0

    for index, value in enumerate(data[:-1]):
        diff = data[index + 1] - value
        if diff == 1:
            ones += 1
        elif diff == 3:
            threes += 1
    return ones * threes

def part2(data):
    data = sorted(data)
    allowed = set(data)
    path_counts = [0] * (data[-1] + 1)
    for i in [1,2,3]:
        if i in data[:3]:
            path_counts[i] = 1 + sum(path_counts[0:i])
    for i in range(4, data[-1] + 1):
        if i in allowed:
            path_counts[i] = sum([path_counts[i - j] for j in range(1, 4)])

    return path_counts[data[-1]]

print(part1(data))
print(part2(data))