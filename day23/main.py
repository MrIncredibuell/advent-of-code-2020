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
def part2(data):
    data = data[:]
    while len(data) < 1000000:
        data.append(len(data) + 1)
    result = part1(data, iterations=10000)

print(part1(data))
print(part2(data))