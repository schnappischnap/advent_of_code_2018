def part_1(data):
    return sum(int(line) for line in data)


def part_2(data):
    cumulative = 0
    reached = {0}
    while True:
        for line in data:
            cumulative += int(line)
            if cumulative in reached:
                return cumulative
            reached.add(cumulative)


if __name__ == '__main__':
    with open('day_01_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
