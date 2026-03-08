"""
game.py

This file contains the core game logic for Tic Tac Toe.
It does NOT handle input or printing to the screen.
Its responsibility is only to manage the game state and rules.
"""

# ----------------------------------------
# Board Class
# ----------------------------------------
# The Board class is responsible for:
# - Creating the game board
# - Checking if spaces are empty
# - Placing moves on the board
# - Detecting wins
# - Detecting ties
class Board:

    # Constructor
    # Runs when a Board object is created
    def __init__(self):

        # Symbol used to represent an empty square
        self.empty = " "

        # Create a 3x3 board using a 2D list
        # This satisfies the assignment requirement of using a 2D data structure
        self.board = [[' ' for i in range(3)] for j in range(3)]
