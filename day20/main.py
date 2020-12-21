import math
from collections import defaultdict
data = open('data.txt').read().replace('\r', '').split('\n\n')
tiles = {}
for t in data:
    rows = t.split('\n')
    tiles[int(rows[0].replace('Tile ', '').replace(':', ''))] = rows[1:]

def rotate(tile):
    new_tile = []
    for i in range(len(tile)):
        row = ''
        for j in range(len(tile)):
            row += tile[len(tile) -1 - j][i]
        new_tile.append(row)
    return new_tile

def flip_horizonatally(tile):
    return [row[::-1] for row in tile]

def orientations(tile):
    n = tile[:]
    for i in range(4):
        n = rotate(n)
        yield n

    n = flip_horizonatally(n)
    for i in range(4):
        n = rotate(n)
        yield n

def get_sides(tile):
    return (
        tile[0],
        ''.join([r[0] for r in tile]),
        tile[-1],
        ''.join([r[-1] for r in tile]),
    )

class PlacedTile:
    def __init__(self, tid, content):
        self.tid = tid
        (
            self.north,
            self.west,
            self.south,
            self.east,
        ) = get_sides(content)
        self.content = content

    def __str__(self):
        return  f'{self.tid}:{self.content}'


seen = set()


class Layout:
    def __init__(self, tiles, sides, grid = None):
        self.tiles = tiles
        self.sides = sides
        self.size = int(math.sqrt(len(tiles)))
        self.unplaced_tiles = set([tid for tid in tiles.keys()])
        self.placed_tiles = set([])
        self.grid = grid or {}

    def get_placeable_squares(self):
        for i in range(self.size):
            for j in range(self.size):
                if (i,j) not in self.grid and (
                    (i, j-1) in self.grid or (i-1, j) in self.grid()):
                    yield (i, j)
    
    def get_candidates(self):
        candidates = []
        for i in range(self.size):
            for j in range(self.size):
                if (i,j) not in self.grid and (
                    (i, j-1) in self.grid or 
                    (i-1, j) in self.grid
                ):
                    possibles = set([])
                    if (i, j-1) in self.grid:
                        neighbor = self.grid[(i, j-1)]
                        possibles |= self.sides[neighbor.south]
                        possibles |= self.sides[neighbor.south[::-1]]
                    if (i-1, j) in self.grid:
                        neighbor = self.grid[(i-1, j)]
                        possibles |= self.sides[neighbor.east]
                        possibles |= self.sides[neighbor.east[::-1]]
                    possibles -= self.placed_tiles
                    if len(possibles) == 0:
                        raise Exception(f'OH NO, {i}, {j}')
                    
                    candidates.append(((i, j), possibles))


        return candidates

    def place_tile(self, location, tid, content):
        placed = PlacedTile(tid, content)
        self.grid[location] = placed
        self.placed_tiles.add(tid)
        self.unplaced_tiles.discard(tid)

    def fill_in(self):
        if len(self.grid) == self.size**2:
            return self
        try:
            candidates = self.get_candidates()
        except:
            return None
        for (i,j), tids in candidates:
            for tid in tids:
                content = self.tiles[tid]
                for orientation in orientations(content):
                    north, west, south, east = get_sides(orientation)
                    if (i, j-1) in self.grid and self.grid[(i, j-1)].south != north:
                        continue
                    if (i-1, j) in self.grid and self.grid[(i-1, j)].east != west:
                        continue
                    r = self.recurse((i,j), tid, orientation)
                    if r is not None:
                        return r
        return None
    
    def __str__(self):
        return str({k: str(v) for k,v in sorted(self.grid.items())})

    def remove_borders(self):
        grid = []
        for row in range(self.size):
            for subrow in range(1, 9):
                s = []
                for col in range(self.size):
                    s += self.grid[col, row].content[subrow][1:-1]
                grid.append(s)
        return grid

    def recurse(self, location, tid, content):
        l = Layout(self.tiles, self.sides, grid={**self.grid})
        l.placed_tiles = {*self.placed_tiles}
        l.unplaced_tiles = {*self.unplaced_tiles}
        l.place_tile(location, tid, content)
        if str(l) in seen:
            return
        seen.add(str(l))
        return l.fill_in()

def find_solution(tiles):
    sides = defaultdict(set)
    for tid, tile in tiles.items():
        sides[tile[0]].add(tid)
        sides[''.join([r[0] for r in tile])].add(tid)
        sides[tile[-1]].add(tid)
        sides[''.join([r[-1] for r in tile])].add(tid)

    sorted_tiles = []

    for tid, content in tiles.items():
        c = 0
        for s in get_sides(content):
            c += len(sides[s] - {tid})
            c += len(sides[s[::-1]] - {tid})
        sorted_tiles.append((c, tid))
    sorted_tiles.sort()

    for _, tid in sorted_tiles:
        content = tiles[tid]
        for orientation in orientations(content):
            l = Layout(tiles, sides)
            l.place_tile((0,0), tid, orientation)
            result = l.fill_in()
            if result is not None:
                return result


def part1(tiles):
    result = find_solution(tiles)
    for i in range(result.size):
        print([result.grid[(i,j)].tid for j in range(result.size)])

    return result.grid[0, 0].tid * result.grid[0, result.size - 1].tid * result.grid[result.size - 1, 0].tid * result.grid[result.size - 1, result.size - 1].tid

SEAMONSTER = '''                  #\n#    ##    ##    ###\n #  #  #  #  #  #   '''
SEAMONSTER_OFFSETS = []
for j, row in enumerate(SEAMONSTER.split('\n')):
    for i, c in enumerate(row):
        if c == '#':
            SEAMONSTER_OFFSETS.append((i,j))


def check_for_seamonster(i, j, grid):
    matches = set()
    for a, b in SEAMONSTER_OFFSETS:
        try:
            if grid[j+b][i+a] == '#':
                matches.add((i+a, j+b))
        except:
            return set()
    if len(matches) == len(SEAMONSTER_OFFSETS):
        return matches
    return set()

def part2(tiles):
    result = find_solution(tiles)

    grid = result.remove_borders()
    for orientation in orientations(grid):
        found_count = 0
        found_indexes = set()
        for i in range(len(orientation[0])):
            for j in range(len(orientation)):
                found = check_for_seamonster(i, j, orientation)
                found_indexes |= found
        if found_indexes:
            for i in range(len(orientation[0])):
                for j in range(len(orientation)):
                    if orientation[j][i] == '#' and (i,j) not in found_indexes:
                        found_count += 1
            return found_count


# I poluted my global namespace so you can only run part1 or part 2, too lazy to figure it out
# print(part1(tiles))
print(part2(tiles))