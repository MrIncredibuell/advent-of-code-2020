import math


rows = open('data.txt').read().split('\n')
goal = int(rows[0])
buses = []
for bus in rows[1].split(','):
    try:
        buses.append(int(bus))
    except ValueError:
        buses.append(None)

def part1(goal, buses):
    offsets = []
    for bus in buses:
        if bus is not None:
            wait = bus - (goal % bus)
            offsets.append((wait, wait * bus))
    return min(offsets)[1]

def lcm(l):
    v = l[0]
    for x in l[1:]:
        v = x * v // math.gcd(x, v)
    return v

def part2(buses):
    i = buses[0]
    seen = [buses[0]]
    for index in range(1, len(buses)):
        current = buses[index]
        if current == None:
            continue
        inc = lcm(seen)
        while (i + index) % current != 0:
            i += inc
        seen.append(current)
    return i



print(part1(goal, buses))
print(part2(buses))