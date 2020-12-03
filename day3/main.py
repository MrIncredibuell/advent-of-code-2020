data = open('data.txt').read().split('\n')

def part1(data, run=3, rise=1):
    x = 0
    count = 0
    width = len(data[0])
    for y in range(1, len(data), rise):
        x = (x + run) % width 
        if data[y][x] == '#':
            count += 1
    return count



def part2(data):
    result = 1
    for (run, rise) in [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]:
        result *= part1(data, run=run, rise=rise)
    return result

print(part1(data))
print(part2(data))