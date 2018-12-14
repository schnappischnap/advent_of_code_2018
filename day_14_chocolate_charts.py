def part_1(data):
    target = int(data)
    scores = [3, 7]
    i, j = 0, 1
    while len(scores) < (target + 10):
        scores.extend(int(a) for a in str(scores[i] + scores[j]))
        i = (i + 1 + scores[i]) % len(scores)
        j = (j + 1 + scores[j]) % len(scores)

    return ''.join(str(c) for c in scores[target:target+10])


def part_2(data):
    target = list(map(int, data))
    scores = [3, 7]
    i, j = 0, 1
    while scores[-len(target):] != target and scores[-len(target)-1:-1] != target:
        scores.extend(int(a) for a in str(scores[i] + scores[j]))
        i = (i + 1 + scores[i]) % len(scores)
        j = (j + 1 + scores[j]) % len(scores)

    if scores[-len(target):] == target:
        return len(scores) - len(target)
    else:
        return len(scores) - len(target) - 1


if __name__ == '__main__':
    with open('day_14_input.txt', 'r') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
