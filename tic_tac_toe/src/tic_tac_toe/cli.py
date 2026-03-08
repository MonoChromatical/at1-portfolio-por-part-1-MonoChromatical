"""
cli.py

This file handles user interaction.
It prints the board and asks for input.
"""

from tic_tac_toe.game import Game


def print_board(board):

    #Print the board in a readable format
    for row in board.board:
        print(row[0], "|", row[1], "|", row[2])
        print("---------")

def main():

    game = Game()

    while True:

        print_board(game.board)

        move = int(input("Enter your move(0 - 8): "))

        if not game.make_move(move):
            print("Invalid move.")
            continue

        if game.winner:
            print_board(game.board)
            print("Player", game.winner, "Wins!")
            break

        if game.board.is_full():
            print_board(game.board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    main()