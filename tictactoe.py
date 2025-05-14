def print_board(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' ')
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' ')
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' ')
    print()

def check_win(board, player):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    
    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    
    # Check diagonals
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    
    return False

def is_board_full(board):
    return ' ' not in board

def main():
    # Initialize the board
    board = [' ' for _ in range(9)]
    
    # Display initial board with positions
    print("Welcome to Tic-Tac-Toe!")
    print("Here are the positions on the board:")
    position_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    print_board(position_board)
    print("Players take turns entering a number 1-9 to place their mark.")
    print()
    
    # Game loop
    current_player = 'X'
    while True:
        # Print current board
        print_board(board)
        
        # Get player move
        while True:
            try:
                position = int(input("Player " + current_player + ", enter position (1-9): ")) - 1
                if 0 <= position <= 8 and board[position] == ' ':
                    board[position] = current_player
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Please enter a number between 1 and 9.")
        
        # Check for win
        if check_win(board, current_player):
            print_board(board)
            print("Player " + current_player + " wins!")
            break
        
        # Check for draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'

    print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    main()