data = [int(x) for x in open('data.txt').read().split('\n')]

def part1(data):
    for i, x in enumerate(data):
        for y in data[i+1:]:
            if x + y == 2020:
                return x * y

def part2(data):
    for i, x in enumerate(data):
        for j, y in enumerate(data[i+1:]):
            for z in data[i+j+1:]:
                if x + y + z == 2020:
                    return x * y * z

print(part1(data))
print(part2(data))