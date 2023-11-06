import random

def ChutesAndLaddersGame(MaximumMoves):
    moves = 1
    winner = 0
    OnePosition = [0] * MaximumMoves
    TwoPosition = [0] * MaximumMoves

    while winner == 0 and moves <= MaximumMoves:
        OnePosition[moves] = OneMove(OnePosition[moves - 1])


        if OnePosition[moves] == 100:
            winner = 1
        else:
            TwoPosition[moves] = OneMove(TwoPosition[moves - 1])

            if TwoPosition[moves] == 100:
                winner = 2

        moves += 1

    return [winner, moves]

def OneMove(Start):
    s = random.randint(1, 6)  # Spin the spinner
    if Start + s > 100:  # Must land on 100 exactly
        Next = Start
    else:
        Next = Start + s
        if Next == 1:
            Next = 38
        elif Next == 4:
            Next = 14
        elif Next == 9:
            Next = 31
        elif Next == 16:
            Next = 7
        elif Next == 21:
            Next = 42
        elif Next == 28:
            Next = 84
        elif Next == 36:
            Next = 44
        elif Next == 48:
            Next = 26
        elif Next == 49:
            Next = 11
        elif Next == 51:
            Next = 67
        elif Next == 56:
            Next = 53
        elif Next == 62:
            Next = 19
        elif Next == 64:
            Next = 60
        elif Next == 71:
            Next = 91
        elif Next == 80:
            Next = 100
        elif Next == 87:
            Next = 24
        elif Next == 93:
            Next = 73
        elif Next == 95:
            Next = 76
        elif Next == 98:
            Next = 78

    return Next

def main():
    n = 10**6
    winners = [[0, 0] for _ in range(n)]
    MaximumMoves = 200
    OneWins = 0
    TwoWins = 0
    MovesWhenOneWins = 0
    MovesWhenTwoWins = 0
    MaximumMovesExceeded = 0

    for i in range(n):
        winners[i] = ChutesAndLaddersGame(MaximumMoves)

        if winners[i][0] == 1:
            OneWins += 1
            MovesWhenOneWins += winners[i][1]
        elif winners[i][0] == 2:
            TwoWins += 1
            MovesWhenTwoWins += winners[i][1]
        else:
            MaximumMovesExceeded += 1

    OneWinsPercentage = 100 * OneWins / (OneWins + TwoWins)
    AverageMovesPerOneWin = MovesWhenOneWins / OneWins
    AverageMovesPerTwoWin = MovesWhenTwoWins / TwoWins

    print(f"Player One wins {OneWinsPercentage:.2f}% of the time.")
    print(f"Average moves when Player One wins: {AverageMovesPerOneWin:.2f}")
    print(f"Average moves when Player Two wins: {AverageMovesPerTwoWin:.2f}")
    print(f"Maximum number of moves {MaximumMoves} exceeded {MaximumMovesExceeded} times")

if __name__ == "__main__":
    main()
