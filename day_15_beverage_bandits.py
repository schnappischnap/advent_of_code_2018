from collections import deque


def neighbours(y, x):
    return [(y+dy, x+dx) for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]]


def get_path(start, ends, unoccupied):
    paths = deque([[start]])
    visited = {start}
    while len(paths):
        path = paths.popleft()
        coord = path[-1]
        if coord in ends:
            return path
        for n in neighbours(coord[0], coord[1]):
            if n in unoccupied and n not in visited:
                visited.add(n)
                paths.append(path+[n])
    return []


def part_1(data):
    units = []
    unoccupied = set()
    for y, line in enumerate(data):
        for x, c in enumerate(line):
            if c in 'GE':
                units.append((y, x, c, 200))
            if c == '.':
                unoccupied.add((y, x))

    r = 0
    while True:
        units.sort()
        i = -1
        while i < len(units) - 1:
            i += 1

            unit = units[i]
            if unit not in units:
                continue
            y, x, c, hp = unit

            # Find enemies
            targets = [u for u in units if u[2] != c]
            if not targets:
                return r * sum(u[3] for u in units)

            # Find spaces next to enemies
            in_range = [(y2, x2)
                        for u in targets
                        for y2, x2 in neighbours(u[0], u[1])]
            if not in_range:
                continue

            # Move closer to enemy
            if (y, x) not in in_range:
                path = get_path((y, x), in_range, unoccupied)
                if not path:
                    continue
                unoccupied.add((y, x))
                y, x = path[1]
                units[i] = (y, x, c, hp)
                unoccupied.remove((y, x))

            n = neighbours(y, x)
            attackable = [u for u in targets if u[:2] in n]
            if not attackable:
                continue
            target = min(attackable, key=lambda tup: (tup[3], tup[0], tup[1]))
            if target[3] < 4:
                if units.index(target) < i:
                    i -= 1
                units.remove(target)
                unoccupied.add(target[:2])
            else:
                units[units.index(target)] = target[:3] + (target[3]-3,)

        r += 1


def part_2(data):
    for elf_attack in range(1000):
        elf_dead = False
        units = []
        unoccupied = set()
        for y, line in enumerate(data):
            for x, c in enumerate(line):
                if c in 'GE':
                    units.append((y, x, c, 200))
                if c == '.':
                    unoccupied.add((y, x))

        r = 0
        while True:
            units.sort()
            i = -1
            while i < len(units) - 1:
                i += 1

                unit = units[i]
                if unit not in units:
                    continue
                y, x, c, hp = unit

                # Find enemies
                targets = [u for u in units if u[2] != c]
                if not targets:
                    return r * sum(u[3] for u in units)

                # Find spaces next to enemies
                in_range = [(y2, x2)
                            for u in targets
                            for y2, x2 in neighbours(u[0], u[1])]
                if not in_range:
                    continue

                # Move closer to enemy
                if (y, x) not in in_range:
                    path = get_path((y, x), in_range, unoccupied)
                    if not path:
                        continue
                    unoccupied.add((y, x))
                    y, x = path[1]
                    units[i] = (y, x, c, hp)
                    unoccupied.remove((y, x))

                n = neighbours(y, x)
                attackable = [u for u in targets if u[:2] in n]
                if not attackable:
                    continue
                target = min(attackable, key=lambda tup: (tup[3], tup[0], tup[1]))
                attack = 3 if unit[2] == 'G' else elf_attack
                if target[3] < attack + 1:
                    if target[2] == 'E':
                        elf_dead = True
                        break
                    if units.index(target) < i:
                        i -= 1
                    units.remove(target)
                    unoccupied.add(target[:2])
                else:
                    units[units.index(target)] = target[:3] + (target[3]-attack,)
            if elf_dead:
                break

            r += 1


if __name__ == '__main__':
    with open('day_15_input.txt', 'r') as f:
        inp = f.read().splitlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
