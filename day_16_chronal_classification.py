import re


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

    sample_count = 0
    for i in range(0, 3219, 4):
        pre, instr, post = [list(map(int, re.findall(r'\d+', l))) for l in data[i:i+3]]

        opcode_count = 0
        for opcode in opcodes.values():
            temp = pre[:]
            temp[instr[3]] = opcode(pre, instr[1], instr[2])
            if temp == post:
                opcode_count += 1

        if opcode_count >= 3:
            sample_count += 1

    return sample_count


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

    opcode_ids = [[o for o in opcodes] for _ in range(16)]

    for i in range(0, 3219, 4):
        pre, instr, post = [list(map(int, re.findall(r'\d+', line))) for line in data[i:i + 3]]

        for opcode, func in opcodes.items():
            temp = pre[:]
            temp[instr[3]] = func(pre, instr[1], instr[2])
            if temp != post and opcode in opcode_ids[instr[0]]:
                opcode_ids[instr[0]].remove(opcode)

    while any(len(o) > 1 for o in opcode_ids):
        unique = [a[0] for a in opcode_ids if len(a) == 1]
        for i, opcode_id in enumerate(opcode_ids):
            if len(opcode_id) > 1:
                opcode_ids[i] = [b for b in opcode_id if b not in unique]
    opcode_ids = [o[0] for o in opcode_ids]

    registers = [0, 0, 0, 0]
    for line in data[3222:]:
        o, a, b, c = list(map(int, re.findall(r'\d+', line)))
        registers[c] = opcodes[opcode_ids[o]](registers, a, b)

    return registers[0]


if __name__ == '__main__':
    with open('day_16_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
