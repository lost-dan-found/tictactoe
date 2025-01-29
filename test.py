import unittest
from tictactoe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_checkWinner_horizontal_win(self):
        board = [
            ["x", "x", "x", "x"],
            ["", "o", "o", ""],
            ["o", "o", "x", ""],
            ["", "", "", ""]
        ]
        self.assertEqual(self.game.checkWinner(board), "x")

    def test_checkWinner_vertical_win(self):
        board = [
            ["o", "x", "x", "x"],
            ["o", "", "o", ""],
            ["o", "o", "x", ""],
            ["o", "", "", ""]
        ]
        self.assertEqual(self.game.checkWinner(board), "o")

    def test_checkWinner_diagonal_win(self):
        board = [
            ["o", "x", "x", "x"],
            ["o", "o", "x", ""],
            ["x", "x", "x", ""],
            ["x", "", "", "x"]
        ]
        self.assertEqual(self.game.checkWinner(board), "x")

    def test_checkWinner_no_winner(self):
        board = [
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"],
            ["x", "x", "o", "o"],
            ["o", "x", "o", "x"]
        ]
        self.assertEqual(self.game.checkWinner(board), "")

    def test_anyMovesLeft_true(self):
        board = [
            ["x", "o", "x", "o"],
            ["o", "x", "", "x"],
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"]
        ]
        self.assertTrue(self.game.anyMovesLeft(board))

    def test_anyMovesLeft_false(self):
        board = [
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"],
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"]
        ]
        self.assertFalse(self.game.anyMovesLeft(board))

    def test_isGameOver_win(self):
        board = [
            ["x", "x", "x", "x"],
            ["o", "x", "", ""],
            ["o", "o", "x", ""],
            ["", "", "", ""]
        ]
        self.assertTrue(self.game.isGameOver(board))

    def test_isGameOver_tie(self):
        board = [
            ["x", "o", "x", "o"],
            ["o", "x", "o", "x"],
            ["x", "o", "o", "o"],
            ["o", "x", "o", "x"]
        ]
        self.assertTrue(self.game.isGameOver(board))

if __name__ == "__main__":
    unittest.main()
