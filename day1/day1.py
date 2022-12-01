def star1(input_file):
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
    calories = []
    with open(input_file,'r') as f:
        elf_calories = 0
        for line in f:
            if line == '\n':
                calories.append(elf_calories)
                elf_calories = 0
            else:
                elf_calories += int(line)


    return sum(sorted(calories)[-3:])

data = 'day1_input.txt'
print('Result for the 1st star',star1(data))
print('Result for the 2nd star',star2(data))