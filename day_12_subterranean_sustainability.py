def run(s, r, iterations):
    s = ['.']*6 + list(s) + ['.']*(iterations+2)
    for _ in range(iterations):
        s = ['.']*2 + [r[tuple(s[i-2:i+3])] for i in range(2, len(s)-2)] + ['.']*2
    return sum(i for i, c in enumerate(s, start=-6) if c == '#')


def part_1(data):
    state = data[0].split()[-1]
    rules = {tuple(k): v for line in data[2:] for k, v in [line.split(' => ')]}
    return run(state, rules, 20)


def part_2(data):
    state = data[0].split()[-1]
    rules = {tuple(k): v for line in data[2:] for k, v in [line.split(' => ')]}
    return run(state, rules, 124) + (63*(50000000000-124))


if __name__ == '__main__':
    with open('day_12_input.txt', 'r') as f:
        inp = f.read().splitlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
