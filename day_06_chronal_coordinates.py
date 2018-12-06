from collections import defaultdict


def dist(c1, c2):
    return abs(c1[0] - c2[0]) + abs(c1[1] - c2[1])


def part_1(data):
    coords = [tuple(map(int, line.split(', '))) for line in data]
    max_x = max(c[0] for c in coords)
    max_y = max(c[1] for c in coords)

    areas = defaultdict(int)
    infinites = set()
    for x in range(max_x+1):
        for y in range(max_y+1):
            min1, min2, *_ = sorted([(dist((x, y), c), c) for c in coords])
            if min1[0] != min2[0]:
                areas[min1[1]] += 1
                if not (0 < x < max_x and 0 < y < max_y):
                    infinites.add(min1[1])

    return max(v for c, v in areas.items() if c not in infinites)


def part_2(data):
    coords = [tuple(map(int, line.split(', '))) for line in data]
    max_x = max(c[0] for c in coords)
    max_y = max(c[1] for c in coords)

    return sum(sum(dist((x, y), c) for c in coords) < 10000
               for x in range(max_x)
               for y in range(max_y))


if __name__ == '__main__':
    with open('day_06_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
