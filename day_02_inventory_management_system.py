from collections import Counter
import itertools


def part_1(data):
    doubles, triples = 0, 0
    for line in data:
        counter = Counter(line)
        if 2 in counter.values():
            doubles += 1
        if 3 in counter.values():
            triples += 1
    return doubles * triples


def part_2(data):
    for line_1, line_2 in itertools.combinations(data, 2):
        similarity = "".join(a for a, b in zip(line_1, line_2) if a == b)
        if len(similarity) == len(line_1) - 1:
            return similarity


if __name__ == '__main__':
    with open('day_02_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
