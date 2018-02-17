"""Tic Tac Toe."""


from game import Game
import sys


class TicTacToe(Game):
    """Tic Tac Toe game class."""

    def __init__(self):
        """Construct new tictactoe game instance."""
        self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.player = 'X'
        self.winner = None

    def reset(self):
        """Reset board between games."""
        self.board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        self.player = 'X'
        self.winner = None

    def get_open_moves(self):
        """Returns list of available moves given current states and next states."""
        actions = []
        states = []
        for i, val in enumerate(self.board):
            if val == '-':
                actions.append(i)
                self.board[i] = self.player
                states.append(self.get_state(self.board))
                self.board[i] = '-'
        return states, actions

    def get_state(self, board):
        """Returns board state as String."""
        return ''.join(board)

    def is_win(self):
        """Check the board for win condition.

        Possible outputs are X, O, Draw, None.
        """
        # Check win condition
        row_1 = self.board[0] + self.board[1] + self.board[2]
        row_2 = self.board[3] + self.board[4] + self.board[5]
        row_3 = self.board[6] + self.board[7] + self.board[8]
        col_1 = self.board[0] + self.board[3] + self.board[6]
        col_2 = self.board[1] + self.board[4] + self.board[7]
        col_3 = self.board[2] + self.board[5] + self.board[8]
        diag_1 = self.board[0] + self.board[4] + self.board[8]
        diag_2 = self.board[2] + self.board[4] + self.board[6]
        triples = [row_1, row_2, row_3, col_1, col_2, col_3, diag_1, diag_2]

        for triple in triples:
            if (triple == 'OOO'):
                return 'O'
            elif (triple == 'XXX'):
                return 'X'

        # Check draw condition
        if '-' not in self.board:
            return 'Draw'

        return None

    def is_valid_move(self, position):
        """Check that potential move is in a valid position.

        Valid means inbounds and not occupied.
        """
        if position >= 0 and position < len(self.board):
            return self.board[position] == '-'
        else:
            return False

    def make_move(self, position):
        """Makes move by setting position to player value.

        Also toggles player and returns is_win result.
        """
        self.board[position] = self.player
        self.player = 'O' if self.player == 'X' else 'X'
        return self.is_win()

    def read_input(self):
        """Define game specific read in function from command line."""
        return int(sys.stdin.readline()[:-1])

    def print_board(self):
        print('{} {} {}\n{} {} {}\n{} {} {}'.format(self.board[0], self.board[1], self.board[2],
                                                    self.board[3], self.board[4], self.board[5],
                                                    self.board[6], self.board[7], self.board[8]))
        print('=====')

    def print_instructions(self):
        print('===============\n'
              'How to play:\n'
              'Possible moves are [0,9) corresponding to these spaces on the board:\n\n'
              '0 | 1 | 2\n'
              '3 | 4 | 5\n'
              '6 | 7 | 8\n')
