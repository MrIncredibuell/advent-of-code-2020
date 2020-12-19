from functools import lru_cache

raw_rules, tests = open('data.txt').read().split('\n\n')
rules = {}

class Rule:
    def __init__(self, values, rules):
        self.rules = rules
        if values.startswith('"'):
            self.options = None
            self.terminal = values[1:-1]
        else:
            self.options = []
            self.terminal = None
            values = values.split(' | ')
            for value in values:
                self.options.append([int(x) for x in value.split(' ')])

    def match(self, s):
        if self.terminal:
            return s == self.terminal
        for option in self.options:
            if match_rule_list(self.rules, option, s):
                return True
        return False

seen = {}
def match_rule_list(all_rules, rule_indexes, s):
    if str(rule_indexes) + s in seen:
        return seen[str(rule_indexes) + s]
    if len(rule_indexes) == 1:
        seen[str(rule_indexes) + s] = rules[rule_indexes[0]].match(s)
        return seen[str(rule_indexes) + s]
    for i in range(1, len(s)):
        if match_rule_list(all_rules, rule_indexes[:1], s[:i]) and match_rule_list(all_rules, rule_indexes[1:], s[i:]):
            seen[str(rule_indexes) + s] = True
            return True
    seen[str(rule_indexes) + s] = False
    return False


for line in raw_rules.split('\n'):
    key, values = line.split(': ')
    key = int(key)
    rules[key] = Rule(values, rules)

tests = tests.split('\n')

def part1(rules, tests):
    c = 0
    for test in tests:
        if rules[0].match(test):
            c += 1
    return c

def part2(rules, tests):
    global seen
    seen = {}
    c = 0
    rules[8] = Rule('42 | 42 8', rules)
    rules[11] = Rule('42 31 | 42 11 31', rules)
    for test in tests:
        if rules[0].match(test):
            c += 1
    return c


print(part1(rules, tests))
print(part2(rules, tests))