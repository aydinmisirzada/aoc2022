def get_elf_sections(elf_range: str) -> set[int]:
    lower, upper = elf_range.split('-')
    return set(range(int(lower), int(upper) + 1))


def star1(input_file: str) -> int:
    """Should return 2 for sample data.

    >>> star1('day4_test_input.txt')
    2
    """
    total = 0

    with open(input_file, 'r') as f:
        for line in f:
            elf_one_range, elf_two_range = line.split(',')
            elf_one = get_elf_sections(elf_one_range)
            elf_two = get_elf_sections(elf_two_range)

            if (elf_one.issubset(elf_two) or elf_one.issuperset(elf_two)):
                total += 1

    return total


def star2(input_file: str) -> int:
    """Should return 4 for sample data.

    >>> star2('day4_test_input.txt')
    4
    """

    total = 0

    with open(input_file, 'r') as f:
        for line in f:
            elf_one_range, elf_two_range = line.split(',')
            elf_one = get_elf_sections(elf_one_range)
            elf_two = get_elf_sections(elf_two_range)

            if (not set(elf_one).isdisjoint(elf_two)):
                total += 1

    return total


if __name__ == "__main__":
    data = 'day4_input.txt'
    print('Result for the 1st star', star1(data))
    print('Result for the 2nd star', star2(data))
