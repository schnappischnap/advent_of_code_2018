def part_1(data):
    def solve(i):
        c_count = data[i]
        m_count = data[i+1]
        i += 2
        m_sum = 0
        for children in range(c_count):
            i, m = solve(i)
            m_sum += m
        m_sum += sum(data[i:i+m_count])
        return i + m_count, m_sum

    data = list(map(int, data.split()))
    return solve(0)[1]


def part_2(data):
    def build(i):
        c_count = data[i]
        m_count = data[i+1]
        i += 2
        children = []
        for _ in range(c_count):
            i, c, m = build(i)
            children.append((c, m))
        return i + m_count, children, data[i:i+m_count]

    def solve(children, metadata):
        if not children:
            return sum(metadata)
        return sum(solve(*children[m-1]) for m in metadata if 1 <= m <= len(children))

    data = list(map(int, data.split()))
    return solve(*build(0)[-2:])


if __name__ == '__main__':
    with open('day_08_input.txt', 'r') as f:
        inp = f.readlines()[0]
        print("Part 1 answer: " + str(part_1(inp)))
        print("Part 2 answer: " + str(part_2(inp)))
