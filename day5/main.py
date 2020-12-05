data = open('data.txt').read().split('\n')

def parse_seat(seat):
    row = 0
    col = 0
    for i, c in enumerate(seat[6::-1]):
        if c == 'B':
            row += 2**i

    for i, c in enumerate(seat[-3:][::-1]):
        if c == 'R':
            col += 2**i

    return row, col
    

def part1(data):
    m = 0
    for seat in data:
        row, col = parse_seat(seat)
        curr = (row * 8) + col
        if curr > m:
            m = curr
    return m
        

def part2(data):
    seats = []
    for seat in data:
        row, col = parse_seat(seat)
        seats.append((row * 8) + col)
    seats.sort()
    for i, seat in enumerate(seats):
        if seats[i+1] == seat + 2:
            return seat+1

print(part1(data))
print(part2(data))