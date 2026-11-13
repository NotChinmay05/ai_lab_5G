import random

def calculate_heuristic(board):
    attacks = 0
    n = len(board)
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_best_neighbor(board):
    n = len(board)
    best_board = list(board)
    min_heuristic = calculate_heuristic(board)
    
    for col in range(n):
        original_row = board[col]
        for row in range(n):
            if row != original_row:
                board[col] = row
                h = calculate_heuristic(board)
                if h < min_heuristic:
                    min_heuristic = h
                    best_board = list(board)
        board[col] = original_row
        
    return best_board, min_heuristic

def hill_climbing(n=8):
    board = [random.randint(0, n - 1) for _ in range(n)]
    current_h = calculate_heuristic(board)
    
    while current_h > 0:
        next_board, next_h = get_best_neighbor(board)
        if next_h >= current_h:
            board = [random.randint(0, n - 1) for _ in range(n)]
            current_h = calculate_heuristic(board)
        else:
            board = next_board
            current_h = next_h
            
    return board

def print_board(board):
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            if board[col] == row:
                line += "Q "
            else:
                line += ". "
        print(line)

solution = hill_climbing(8)
print_board(solution)
