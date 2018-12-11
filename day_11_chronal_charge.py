def gen_summed_area_table(serial):
    grid = [[0 for _ in range(301)] for _ in range(301)]
    for y in range(1, 301):
        for x in range(1, 301):
            p = ((((((x + 10) * y) + serial) * (x + 10)) // 100) % 10) - 5
            grid[y][x] = p + grid[y][x-1] + grid[y-1][x] - grid[y-1][x-1]
    return grid


def part_1(data):
    t = gen_summed_area_table(int(data))
    return max((t[y][x] - t[y-3][x] - t[y][x-3] + t[y-3][x-3], x-2, y-2)
               for y in range(3, 301)
               for x in range(3, 301))[1:]


def part_2(data):
    t = gen_summed_area_table(int(data))
    return max((t[y][x] - t[y-i][x] - t[y][x-i] + t[y-i][x-i], x-i+1, y-i+1, i)
               for i in range(1, 301)
               for y in range(i, 301)
               for x in range(i, 301))[1:]


if __name__ == '__main__':
    with open('day_11_input.txt', 'r') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
