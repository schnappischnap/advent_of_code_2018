from collections import deque


def solve(players, last):
    circle = deque([0])
    scores = [0] * players
    for i in range(last):
        if i % 23 == 0:
            circle.rotate(7)
            scores[i % players] += i + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(i)
    return max(scores)


def part_1(data):
    players = int(data.split()[0])
    last = int(data.split()[-2])
    return solve(players, last)


def part_2(data):
    players = int(data.split()[0])
    last = int(data.split()[-2]) * 100
    return solve(players, last)


if __name__ == '__main__':
    with open('day_09_input.txt', 'r') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
