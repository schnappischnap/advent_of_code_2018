def part_1(data):
    opcodes = {'addr': lambda r, a, b: r[a] + r[b],
               'addi': lambda r, a, b: r[a] + b,
               'mulr': lambda r, a, b: r[a] * r[b],
               'muli': lambda r, a, b: r[a] * b,
               'banr': lambda r, a, b: r[a] & r[b],
               'bani': lambda r, a, b: r[a] & b,
               'borr': lambda r, a, b: r[a] | r[b],
               'bori': lambda r, a, b: r[a] | b,
               'setr': lambda r, a, b: r[a],
               'seti': lambda r, a, b: a,
               'gtir': lambda r, a, b: 1 if a > r[b] else 0,
               'gtri': lambda r, a, b: 1 if r[a] > b else 0,
               'gtrr': lambda r, a, b: 1 if r[a] > r[b] else 0,
               'eqir': lambda r, a, b: 1 if a == r[b] else 0,
               'eqri': lambda r, a, b: 1 if r[a] == b else 0,
               'eqrr': lambda r, a, b: 1 if r[a] == r[b] else 0}

    instructions = [(line.split()[0], *map(int, line.split()[1:])) for line in data[1:]]
    registers = [0, 0, 0, 0, 0, 0]
    ip_r = int(data[0][-1])
    ip = 0
    while 0 <= ip < len(instructions):
        registers[ip_r] = ip
        op, a, b, c = instructions[ip]
        registers[c] = opcodes[op](registers, a, b)
        ip = registers[ip_r]
        ip += 1

    return registers[0]


def part_2(data):
    opcodes = {'addr': lambda r, a, b: r[a] + r[b],
               'addi': lambda r, a, b: r[a] + b,
               'mulr': lambda r, a, b: r[a] * r[b],
               'muli': lambda r, a, b: r[a] * b,
               'banr': lambda r, a, b: r[a] & r[b],
               'bani': lambda r, a, b: r[a] & b,
               'borr': lambda r, a, b: r[a] | r[b],
               'bori': lambda r, a, b: r[a] | b,
               'setr': lambda r, a, b: r[a],
               'seti': lambda r, a, b: a,
               'gtir': lambda r, a, b: 1 if a > r[b] else 0,
               'gtri': lambda r, a, b: 1 if r[a] > b else 0,
               'gtrr': lambda r, a, b: 1 if r[a] > r[b] else 0,
               'eqir': lambda r, a, b: 1 if a == r[b] else 0,
               'eqri': lambda r, a, b: 1 if r[a] == b else 0,
               'eqrr': lambda r, a, b: 1 if r[a] == r[b] else 0}

    instructions = [(line.split()[0], *map(int, line.split()[1:])) for line in data[1:]]
    registers = [1, 0, 0, 0, 0, 0]
    ip_r = int(data[0][-1])
    ip = 0
    while 0 <= ip < len(instructions):
        if ip == 2 and registers[1] != 0:
            if registers[5] % registers[1] == 0:
                registers[0] += registers[1]
            registers[4] = 0
            registers[3] = registers[5]
            ip = 12
            continue

        registers[ip_r] = ip
        op, a, b, c = instructions[ip]
        registers[c] = opcodes[op](registers, a, b)
        ip = registers[ip_r]
        ip += 1

    return registers[0]


if __name__ == '__main__':
    with open('day_19_input.txt', 'r') as f:
        inp = f.read().splitlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
