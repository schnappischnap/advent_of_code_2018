import re
from string import ascii_lowercase


def part_1(data):
    i = 0
    while i < len(data) - 1:
        if abs(ord(data[i]) - ord(data[i+1])) == 32:
            data = data[:i]+data[i+2:]
            i = max(0, i-1)
            continue
        i += 1
    return len(data)


def part_2(data):
    return min(part_1(re.sub(c, '', data, flags=re.IGNORECASE))
               for c in ascii_lowercase)


if __name__ == '__main__':
    with open('day_05_input.txt', 'r') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
