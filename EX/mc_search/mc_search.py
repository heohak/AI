import random

# Constants
ROWS, COLS = 6, 7
EMPTY = " "
PLAYER = "X"
COMPUTER = "O"
WIN, DRAW, LOSS = 1, 0, -1

# Helper Functions
def is_full(board):
    return not EMPTY in board[0]

def is_winner(board, player):
    # Check rows, columns, diagonals
    for i in range(ROWS):
        for j in range(COLS):
            if board[i][j] == player:
                # Check right
                if j <= COLS - 4 and all(board[i][k] == player for k in range(j, j + 4)):
                    return True
                # Check down
                if i <= ROWS - 4 and all(board[k][j] == player for k in range(i, i + 4)):
                    return True
                # Check right diagonal
                if i <= ROWS - 4 and j <= COLS - 4 and all(board[i + k][j + k] == player for k in range(4)):
                    return True
                # Check left diagonal
                if i <= ROWS - 4 and j >= 3 and all(board[i + k][j - k] == player for k in range(4)):
                    return True
    return False

# Function to return a list of columns where a move can be made
def legal_moves(board):
    return [col for col in range(COLS) if board[0][col] == EMPTY]

# Function to make a move on the board for a given side
def make_move(board, move, side):
    for i in reversed(range(ROWS)):
        if board[i][move] == EMPTY:
            board[i][move] = side
            break
    return board


# Function to simulate a game from a given position after making a move for a given side
def simulate(pos, move, my_side):
    board = [row[:] for row in pos]
    board = make_move(board, move, my_side)

    other_side = COMPUTER if my_side == PLAYER else PLAYER
    current_turn = other_side

    while not (is_winner(board, PLAYER) or is_winner(board, COMPUTER) or is_full(board)):
        move = random.choice(legal_moves(board))
        board = make_move(board, move, current_turn)
        current_turn = PLAYER if current_turn == COMPUTER else COMPUTER

    if is_winner(board, my_side):
        return WIN
    elif is_winner(board, other_side):
        return LOSS
    return DRAW

# Monte Carlo function
def pure_mc(pos, N=200):
    my_side = COMPUTER
    moves_list = legal_moves(pos)
    win_counts = {move: 0 for move in moves_list}

    for move in moves_list:
        for _ in range(N):
            res = simulate(pos, move, my_side)
            if res == WIN:
                win_counts[move] += 1
            elif res == DRAW:
                win_counts[move] += 0.5

    return max(win_counts, key=win_counts.get)

# Text-based UI functions
def dump_pos(board):
    for row in board:
        print("|" + "|".join(row) + "|")
    print("|" + "".join(map(str, range(COLS))) + "|")

def play_game():
    board = [[EMPTY] * COLS for _ in range(ROWS)]

    while True:
        dump_pos(board)
        if is_full(board) or is_winner(board, PLAYER) or is_winner(board, COMPUTER):
            break

        if not legal_moves(board):
            break

        movestr = input("Your move? ")
        move = int(movestr)
        board = make_move(board, move, PLAYER)
        write_stats_to_file(board)  # Update stats after player's move
        if is_full(board) or is_winner(board, PLAYER):
            break

        print("Computer's turn...\n")
        move = pure_mc(board)
        board = make_move(board, move, COMPUTER)
        write_stats_to_file(board)  # Update stats after computer's move

        if is_full(board) or is_winner(board, COMPUTER):
            break

    if is_winner(board, PLAYER):
        dump_pos(board)
        print("You win!")
    elif is_winner(board, COMPUTER):
        dump_pos(board)
        print("Computer wins!")
    else:
        dump_pos(board)
        print("It's a draw!")



def write_stats_to_file(board):
    with open('game_stats.txt', 'w') as file:
        # Dumping position
        for row in board:
            file.write("|".join(row) + "\n")
        file.write("".join(map(str, range(COLS))) + "\n")
        moves_list = legal_moves(board)
        win_counts = {move: 0 for move in moves_list}
        total_simulations = 200  # As per the pure_mc function

        # Running Monte Carlo for statistics
        for move in moves_list:
            for _ in range(total_simulations):
                res = simulate(board, move, COMPUTER)
                if res == WIN:
                    win_counts[move] += 1
                elif res == DRAW:
                    win_counts[move] += 0.5

        # Writing statistics
        for move, count in win_counts.items():
            percentage_win = (count / total_simulations) * 100
            file.write(f"Move {move}: Winning Percentage = {percentage_win:.2f}%\n")


def main():
    while True:
        play_game()

        # Check if the game has ended and then write the final stats
        again = input("Play again? (y/n): ")
        if again.lower() != 'y':
            break


if __name__ == "__main__":
    main()



