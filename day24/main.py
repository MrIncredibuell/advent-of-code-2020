def parse_line(line):
    steps = []
    i = 0
    while i < len(line):
        if line[i] in ('e', 'w'):
            steps.append(line[i])
            i += 1
        else:
            steps.append(line[i:i+2])
            i += 2
    return steps

data = [parse_line(line) for line in open('data.txt').read().split('\n')]

def initialize(data):
    flipped = set([])
    for path in data:
        x, y = 0.0, 0.0
        for step in path:
            if step == 'e':
                x += 1
            elif step == 'w':
                x -= 1
            elif step == 'ne':
                x += 0.5
                y += 0.5
            elif step == 'nw':
                x -= 0.5
                y += 0.5
            elif step == 'se':
                x += 0.5
                y -= 0.5
            elif step == 'sw':
                x -= 0.5
                y -= 0.5
        if (x,y) in flipped:
            flipped.remove((x,y))
        else:
            flipped.add((x,y))
    return flipped

def get_neighbors(tile):
    (x,y) = tile
    return {
        (x - 1, y),
        (x + 1, y),
        (x + 0.5, y + 0.5),
        (x + 0.5, y - 0.5),
        (x - 0.5, y + 0.5),
        (x - 0.5, y - 0.5),
    }

def part1(data):
    flipped = initialize(data)
    return len(flipped)

def part2(data):
    flipped = initialize(data)
    for i in range(100):
        new_flipped = set()
        for tile in flipped:
            neighbors = get_neighbors(tile)
            if len(neighbors & flipped) in (1, 2):
                new_flipped.add(tile)
            for neighbor in neighbors - flipped:
                others = get_neighbors(neighbor)
                if len(others & flipped) == 2:
                    new_flipped.add(neighbor)
        flipped = new_flipped
    return len(flipped)


print(part1(data))
print(part2(data))