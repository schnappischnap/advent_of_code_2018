def neighbours(x, y):
    return [(x + dx, y + dy)
            for dx in range(-1, 2)
            for dy in range(-1, 2)
            if (dx, dy) != (0, 0) if 0 <= (x+dx) < 50 and 0 <= (y+dy) < 50]


def part_1(data):
    grid = [list(line) for line in data]

    for _ in range(10):
        new_grid = [row[:] for row in grid]
        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                n = [grid[p[1]][p[0]] for p in neighbours(x, y)]
                if c == '.':
                    if sum(p == '|' for p in n) >= 3:
                        new_grid[y][x] = '|'
                elif c == '|':
                    if sum(p == '#' for p in n) >= 3:
                        new_grid[y][x] = '#'
                else:
                    if sum(p == '#' for p in n) < 1 or sum(p == '|' for p in n) < 1:
                        new_grid[y][x] = '.'
        grid = new_grid

    return sum(c == '|' for r in grid for c in r) * sum(c == '#' for r in grid for c in r)


def part_2(data):
    grid = [list(line) for line in data]

    for i in range(1, 1000000000):
        new_grid = [row[:] for row in grid]
        for y, row in enumerate(grid):
            for x, c in enumerate(row):
                n = [grid[p[1]][p[0]] for p in neighbours(x, y)]
                if c == '.':
                    if sum(p == '|' for p in n) >= 3:
                        new_grid[y][x] = '|'
                elif c == '|':
                    if sum(p == '#' for p in n) >= 3:
                        new_grid[y][x] = '#'
                else:
                    if sum(p == '#' for p in n) < 1 or sum(p == '|' for p in n) < 1:
                        new_grid[y][x] = '.'
        grid = new_grid

        if i >= 512 and i % 28 == 1000000000 % 28:
            return sum(c == '|' for r in grid for c in r) * sum(c == '#' for r in grid for c in r)


if __name__ == '__main__':
    with open('day_18_input.txt', 'r') as f:
        inp = f.read().splitlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
