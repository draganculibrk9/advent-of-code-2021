import functools


def row_complete(board):
    for row in [board[i:i + 5] for i in range(0, len(board), 5)]:
        if all(value[1] == 1 for value in row):
            return True
    return False


def column_complete(board):
    for i in range(0, 5):
        if all(board[i + j][1] == 1 for j in range(0, len(board), 5)):
            return True
    return False


def read_boards(file):
    boards = []
    with open(file) as f:
        lines = list(line for line in (l.strip() for l in f) if line)
        while not len(lines) == 0:
            board = functools.reduce(lambda a, b: a + b,
                                     map(lambda line: list(map(lambda v: [int(v), 0], line.split())), lines[:5]))
            boards.append(board)
            lines = lines[5:]
    return boards


def find_winning_boards(boards):
    winners = []
    for board in boards:
        if row_complete(board) or column_complete(board):
            winners.append(board)

    return winners


def sum_unmarked(board):
    sum = 0
    for value in board:
        if value[1] == 0:
            sum += value[0]
    return sum


if __name__ == '__main__':
    drawn_numbers = [59, 91, 13, 82, 8, 32, 74, 96, 55, 51, 19, 47, 46, 44, 5, 21, 95, 71, 48, 60, 68, 81, 80, 14, 23,
                     28, 26, 78, 12, 22, 49, 1, 83, 88, 39, 53, 84, 37, 93, 24, 42, 7, 56, 20, 92, 90, 25, 36, 34, 52,
                     27, 50, 85, 75, 89, 63, 33, 4, 66, 17, 98, 57, 3, 9, 54, 0, 94, 29, 79, 61, 45, 86, 16, 30, 77, 76,
                     6, 38, 70, 62, 72, 43, 69, 35, 18, 97, 73, 41, 40, 64, 67, 31, 58, 11, 15, 87, 65, 2, 10, 99]

    boards = read_boards("boards.txt")

    counter = 1
    n = None
    last = None
    for number in drawn_numbers:
        for board in list(boards):
            for value in board:
                if value[0] == number:
                    value[1] = 1

        if counter >= 5:
            winners = find_winning_boards(boards)
            for winning_board in winners:
                boards.remove(winning_board)
                last = winning_board
                n = number
        counter += 1

    print(n * sum_unmarked(last))
