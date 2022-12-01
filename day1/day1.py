def star1(input_file):
    """Should return 24000 for sample data.

    >>> star1('day1_test_input.txt')
    24000
    """
    max_calories = 0
    elf_calories = 0

    with open(input_file,'r') as f:
        for line in f:
            if line == '\n':
                max_calories = max(elf_calories, max_calories)
                elf_calories = 0
            else:
                elf_calories += int(line)

    return max_calories

def star2(input_file):
    """Should return 45000 for sample data.

    >>> star2('day1_test_input.txt')
    45000
    """
    calories = []
    with open(input_file,'r') as f:
        elf_calories = 0
        for line in f:
            if not line or line == '\n':
                calories.append(elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(line)
        if elf_calories:
            calories.append(elf_calories)

    return sum(sorted(calories)[-3:])


data = 'day1_input.txt'
print('Result for the 1st star',star1(data))
print('Result for the 2nd star',star2(data))