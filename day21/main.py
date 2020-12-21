lines = open('data.txt').read().split('\n')

data = []
for line in lines:
    ingredients, allergens = line.replace(')', '').split(' (contains ')
    data.append((ingredients.split(' '), allergens.split(', ')))

def part1(data):
    possibilities = {}
    all_ingredients = set()
    for ingredients, allergens in data:
        ingredients = set(ingredients)
        all_ingredients |= ingredients
        for allergen in allergens:
            if allergen not in possibilities:
                possibilities[allergen] = {*ingredients}
            else:
                possibilities[allergen] &= ingredients

    for vs in possibilities.values():
        all_ingredients -= vs

    s = 0
    for ingredients, _ in data:
        for i in all_ingredients:
            s += ingredients.count(i)

    return s

def part2(data):
    possibilities = {}
    all_ingredients = set()
    for ingredients, allergens in data:
        ingredients = set(ingredients)
        all_ingredients |= ingredients
        for allergen in allergens:
            if allergen not in possibilities:
                possibilities[allergen] = {*ingredients}
            else:
                possibilities[allergen] &= ingredients

    for vs in possibilities.values():
        all_ingredients -= vs

    solutions = {}
    while len(possibilities) > 0:
        for k, vs in list(possibilities.items()):
            if len(vs) == 1:
                value = vs.pop()
                solutions[k] = value
                del possibilities[k]
                for v in possibilities.values():
                    v.discard(value)

    return ','.join([v for k, v in sorted(solutions.items())])

print(part1(data))
print(part2(data))