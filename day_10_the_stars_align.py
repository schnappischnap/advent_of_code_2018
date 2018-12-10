import re


def solve(data):
    data = [tuple(map(int, re.findall(r'-?\d+', line))) for line in data]

    i = 1
    prev_width = None
    while True:
        width = max(d[0]+d[2]*i for d in data) - min(d[0]+d[3]*i for d in data)
        if prev_width is not None and width > prev_width:
            break
        prev_width = width
        i += 1

    points = [(d[0]+(d[2]*i), d[1]+(d[3]*i)) for d in data]
    for y in range(min(p[1] for p in points), max(p[1] for p in points) + 1):
        for x in range(min(p[0] for p in points), max(p[0] for p in points) + 1):
            print("#" if (x, y) in points else ".", end="")
        print()

    return i


if __name__ == '__main__':
    with open('day_10_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer:")
        print("Part 2 answer: " + str(solve(inp)))
