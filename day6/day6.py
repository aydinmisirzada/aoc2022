def are_all_chars_unique(s: str) -> bool:
    return len(set(s)) == len(s)


def star1(input_file: str) -> int:
    """Should return 7 for sample data.

    >>> star1('day6_test_input.txt')
    7
    """

    with open(input_file, 'r') as f:
        stream = f.readline()
        for i in range(len(stream)):
            end_index = i + 4
            if are_all_chars_unique(stream[i:end_index]):
                return end_index

        return 0


def star2(input_file: str) -> int:
    """Should return 19 for sample data.

    >>> star2('day6_test_input.txt')
    19
    """

    with open(input_file, 'r') as f:
        stream = f.readline()
        for i in range(len(stream)):
            end_index = i + 14
            if are_all_chars_unique(stream[i:end_index]):
                return end_index

        return 0


if __name__ == "__main__":
    data = 'day6_input.txt'
    print('Result for the 1st star', star1(data))
    print('Result for the 2nd star', star2(data))
