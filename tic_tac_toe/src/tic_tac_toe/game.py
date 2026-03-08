"""
game.py

This file contains the core game logic for Tic Tac Toe.
It does NOT handle input or printing to the screen.
Its responsibility is only to manage the game state and rules.
"""


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
        self.board = [[' ' for i in range(3)] for j in range(3)]


    # ----------------------------------------
    # Check if a square is empty
    # ----------------------------------------
    def is_empty(self, row, col):

        #If the position on the board equals the empty symbol
        #return True, otherwise return false
        return self.board[row][col] == self.empty

    # ----------------------------------------
    # Place a mark on the board
    # ----------------------------------------
    # mark will be either "X" or "O"
    def place(self,row, col, mark):

        #checks if the cell is empty
        if self.is_empty(row, col):

            #Place the players mark
            self.board[row][col] = mark

            #Return True to indicate the move was successful
            return True

    #If the square was already full
        return False

    # ----------------------------------------
    # Check if a player has won
    # ----------------------------------------
    def check_winner(self):

        #Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != self.empty:
                return row[0]

        #Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != self.empty:
                return self.board[0][0]

        #Check main diagonal
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != self.empty:
            return self.board[0][0]


        #Check opposite diagonal
        if self.board[0][2] == self.board[1][1] == self.board [2][0] != self.empty:

        #If nobody has won
        return None

    # ----------------------------------------
    # Check if the board is full (tie condition)
    # ----------------------------------------
    def is_full(self):

        #Loop through every row and cell
        for row in self.board:
            for cell in row:
                if cell == self.empty:
                    return False

        #If no empty cells remain
        return True

# ----------------------------------------
# Game Class
# ----------------------------------------

class Game:

    #Constructor
    def __init__(self):

        #Create a board object
        self.board = Board()

        #X always starts firstt
        self.current_player = "X"

        #Store winner state
        self.winner = None

    # ----------------------------------------
    # Convert a move from 0-8 into row/column
    # ----------------------------------------
    def convert_move(self, move):

        #Integer division gives row
        row = move // 3

        #Modulo gives column
        col = move % 3

        return row, col
