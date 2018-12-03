import re


def part_1(data):
    rects = [tuple(map(int, re.findall(r'\d+', line))) for line in data]
    claimed = set()
    overlaps = set()
    for _, x, y, w, h in rects:
        for i in range(x, x+w):
            for j in range(y, y+h):
                if (i, j) in claimed:
                    overlaps.add((i, j))
                claimed.add((i, j))
    return len(overlaps)


def part_2(data):
    rects = [tuple(map(int, re.findall(r'\d+', line))) for line in data]
    for c1, x1, y1, w1, h1 in rects:
        for c2, x2, y2, w2, h2 in rects:
            if c1 == c2:
                continue
            if x1 < x2+w2 and x1+w1 > x2 and y1 < y2+h2 and y1+h1 > y2:
                break
        else:
            return c1


if __name__ == '__main__':
    with open('day_03_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
