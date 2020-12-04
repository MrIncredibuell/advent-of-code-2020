data = open('data.txt').read().split('\n\n')

def parse_passport(passport):
    parsed = {}
    for line in passport.split('\n'):
        for token in line.split(' '):
            if ':' in token:
                key, value = token.split(':')
                parsed[key] = value
    return parsed

def byr(value):
    try:
        return 1920 <= int(value) <= 2002
    except:
        return False

def iyr(value):
    try:
        return 2010 <= int(value) <= 2020
    except:
        return False

def eyr(value):
    try:
        return 2020 <= int(value) <= 2030
    except:
        return False

def hgt(value):
    if value.endswith('cm'):
        return 150 <= int(value[:-2]) <= 193
    elif value.endswith('in'):
        return 59 <= int(value[:-2]) <= 76
    return False

def hcl(value):
    if value.startswith('#') and len(value) == 7:
        try:
            int(value[1:], base=16)
            return True
        except:
            pass
    return False

def ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def pid(value):
    if len(value) != 9:
        return False
    for c in value:
        try:
            int(c)
        except:
            return False
    return True

REQUIRED = {
    'byr': byr,
    'iyr': iyr,
    'eyr': eyr,
    'hgt': hgt,
    'hcl': hcl,
    'ecl': ecl,
    'pid': pid,
}

def part1(data):
    count = 0
    for passport in data:
        parsed = parse_passport(passport)
        valid = True
        for k in REQUIRED.keys():
            if k not in parsed:
                valid = False
        if valid:
            count += 1
    return count
        

def part2(data):
    count = 0
    for passport in data:
        parsed = parse_passport(passport)
        valid = True
        for k, f in REQUIRED.items():
            field_is_valid = f(parsed.get(k, ''))
            if not field_is_valid:
                valid = False
        if valid:
            count += 1

    return count

print(part1(data))
print(part2(data))
