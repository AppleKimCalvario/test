import random


# Dictionary for location of chutes and ladders.Increasing values are ladders, decreasing values are chutes
chutes_and_ladders = {
    4: 14,
    9: 31,
    17: 7,
    20: 38,
    28: 84,
    40: 59,
    51: 67,
    54: 34,
    62: 19,
    63: 81,
    64: 60,
    71: 91,
    87: 24,
    93: 73,
    95: 75,
    99: 78
}

def roll_dice():
    return random.randint(1, 6)

def move_player(player_position, dice_roll):
    player_position += dice_roll
    if player_position in chutes_and_ladders:
        player_position = chutes_and_ladders[player_position]
    if player_position > 100:
        player_position = 100
    return player_position

def simulate_one_game(starting_player):
    player_positions = [0, 0]
    moves_count = 0
    current_player = starting_player

    while True:
        moves_count += 1
        dice_roll_result = roll_dice()
        player_positions[current_player - 1] = move_player(player_positions[current_player - 1], dice_roll_result)

        if player_positions[current_player - 1] == 100:
            return current_player, moves_count

        current_player = 3 - current_player  # Switch player (assuming there are only 2 players)

def monte_carlo_simulation(num_simulations):
    player_one_wins = 0
    player_two_wins = 0
    total_moves_one = 0
    total_moves_two = 0

    for _ in range(num_simulations):
        winner, moves = simulate_one_game(player_choice.isdigit())
        if winner == 1:
            player_one_wins += 1
            total_moves_one += moves
        else:
            player_two_wins += 1
            total_moves_two += moves

    player_one_win_probability = player_one_wins / num_simulations
    player_two_win_probability = player_two_wins / num_simulations

    return player_one_win_probability, player_two_win_probability, total_moves_one, total_moves_two


print("\t\tChutes and Ladders: Monte Carlo Simulation\n")

print("=============================================================")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| 100 | \033[91mC8\033[0m  | 98  | 97  | 96  | \033[91mC7\033[0m  | 94  | \033[91mC6\033[0m  | 92  | \033[94mL6\033[0m  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| \033[94mL6\033[0m  | 82  | 83  | \033[94mL4\033[0m  | 85  | 86  | \033[91mC5\033[0m  | 88  | 89  | 90  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| 80  | 79  | \033[91mC8\033[0m  | 77  | 76  | \033[91mC7\033[0m  | 74  | \033[91mC6\033[0m  | 72  | \033[94mL7\033[0m  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| 61  | \033[91mC3\033[0m  | \033[94mL6\033[0m  | \033[91mC4\033[0m  | 65  | 66  | 67  | 68  | 69  | 70  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| \033[91mC4\033[0m  | \033[94mL5\033[0m  | 58  | 57  | 56  | 55  | \033[91mC2\033[0m  | 53  | 52  | 51  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| 41  | 42  | 43  | 44  | 45  | 46  | 47  | 48  | 49  | 50  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| \033[94mL5\033[0m  | 39  | \033[94mL3\033[0m  | 37  | 36  | 35  | \033[91mC2\033[0m  | 33  | 32  | \033[94mL2\033[0m  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| 21  | 22  | 23  | \033[91mC5\033[0m  | 25  | 26  | 27  | \033[94mL4\033[0m  | 29  | 30  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| \033[94mL3\033[0m  | \033[91mC3\033[0m  | 18  | \033[91mC1\033[0m  | 16  | 15  |  \033[94mL1\033[0m | 13  | 12  | 11  |")
print("+-----+-----+-----+-----+-----+-----+-----+-----+-----+------+")
print("|     |     |     |     |     |     |     |     |     |     |")
print("| 1   | 2   | 3   | \033[94mL1\033[0m  | 5   | 6   | \033[91mC1\033[0m  | 8   | \033[94mL2\033[0m  | 10  |")
print("=============================================================")

print("\n")

player_one_position = 0
player_two_position = 0
count1 = 0
count2 = 0


while True:

    player_choice = input("Choose Player [1 or 2]: ")

    if player_choice not in ["1", "2"]:
        print("Invalid choice. Please choose either 1 or 2.")
        continue

    sim = input("Type how many simulations you want:  ")

    try:
        num_simulations = int(sim)
        player_one_prob, player_two_prob, total_moves_one, total_moves_two = monte_carlo_simulation(num_simulations)
        print(f"Player One win probability: {player_one_prob}")
        print(f"Player Two win probability: {player_two_prob}")
        print(f"Player One win moves: {total_moves_one}")
        print(f"Player Two win moves: {total_moves_two}", "\n")


    except ValueError:
        print("Wrong input please try again!\n")
        continue

    while True:

        ask = input("Play and choose [1 or 2]: ")

        if ask == "1":
            dice_roll_result = roll_dice()
            print("Dice rolled...")
            player_one_position = move_player(player_one_position, dice_roll_result)
            print(f"Move to {dice_roll_result} space/s")
            print(f"Current position {player_one_position}", "\n")
            count1 += 1
            if player_one_position == 100:
                print("You are the winner!")
                print(f"Number of moves for Player 1: {count1}")
                # print(count1, "\n")
                exit()

        elif ask == "2":
            # print("Player 2")
            dice_roll_result = roll_dice()
            print("Dice rolled...")
            player_two_position = move_player(player_two_position, dice_roll_result)
            print(f"Move to {dice_roll_result} space/s")
            print(f"Current position {player_two_position}", "\n")
            count2 += 1
            # print(count2,"\n")
            if player_two_position == 100:
                print("You are the winner!")
                print(f"Number of moves for Player 2: {count2}")
                exit()

        else:
            print("Try again!")
            continue



