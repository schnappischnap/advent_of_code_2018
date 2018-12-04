from collections import defaultdict
import re


def part_1(data):
    guards = defaultdict(lambda: defaultdict(int))
    totals = defaultdict(int)
    active_guard = None
    sleep_start = None
    for line in sorted(data):
        if 'begins shift' in line:
            active_guard = int(re.search(r'#(\d+)', line).group(1))
        elif 'falls asleep' in line:
            sleep_start = int(re.search(r':(\d+)', line).group(1))
        elif 'wakes up' in line:
            sleep_end = int(re.search(r':(\d+)', line).group(1))
            for i in range(sleep_start, sleep_end):
                guards[active_guard][i] += 1
                totals[active_guard] += 1

    guard = max(totals, key=lambda k: totals[k])
    minute = max(guards[guard], key=lambda k: guards[guard][k])
    return guard * minute


def part_2(data):
    minutes = defaultdict(lambda: defaultdict(int))
    active_guard = None
    sleep_start = None
    for line in sorted(data):
        if 'begins shift' in line:
            active_guard = int(re.search(r'#(\d+)', line).group(1))
        elif 'falls asleep' in line:
            sleep_start = int(re.search(r':(\d+)', line).group(1))
        elif 'wakes up' in line:
            sleep_end = int(re.search(r':(\d+)', line).group(1))
            for i in range(sleep_start, sleep_end):
                minutes[i][active_guard] += 1

    guard, minute = max([(m, g, minutes[m][g])
                         for m in minutes
                         for g in minutes[m]],
                        key=lambda tup: tup[2])[:2]
    return guard * minute


if __name__ == '__main__':
    with open('day_04_input.txt', 'r') as f:
        inp = f.readlines()
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
