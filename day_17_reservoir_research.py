import re
import sys


def solve(data):
    sys.setrecursionlimit(10000)

    clay = set()
    for line in data:
        if line[0] == 'x':
            x_start = x_stop = int(re.search(r'\d+', line).group())
            y_start, y_stop = list(map(int, re.findall(r'\d+', line)[1:]))
        else:
            x_start, x_stop = list(map(int, re.findall(r'\d+', line)[1:]))
            y_start = y_stop = int(re.search(r'\d+', line).group())
        clay.update((x, y)
                    for x in range(x_start, x_stop+1)
                    for y in range(y_start, y_stop+1))

    min_y = min(p[1] for p in clay)
    max_y = max(p[1] for p in clay)

    moving = set()
    settled = set()

    def recursive(point, direction):
        moving.add(point)

        under = (point[0], point[1]+1)
        if under not in clay and under not in moving and 1 <= under[1] <= max_y:
            recursive(under, (0, 1))
        if under not in clay and under not in settled:
            return False

        left = (point[0]-1, point[1])
        right = (point[0]+1, point[1])

        left_filled = False
        if left in clay:
            left_filled = True
        elif left not in moving:
            left_filled = recursive(left, (-1, 0))

        right_filled = False
        if right in clay:
            right_filled = True
        elif right not in moving:
            right_filled = recursive(right, (1, 0))

        if direction[1] == 1 and left_filled and right_filled:
            settled.add(point)

            while left in moving:
                settled.add(left)
                left = (left[0]-1, left[1])

            while right in moving:
                settled.add(right)
                right = (right[0]+1, right[1])

        return direction[0] == -1 and (left_filled or left in clay) or \
               direction[0] == 1 and (right_filled or right in clay)

    recursive((501, 0), (0, 1))

    return len([pt for pt in moving | settled if min_y <= pt[1] <= max_y]), \
           len([pt for pt in settled if min_y <= pt[1] <= max_y])


if __name__ == '__main__':
    with open('day_17_input.txt', 'r') as f:
        inp = f.readlines()
        ans = solve(inp)
        print("Part 1 answer: " + str(ans[0]))
        print("Part 2 answer: " + str(ans[1]))
