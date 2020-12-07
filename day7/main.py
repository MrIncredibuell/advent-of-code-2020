from collections import defaultdict
from functools import lru_cache

data = open('data.txt').read().split('\n')

def parse(lines):
    parsed = defaultdict(list)
    for line in lines:
        outer, rest = line.split(' bags contain ')
        if rest == 'no other bags.':
            parsed[outer] = []
            continue
            
        inners = rest.split(', ')
        for inner in inners:
            inner = inner.replace(' bags.', '')
            inner = inner.replace(' bags', '')
            inner = inner.replace(' bag.', '')
            inner = inner.replace(' bag', '')
            inner = inner.split(' ')
            count = int(inner[0])
            color = ' '.join(inner[1:])
            parsed[outer].append((color, count))
    return parsed

parsed = parse(data)

@lru_cache()
def expand(color, count):
    output = defaultdict(lambda: 0)
    output[color] = count
    if color == None:
        return
    for (nested_color, nested_count) in parsed[color]:
        nested = expand(nested_color, nested_count * count)
        for k, v in nested.items():
            output[k] += v
    return output

def part1(data):
    count = 0
    colors = list(parsed.keys())
    for color in colors:
        expanded = expand(color, 1)
        if expanded.get('shiny gold', 0) > 0:
            count += 1
    return count - 1


def part2(data):
    expanded = expand('shiny gold', 1)
    return sum(expanded.values()) - 1

print(part1(data))
print(part2(data))