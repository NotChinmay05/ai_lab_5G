import random

# Initialize board
board = [['-' for _ in range(3)] for _ in range(3)]

# Randomly assign symbols
user = random.choice(['X', 'O'])
agent = 'O' if user == 'X' else 'X'

print("You are:", user)
print("Agent is:", agent)
print("X plays first.")


def display_board():
    for row in board:
        print(' '.join(row))
    print()


def check_win(player):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True

    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def board_full():
    for row in board:
        for cell in row:
            if cell == '-':
                return False
    return True


def agent_move():
    # 1. Try to win
    for r in range(3):
        for c in range(3):
            if board[r][c] == '-':
                board[r][c] = agent
                if check_win(agent):
                    return
                board[r][c] = '-'

    # 2. Try to block the user
    for r in range(3):
        for c in range(3):
            if board[r][c] == '-':
                board[r][c] = user
                if check_win(user):
                    board[r][c] = agent
                    return
                board[r][c] = '-'

    # 3. Try an empty position adjacent to an agent symbol
    adjacent = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == agent:
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        nr = r + dr
                        nc = c + dc

                        if (0 <= nr < 3 and 0 <= nc < 3
                                and board[nr][nc] == '-'):
                            adjacent.append((nr, nc))

    if adjacent:
        r, c = random.choice(adjacent)
        board[r][c] = agent
        return

    # 4. If the agent has no symbol yet, or no adjacent
    # position is available, choose a random empty position
    empty = []

    for r in range(3):
        for c in range(3):
            if board[r][c] == '-':
                empty.append((r, c))

    if empty:
        r, c = random.choice(empty)
        board[r][c] = agent


# Main game loop
while True:
    display_board()

    # X always plays first
    current = 'X' if sum(
        cell != '-' for row in board for cell in row
    ) % 2 == 0 else 'O'

    if current == user:
        print("Your turn")
        while True:
            try:
                r = int(input("Enter row (1-3): ")) - 1
                c = int(input("Enter column (1-3): ")) - 1

                if (0 <= r < 3 and 0 <= c < 3
                        and board[r][c] == '-'):
                    board[r][c] = user
                    break
                else:
                    print("Invalid position. Try again.")

            except ValueError:
                print("Enter valid numbers.")

    else:
        print("Agent's turn")
        agent_move()

    # Check game result
    if check_win(current):
        display_board()

        if current == user:
            print("You win!")
        else:
            print("Agent wins!")

        break

    if board_full():
        display_board()
        print("It's a draw!")
        break
