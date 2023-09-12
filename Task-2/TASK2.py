
### CODSOFT TASK-2 [TIC - TAC - TOE AI Using algorithms like Minimax with  Alpha-Beta Pruning] ###

import random

# Assisgning the roles for the players
USER = ''
AI_BOT = ''
EMPTY = ' '
piece = input("Please Select your Piece (X or O): ")
if piece=='X':
    USER = 'X'
    if USER == 'X':
        AI_BOT = 'O'
else:
    USER = 'O'
    if USER == 'O':
        AI_BOT = 'X'



# Function to print the board
def board_set(board):
    for row in board:
        print(' | '.join(row))
        print('-' * 9)

# Function to check if a player has won
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

# Function to check if the game is a draw
def is_draw(board):
    return all(all(cell != EMPTY for cell in row) for row in board)

# Minimax algorithm with Alpha-Beta Pruning
def minimax(board, depth, maximizing_player, alpha, beta):
    if check_winner(board, USER):
        return -1
    if check_winner(board, AI_BOT):
        return 1
    if is_draw(board):
        return 0
    
    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI_BOT
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = USER
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

# Function to find the best move using Minimax
def best_move(board):
    best_eval = float('-inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI_BOT
                eval = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = EMPTY
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)
    return best_move

# Main game loop
def start_game():
    board = [[EMPTY] * 3 for _ in range(3)]
    player_turn = random.choice([USER, AI_BOT])
    board_set(board)
    
    while True:
        if player_turn == USER:
            move = input("Enter row and column (0-2) for your move: ").split()
            row, col = map(int, move)
            if board[row][col] == EMPTY:
                board[row][col] = USER
                player_turn = AI_BOT
            else:
                print("Cell is already occupied. Try again.")
        else:
            print("AI is making a move...")
            row, col = best_move(board)
            board[row][col] = AI_BOT
            player_turn = USER
        
        board_set(board)
        
        if check_winner(board, USER):
            print("You win!")
            break
        elif check_winner(board, AI_BOT):
            print("AI wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

# Start the game
if __name__ == "__main__":
    start_game()
