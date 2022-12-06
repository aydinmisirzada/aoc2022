from typing import Dict
import re


def parse_line(line: str, stacks: dict) -> dict:
    length = len(line)
    for i in range(length):
        if line[i].isalpha():
            container_no = (i // 4) + 1
            if container_no not in stacks:
                stacks[container_no] = []

            stacks[container_no].insert(0, line[i])

    return stacks


def parse_movement(line: str) -> tuple[int, ...]:
    numbers = re.findall(r'\d+', line)
    return tuple([int(i) for i in numbers])


def move_crates(stacks: dict, src: int, dst: int, q: int) -> dict:
    for i in range(q):
        item = stacks[src].pop()
        stacks[dst].append(item)

    return stacks


def move_crates_together(stacks: dict, src: int, dst: int, q: int) -> dict:
    items = stacks[src][-q:]
    stacks[dst] = stacks[dst] + items
    stacks[src] = stacks[src][:-q]

    return stacks


def star1(input_file: str) -> str:
    """Should return CMZ for sample data.

    >>> star1('day5_test_input.txt')
    'CMZ'
    """

    stacks = {}  # type: Dict[int, str]
    read_mode = 0

    with open(input_file, 'r') as f:
        for line in f:
            if line == '\n':
                read_mode = 1
                continue
            if read_mode == 1:
                quantity, source, dest = parse_movement(line)
                stacks = move_crates(stacks, source, dest, quantity)
            else:
                stacks = parse_line(line, stacks)

        result = ''

        for crate in sorted(stacks.keys()):
            result += stacks[crate][-1]

        return result


def star2(input_file: str) -> str:
    """Should return MCD for sample data.

    >>> star2('day5_test_input.txt')
    'MCD'
    """

    stacks = {}  # type: Dict[int, str]
    read_mode = 0

    with open(input_file, 'r') as f:
        for line in f:
            if line == '\n':
                read_mode = 1
                continue
            if read_mode == 1:
                quantity, source, dest = parse_movement(line)
                stacks = move_crates_together(stacks, source, dest, quantity)
            else:
                stacks = parse_line(line, stacks)

        result = ''

        for crate in sorted(stacks.keys()):
            result += stacks[crate][-1]

        return result


if __name__ == "__main__":
    data = 'day5_input.txt'
    print('Result for the 1st star', star1(data))
    print('Result for the 2nd star', star2(data))
