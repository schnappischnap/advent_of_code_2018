from collections import defaultdict
from string import ascii_uppercase


def pop_min(l):
    return l.pop(l.index(min(l)))


def part_1(data):
    requirements = defaultdict(list)
    for line in data:
        requirements[line[36]].append(line[5])

    stack = [c for c in ascii_uppercase if c not in requirements.keys()]
    done = []
    while stack:
        done.append(pop_min(stack))
        for step, requires in requirements.items():
            if all(r in done for r in requires) and step not in (done+stack):
                stack.append(step)

    return "".join(done)


def part_2(data):
    requirements = defaultdict(list)
    for line in data:
        requirements[line[36]].append(line[5])

    stack = [c for c in ascii_uppercase if c not in requirements.keys()]
    workers = []
    done = []
    total = 0
    while workers or stack:
        if workers:
            time, step = pop_min(workers)
            total += time - total
            done.append(step)

        for step, requires in requirements.items():
            seen = set(done + stack + [w[1] for w in workers])
            if all(r in done for r in requires) and step not in seen:
                stack.append(step)

        for _ in range(min(5-len(workers), len(stack))):
            step = pop_min(stack)
            workers.append((60 + total + ord(step) - 64, step))

    return total


if __name__ == '__main__':
    with open('day_07_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
