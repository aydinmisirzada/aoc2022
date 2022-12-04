
from typing import List


def get_letter_priority(char: str) -> int:
    return ord(char) - 96 if char.islower() else ord(char) - 64 + 26


def star1(input_file: str) -> int:
    """Should return 157 for sample data.

    >>> star1('day3_test_input.txt')
    157
    """

    total = 0

    with open(input_file, 'r') as f:
        for line in f:
            half_index = int(len(line) / 2)

            first_section = line[:half_index]
            second_section = line[half_index:]

            for c in first_section:
                if c in second_section:
                    total += get_letter_priority(c)
                    break

    return total


def analyze_group(group_rucksacks: List[str]) -> int:
    priority = 0
    for c in group_rucksacks[0]:
        if c in group_rucksacks[1] and c in group_rucksacks[2]:
            priority = get_letter_priority(c)
            break

    return priority


def star2(input_file: str) -> int:
    """Should return 70 for sample data.

    >>> star2('day3_test_input.txt')
    70
    """

    total = 0
    group_rucksacks: List[str] = []

    with open(input_file, 'r') as f:
        for line in f:
            if (len(group_rucksacks) == 3):
                total += analyze_group(group_rucksacks)
                group_rucksacks = []

            group_rucksacks.append(line.rstrip())

        if (len(group_rucksacks) == 3):
            total += analyze_group(group_rucksacks)

    return total


if __name__ == "__main__":
    data = 'day3_input.txt'
    print('Result for the 1st star', star1(data))
    print('Result for the 2nd star', star2(data))
