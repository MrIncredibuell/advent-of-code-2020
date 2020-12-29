data = [int(c) for c in open('data.txt').read()]

def part1(data, iterations=100):
    data = data[:]
    size = len(data)
    current_index = 0
    for i in range(iterations):
        current_label = data[current_index]
        removed = []
        remove_index = (current_index + 1)
        for i in range(3):
            remove_index = remove_index % len(data)
            removed.append(data[remove_index])
            data.remove(removed[-1])
            
        destination_label = current_label - 1
        while destination_label not in data:
            if destination_label == 0:
                destination_label = size
            else:
                destination_label = (destination_label - 1) % size
        destination = data.index(destination_label) + 1
        # print(removed, current_label, destination_label)
        data = data[:destination] + removed + data[destination:]
        current_index = (data.index(current_label) + 1) % size
        # print(data)

    one = data.index(1)
    return ''.join([str(x) for x in data[one:] + data[:one]])[1:]

class Node:
    def __init__(self, value):
        self.value = value
        self.successor = None
        self.destination = None

def print_thing(node):
    x = node.successor
    s = str(node.value)
    while x != node:
        s += str(x.value)
        x = x.successor
    print(s)

def part2(data, iterations = 10000000):
    nodes = {}
    prev = None
    for v in data:
        current = Node(v)
        nodes[v] = current
        if prev:
            prev.successor = current
        prev = current
    for node in nodes.values():
        node.destination = nodes.get(node.value - 1)
    
    prev.successor = Node(10)
    prev = prev.successor
    prev.destination = nodes[9]
    for i in range(11, 1000000 + 1):
        current = Node(i)
        prev.successor = current
        current.destination = prev
        prev = current
    prev.successor = list(nodes.values())[0]
    nodes[1].destination = prev

    current = prev.successor
    for iteration in range(iterations):
        destination = current.destination
        moving = []
        moved = current
        for i in range(3):
            moving.append(moved.successor)
            moved = moved.successor
        while destination in moving:
            destination = destination.destination

        current.successor = moving[-1].successor
        destination.successor, moving[-1].successor = moving[0], destination.successor
        current = current.successor
    n = nodes[1].successor
    return n.value * n.successor.value


print(part1(data))
print(part2(data))