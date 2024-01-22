def initialize_board(given_board):
    pos = 1
    for i in range(3):
        given_board.append([])
        for j in range(1, 4):
            given_board[i].append(pos)
            pos += 1
    return given_board


def reset_board(given_board):
    pos = 1
    for i in range(3):
        given_board[i] = []
        for j in range(1, 4):
            given_board[i].append(pos)
            pos += 1
    return given_board


def display_board(given_board):
    print("Here is the board with the position number")
    for i in range(3):
        print(" --- " * 3)
        print("|", end="")
        for j in range(3):
            print(f" {given_board[i][j]}  |", end="")
        print()
        print(" --- " * 3)


def check_win(given_board):
    # Check rows for win
    for row in given_board:
        if len(set(row)) == 1:
            return row[0]

    # Check columns for win
    for col in range(3):
        if len(set([given_board[row][col] for row in range(3)])) == 1:
            return given_board[0][col]

    # Check diagonals for win
    if len(set([given_board[i][i] for i in range(3)])) == 1:
        return given_board[0][0]
    if len(set([given_board[i][2 - i] for i in range(3)])) == 1:
        return given_board[0][2]

    # No winner
    return None


def check_tie(given_board):
    for sublist in given_board:
        for value in sublist:
            if not isinstance(value, str):
                return False
    return True


# Variable initialization
players = (["First Player", "O"], ["Second Player", "X"])
which_player_turn = 0

board = []
board = initialize_board(board)

# x,y
board_indexes = [
    [0, 0],
    [0, 1],
    [0, 2],
    [1, 0],
    [1, 1],
    [1, 2],
    [2, 0],
    [2, 1],
    [2, 2]
]

# Core loop
while True:
    is_player_won = False
    print("Welcome to tic-tac-toe game!\n")
    print("The first player's symbol is 'O' and the second player's symbol is 'X'\n")

    display_board(board)

    # Core Gameplay loop
    while not is_player_won:
        print(players[which_player_turn][0] + " move\n")
        try:
            position = int(input("Enter your position (1-9): "))
        except ValueError:
            print("Not valid position")
            continue

        indexes = board_indexes[position - 1]

        if isinstance(board[indexes[0]][indexes[1]], str):
            print("Position is taken by another player. Please select another position.")
            continue
        board[indexes[0]][indexes[1]] = players[which_player_turn][1]
        display_board(board)

        is_player_won = check_win(board)

        if is_player_won:
            print(is_player_won)
            print(players[which_player_turn][0] + " won!")
            print("Game over\n")
            break
        elif check_tie(board):
            print("The game is draw!")
            print("Game over\n")
            break

        which_player_turn = 0 if which_player_turn == 1 else 1

    is_replay_valid = False
    replay = ""
    while not is_replay_valid:
        replay = input("Do you want to play again? Y / N")
        if replay == "Y" or replay == "N":
            is_replay_valid = True
        else:
            print("Only 'Y' and 'N' are allowed")

    if replay == "N":
        print("Thanks for playing!\nGame over")
        break

    # Reset Board States
    board = reset_board(board)
    print("")
