points = {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissors
    "X": 1,
    "Y": 2,
    "Z": 3,
}

def get_game_outcome(opponent: str, player: str) -> int:
    if points[player] == points[opponent]:
        return 3

    match player:
        case 'X':
            return (6 if opponent == 'C' else 0)
        case 'Y':
            return (6 if opponent == 'A' else 0)
        case 'Z':
            return (6 if opponent == 'B' else 0)

    return 0


def get_players_move_score(opponent_move: str, result: str) -> int:
    if result == 'Y':
        return points[opponent_move] + 3

    match opponent_move:
        case 'A':
            return (points['C'] if result == 'X' else points['B'] + 6)
        case 'B':
            return (points['A'] if result == 'X' else points['C'] + 6)
        case 'C':
            return (points['B'] if result == 'X' else points['A'] + 6)

    return points[opponent_move]


def star1(input_file: str) -> int:
    """Should return 15 for sample data.

    >>> star1('day2_test_input.txt')
    15
    """

    score = 0

    with open(input_file, 'r') as f:
        for line in f:
            moves = line.rstrip('\n').split(' ')
            score += points[moves[1]] + get_game_outcome(*moves)

    return score


def star2(input_file: str) -> int:
    """Should return 12 for sample data.

    >>> star2('day2_test_input.txt')
    12
    """
    score = 0

    with open(input_file, 'r') as f:
        for line in f:
            moves = line.rstrip('\n').split(' ')
            score += get_players_move_score(*moves)

    return score


if __name__ == "__main__":
    data = 'day2_input.txt'
    print('Result for the 1st star', star1(data))
    print('Result for the 2nd star', star2(data))
