data = open('data.txt').read().split('\n')

class CPU:
    def __init__(self):
        self.memory = {}
        self.mask = 'X' * 36
        self.mask_prefix = 'mask = '
        self.mem_prefix = 'mem['

    def execute(self, instruction):
        if instruction.startswith(self.mask_prefix):
            self.mask = instruction[len(self.mask_prefix):]
        elif instruction.startswith('mem['):
            instruction = instruction.replace('mem[', '')
            index, value = instruction.split('] = ')
            index = int(index)
            value = "{0:b}".format(int(value))
            while len(value) < 36:
                value = '0' + value
            value = [c for c in value]
            for i, c in enumerate(self.mask):
                if c != 'X':
                    value[i] = c
            self.memory[index] = int(''.join(value), base=2)
        else:
            raise NotImplementedError("OH NO")

def expand(index):
    for i, c in enumerate(index):
        if c == 'X':
            yield from expand(index[:i] + ['0'] + index[i+1:])
            yield from expand(index[:i] + ['1'] + index[i+1:])
            return
    yield index


class CPU2:
    def __init__(self):
        self.memory = {}
        self.mask = 'X' * 36
        self.mask_prefix = 'mask = '
        self.mem_prefix = 'mem['

    def execute(self, instruction):
        if instruction.startswith(self.mask_prefix):
            self.mask = instruction[len(self.mask_prefix):]
        elif instruction.startswith('mem['):
            instruction = instruction.replace('mem[', '')
            index, value = instruction.split('] = ')
            index = "{0:b}".format(int(index))
            value = int(value)
            while len(index) < 36:
                index = '0' + index
            index = [c for c in index]
            for i, c in enumerate(self.mask):
                if c in ('1', 'X'):
                    index[i] = c
            for i in expand(index):
                i = int(''.join(i), base=2)
                self.memory[i] = value
        else:
            raise NotImplementedError("OH NO")

def part1(data):
    cpu = CPU()
    for inst in data:
        cpu.execute(inst)
    return sum(cpu.memory.values())

def part2(data):
    cpu = CPU2()
    for inst in data:
        cpu.execute(inst)
    return sum(cpu.memory.values())

print(part1(data))
print(part2(data))