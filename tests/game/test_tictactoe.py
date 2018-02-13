"""Test suite for Tic Tac Toe.

To run:
    python -m unittest -v tests.game.test_tictactoe.py

"""


import unittest
from game.tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Collection of unittests for Tic Tac Toe."""

    def setUp(self):
        """Initialize Tic Tac Toe game instance."""
        self.game = TicTacToe()

    def tearDown(self):
        """Reinitialize Tic Tac Toe game instance."""
        self.game = TicTacToe()

    def test_init(self):
        """Test __init__ method."""
        self.assertEqual(['-', '-', '-',
                          '-', '-', '-',
                          '-', '-', '-'], self.game.board)
        self.assertEqual('X', self.game.player)
        self.assertEqual(None, self.game.winner)

    def test_reset(self):
        """Test reset method."""
        modified_board = ['-', 'X', 'X',
                          'O', 'O', 'X',
                          'O', '-', '-']
        self.game.board = modified_board
        self.game.reset()
        self.assertEqual(['-', '-', '-',
                          '-', '-', '-',
                          '-', '-', '-'], self.game.board)
        self.assertNotEqual(modified_board, self.game.board)

    def test_get_open_moves(self):
        """Test get_open_moves method."""
        self.game.board = ['-', 'O', '-',
                           'X', 'X', 'O',
                           'O', 'X', '-']
        next_moves = self.game.get_open_moves()
        states = next_moves[0]
        actions = next_moves[1]
        self.assertEqual(['XO-XXOOX-', '-OXXXOOX-', '-O-XXOOXX'], states)
        self.assertEqual([0, 2, 8], actions)

    def test_get_state(self):
        """Test get_state method."""
        board1 = ['-', 'O', '-',
                  'X', 'X', 'O',
                  'O', 'X', '-']
        board2 = ['-', 'O', '-',
                  '-', 'X', 'O',
                  '-', 'X', '-']
        self.assertEqual('-O-XXOOX-', self.game.get_state(board1))
        self.assertEqual('-O--XO-X-', self.game.get_state(board2))

    def test_is_win_O_winner(self):
        """Test is_win method with O winner."""
        self.game.board = ['X', 'O', 'X',
                           'X', 'O', 'X',
                           'O', 'O', '-']
        self.assertEqual('O', self.game.is_win())

    def test_is_win_X_winner(self):
        """Test is_win method with X winner."""
        self.game.board = ['-', 'O', 'O',
                           'X', 'X', 'X',
                           'O', 'X', '-']
        self.assertEqual('X', self.game.is_win())

    def test_is_win_draw(self):
        """Test is_win method with draw condition."""
        self.game.board = ['X', 'O', 'X',
                           'X', 'O', 'O',
                           'O', 'X', 'X']
        self.assertEqual('Draw', self.game.is_win())

    def test_is_win_none(self):
        """Test is_win method with incomplete game."""
        self.game.board = ['-', 'O', '-',
                           'X', 'X', 'O',
                           'O', 'X', '-']
        self.assertEqual(None, self.game.is_win())

    def test_is_valid_move_bounds(self):
        """Test is_valid_move method with out of bounds."""
        self.game.board = ['-', 'O', '-',
                           'X', 'X', 'O',
                           'O', 'X', '-']
        self.assertFalse(self.game.is_valid_move(-1))
        self.assertFalse(self.game.is_valid_move(9))

    def test_is_valid_move_occupied(self):
        """Test is_valid_move method with occupied space."""
        self.game.board = ['-', 'O', '-',
                           'X', 'X', 'O',
                           'O', 'X', '-']
        self.assertFalse(self.game.is_valid_move(1))
        self.assertFalse(self.game.is_valid_move(3))

    def test_is_valid_move(self):
        """Test is_valid_move method with valid move."""
        self.game.board = ['-', 'O', '-',
                           'X', 'X', 'O',
                           'O', 'X', '-']
        self.assertTrue(self.game.is_valid_move(0))
        self.assertTrue(self.game.is_valid_move(2))

    def test_make_move(self):
        """Test make_move method."""
        self.game.board = ['-', '-', '-',
                           '-', '-', '-',
                           '-', '-', '-']
        # Check win result
        self.assertEqual(None, self.game.make_move(0))
        # Check board state
        self.assertEqual(['X', '-', '-',
                          '-', '-', '-',
                          '-', '-', '-'], self.game.board)
        # Check toggled game player
        self.assertEqual('O', self.game.player)


if __name__ == '__main__':
    unittest.main()
