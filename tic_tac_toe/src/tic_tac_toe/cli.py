"""
cli.py

This file handles user interaction.
It prints the board and asks for input.
"""

from tic_tac_toe.game import Game



def print_board(board):

    #Print the board in a readable format
    for row in board:
        print(row[0], "|", row[1], "|", row[2])
        print("---------")

def main():

    game = Game()

    while True:

        print_board(game.get_board())

        max_move = game.board.size * game.board.size - 1

        try:
            move = int(input(f"Enter your move (0 - {max_move}): "))
        except ValueError:
            print("Please enter a number.")
            continue
        if move < 0 or move > max_move:
            print("Move must be between 0 and {max_move}.")
            continue

        if not game.make_move(move):
            print("Invalid move.")
            continue

        if game.winner:
            print_board(game.get_board())
            print("Player", game.winner, "Wins!")
            break

        if game.board.is_full():
            print_board(game.get_board())
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()