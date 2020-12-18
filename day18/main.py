data = open('data.txt').read().replace(' ', '').split('\n')

def parse(line, index=0):
    tokens = []
    while index < len(line):
        if line[index] == '(':
            expr, new_index = parse(line, index + 1)
            tokens.append(expr)
            index = new_index
            continue
        elif line[index] == ')':
            return tokens, index + 1
        elif line[index] in ('+', '*'):
            tokens.append(line[index])
        elif line[index] in '1234567890':
            tokens.append(int(line[index]))
        index += 1
    return tokens, index

def evaluate(expr):
    if isinstance(expr[0], list):
        value = evaluate(expr[0])
    else:
        value = expr[0]
    index = 1
    while index < len(expr) - 1:
        next_op = expr[index]
        next_value = expr[index + 1]
        if isinstance(next_value, list):
            next_value = evaluate(next_value)
        if next_op == '+':
            value += next_value
        elif next_op == '*':
            value *= next_value
        index += 2
    return value

def prioritize_plus(tokens):
    new_tokens = []
    index = 1
    if isinstance(tokens[0], list):
        new_tokens.append(prioritize_plus(tokens[0]))
    else:
        new_tokens.append(tokens[0])
    while index < len(tokens):
        b = tokens[index + 1]
        if isinstance(b, list):
            b = prioritize_plus(b)
        if tokens[index] == '+':
            a = new_tokens[-1]
            new_tokens[-1] = [a, '+', b]
        else:
            new_tokens.append(tokens[index])
            new_tokens.append(b)
        index += 2
    return new_tokens

def part1(data):
    s = 0
    for line in data:
        exprs, _ = parse(line)
        s += evaluate(exprs)
    return s

def part2(data):
    s = 0
    for line in data:
        exprs, _ = parse(line)
        exprs2 = prioritize_plus(exprs)
        s += evaluate(exprs2)
    return s

print(part1(data))
print(part2(data))