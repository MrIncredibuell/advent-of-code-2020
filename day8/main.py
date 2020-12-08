from copy import deepcopy

data = open('data.txt').read().split('\n')

def parse(lines):
    instructions = []
    for line in lines:
        instruction, value = line.split(' ')
        instructions.append([instruction, int(value)])
    return instructions

data = parse(data)

class InfiniteLoopException(Exception):
    pass

class Program:
    def __init__(self, instructions: list):
        self.instructions = instructions
        self.accumulator = 0
        self.index = 0
        self.seen = set()

    def run(self):
        while self.index not in self.seen:
            self.seen.add(self.index)
            inst, value = self.instructions[self.index]
            if inst == 'acc':
                self.accumulator += value
            elif inst == 'jmp':
                self.index += (value - 1)
            self.index += 1
            if self.index == len(self.instructions):
                return self.accumulator
        raise InfiniteLoopException(f'Infinite Loop On Line {self.index}')

def part1(data):
    p = Program(data)
    try:
        p.run()
    except InfiniteLoopException as e:
        return p.accumulator

def part2(data):
    for i in range(len(data)):
        try:
            changed = deepcopy(data)
            if changed[i][0] == 'nop':
                changed[i][0] = 'jmp'
            elif changed[i][0] == 'jmp':
                changed[i][0] = 'nop'

            return Program(changed).run()
        except InfiniteLoopException:
            pass
    


print(part1(data))
print(part2(data))