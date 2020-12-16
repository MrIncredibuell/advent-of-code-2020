data = open('data.txt').read()
rules, rest = data.split('\nyour ticket:\n')
my_ticket, other_tickets = rest.split('\n\nnearby tickets:\n')
parsed_rules = {}
for rule in rules.split('\n'):
    if not rule:
        continue
    key, values = rule.split(': ')
    pairs = []
    for pair in values.split(' or '):
        low, high = pair.split('-')
        pairs.append((int(low), int(high)))
        parsed_rules[key] = pairs

my_ticket = [
    [int(x) for x in ticket.split(',')]
    for ticket in my_ticket.split('\n') if ticket
][0]

other_tickets = [
    [int(x) for x in ticket.split(',')]
    for ticket in other_tickets.split('\n') if ticket
]


def invalids(rules, numbers):
    result = 0
    for number in numbers:
        valid = False
        for rule in rules:
            for (low, high) in rule:
                if low <= number <= high:
                    valid = True
        if not valid:
            result += number
    return result


def part1(rules, tickets):
    rules = list(rules.values())
    count = 0
    for ticket in tickets:
       count += invalids(rules, ticket)
    return count


def validate_number(rules, number):
    for low, high in rules:
        if (low <= number <= high):
            return True
    return False


def part2(rules, my_ticket, tickets):
    rule_list = list(rules.values())
    valid_tickets = []
    for ticket in tickets:
       if not invalids(rule_list, ticket):
           valid_tickets.append(ticket)

    possibilities = {
        key: set(range(len(my_ticket)))
        for key in rules.keys()
    }
    
    for key, ns in list(possibilities.items()):
        for n in list(ns):
            number_is_valid = True
            for t in valid_tickets:
                if not validate_number(rules[key], t[n]):
                    number_is_valid = False
                    break
            if not number_is_valid:
                possibilities[key].remove(n)

    actual = {}
    while len(possibilities) > 0:
        for k, v in list(possibilities.items()):
            if len(v) == 1:
                value =  v.pop()
                actual[k] = value
                del possibilities[k]
                for p_values in possibilities.values():
                    p_values.discard(value)

    result = 1
    for key, index in actual.items():
        if key.startswith('departure'):
            result *= my_ticket[index]
    return result


print(part1(parsed_rules, other_tickets))
print(part2(parsed_rules, my_ticket, other_tickets))