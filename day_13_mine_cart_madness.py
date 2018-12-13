def part_1(data):
    track = [line.replace('>', '-').replace('<', '-').replace('^', '|').replace('v', '|')
             for line in data]

    directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    carts = [(x, y) + directions[c] + (0,)
             for y, row in enumerate(data)
             for x, c in enumerate(row)
             if c in directions]

    while True:
        carts.sort()
        for i, (x, y, dx, dy, t) in enumerate(carts):
            x, y = x + dx, y + dy

            if track[y][x] == '\\':
                dx, dy = dy, dx
            elif track[y][x] == '/':
                dx, dy = -dy, -dx
            elif track[y][x] == '+':
                if t % 3 == 0:
                    dx, dy = dy, -dx
                elif t % 3 == 2:
                    dx, dy = -dy, dx
                t += 1

            if any(x == x2 and y == y2 for x2, y2, *_ in carts):
                return x, y

            carts[i] = (x, y, dx, dy, t)


def part_2(data):
    track = [line.replace('>', '-').replace('<', '-').replace('^', '|').replace('v', '|')
             for line in data]

    directions = {'<': (-1, 0), '>': (1, 0), '^': (0, -1), 'v': (0, 1)}
    carts = [(x, y) + directions[c] + (0,)
             for y, row in enumerate(data)
             for x, c in enumerate(row)
             if c in directions]

    while len(carts) > 1:
        carts.sort(key=lambda tup: (tup[1], tup[0]))
        i = 0
        while i < len(carts):
            x, y, dx, dy, t = carts[i]
            x, y = x+dx, y+dy

            if track[y][x] == '\\':
                dx, dy = dy, dx
            elif track[y][x] == '/':
                dx, dy = -dy, -dx
            elif track[y][x] == '+':
                if t % 3 == 0:
                    dx, dy = dy, -dx
                elif t % 3 == 2:
                    dx, dy = -dy, dx
                t += 1

            for i2, (x2, y2, *_) in enumerate(carts):
                if x == x2 and y == y2:
                    for j in sorted((i, i2), reverse=True):
                        del carts[j]
                    if i > i2:
                        i -= 1
                    break
            else:
                carts[i] = (x, y, dx, dy, t)
                i += 1

    return carts[0][:2]


if __name__ == '__main__':
    with open('day_13_input.txt', 'r') as f:
        inp = f.read().splitlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
