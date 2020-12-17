data = open('data.txt').read().replace('\r', '').split('\n')

class grid:
    def __init__(self, state):
        self.state = {}
        for y, row in enumerate(state):
            for x, c in enumerate(row):
                self.state[(x,y,0)] = c
        self.min_x = 0
        self.min_y = 0
        self.min_z = 0
        self.max_x = len(row) - 1
        self.max_y = len(state) - 1
        self.max_z = 0

    @staticmethod
    def neighbors(x, y, z):
        for i in range(x-1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    if not ((i == x) and (j == y) and (k == z)):
                        yield (i,j,k)

    def iter_locations(self):
        self.min_x -= 1
        self.min_y -= 1
        self.min_z -= 1
        self.max_x += 1
        self.max_y += 1
        self.max_z += 1
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                for z in range(self.min_z, self.max_z + 1):
                    yield (x,y,z)

    def step(self):
        new_state = {}
        for (x,y,z) in self.iter_locations():
            c = self.state.get((x,y,z), '.')
            if c == '#' and [self.state.get(neighbor, '.') for neighbor in self.neighbors(x,y,z)].count('#') in (2,3):
                new_state[(x,y,z)] = '#'
            elif c == '.' and [self.state.get(neighbor, '.') for neighbor in self.neighbors(x,y,z)].count('#') in (3,):
                new_state[(x,y,z)] = '#'
            else:
                new_state[(x,y,z)] = '.'
        self.state = new_state

    def active_count(self):
        return len([v for v in self.state.values() if v == '#'])


class grid4d:
    def __init__(self, state):
        self.state = {}
        for y, row in enumerate(state):
            for x, c in enumerate(row):
                self.state[(x,y,0,0)] = c
        self.min_x = 0
        self.min_y = 0
        self.min_z = 0
        self.min_w = 0
        self.max_x = len(row) - 1
        self.max_y = len(state) - 1
        self.max_z = 0
        self.max_w = 0

    @staticmethod
    def neighbors(x, y, z, w):
        for i in range(x-1, x + 2):
            for j in range(y - 1, y + 2):
                for k in range(z - 1, z + 2):
                    for l in range(w - 1, w + 2):
                        if not ((i == x) and (j == y) and (k == z) and (l == w)):
                            yield (i,j,k,l)

    def iter_locations(self):
        self.min_x -= 1
        self.min_y -= 1
        self.min_z -= 1
        self.min_w -= 1
        self.max_x += 1
        self.max_y += 1
        self.max_z += 1
        self.max_w += 1
        for x in range(self.min_x, self.max_x + 1):
            for y in range(self.min_y, self.max_y + 1):
                for z in range(self.min_z, self.max_z + 1):
                    for w in range(self.min_w, self.max_w + 1):
                        yield (x,y,z,w)

    def step(self):
        new_state = {}
        for (x,y,z,w) in self.iter_locations():
            c = self.state.get((x,y,z,w), '.')
            if c == '#' and [self.state.get(neighbor, '.') for neighbor in self.neighbors(x,y,z,w)].count('#') in (2,3):
                new_state[(x,y,z,w)] = '#'
            elif c == '.' and [self.state.get(neighbor, '.') for neighbor in self.neighbors(x,y,z,w)].count('#') in (3,):
                new_state[(x,y,z,w)] = '#'
            else:
                new_state[(x,y,z,w)] = '.'
        self.state = new_state

    def active_count(self):
        return len([v for v in self.state.values() if v == '#'])

def part1(data):
    g = grid(data)
    for i in range(6):
        g.step()
    return g.active_count()

def part2(data):
    g = grid4d(data)
    for i in range(6):
        g.step()
    return g.active_count()

print(part1(data))
print(part2(data))