if __name__ == '__main__':
    lanternfish = [1, 3, 1, 5, 5, 1, 1, 1, 5, 1, 1, 1, 3, 1, 1, 4, 3, 1, 1, 2, 2, 4, 2, 1, 3, 3, 2, 4, 4, 4, 1, 3, 1, 1,
                   4, 3, 1, 5, 5, 1, 1, 3, 4, 2, 1, 5, 3, 4, 5, 5, 2, 5, 5, 1, 5, 5, 2, 1, 5, 1, 1, 2, 1, 1, 1, 4, 4, 1,
                   3, 3, 1, 5, 4, 4, 3, 4, 3, 3, 1, 1, 3, 4, 1, 5, 5, 2, 5, 2, 2, 4, 1, 2, 5, 2, 1, 2, 5, 4, 1, 1, 1, 1,
                   1, 4, 1, 1, 3, 1, 5, 2, 5, 1, 3, 1, 5, 3, 3, 2, 2, 1, 5, 1, 1, 1, 2, 1, 1, 2, 1, 1, 2, 1, 5, 3, 5, 2,
                   5, 2, 2, 2, 1, 1, 1, 5, 5, 2, 2, 1, 1, 3, 4, 1, 1, 3, 1, 3, 5, 1, 4, 1, 4, 1, 3, 1, 4, 1, 1, 1, 1, 2,
                   1, 4, 5, 4, 5, 5, 2, 1, 3, 1, 4, 2, 5, 1, 1, 3, 5, 2, 1, 2, 2, 5, 1, 2, 2, 4, 5, 2, 1, 1, 1, 1, 2, 2,
                   3, 1, 5, 5, 5, 3, 2, 4, 2, 4, 1, 5, 3, 1, 4, 4, 2, 4, 2, 2, 4, 4, 4, 4, 1, 3, 4, 3, 2, 1, 3, 5, 3, 1,
                   5, 5, 4, 1, 5, 1, 2, 4, 2, 5, 4, 1, 3, 3, 1, 4, 1, 3, 3, 3, 1, 3, 1, 1, 1, 1, 4, 1, 2, 3, 1, 3, 3, 5,
                   2, 3, 1, 1, 1, 5, 5, 4, 1, 2, 3, 1, 3, 1, 1, 4, 1, 3, 2, 2, 1, 1, 1, 3, 4, 3, 1, 3]

    days = 256

    initial_state = [0] * 9

    for fish in lanternfish:
        initial_state[fish] += 1

    for i in range(days):
        day0 = initial_state[0]
        day1 = initial_state[1]
        day2 = initial_state[2]
        day3 = initial_state[3]
        day4 = initial_state[4]
        day5 = initial_state[5]
        day6 = initial_state[6]
        day7 = initial_state[7]
        day8 = initial_state[8]

        initial_state[0] = day1
        initial_state[1] = day2
        initial_state[2] = day3
        initial_state[3] = day4
        initial_state[4] = day5
        initial_state[5] = day6
        initial_state[6] = day7 + day0
        initial_state[7] = day8
        initial_state[8] = day0

    print(sum(initial_state))
