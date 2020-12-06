data = open('data.txt').read().split('\n\n')
    

def part1(data):
    count = 0
    for group in data:
        people = group.split('\n')
        seen = set()
        for person in people:
            seen |= {c for c in person}
        count += len(seen)
    return count
        

def part2(data):
    count = 0
    for group in data:
        people = group.split('\n')
        seen = {c for c in people[0]}
        for person in people[1:]:
            seen  &= {c for c in person}
        count += len(seen)
    return count

print(part1(data))
print(part2(data))