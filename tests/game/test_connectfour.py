"""Test suite for Connect Four.

To run:
    python -m unittest -v tests.game.test_connectfour.py

"""


import unittest
from game.connectfour import ConnectFour


class TestConnectFour(unittest.TestCase):
    """Collection of unittests for Connect Four."""

    def setUp(self):
        """Initialize Connect Four game instance."""
        self.game = ConnectFour(rows=4, cols=4)

    def tearDown(self):
        """Reinitialize Connect Four game instance."""
        self.game = ConnectFour(rows=4, cols=4)

    def test_init(self):
        """Test __init__ method."""
        self.assertEqual(['-', '-', '-', '-',
                          '-', '-', '-', '-',
                          '-', '-', '-', '-',
                          '-', '-', '-', '-'], self.game.board)
        self.assertEqual('X', self.game.player)
        self.assertEqual(None, self.game.winner)
        self.assertEqual(4, self.game.rows)
        self.assertEqual(4, self.game.cols)

    def test_reset(self):
        """Test reset method."""
        modified_board = ['X', '-', '-', '-',
                          '-', '-', '-', 'X',
                          'O', '-', '-', '-',
                          'O', '-', '-', '-']
        self.game.board = modified_board
        self.game.reset()
        self.assertEqual(['-', '-', '-', '-',
                          '-', '-', '-', '-',
                          '-', '-', '-', '-',
                          '-', '-', '-', '-'], self.game.board)
        self.assertNotEqual(modified_board, self.game.board)

    def test_get_open_moves(self):
        """Test get_open_moves method."""
        self.game.board = ['-', '-', 'X', 'X',
                           'O', 'O', 'O', 'O',
                           'O', 'O', 'X', 'X',
                           'X', 'X', 'X', 'O']
        next_moves = self.game.get_open_moves()
        states = next_moves[0]
        actions = next_moves[1]
        self.assertEqual(['X-XXOOOOOOXXXXXO', '-XXXOOOOOOXXXXXO'], states)
        self.assertEqual([0, 1], actions)

    def test_get_state(self):
        """Test get_state method."""
        board1 = ['X', '-', 'X', 'X',
                  'O', 'O', 'O', 'O',
                  'O', 'O', 'X', 'X',
                  'X', 'X', 'X', 'O']
        board2 = ['-', '-', 'X', 'X',
                  'O', 'O', 'O', 'O',
                  'O', 'O', 'X', 'X',
                  'X', 'X', 'X', 'O']
        self.assertEqual('X-XXOOOOOOXXXXXO', self.game.get_state(board1))
        self.assertEqual('--XXOOOOOOXXXXXO', self.game.get_state(board2))

    def test_is_win_horizontal(self):
        """Test is_win with horizontal win condition."""
        self.game.board = ['-', '-', '-', '-',
                           '-', '-', '-', '-',
                           '-', '-', '-', '-',
                           'O', 'O', 'O', 'O']
        self.assertEqual('O', self.game.is_win())

    def test_is_win_vertical(self):
        """Test is_win with vertical win condition."""
        self.game.board = ['-', '-', 'O', '-',
                           '-', '-', 'O', '-',
                           '-', '-', 'O', '-',
                           '-', '-', 'O', '-']
        self.assertEqual('O', self.game.is_win())

    def test_is_win_diagonal_left(self):
        """Test is_win with diagonal left win condition."""
        self.game.board = ['-', '-', '-', 'O',
                           '-', '-', 'O', '-',
                           '-', 'O', '-', '-',
                           'O', '-', '-', '-']
        self.assertEqual('O', self.game.is_win())

    def test_is_win_diagonal_right(self):
        """Test is_win with diagonal right win condition."""
        self.game.board = ['O', '-', '-', '-',
                           '-', 'O', '-', '-',
                           '-', '-', 'O', '-',
                           '-', '-', '-', 'O']
        self.assertEqual('O', self.game.is_win())

    def test_is_win_O_winner(self):
        """Test is_win method with O winner."""
        self.game.board = ['O', '-', '-', '-',
                           'O', '-', '-', '-',
                           'O', '-', '-', '-',
                           'O', '-', '-', '-']
        self.assertEqual('O', self.game.is_win())

    def test_is_win_X_winner(self):
        """Test is_win method with X winner."""
        self.game.board = ['X', '-', '-', '-',
                           'X', '-', '-', '-',
                           'X', '-', '-', '-',
                           'X', '-', '-', '-']
        self.assertEqual('X', self.game.is_win())

    def test_is_win_draw(self):
        """Test is_win method with draw condition."""
        self.game.board = ['O', 'X', 'O', 'X',
                           'O', 'X', 'O', 'X',
                           'X', 'O', 'X', 'O',
                           'O', 'X', 'O', 'X']
        self.assertEqual('Draw', self.game.is_win())

    def test_is_win_none(self):
        """Test is_win method with incomplete game."""
        self.game.board = ['X', '-', '-', '-',
                           'O', '-', '-', '-',
                           'O', '-', '-', '-',
                           'X', '-', '-', '-']
        self.assertEqual(None, self.game.is_win())

    def test_is_valid_move_bounds(self):
        """Test is_valid_move method with out of bounds."""
        self.game.board = ['X', '-', '-', '-',
                           'O', '-', '-', '-',
                           'O', '-', '-', '-',
                           'X', '-', '-', '-']
        self.assertFalse(self.game.is_valid_move(-1))
        self.assertFalse(self.game.is_valid_move(16))

    def test_is_valid_move_occupied(self):
        """Test is_valid_move method with occupied space."""
        self.game.board = ['X', '-', '-', '-',
                           'O', '-', '-', '-',
                           'O', '-', '-', '-',
                           'X', '-', '-', '-']
        self.assertFalse(self.game.is_valid_move(0))
        self.assertFalse(self.game.is_valid_move(4))

    def test_is_valid_move(self):
        """Test is_valid_move method with valid move."""
        self.game.board = ['X', '-', '-', '-',
                           'O', '-', '-', '-',
                           'O', '-', '-', '-',
                           'X', '-', '-', '-']
        self.assertTrue(self.game.is_valid_move(1))
        self.assertTrue(self.game.is_valid_move(2))

    def test_make_move(self):
        """Test make_move method."""
        self.game.board = ['-', '-', '-', '-',
                           '-', '-', '-', '-',
                           '-', '-', '-', '-',
                           '-', '-', '-', '-']
        # Check win result
        self.assertEqual(None, self.game.make_move(0))
        # Check board state
        self.assertEqual(['X', '-', '-', '-',
                          '-', '-', '-', '-',
                          '-', '-', '-', '-',
                          '-', '-', '-', '-'], self.game.board)
        # Check toggled game player
        self.assertEqual('O', self.game.player)


if __name__ == '__main__':
    unittest.main()
