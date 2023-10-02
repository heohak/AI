import random

class NQueens:
    def __init__(self, N):
        self.N = N
        self.state = list(range(N))  # Initialize the board state where index represents row and value represents column
        random.shuffle(self.state)  # Shuffle to get a random initial state
        self.conflicts = self.value()  # Find the initial set of conflicting queen pairs.

    def value(self):
        conflicts = set()
        for i in range(self.N):
            for j in range(i + 1, self.N):
                # Check for queens in the same column or diagonally aligned
                if self.state[i] == self.state[j] or abs(self.state[i] - self.state[j]) == abs(i - j):
                    conflicts.add((i, j))  # Add conflicting pairs to the set
        return conflicts

    def best_move(self):
        candidates = []
        min_conflicts = len(self.conflicts)  # Initialize the minimum conflicts to current number of conflicts
        for i in range(self.N):
            original_col = self.state[i]  # Store the original column before making a move
            for j in range(self.N):
                if j == original_col:  # Skip if it’s the original column
                    continue

                self.state[i] = j  # Temporarily move queen to a new column
                new_conflicts = self.value()  # Calculate the new conflicts after the move
                num_conflicts = len(new_conflicts)

                if num_conflicts < min_conflicts:  # Update the candidate moves if new conflicts are minimum
                    min_conflicts = num_conflicts
                    candidates = [(i, j, original_col)]
                elif num_conflicts == min_conflicts:  # Add to candidate moves if conflicts are equal to minimum
                    candidates.append((i, j, original_col))

            self.state[i] = original_col  # Reset the column back to original after all moves are checked for the queen

        return random.choice(candidates) if candidates else None  # Return a random move from the candidate moves

def hill_climbing(queens):
    while queens.conflicts:  # Continue until there are conflicts
        move = queens.best_move()
        if not move:  # Stop if no move can reduce the number of conflicts
            break
        i, j, original_col = move
        queens.state[i] = j  # Make the best move
        queens.conflicts = queens.value()  # Update conflicts after the move

def print_board(state):
    N = len(state)
    for i in range(N):
        row = ['_'] * N
        row[state[i]] = 'Q'
        print(' '.join(row))

if __name__ == "__main__":
    N = 8
    queens = NQueens(N)
    print("Initial Board:")
    print_board(queens.state)
    print("Initial Conflicts:", len(queens.conflicts))
    hill_climbing(queens)
    print("Final Board:")
    print_board(queens.state)
    print("Final Conflicts:", len(queens.conflicts))



