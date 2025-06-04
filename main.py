
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*5)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row): return True
    for col in range(3):
        if all(row[col] == player for row in board): return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def ai_move(board):
    empty = [(i, j) for i in range(3) for j in range(3) if board[i][j] == ' ']
    if empty:
        i, j = random.choice(empty)
        board[i][j] = 'O'

# Game loop
board = [[' ']*3 for _ in range(3)]
print_board(board)

while True:
    try:
        x, y = map(int, input("Enter your move (row col): ").split())
        if board[x][y] != ' ':
            print("Cell taken!")
            continue
        board[x][y] = 'X'
        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        ai_move(board)
        print_board(board)
        if check_winner(board, 'O'):
            print("AI wins!")
            break
        if all(cell != ' ' for row in board for cell in row):
            print("Draw!")
            break
    except:
        print("Invalid input. Enter row and column like: 0 1")
