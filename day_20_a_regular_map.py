from collections import defaultdict


def solve(data):
    distances = defaultdict(int)
    positions = []
    x, y = 0, 0
    for c in data[1:-1]:
        if c == '(':
            positions.append((x, y))
        elif c == ')':
            x, y = positions.pop()
        elif c == '|':
            x, y = positions[-1]
        else:
            dx, dy = {'N': (0, -1), 'E': (1, 0), 'S': (0, 1), 'W': (-1, 0)}[c]
            new_x, new_y = x+dx, y+dy
            prev_distance = distances.get((new_x, new_y), 10000000000)
            distances[(new_x, new_y)] = min(prev_distance, distances[(x, y)] + 1)
            x, y = new_x, new_y

    return max(distances.values()), sum(d >= 1000 for d in distances.values())


if __name__ == '__main__':
    with open('day_20_input.txt', 'r') as f:
        inp = f.readlines()[0]
        ans = solve(inp)
        print("Part 1 answer: " + str(ans[0]))
        print("Part 2 answer: " + str(ans[1]))
