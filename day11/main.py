from collections import defaultdict

data = open('data.txt').read().split('\n')
grid = {}

for y, row in enumerate(data):
    for x, seat in enumerate(row):
        grid[(x,y)] = seat

data = grid

def neighbors(grid, x, y):
    neighbs = []
    for i in range(x -1, x + 2):
        for j in range(y - 1, y + 2):
            if (i, j) == (x,y):
                continue
            neighbs.append(grid.get((i,j), '.'))
    return neighbs

def walk(grid, x, y, run, rise):
    (new_x, new_y) = (x + run, y + rise)
    while (new_x, new_y) in grid:
        if grid[(new_x, new_y)] != '.':
            return (new_x, new_y)
        (new_x, new_y) = (new_x + run, new_y + rise)
    return None

def find_neighbors(grid, x, y):
    width, height = sorted(grid.keys())[-1]
    neighbs = []
    for (run, rise) in [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0,),
        (1, 1),
    ]:
        neighbs.append(walk(grid, x, y, run, rise))
    return [n for n in neighbs if n]

def find_all_neighbors(grid):
    ns = {}
    for x, y in grid.keys():
        ns[x,y] = find_neighbors(grid, x, y)
    return ns

def part1(grid):
    changed = True
    while changed:
        changed = False
        next_grid = {}
        for (x,y), seat in grid.items():
            neighbs = neighbors(grid, x, y)
            if seat == 'L' and neighbs.count('#') == 0:
                next_grid[(x,y)] = '#'
                changed = True
            elif seat == '#' and neighbs.count('#') >= 4:
                next_grid[(x,y)] = 'L'
                changed = True
            else:
                next_grid[(x,y)] = seat
        grid = next_grid

    return [v for v in grid.values()].count('#')


def part2(grid):
    ns = find_all_neighbors(grid)
    changed = True
    while changed:
        changed = False
        next_grid = {}
        for (x,y), seat in grid.items():
            neighbs = [grid[n] for n in ns[x,y]]
            if seat == 'L' and neighbs.count('#') == 0:
                next_grid[(x,y)] = '#'
                changed = True
            elif seat == '#' and neighbs.count('#') >= 5:
                next_grid[(x,y)] = 'L'
                changed = True
            else:
                next_grid[(x,y)] = seat
        grid = next_grid

    return [v for v in grid.values()].count('#')

print(part1(data))
print(part2(data))