import unittest
from tic_tac_toe.game import Game

class TestTicTacToe(unittest.TestCase):

    def test_diagonal_win(self):

        game = Game()

        game.make_move(0)
        game.make_move(1)
        game.make_move(4)
        game.make_move(2)
        game.make_move(8)

        self.assertEqual(game.winner, "X")

if __name__ == '__main__':
    unittest.main()

