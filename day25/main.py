a, b = [int(x) for x in open('data.txt').read().split('\n')]

def transform(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value

def find_loop_size(subject_number, goal):
    loop_size = 0
    value = 1
    while value != goal:
        value *= subject_number
        value %= 20201227
        loop_size += 1
    return loop_size

def part1(a, b):
    v = 7
    loop_size = find_loop_size(7, a)
    return transform(b, loop_size)

def part2(a, b):
    pass

print(part1(a, b))
print(part2(a, b))