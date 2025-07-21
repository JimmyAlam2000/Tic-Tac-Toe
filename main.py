def print_board(board):
    print("\n   ┏━━━┳━━━┳━━━┓")
    for i in range(3):
        print(f"   ┃ {board[i][0]} ┃ {board[i][1]} ┃ {board[i][2]} ┃")
        if i < 2:
            print("   ┣━━━╋━━━╋━━━┫")
    print("   ┗━━━┻━━━┻━━━┛\n")

def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_move(player_symbol, board):
    while True:
        move = input(f"Player {player_symbol} ➤ Enter a number (1-9): ")
        if move in '123456789':
            move = int(move) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                return row, col
            else:
                print("⛔ That cell is already taken.")
        else:
            print("⚠ Please enter a number from 1 to 9.")

def main():
    board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    player1 = "X"
    player2 = "O"
    current_symbol = player1

    print("\n🎮 Welcome to Clean Tic Tac Toe!")
    print("👉 Choose your move by typing a number (1-9):")
    print("""
 Positions:

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
""")
    print_board(board)

    while True:
        row, col = get_move(current_symbol, board)
        board[row][col] = current_symbol
        print_board(board)

        if check_winner(board, current_symbol):
            print(f"🏆 Player '{current_symbol}' wins!")
            break
        elif is_full(board):
            print("🤝 It's a draw!")
            break

        current_symbol = player2 if current_symbol == player1 else player1

if __name__ == "__main__":
    main()
