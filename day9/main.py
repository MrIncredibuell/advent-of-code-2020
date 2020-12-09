data = [int(x) for x in open('data.txt').read().split('\n')]

def find(data, index, preamble):
    found = False
    value = data[index]
    start = index - preamble
    for offset, x in enumerate(data[start: index]):
        for y in data[start + offset + 1: index]:
            if x + y == value:
                return True

    return False


def part1(data, preamble=25):
    i = preamble
    while i < len(data):
        if not find(data, i, preamble=preamble):
            return data[i]
        i += 1

def dynamic_find(data, value):
    output = {}
    for i in range(len(data)):
        output[(i, i)] = data[i]
        if output[(i, i)] == value:
            return (i,i)
        for j in range(i + 1, len(data)):
            output[(i, j)] = data[j] + output[(i, j-1)]
            if output[(i,j)] == value:
                return (i,j)
    return None

def part2(data):
    goal = part1(data)
    x, y = dynamic_find(data, goal)
    l = data[x:y+1]
    return min(l) + max(l)
    


print(part1(data))
print(part2(data))