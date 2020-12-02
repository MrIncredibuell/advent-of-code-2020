raw_data = open('data.txt').read().split('\n')
data = []
for row in raw_data:
    r, char, password = row.split(' ')
    low, high = r.split('-')
    char = char[0]
    data.append(((int(low), int(high)), char, password))

def part1(data):
    valid = 0
    for (low, high), char, password in data:
        if low <= password.count(char) <= high:
            valid += 1
    return valid


def part2(data):
    valid = 0
    for (low, high), char, password in data:
        c = 0
        if password[low - 1] == char:
            c += 1
        if password[high - 1] == char:
            c += 1

        if c == 1:
            valid += 1

    return valid

print(part1(data))
print(part2(data))