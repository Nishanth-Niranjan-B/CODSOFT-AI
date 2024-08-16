import random

HUMAN = "X"
AI = "O"

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_win(board, player):
    win_conditions = [
        [(i, j) for j in range(3)] for i in range(3)] + \
        [[(j, i) for j in range(3)] for i in range(3)] + \
        [[(i, i) for i in range(3)], [(i, 2-i) for i in range(3)]]

    for condition in win_conditions:
        if all(board[x][y] == player for x, y in condition):
            return True
    return False

def check_tie(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def minimax(board, depth, is_maximizing):
    if check_win(board, AI):
        return 1
    if check_win(board, HUMAN):
        return -1
    if check_tie(board):
        return 0

    if is_maximizing:
        best_score = float("-inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = AI
            score = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = " "
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move[0]][move[1]] = HUMAN
            score = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = " "
            best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = float("-inf")
    move = None
    for available_move in get_available_moves(board):
        board[available_move[0]][available_move[1]] = AI
        score = minimax(board, 0, False)
        board[available_move[0]][available_move[1]] = " "
        if score > best_score:
            best_score = score
            move = available_move
    return move

def human_move(board):
    while True:
        move = input("Enter your move (row col): ").split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
            move = tuple(map(int, move))
            if move in get_available_moves(board):
                return move
        print("Invalid move. Please try again.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = random.choice([HUMAN, AI])

    while True:
        print_board(board)

        if current_player == HUMAN:
            print("Your turn (X)")
            move = human_move(board)
        else:
            print("AI's turn (O)")
            move = best_move(board)

        board[move[0]][move[1]] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"{current_player} wins!")
            break
        elif check_tie(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = HUMAN if current_player == AI else AI

play_game()
